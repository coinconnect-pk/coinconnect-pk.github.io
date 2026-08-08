#!/usr/bin/env python3
"""
CoinConnect Intelligence — article publisher.

This is a QUEUE publisher, not a generator. Nothing here calls a model API.
Articles are written in advance in batched sessions, committed into _queue/,
and released from there.

Two articles are released per day, via two separate runs.

Order of operations each run:

  1. Stop if the daily limit has already been reached (unless FORCE=1).
  2. Look for a manual article in overrides/<today>/article.md that has not
     already been used today -> publish it and DO NOT consume the queue, so
     the queued article simply moves along one slot.
  3. Otherwise take the lowest-numbered file in _queue/, validate it, stamp
     today's date on it, move it into _posts/, and log it.

Environment:
  DRY_RUN   optional, "1" validates and prints but writes nothing
  FORCE     optional, "1" publishes even if the daily limit is reached
"""

import csv
import os
import re
import sys
from datetime import datetime, timedelta, timezone

# --------------------------------------------------------------- constants --

PKT = timezone(timedelta(hours=5))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

QUEUE_DIR = os.path.join(ROOT, "_queue")
POSTS_DIR = os.path.join(ROOT, "_posts")
OVERRIDES = os.path.join(ROOT, "overrides")
LOG_FILE = os.path.join(ROOT, "_data", "published-log.csv")

DRY_RUN = os.environ.get("DRY_RUN") == "1"
FORCE = os.environ.get("FORCE") == "1"

AUTHOR = "Malik Abbas"
TODAY = datetime.now(PKT)
TODAY_STR = TODAY.strftime("%Y-%m-%d")

# Two articles a day.
MAX_POSTS_PER_DAY = 2

# The times each day's articles are due, in PKT. Each of these has retry runs
# scheduled behind it in auto-publish.yml, because GitHub drops scheduled jobs
# under load and a dropped run must not cost the site a slot.
#
# A run publishes only what is DUE by the time it fires -- not the whole day's
# quota. Otherwise the first run of the morning would push both articles out at
# once and the site would go quiet for the rest of the day.
PUBLISH_SLOTS = [(6, 17), (18, 17)]


def articles_due_today():
    """How many articles should have gone out by now."""
    now_minutes = TODAY.hour * 60 + TODAY.minute
    due = sum(1 for h, m in PUBLISH_SLOTS if h * 60 + m <= now_minutes)
    return min(due, MAX_POSTS_PER_DAY)

MIN_WORDS = 1200
MAX_WORDS = 2600

VALID_CATEGORIES = {
    "Licensing",
    "Compliance",
    "Tax & Banking",
    "Corporate Setup",
    "Sandbox",
    "Enforcement",
    "Market Entry",
}

# Our own properties. Links to these are INTERNAL links.
INTERNAL_HOSTS = {
    "coinconnect.site",
    "blog.coinconnect.site",
}

# Outbound links are restricted to primary regulators, the intergovernmental
# bodies they answer to, and a short list of recognised data providers.
#
# THE RULE THAT MATTERS: never link a law firm, a consultancy, a licensing
# adviser, or anything else that competes with CoinConnect for the same client.
# A link is an endorsement and a transfer of authority -- we do not hand either
# to a competitor. Data providers are fine; they sell numbers, not our service.
EXTERNAL_HOSTS = {
    # Pakistani regulators and legislation
    "pvara.gov.pk",
    "secp.gov.pk",
    "sbp.org.pk",
    "fbr.gov.pk",
    "fmu.gov.pk",
    "na.gov.pk",
    "senate.gov.pk",
    "finance.gov.pk",
    "pakistancode.gov.pk",
    "pbs.gov.pk",
    # Intergovernmental bodies
    "fatf-gafi.org",
    "worldbank.org",
    "imf.org",
    "bis.org",
    "oecd.org",
    "un.org",
    # Recognised data and research providers (not competitors)
    "chainalysis.com",
    "statista.com",
}

ALLOWED_LINK_HOSTS = INTERNAL_HOSTS | EXTERNAL_HOSTS

# Every article must weave in at least this many links to our own pages and
# articles. Internal linking is the single biggest on-site ranking lever we
# control, and it only works if it is enforced rather than hoped for.
MIN_INTERNAL_LINKS = 10


# ----------------------------------------------------------------- helpers --

def log(msg):
    print(f"[publish] {msg}", flush=True)


def slugify(text):
    text = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    return re.sub(r"[\s_-]+", "-", text)[:70].strip("-")


def split_front_matter(body):
    """Return (front_matter_dict, raw_front_matter, article_body)."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", body, re.S)
    if not match:
        return None, "", body
    raw, rest = match.group(1), match.group(2)
    fm = {}
    for line in raw.split("\n"):
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            val = val.strip('"').strip("'")
            fm[key] = val
    return fm, raw, rest


def queued_files():
    """Every queued article, lowest sequence number first."""
    if not os.path.isdir(QUEUE_DIR):
        return []
    names = sorted(
        n for n in os.listdir(QUEUE_DIR)
        if n.endswith(".md") and not n.startswith(("_", "."))
        and n.lower() != "readme.md"
    )
    return [os.path.join(QUEUE_DIR, n) for n in names]


def posts_today():
    """How many articles have already gone out today."""
    if not os.path.isdir(POSTS_DIR):
        return 0
    return sum(1 for n in os.listdir(POSTS_DIR)
               if n.startswith(TODAY_STR) and n.endswith(".md"))


def read_log():
    if not os.path.isfile(LOG_FILE):
        return []
    with open(LOG_FILE, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def override_used_today():
    """A manual article is used once per day, not once per run."""
    return any(r.get("date") == TODAY_STR and r.get("source") == "override"
               for r in read_log())


# The review section Malik reads before approving an article. It is internal
# notes to himself and must never reach the site. Stripped here rather than by
# hand, so the queued file keeps the notes and the published post never has them.
FLAGS_HEADING = re.compile(
    r"^##\s*Flags?(?:\s+for\s+Malik)?\b.*$",
    re.IGNORECASE | re.MULTILINE,
)


def strip_flags(body):
    """Remove the '## Flags for Malik' section. Returns (cleaned_body, was_found)."""
    match = FLAGS_HEADING.search(body)
    if not match:
        return body, False

    # Cut from the heading to the next H2, or to the end of the file if it is last.
    tail = body[match.end():]
    following = re.search(r"^##\s+", tail, re.MULTILINE)
    cut_end = match.end() + following.start() if following else len(body)

    cleaned = body[:match.start()].rstrip() + "\n"
    if following:
        cleaned += "\n" + body[cut_end:].lstrip()
    return cleaned, True


def stamp_date(body, date_str):
    """
    Force the front matter date to the real publication moment.

    Uses the actual run time, not a fixed hour. A hardcoded time ahead of the
    run (e.g. 09:00 stamped by the 06:00 job) makes the post future-dated, and
    Jekyll silently refuses to build future-dated posts -- the article would
    publish to the repository but never appear on the site.
    """
    stamped = TODAY.strftime("%Y-%m-%d %H:%M:%S %z")
    if re.search(r"^date:", body, re.M):
        return re.sub(r"^date:.*$", f"date: {stamped}", body, count=1, flags=re.M)
    return re.sub(r"^---\s*$", f"---\ndate: {stamped}", body, count=1, flags=re.M)


LINKMAP = os.path.join(ROOT, "_data", "linkmap.yml")

_LINK_STOP = set("""
a an the and or of for to in on at is are was were be been with by from as it its this that
what who how why when where which pakistan pakistans coinconnect complete guide
2024 2025 2026
""".split())


def _link_topics(title, category, slug):
    """Keywords a future article uses to decide whether to link here."""
    words = re.split(r"[-\s:,&|?()/]+", f"{slug} {title} {category}".lower())
    out = []
    for word in words:
        word = re.sub(r"[^a-z0-9]", "", word)
        if len(word) > 2 and word not in _LINK_STOP and word not in out:
            out.append(word)
    return out[:10]


def add_to_linkmap(title, category, slug):
    """
    Register a newly published article in _data/linkmap.yml so later articles
    can link to it. Without this the link map goes stale the moment the site
    starts publishing, and internal linking only ever points backwards at the
    main site.

    Edited as text rather than via PyYAML so the publisher keeps zero
    third-party dependencies in CI.
    """
    url = f"https://blog.coinconnect.site/{slug}/"

    if not os.path.isfile(LINKMAP):
        log("no _data/linkmap.yml — skipping link map update")
        return

    with open(LINKMAP, encoding="utf-8") as fh:
        text = fh.read()

    if url in text:
        return  # already registered; nothing to do

    entry = (
        f'  - url: "{url}"\n'
        f'    title: "{title.replace(chr(92), "").replace(chr(34), chr(39))}"\n'
        f'    topics: [{", ".join(_link_topics(title, category, slug))}]\n'
    )

    if re.search(r"^blog:\s*\[\]\s*$", text, re.M):
        text = re.sub(r"^blog:\s*\[\]\s*$", "blog:\n" + entry.rstrip(), text, count=1, flags=re.M)
    elif re.search(r"^blog:\s*$", text, re.M):
        text = text.rstrip() + "\n" + entry
    else:
        log("WARNING: could not find the 'blog:' section in linkmap.yml")
        return

    with open(LINKMAP, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text if text.endswith("\n") else text + "\n")

    log(f"added to link map: {url}")


def append_log(date_str, source, title, words):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    new = not os.path.isfile(LOG_FILE)
    safe_title = title.replace('"', "'")
    with open(LOG_FILE, "a", encoding="utf-8", newline="\n") as fh:
        if new:
            fh.write("date,source,title,words\n")
        fh.write(f'{date_str},{source},"{safe_title}",{words}\n')


# -------------------------------------------------------------- validation --

def validate(body, path):
    """Refuse to publish anything that breaks a hard rule."""
    problems = []
    fm, _, article = split_front_matter(body)

    if fm is None:
        return [f"{os.path.basename(path)}: missing or malformed front matter"]

    title = fm.get("title", "")
    desc = fm.get("description", "")

    # --- structural ---
    if not title:
        problems.append("no title in front matter")
    elif len(title) > 75:
        problems.append(f"title too long for search ({len(title)} chars, max 75)")

    if not desc:
        problems.append("no description in front matter")
    elif not (120 <= len(desc) <= 165):
        problems.append(f"description is {len(desc)} chars, should be 120-165")

    category = fm.get("categories", "").strip("[] ")
    if category not in VALID_CATEGORIES:
        problems.append(
            f"category '{category}' is not one of: {', '.join(sorted(VALID_CATEGORIES))}"
        )

    words = len(article.split())
    if words < MIN_WORDS:
        problems.append(f"too short ({words} words, minimum {MIN_WORDS})")
    if words > MAX_WORDS:
        problems.append(f"too long ({words} words, maximum {MAX_WORDS})")

    # --- links ---
    internal = 0
    for host in re.findall(r"https?://([\w.-]+)", article):
        host = host.lower()
        if host.startswith("www."):
            host = host[4:]
        if host in INTERNAL_HOSTS:
            internal += 1
        elif host not in EXTERNAL_HOSTS:
            problems.append(
                f"disallowed link: {host} — external links are limited to "
                "government bodies and intergovernmental organisations"
            )

    if internal < MIN_INTERNAL_LINKS:
        problems.append(
            f"only {internal} internal links, needs at least {MIN_INTERNAL_LINKS} "
            "(link to coinconnect.site pages and other blog articles — see _data/linkmap.yml)"
        )

    # --- structure of the article itself ---
    h2s = re.findall(r"^##\s+(.+)$", article, re.M)
    if len(h2s) < 4:
        problems.append(f"only {len(h2s)} H2 headings, needs at least 4")

    if not any(h.strip().lower().startswith("about this analysis") for h in h2s):
        problems.append("missing the '## About this analysis' closing section")

    return problems


# ------------------------------------------------------------------- modes --

def publish_override():
    """Publish a hand-written article for today, if one is waiting."""
    article_path = os.path.join(OVERRIDES, TODAY_STR, "article.md")
    if not os.path.isfile(article_path):
        return False

    if override_used_today() and not FORCE:
        log("manual article for today has already been published — moving to the queue")
        return False

    log(f"manual article found at {article_path}")
    with open(article_path, encoding="utf-8") as fh:
        body = fh.read().strip()

    body, had_flags = strip_flags(body)
    if had_flags:
        log("removed the 'Flags for Malik' section — internal notes are not published")

    problems = validate(body, article_path)
    if problems:
        log("MANUAL ARTICLE REJECTED — it breaks the house rules:")
        for p in problems:
            log(f"  - {p}")
        raise RuntimeError("manual article failed validation")

    fm, _, article = split_front_matter(body)
    title = fm.get("title", "update")
    body = stamp_date(body, TODAY_STR)

    filename = f"{TODAY_STR}-{slugify(title)}.md"
    if DRY_RUN:
        log(f"DRY RUN — would publish manual article as {filename}")
        return True

    os.makedirs(POSTS_DIR, exist_ok=True)
    with open(os.path.join(POSTS_DIR, filename), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(body)

    add_to_linkmap(title, fm.get("categories", "").strip("[] "), slugify(title))
    append_log(TODAY_STR, "override", title, len(article.split()))
    log(f"published manual article: {filename}")
    log("queue left untouched — the queued article keeps its place")
    return True


def publish_from_queue():
    files = queued_files()
    if not files:
        log("QUEUE EMPTY — nothing to publish. Write a new batch.")
        return False

    path = files[0]
    log(f"next in queue: {os.path.basename(path)} ({len(files)} waiting)")

    with open(path, encoding="utf-8") as fh:
        body = fh.read().strip()

    body, had_flags = strip_flags(body)
    if had_flags:
        log("removed the 'Flags for Malik' section — internal notes are not published")

    problems = validate(body, path)
    if problems:
        log(f"REJECTED {os.path.basename(path)}:")
        for p in problems:
            log(f"  - {p}")
        raise RuntimeError(
            f"{os.path.basename(path)} failed validation — fix it in _queue/ and re-run"
        )

    fm, _, article = split_front_matter(body)
    title = fm["title"]
    body = stamp_date(body, TODAY_STR)
    filename = f"{TODAY_STR}-{slugify(title)}.md"
    words = len(article.split())

    if DRY_RUN:
        log(f"DRY RUN — would publish {filename} ({words} words)")
        log(f"DRY RUN — would remove {os.path.basename(path)} from the queue")
        return True

    os.makedirs(POSTS_DIR, exist_ok=True)
    with open(os.path.join(POSTS_DIR, filename), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(body)
    os.remove(path)

    add_to_linkmap(title, fm.get("categories", "").strip("[] "), slugify(title))
    append_log(TODAY_STR, "queue", title, words)
    log(f"published {filename} ({words} words)")

    remaining = len(files) - 1
    log(f"queue now holds {remaining} article(s) — about {remaining // MAX_POSTS_PER_DAY} day(s) left")

    if remaining <= MAX_POSTS_PER_DAY * 7:
        log(f"WARNING: only {remaining} articles left — time to write a new batch")

    return True


# -------------------------------------------------------------------- main --

def main():
    log(f"run for {TODAY_STR} (PKT)")

    already = posts_today()

    if already >= MAX_POSTS_PER_DAY and not FORCE:
        log(f"daily limit reached ({already} of {MAX_POSTS_PER_DAY}) - stopping")
        log("(re-run from Actions with 'force' ticked to publish anyway)")
        return 0

    # Publish whatever is owed, not a fixed one per run.
    #
    # Each slot has retry runs behind it. A retry that finds nothing owed does
    # nothing and exits quietly; a retry that finds a dropped slot fills it. The
    # effect is that a missed run costs nothing as long as one run in the group
    # gets through.
    due = MAX_POSTS_PER_DAY if FORCE else articles_due_today()
    log(f"due by now: {due}   published today: {already}")

    if already >= due and not FORCE:
        log("nothing owed - this run has nothing to do")
        return 0

    try:
        if publish_override():
            already = posts_today()

        while posts_today() < due:
            before = posts_today()
            if not publish_from_queue():
                break                      # queue is empty; nothing more to do
            if posts_today() == before:
                break                      # dry run, or nothing actually written
            if FORCE:
                break                      # force publishes one extra article only
    except RuntimeError as exc:
        log(f"ERROR: {exc}")
        return 1

    total = posts_today()
    if total < due:
        log(f"NOTE: {total} published but {due} were owed "
            "(queue empty, or an article failed validation)")
    else:
        log(f"up to date: {total} published, {due} owed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
