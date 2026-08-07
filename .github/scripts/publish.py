#!/usr/bin/env python3
"""
CoinConnect Intelligence — daily article publisher.

This is a QUEUE publisher, not a generator. Unlike the Sarzif build, nothing
here calls a model API. Articles are written in advance by Claude in batched
sessions, committed into _queue/, and released one per day.

Order of operations each run:

  1. If a post already exists for today, stop (unless FORCE=1).
  2. Look for a manual article in overrides/<today>/article.md
     -> if found, publish that and DO NOT consume the queue, so the queued
        article simply runs the next day instead.
  3. Otherwise take the lowest-numbered file in _queue/, validate it, stamp
     today's date on it, move it into _posts/, and log it.

Environment:
  DRY_RUN   optional, "1" validates and prints but writes nothing
  FORCE     optional, "1" publishes even if today already has a post
"""

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

MIN_WORDS = 1200
MAX_WORDS = 2100

VALID_CATEGORIES = {
    "Market Entry",
    "Listings",
    "PR & Comms",
    "Partnerships",
    "Positioning",
    "Market Data",
}

# Only these hosts may be linked from an article.
ALLOWED_LINK_HOSTS = {
    "coinconnect.site",
    "blog.coinconnect.site",
    "pvara.gov.pk",
    "secp.gov.pk",
    "sbp.org.pk",
    "fbr.gov.pk",
    "fatf-gafi.org",
    "worldbank.org",
    "imf.org",
    "chainalysis.com",
    "statista.com",
}

# --------------------------------------------------------- SARZIF FIREWALL --
#
# Sarzif Policy (Noor Aslam's separate company) owns Pakistan's crypto
# REGULATORY keyword set and has 120 queued articles on it. CoinConnect
# Intelligence answers a different question -- "how do I enter and win this
# market?" -- and must never compete for those terms.
#
# These phrases are banned from the TITLE and DESCRIPTION, which is what
# actually determines the keyword an article targets. They remain legal in
# body text, because regulation is often necessary context inside a
# commercial article. It just may never be the subject of one.
#
# The second list is banned everywhere in the title because those terms are
# the money-page keywords of coinconnect.site itself -- the blog must not
# cannibalise its own parent domain either.

SARZIF_RESERVED = [
    "pvara licence", "pvara license", "pvara licensing",
    "vasp licence", "vasp license", "vasp licensing",
    "noc application", "noc requirements", "how to get a noc",
    "travel rule",
    "aml/cft", "aml cft", "anti-money laundering",
    "fit and proper",
    "goaml", "go-aml",
    "section 285baa",
    "sandbox eligibility", "regulatory sandbox requirements",
    "compliance requirements", "licensing requirements",
    "kyc requirements",
    "virtual assets act", "virtual assets ordinance",
    "mlro",
]

PARENT_RESERVED = [
    "crypto market entry pakistan",
    "pakistan market entry consultancy",
    "blockchain consultancy pakistan",
]


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


def post_exists_for_today():
    """Guard against double-publishing if the workflow is triggered twice."""
    if not os.path.isdir(POSTS_DIR):
        return False
    return any(name.startswith(TODAY_STR) for name in os.listdir(POSTS_DIR))


def stamp_date(body, date_str):
    """Force the front matter date to the real publication date."""
    stamped = f"{date_str} 09:00:00 +0500"
    if re.search(r"^date:", body, re.M):
        return re.sub(r"^date:.*$", f"date: {stamped}", body, count=1, flags=re.M)
    return re.sub(r"^---\s*$", f"---\ndate: {stamped}", body, count=1, flags=re.M)


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

    # --- the Sarzif firewall ---
    headline_text = f"{title} {desc}".lower()
    for phrase in SARZIF_RESERVED:
        if phrase in headline_text:
            problems.append(
                f"SARZIF COLLISION: '{phrase}' appears in the title/description. "
                "That keyword belongs to Sarzif Policy. Regulation may be context "
                "inside the article, never its subject."
            )
    for phrase in PARENT_RESERVED:
        if phrase in title.lower():
            problems.append(
                f"PARENT COLLISION: '{phrase}' in the title competes with "
                "coinconnect.site's own money pages."
            )

    # --- links ---
    for host in re.findall(r"https?://([\w.-]+)", article):
        host = host.lower()
        if host.startswith("www."):
            host = host[4:]
        if host not in ALLOWED_LINK_HOSTS:
            problems.append(f"disallowed link: {host}")

    if article.lower().count("coinconnect.site") > 1:
        problems.append("more than one CoinConnect link in the body")

    # --- structure of the article itself ---
    h2s = re.findall(r"^##\s+(.+)$", article, re.M)
    if len(h2s) < 4:
        problems.append(f"only {len(h2s)} H2 headings, needs at least 4")

    if not any(h.strip().lower().startswith("about this analysis") for h in h2s):
        problems.append("missing the '## About this analysis' closing section")

    return problems


# ------------------------------------------------------------------- modes --

def publish_override():
    """Publish a hand-written article for today, if one exists."""
    article_path = os.path.join(OVERRIDES, TODAY_STR, "article.md")
    if not os.path.isfile(article_path):
        return False

    log(f"manual override found at {article_path}")
    with open(article_path, encoding="utf-8") as fh:
        body = fh.read().strip()

    problems = validate(body, article_path)
    if problems:
        log("OVERRIDE REJECTED — it breaks the house rules:")
        for p in problems:
            log(f"  - {p}")
        raise RuntimeError("manual override failed validation")

    fm, _, article = split_front_matter(body)
    title = fm.get("title", "update")
    body = stamp_date(body, TODAY_STR)

    filename = f"{TODAY_STR}-{slugify(title)}.md"
    if DRY_RUN:
        log(f"DRY RUN — would publish override as {filename}")
        return True

    os.makedirs(POSTS_DIR, exist_ok=True)
    with open(os.path.join(POSTS_DIR, filename), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(body)

    append_log(TODAY_STR, "override", title, len(article.split()))
    log(f"published override: {filename}")
    # Deliberately do NOT consume the queue. The queued article waits its turn.
    log("queue left untouched — tomorrow's queued article is unaffected")
    return True


def publish_from_queue():
    files = queued_files()
    if not files:
        log("QUEUE EMPTY — nothing to publish. Generate a new batch.")
        return False

    path = files[0]
    log(f"next in queue: {os.path.basename(path)} ({len(files)} remaining)")

    with open(path, encoding="utf-8") as fh:
        body = fh.read().strip()

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

    append_log(TODAY_STR, "queue", title, words)
    log(f"published {filename} ({words} words)")
    log(f"queue now holds {len(files) - 1} article(s)")

    remaining = len(files) - 1
    if remaining <= 7:
        log(f"WARNING: only {remaining} days of queue left — time to generate a new batch")

    return True


# -------------------------------------------------------------------- main --

def main():
    log(f"run for {TODAY_STR} (PKT)")

    if post_exists_for_today():
        if not FORCE:
            log("a post already exists for today — stopping so nothing is duplicated")
            log("(re-run from Actions with 'force' ticked to publish anyway)")
            return 0
        log("a post already exists for today, but FORCE is set — publishing anyway")

    try:
        if publish_override():
            return 0
        publish_from_queue()
    except RuntimeError as exc:
        log(f"ERROR: {exc}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
