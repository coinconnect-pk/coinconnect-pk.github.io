#!/usr/bin/env python3
"""
Weave internal links into an article's prose.

Links are inserted where the phrase ALREADY appears in the text, so the anchor
reads naturally and sits in content rather than in a link block at the foot of
the page. Google discounts footer link lists; in-content links carry the weight.

Rules enforced here:
  * never link inside a heading, table, blockquote, code block, or an existing link
  * never link inside the closing "About this analysis" section
  * one link per target, first occurrence only
  * longest phrases matched first, so "capital requirements" wins over "capital"

Usage:
    python .github/scripts/add_links.py _queue/002-who-needs-a-pvara-licence.md
    python .github/scripts/add_links.py _queue/*.md
    python .github/scripts/add_links.py --check _queue/*.md     # report only
"""

import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LINKMAP = os.path.join(ROOT, "_data", "linkmap.yml")

TARGET_LINKS = 12          # aim slightly above the minimum of 10
MIN_LINKS = 10

# Anchors written to match the vocabulary these articles actually use --
# statutory language, not marketing phrasing. Ordered by specificity: the
# longest phrase that matches wins, so "asset-referenced token" beats "token".
#
# Main-site service pages come first because a link there is worth most.
SITE = "https://www.coinconnect.site"
BLOG = f"{SITE}/blog/coinconnect-insights-1"
BLOG3 = f"{SITE}/blog/3"

PRIORITY_ANCHORS = [
    # --- money pages -------------------------------------------------------
    ("no objection certificate",        f"{SITE}/regulatory-licensing"),
    ("licence application",             f"{SITE}/regulatory-licensing"),
    ("licensing framework",             f"{SITE}/pvara-guide"),
    ("licensing regime",                f"{SITE}/pvara-guide"),
    ("SECP",                            f"{SITE}/corporate-setup"),
    ("resident director",               f"{SITE}/corporate-setup"),
    ("incorporation",                   f"{SITE}/corporate-setup"),
    ("Section 285BAA",                  f"{SITE}/tax-banking"),
    ("FBR",                             f"{SITE}/tax-banking"),
    ("bank account",                    f"{SITE}/tax-banking"),
    ("market entry",                    f"{SITE}/launch-growth"),

    # --- statutory concepts to existing articles ---------------------------
    ("virtual asset service provider",  f"{BLOG}/vasp-license-pakistan-3"),
    ("asset-referenced token",          f"{BLOG}/pvara-art-tokenized-gold-issuance-33"),
    ("fiat-referenced token",           f"{BLOG}/pvara-frt-stablecoin-issuance-32"),
    ("customer assets",                 f"{BLOG3}/customer-assets-definition-pvara-pakistan-62"),
    ("capital requirement",             f"{BLOG}/pvara-capital-requirements-pakistan-18"),
    ("fit and proper",                  f"{BLOG}/url-slug-fit-and-proper-test-pvara-form-a3-14"),
    ("closed-loop",                     f"{BLOG3}/pakistan-pvara-closed-loop-token-exemption-2026-60"),
    ("regulatory sandbox",              f"{BLOG}/pvara-sandbox-form-i-complete-walkthrough-2026-8"),
    ("broker-dealer",                   f"{BLOG}/pvara-broker-dealer-license-what-it-covers-27"),
    ("custody",                         f"{BLOG}/pvara-custody-license-safeguarding-customer-assets-25"),
    ("derivatives",                     f"{BLOG}/pvara-derivatives-leverage-license-31"),
    ("stablecoin",                      f"{BLOG}/pvara-frt-stablecoin-issuance-32"),
    ("controller",                      f"{BLOG3}/pakistan-pvara-controller-virtual-assets-act-2026-58"),
    ("goAML",                           f"{BLOG}/fmu-goaml-vasp-pakistan-17"),
    ("mining",                          f"{BLOG3}/pakistan-pvara-virtual-asset-mining-licensing-63"),
    ("Schedule I",                      f"{BLOG}/pvara-license-categories-explained-23"),
    ("sandbox",                         f"{BLOG}/pvara-sandbox-reduced-capital-pakistan-19"),
    ("NFT",                             f"{BLOG3}/nft-exemption-pakistan-pvara-virtual-assets-act-2026-61"),
    ("tax",                             f"{BLOG}/crypto-tax-pakistan-7"),
    ("banking",                         f"{BLOG}/crypto-banking-vasp-15"),

    # --- service categories -------------------------------------------------
    ("transfer and settlement",         f"{BLOG}/pvara-transfer-settlement-license-payments-remittance-28"),
    ("lending",                         f"{BLOG}/pvara-lending-borrowing-license-30"),
    ("investment services",             f"{BLOG}/pvara-management-investment-services-license-29"),
    ("exchange licence",                f"{BLOG}/pvara-exchange-license-requirements-capital-obligations-24"),
    ("tokenised gold",                  f"{BLOG}/pvara-art-tokenized-gold-issuance-33"),

    # --- process and consequences ------------------------------------------
    ("foreign exchange operating",      f"{BLOG}/foreign-crypto-exchange-enter-pakistan-pvara-21"),
    ("ongoing compliance",              f"{BLOG}/pvara-phase-2-compliance-failure-11"),
    ("anti-money laundering",           f"{BLOG3}/fit-and-proper-aml-pvara-mistakes-54"),
    ("AML",                             f"{BLOG3}/fit-and-proper-aml-pvara-mistakes-54"),
    ("refused",                         f"{BLOG3}/pvara-application-rejected-36"),
    ("rejected",                        f"{BLOG3}/pvara-application-rejected-36"),
    ("how long",                        f"{BLOG3}/how-long-pvara-license-takes-39"),
    ("legal in Pakistan",               f"{BLOG}/is-crypto-legal-in-pakistan-13"),
    ("licensing routes",                f"{BLOG}/pvara-routes-compared-sandbox-noc-license-20"),
    ("once the NOC",                    f"{BLOG}/post-noc-pakistan-operational-playbook-12"),

    # --- our own published articles ----------------------------------------
    ("Virtual Assets Act",              "https://blog.coinconnect.site/pakistans-virtual-assets-act-2026-the-complete-guide/"),

    # --- broad fallbacks (matched last) ------------------------------------
    ("virtual asset",                   f"{BLOG}/pvara-license-pakistan-complete-guide-22"),
    ("PVARA",                           f"{SITE}/pvara-guide"),
]

# Slug words that carry no meaning as an anchor phrase.
SLUG_NOISE = {"pvara", "pakistan", "pakistans", "blog", "coinconnect", "insights",
              "the", "a", "an", "and", "or", "of", "for", "to", "in", "on", "is",
              "what", "why", "how", "who", "url", "slug", "guide", "complete",
              "2026", "2025", "under", "your", "you"}


def log(msg):
    print(f"[links] {msg}", flush=True)


def load_linkmap():
    """Minimal reader for our own generated linkmap.yml — no PyYAML dependency."""
    if not os.path.isfile(LINKMAP):
        log("ERROR: _data/linkmap.yml not found — run refresh_linkmap.py first")
        return []
    entries, url, title = [], None, None
    for line in open(LINKMAP, encoding="utf-8"):
        m = re.match(r'\s*-?\s*url:\s*"(.*?)"', line)
        if m:
            url, title = m.group(1), None
            continue
        m = re.match(r'\s*title:\s*"(.*?)"', line)
        if m and url:
            title = m.group(1)
            entries.append((url, title))
            url = None
    return entries


def anchor_from_url(url):
    """Turn a URL slug into a phrase likely to appear in prose."""
    slug = url.rstrip("/").split("/")[-1]
    slug = re.sub(r"-\d+$", "", slug)
    words = [w for w in slug.split("-") if w and w.lower() not in SLUG_NOISE]
    return " ".join(words) if len(words) >= 2 else None


def build_anchors(exclude_url=None):
    """Ordered anchor list: curated money pages first, then derived phrases."""
    anchors = list(PRIORITY_ANCHORS)
    for url, _title in load_linkmap():
        if exclude_url and url.rstrip("/") == exclude_url.rstrip("/"):
            continue
        phrase = anchor_from_url(url)
        if phrase and len(phrase) > 8:
            anchors.append((phrase, url))
    # Longest first so specific phrases win over their substrings.
    anchors.sort(key=lambda a: -len(a[0]))
    return anchors


def linkable_lines(body):
    """Yield (index, line, is_linkable) respecting markdown context."""
    in_code = False
    reached_closing = False
    for i, line in enumerate(body.split("\n")):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            yield i, line, False
            continue
        if re.match(r"^##\s+About this analysis", line, re.I):
            reached_closing = True
        skip = (
            in_code
            or reached_closing
            or not stripped
            or stripped.startswith(("#", ">", "|", "---"))
        )
        yield i, line, not skip


def insert_links(body, anchors, limit=TARGET_LINKS):
    """Insert links into prose, first occurrence of each anchor only."""
    lines = body.split("\n")
    used_urls, added = set(), 0

    for i, line, ok in linkable_lines(body):
        if added >= limit:
            break
        if not ok:
            continue

        for phrase, url in anchors:
            if added >= limit:
                break
            if url in used_urls:
                continue

            # Split the line so we never touch text inside an existing link.
            parts = re.split(r"(\[[^\]]*\]\([^)]*\))", lines[i])
            hit = False
            for idx, part in enumerate(parts):
                if part.startswith("["):
                    continue
                m = re.search(r"\b" + re.escape(phrase) + r"\b", part, re.I)
                if m:
                    matched = part[m.start():m.end()]
                    parts[idx] = (
                        part[:m.start()] + f"[{matched}]({url})" + part[m.end():]
                    )
                    hit = True
                    break
            if hit:
                lines[i] = "".join(parts)
                used_urls.add(url)
                added += 1

    return "\n".join(lines), added


def add_related_block(body, anchors, needed):
    """
    Fallback for articles whose subject simply lacks the vocabulary to carry
    enough in-prose links -- a governance piece has no reason to say "custody".

    Inserted immediately BEFORE the closing section, so it still sits in the
    body of the article rather than below it. Only used to top up; phrase
    matching is always tried first.
    """
    if needed <= 0:
        return body, 0

    already = set(re.findall(r"\]\((https?://[^)]+)\)", body))
    picks = []
    for phrase, url in anchors:
        if url in already or any(url == u for _, u in picks):
            continue
        picks.append((phrase, url))
        if len(picks) >= needed:
            break
    if not picks:
        return body, 0

    # Use the page's real <title> from the link map. Slug-derived labels read
    # like machine output ("Blogpvara licensing gold rush") and belong nowhere
    # near a legal publication.
    titles = {url: title for url, title in load_linkmap()}

    lines = ["", "## Related reading", ""]
    for phrase, url in picks:
        label = titles.get(url) or titles.get(url.rstrip("/"))
        if not label:
            label = phrase[0].upper() + phrase[1:]
        lines.append(f"- [{label}]({url})")
    lines.append("")
    block = "\n".join(lines)

    match = re.search(r"^##\s+About this analysis", body, re.M)
    if match:
        body = body[:match.start()] + block.lstrip("\n") + "\n" + body[match.start():]
    else:
        body = body.rstrip() + "\n" + block
    return body, len(picks)


def count_internal(body):
    hosts = re.findall(r"\]\(https?://([\w.-]+)", body)
    return sum(1 for h in hosts
               if h.lower().replace("www.", "") in
               {"coinconnect.site", "blog.coinconnect.site"})


def process(path, check_only=False):
    raw = open(path, encoding="utf-8").read()
    match = re.match(r"^(---\s*\n.*?\n---\s*\n)(.*)$", raw, re.S)
    if not match:
        log(f"SKIP {os.path.basename(path)} — no front matter")
        return None
    front, body = match.group(1), match.group(2)

    before = count_internal(body)
    if check_only:
        flag = "ok " if before >= MIN_LINKS else "LOW"
        log(f"{flag} {os.path.basename(path)[:46]:46} {before:>3} internal links")
        return before

    if before >= MIN_LINKS:
        log(f"ok   {os.path.basename(path)[:46]:46} already has {before}")
        return before

    # Never let an article link to itself. Published posts are named
    # YYYY-MM-DD-<slug>.md and served at /<slug>/, so the own-URL is derivable.
    name = os.path.basename(path)
    own_slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", name)
    own_slug = re.sub(r"^\d{3}-", "", own_slug)
    own_url = f"https://blog.coinconnect.site/{own_slug[:-3]}/"

    anchors = [a for a in build_anchors() if a[1].rstrip("/") != own_url.rstrip("/")]
    body, added = insert_links(body, anchors, TARGET_LINKS - before)
    after = count_internal(body)

    if after < MIN_LINKS:
        body, extra = add_related_block(body, anchors, MIN_LINKS - after)
        added += extra
        after = count_internal(body)

    open(path, "w", encoding="utf-8", newline="\n").write(front + body)
    status = "OK " if after >= MIN_LINKS else "LOW"
    log(f"{status} {os.path.basename(path)[:46]:46} {before} -> {after} (+{added})")
    return after


def main(argv):
    check_only = "--check" in argv
    paths = []
    for arg in argv:
        if arg.startswith("--"):
            continue
        paths.extend(sorted(glob.glob(arg)))
    if not paths:
        print(__doc__)
        return 1

    results = [process(p, check_only) for p in paths]
    results = [r for r in results if r is not None]
    low = [r for r in results if r < MIN_LINKS]
    log(f"{len(results)} file(s); {len(low)} still below {MIN_LINKS}")
    return 1 if low and not check_only else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
