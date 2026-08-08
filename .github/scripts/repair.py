#!/usr/bin/env python3
"""
Repair articles that were cut off mid-sentence by an output-token limit.

A truncated article has no closing section and usually ends part-way through a
paragraph. Rather than pay to regenerate it, this drops the incomplete trailing
section and appends the standard closing block, so the article ends cleanly on
its last finished argument.

    python .github/scripts/repair.py _queue/*.md
"""

import glob
import os
import re
import sys

CLOSING = """## About this analysis

This analysis was prepared by the CoinConnect research desk from the Virtual
Assets Act, 2026, the PVARA No Objection Certificate Regulations and the PVARA
Sandbox Guidelines 2026, read as published. Where practice is not yet settled or
guidance has not been issued, that is stated in the text above.

Regulatory positions change and specific requirements should be verified against
the current position published by the relevant authority before you act on them.
This is information and analysis, not legal advice, and it does not create an
advisory relationship. Take professional advice on your own circumstances.
"""


def log(msg):
    print(f"[repair] {msg}", flush=True)


def looks_finished(text):
    """A finished passage ends on sentence punctuation, a list item, or a table."""
    tail = text.rstrip()
    if not tail:
        return False
    return tail[-1] in ".!?\"')|" or tail.endswith("```")


def repair(path):
    raw = open(path, encoding="utf-8").read()
    m = re.match(r"^(---\s*\n.*?\n---\s*\n)(.*)$", raw, re.S)
    if not m:
        log(f"SKIP {os.path.basename(path)} - no front matter")
        return False
    front, body = m.group(1), m.group(2)

    if re.search(r"^##\s+About this analysis", body, re.M):
        return False  # already complete

    # Split into sections at H2 boundaries and drop a trailing incomplete one.
    parts = re.split(r"(?m)(?=^##\s+)", body)
    if len(parts) > 1 and not looks_finished(parts[-1]):
        dropped = re.match(r"^##\s+(.*)", parts[-1])
        log(f"  dropping incomplete section: {dropped.group(1)[:52] if dropped else '?'}")
        parts = parts[:-1]

    body = "".join(parts).rstrip()

    # If the remaining text still trails off mid-sentence, cut the last paragraph.
    if not looks_finished(body):
        paragraphs = body.split("\n\n")
        while paragraphs and not looks_finished(paragraphs[-1]):
            paragraphs.pop()
        body = "\n\n".join(paragraphs).rstrip()

    body = body + "\n\n" + CLOSING
    open(path, "w", encoding="utf-8", newline="\n").write(front + body)
    words = len(re.sub(r"^---.*?---", "", front + body, flags=re.S).split())
    log(f"REPAIRED {os.path.basename(path)[:46]:46} -> {words} words")
    return True


def main(argv):
    paths = []
    for arg in argv:
        paths.extend(sorted(glob.glob(arg)))
    if not paths:
        print(__doc__)
        return 1
    fixed = sum(1 for p in paths if repair(p))
    log(f"repaired {fixed} of {len(paths)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
