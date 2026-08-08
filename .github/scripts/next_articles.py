#!/usr/bin/env python3
"""
Print the next N calendar rows that have not been written yet.

Used by the scheduled generation task so each run knows exactly what to write
without having to reason about what already exists.

    python .github/scripts/next_articles.py          # next 5
    python .github/scripts/next_articles.py 10       # next 10
"""

import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CALENDAR = os.path.join(ROOT, "pvara-content-calendar-phase1.md")
QUEUE_DIR = os.path.join(ROOT, "_queue")
POSTS_DIR = os.path.join(ROOT, "_posts")


def written_numbers():
    """Article numbers already queued or published."""
    done = set()
    for path in glob.glob(os.path.join(QUEUE_DIR, "*.md")):
        m = re.match(r"(\d{3})-", os.path.basename(path))
        if m:
            done.add(int(m.group(1)))
    # Published posts lose their number, so match them back by slug.
    published_slugs = {
        re.sub(r"^\d{4}-\d{2}-\d{2}-", "", os.path.basename(p))[:-3]
        for p in glob.glob(os.path.join(POSTS_DIR, "*.md"))
    }
    return done, published_slugs


def rows():
    out = []
    for line in open(CALENDAR, encoding="utf-8"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 6 and re.fullmatch(r"\d{1,3}", cells[0]):
            out.append(cells)
    return out


def main():
    want = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    done, published_slugs = written_numbers()

    pending = []
    for cells in rows():
        n = int(cells[0])
        if n in done:
            continue
        # Skip anything already published under a different filename.
        slug_words = set(re.findall(r"[a-z]+", cells[1].lower()))
        if any(len(slug_words & set(re.findall(r"[a-z]+", s))) >= 4
               for s in published_slugs):
            continue
        pending.append(cells)

    total = len(rows())
    print(f"Written so far : {total - len(pending)} of {total}")
    print(f"Remaining      : {len(pending)}")
    print(f"\nWRITE THESE {min(want, len(pending))} ARTICLES NOW:\n")
    for cells in pending[:want]:
        print(f"--- Article {cells[0]} ---")
        print(f"Working title : {cells[1]}")
        print(f"Category      : {cells[2]}")
        print(f"Target keyword: {cells[3]}")
        print(f"Source        : {cells[4]}")
        print(f"Reader learns : {cells[5]}")
        print(f"Save as       : _queue/{cells[0]}-<slug>.md")
        print()
    if not pending:
        print("ALL ARTICLES WRITTEN - nothing to do.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
