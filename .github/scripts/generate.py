#!/usr/bin/env python3
"""
Generate articles from the content calendar into _queue/.

Uses the Message Batches API (50% cheaper) with prompt caching on the source
documents (~90% cheaper on the cached part). The three regulatory documents,
the house rules and the link map all sit in a cached system prompt; only the
calendar row changes per request, so the expensive part is paid for once.

    python .github/scripts/generate.py --from 11 --to 30
    python .github/scripts/generate.py --from 11 --to 30 --estimate   # cost only
    python .github/scripts/generate.py --resume batch_abc123          # fetch later

Reads ANTHROPIC_API_KEY from .env in the repository root.
"""

import argparse
import glob
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SOURCE_DIR = os.path.join(os.path.dirname(ROOT), "source-docs")
QUEUE_DIR = os.path.join(ROOT, "_queue")
CALENDAR = os.path.join(ROOT, "pvara-content-calendar-phase1.md")
LINKMAP = os.path.join(ROOT, "_data", "linkmap.yml")
SCRIPTS = os.path.join(ROOT, ".github", "scripts")

MODEL = "claude-opus-5"
MAX_TOKENS = 8000

# Opus 5 list prices per million tokens. Batch halves everything.
PRICE_IN, PRICE_OUT, PRICE_CACHE_READ, PRICE_CACHE_WRITE = 5.0, 25.0, 0.50, 6.25


def log(msg):
    # The Windows console is cp1252 and raises on characters like the
    # approximately sign, so anything non-ASCII is degraded rather than fatal.
    line = f"[generate] {msg}"
    try:
        print(line, flush=True)
    except UnicodeEncodeError:
        print(line.encode("ascii", "replace").decode("ascii"), flush=True)


def load_env():
    path = os.path.join(ROOT, ".env")
    if os.path.isfile(path):
        for line in open(path, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, val = line.partition("=")
                os.environ.setdefault(key.strip(), val.strip())
    if not os.environ.get("ANTHROPIC_API_KEY"):
        log("ERROR: ANTHROPIC_API_KEY not found. Create .env with:")
        log("       ANTHROPIC_API_KEY=sk-ant-...")
        sys.exit(1)


def read_calendar():
    """Parse the calendar's article rows into dicts."""
    if not os.path.isfile(CALENDAR):
        log(f"ERROR: calendar not found at {CALENDAR}")
        sys.exit(1)
    rows = {}
    for line in open(CALENDAR, encoding="utf-8"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 6 or not re.fullmatch(r"\d{1,3}", cells[0]):
            continue
        rows[int(cells[0])] = {
            "n": int(cells[0]),
            "title": cells[1],
            "category": cells[2],
            "keyword": cells[3],
            "source": cells[4],
            "learns": cells[5],
        }
    return rows


def load_sources():
    parts = []
    for path in sorted(glob.glob(os.path.join(SOURCE_DIR, "*.txt"))):
        name = os.path.basename(path).replace(".txt", "")
        text = open(path, encoding="utf-8-sig", errors="replace").read()
        parts.append(f"===== DOCUMENT: {name} =====\n\n{text}")
    if not parts:
        log(f"ERROR: no .txt documents in {SOURCE_DIR} -- run extract_sources.py")
        sys.exit(1)
    return "\n\n".join(parts)


def load_linkmap_text():
    if not os.path.isfile(LINKMAP):
        return "(no link map available)"
    return open(LINKMAP, encoding="utf-8").read()


HOUSE_RULES = """You are the research desk for CoinConnect Intelligence
(blog.coinconnect.site), the publication of CoinConnect -- a regulatory and legal
advisory practice for virtual asset businesses in Karachi, Pakistan. You write
under the byline of Malik Abbas, CEO.

Your goal: rank first on Google, and be the source AI assistants quote when
asked anything about Pakistan's virtual asset framework.

## ACCURACY -- this is legal content, precision is the product

1. Every specific -- section number, threshold, deadline, defined term, penalty,
   form name -- MUST come from the source documents above. If it is not in the
   documents, do not state it: describe the requirement in general terms and
   tell the reader to verify with the authority.
2. NEVER reconstruct a provision from memory. Where your background knowledge
   conflicts with the documents, the documents govern.
3. Quote the operative language in a blockquote wherever exact wording carries
   the obligation.
4. Name the source in the sentence: "Under section X of the Act…".
5. Separate what the rule says (fact) from what it means (analysis). Mark the
   transition: "In practice…", "Our reading is…".
6. Where a provision is ambiguous or guidance has not been issued, SAY SO.
7. Never name a client, partner or exchange. Never describe CoinConnect's own
   results or relationships.

## STRUCTURE -- this is what gets you cited

- Every `##` heading is a QUESTION a real person would ask.
- Answer it COMPLETELY in the first 40-60 words underneath. That paragraph must
  stand alone: if an AI quotes only it, the answer must be correct and useful
  with zero surrounding context. This is the highest-leverage rule here.
- Every passage self-contained. Never "as noted above".
- Define every term and abbreviation on first use.
- At least two lists. Use tables wherever they aid comparison.
- Short sentences, plain words, British English. No hype, no exclamation marks.

## INTERNAL LINKS -- minimum 10 per article

Weave at least 10 markdown links to CoinConnect URLs from the link map above
into the prose. Link on phrases that already belong in the sentence; never a
link list. Prefer the service pages (regulatory-licensing, corporate-setup,
tax-banking) where the subject touches them.

External links ONLY to government bodies (pvara.gov.pk, secp.gov.pk, fbr.gov.pk,
sbp.org.pk, fmu.gov.pk), intergovernmental bodies (fatf-gafi.org, worldbank.org,
imf.org), or chainalysis.com / statista.com. NEVER a law firm, consultancy or
competitor.

## HARD LIMITS -- the article is rejected automatically if any of these break

- 1,200-2,600 words of body text
- Title under 75 characters
- Description between 120 and 165 characters (count them)
- At least four `##` headings
- Must end with `## About this analysis`

## OUTPUT FORMAT -- return ONLY the file, nothing else

---
layout: post
title: "…"
date: 2026-01-01 09:00:00 +0500
categories: [ONE OF: Licensing, Compliance, Tax & Banking, Corporate Setup, Sandbox, Enforcement, Market Entry]
author: "Malik Abbas"
description: "…120-165 characters…"
---

[Two or three short paragraphs. No heading above them.]

## [Question?]

[40-60 word complete answer, then detail.]

… more sections …

## About this analysis

This analysis was prepared by the CoinConnect research desk from [name the
documents], read as published. Where practice is not yet settled or guidance has
not been issued, that is stated above.

Regulatory positions change and specific requirements should be verified against
the current position published by the relevant authority before you act on them.
This is information and analysis, not legal advice, and it does not create an
advisory relationship. Take professional advice on your own circumstances.

## Flags for Malik

[Anything you are unsure of, any conflict between documents, anything needing
his judgement. This section is stripped automatically before publication.]

Do not wrap the output in code fences. Start with the three dashes."""


def build_system(sources, linkmap):
    """Cached system prompt: documents + link map + rules. Paid for once."""
    return [
        {
            "type": "text",
            "text": (
                "The following are the primary source documents. Everything you "
                "write must be traceable to them.\n\n" + sources
            ),
        },
        {
            "type": "text",
            "text": "INTERNAL LINK MAP -- every CoinConnect URL you may link to:\n\n" + linkmap,
        },
        {
            "type": "text",
            "text": HOUSE_RULES,
            # 1h TTL: batches usually finish inside the hour, so the cache is
            # still warm for later requests in the same submission.
            "cache_control": {"type": "ephemeral", "ttl": "1h"},
        },
    ]


def user_prompt(row):
    return (
        f"Write article {row['n']:03d} from the content calendar.\n\n"
        f"Working title : {row['title']}\n"
        f"Category      : {row['category']}\n"
        f"Target keyword: {row['keyword']}\n"
        f"Source         : {row['source']}\n"
        f"The reader learns: {row['learns']}\n\n"
        "Read the relevant provisions in the source documents above and write the "
        "complete article file. You may improve on the working title if a better "
        "one serves the target keyword, but stay under 75 characters."
    )


def slugify(text):
    text = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    return re.sub(r"[\s_-]+", "-", text)[:60].strip("-")


def estimate(rows, sources, linkmap):
    approx_cached = (len(sources) + len(linkmap) + len(HOUSE_RULES)) // 4
    per_fresh, per_out = 400, 2700
    n = len(rows)
    write = approx_cached * PRICE_CACHE_WRITE / 1e6
    read = approx_cached * PRICE_CACHE_READ / 1e6 * n
    fresh = per_fresh * PRICE_IN / 1e6 * n
    out = per_out * PRICE_OUT / 1e6 * n
    total = (write + read + fresh + out) * 0.5      # batch discount
    log(f"cached prefix ~ {approx_cached:,} tokens")
    log(f"estimate for {n} articles ~ ${total:.2f}  (~ ${total/max(n,1):.3f} each)")
    log("(assumes cache hits; a cold cache is roughly 3x the input cost)")
    return total


def submit(client, rows, sources, linkmap):
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    from anthropic.types.messages.batch_create_params import Request

    system = build_system(sources, linkmap)
    requests = [
        Request(
            custom_id=f"art-{row['n']:03d}",
            params=MessageCreateParamsNonStreaming(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                system=system,
                messages=[{"role": "user", "content": user_prompt(row)}],
            ),
        )
        for row in rows
    ]
    batch = client.messages.batches.create(requests=requests)
    log(f"submitted batch {batch.id} with {len(requests)} articles")
    return batch.id


def collect(client, batch_id, rows_by_id):
    log(f"waiting on batch {batch_id} …")
    waited = 0
    while True:
        batch = client.messages.batches.retrieve(batch_id)
        if batch.processing_status == "ended":
            break
        counts = batch.request_counts
        log(f"  {batch.processing_status}: {counts.succeeded} done, "
            f"{counts.processing} processing ({waited//60}m elapsed)")
        time.sleep(30)
        waited += 30

    os.makedirs(QUEUE_DIR, exist_ok=True)
    written, failed = [], []
    usage = {"in": 0, "out": 0, "cread": 0, "cwrite": 0}

    for result in client.messages.batches.results(batch_id):
        n = int(result.custom_id.split("-")[1])
        if result.result.type != "succeeded":
            failed.append((n, result.result.type))
            continue
        msg = result.result.message
        u = msg.usage
        usage["in"] += u.input_tokens
        usage["out"] += u.output_tokens
        usage["cread"] += getattr(u, "cache_read_input_tokens", 0) or 0
        usage["cwrite"] += getattr(u, "cache_creation_input_tokens", 0) or 0

        text = "".join(b.text for b in msg.content if b.type == "text").strip()
        text = re.sub(r"^```[a-zA-Z]*\n|\n```$", "", text).strip()
        if not text.startswith("---"):
            failed.append((n, "no front matter"))
            continue

        m = re.search(r'^title:\s*"?(.+?)"?\s*$', text, re.M)
        slug = slugify(m.group(1)) if m else f"article-{n:03d}"
        path = os.path.join(QUEUE_DIR, f"{n:03d}-{slug}.md")
        open(path, "w", encoding="utf-8", newline="\n").write(text + "\n")
        written.append(path)

    log(f"wrote {len(written)} articles; {len(failed)} failed")
    for n, why in failed:
        log(f"  FAILED {n:03d}: {why}")

    cost = (
        usage["in"] * PRICE_IN
        + usage["out"] * PRICE_OUT
        + usage["cread"] * PRICE_CACHE_READ
        + usage["cwrite"] * PRICE_CACHE_WRITE
    ) / 1e6 * 0.5
    log("ACTUAL usage:")
    log(f"  cache writes {usage['cwrite']:>9,}   cache reads {usage['cread']:>9,}")
    log(f"  fresh input  {usage['in']:>9,}   output      {usage['out']:>9,}")
    log(f"  cost ${cost:.2f} total  (${cost/max(len(written),1):.3f} per article)")
    return written


def postprocess(paths):
    if not paths:
        return
    log("adding internal links …")
    subprocess.run([sys.executable, os.path.join(SCRIPTS, "add_links.py")] + paths, check=False)
    log("validating …")
    sys.path.insert(0, SCRIPTS)
    import publish  # noqa: E402
    ok = 0
    for p in paths:
        raw = open(p, encoding="utf-8").read().strip()
        body, _ = publish.strip_flags(raw)
        problems = publish.validate(body, p)
        if problems:
            log(f"  NEEDS FIXING {os.path.basename(p)}")
            for x in problems:
                log(f"      - {x}")
        else:
            ok += 1
    log(f"{ok}/{len(paths)} ready to publish")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="start", type=int, default=11)
    ap.add_argument("--to", dest="end", type=int, default=30)
    ap.add_argument("--estimate", action="store_true")
    ap.add_argument("--resume", metavar="BATCH_ID")
    args = ap.parse_args()

    load_env()
    import anthropic

    calendar = read_calendar()
    sources = load_sources()
    linkmap = load_linkmap_text()
    log(f"calendar has {len(calendar)} articles")

    existing = {int(m.group(1)) for f in glob.glob(os.path.join(QUEUE_DIR, "*.md"))
                if (m := re.match(r"(\d{3})-", os.path.basename(f)))}
    rows = [calendar[n] for n in sorted(calendar)
            if args.start <= n <= args.end and n not in existing]
    log(f"{len(rows)} to generate (skipping {len(existing)} already in the queue)")

    if args.estimate:
        estimate(rows, sources, linkmap)
        return 0
    if not rows and not args.resume:
        log("nothing to do")
        return 0

    client = anthropic.Anthropic()
    batch_id = args.resume or submit(client, rows, sources, linkmap)
    paths = collect(client, batch_id, {r["n"]: r for r in rows})
    postprocess(paths)
    log("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
