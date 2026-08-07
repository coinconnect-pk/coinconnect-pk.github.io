#!/usr/bin/env python3
"""
Rebuild the main-site half of _data/linkmap.yml from coinconnect.site's sitemap.

The blog half of the map is maintained automatically by publish.py as articles
go out, so this script deliberately preserves whatever is already in it.

Run this whenever pages or posts are added to the main Odoo site:

    python .github/scripts/refresh_linkmap.py
"""

import concurrent.futures
import html
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LINKMAP = os.path.join(ROOT, "_data", "linkmap.yml")

SITEMAP = "https://www.coinconnect.site/sitemap.xml"
SITE = "https://www.coinconnect.site"
UA = {"User-Agent": "Mozilla/5.0 (compatible; CoinConnectLinkMap/1.0)"}

# Odoo system pages that should never be linked from an article.
SKIP = ("/website/info", "/contactus-thank-you", "/web/login")

# Words too generic to help match an article to a link target.
STOP = set("""
a an the and or of for to in on at is are was were be been with by from as it its this that
what who how why when where which pakistan pakistans coinconnect complete guide
2024 2025 2026 amp quot nbsp
""".split())


def log(msg):
    print(f"[linkmap] {msg}", flush=True)


def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "replace")


def topics(url, title):
    """Keywords used to match an article's subject to a sensible link target."""
    path = url.replace(SITE, "").strip("/")
    slug = path.split("/")[-1] if path else "home"
    slug = re.sub(r"-\d+$", "", slug)          # drop Odoo's trailing record id
    words = re.split(r"[-\s:,&|?()/]+", f"{slug} {title}".lower())
    seen, out = [], []
    for word in words:
        word = re.sub(r"[^a-z0-9]", "", word)
        if len(word) > 2 and word not in STOP and word not in seen:
            seen.append(word)
            out.append(word)
    return out[:10]


def page_title(url):
    try:
        markup = fetch(url)
    except Exception as exc:                     # noqa: BLE001 - report and continue
        return url, None, str(exc)
    match = re.search(r"<title[^>]*>(.*?)</title>", markup, re.S | re.I)
    if not match:
        return url, None, "no <title>"
    title = html.unescape(re.sub(r"\s+", " ", match.group(1))).strip()
    title = re.sub(r"\s*[|–-]\s*CoinConnect.*$", "", title).strip()
    return url, title, None


def yaml_quote(value):
    """Safe double-quoted YAML scalar."""
    return '"' + value.replace("\\", "").replace('"', "'") + '"'


def existing_blog_section():
    """Preserve the auto-maintained blog list across refreshes."""
    if not os.path.isfile(LINKMAP):
        return "blog: []"
    with open(LINKMAP, encoding="utf-8") as fh:
        text = fh.read()
    match = re.search(r"^blog:.*", text, re.S | re.M)
    return match.group(0).rstrip() if match else "blog: []"


def main():
    log(f"reading {SITEMAP}")
    try:
        raw = fetch(SITEMAP)
    except Exception as exc:                     # noqa: BLE001
        log(f"ERROR: could not fetch the sitemap: {exc}")
        return 1

    urls = [u.strip() for u in re.findall(r"<loc>(.*?)</loc>", raw, re.S)]
    urls = [u for u in urls if not any(s in u for s in SKIP)]
    log(f"{len(urls)} URLs after filtering system pages")

    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
        for url, title, err in pool.map(page_title, urls):
            if err:
                log(f"  skipped {url} ({err})")
            else:
                results[url] = title

    pages, posts = [], []
    for url in sorted(results):
        entry = {"url": url, "title": results[url], "topics": topics(url, results[url])}
        (posts if "/blog" in url else pages).append(entry)

    lines = [
        "# Internal link map — every CoinConnect URL an article may link to.",
        "#",
        "# main_site.* is rebuilt from the coinconnect.site sitemap by",
        "#   python .github/scripts/refresh_linkmap.py",
        "#",
        "# blog: entries are appended AUTOMATICALLY by publish.py each time an",
        "# article goes out. Do not hand-edit the blog section.",
        "",
        "main_site:",
        "  pages:",
    ]
    for entry in pages:
        lines += [
            f'    - url: {yaml_quote(entry["url"])}',
            f'      title: {yaml_quote(entry["title"])}',
            f'      topics: [{", ".join(entry["topics"])}]',
        ]
    lines += ["", "  blog:"]
    for entry in posts:
        lines += [
            f'    - url: {yaml_quote(entry["url"])}',
            f'      title: {yaml_quote(entry["title"])}',
            f'      topics: [{", ".join(entry["topics"])}]',
        ]
    lines += [
        "",
        "# Articles on blog.coinconnect.site. Appended automatically on publish.",
        existing_blog_section(),
        "",
    ]

    os.makedirs(os.path.dirname(LINKMAP), exist_ok=True)
    with open(LINKMAP, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines))

    log(f"wrote {LINKMAP}")
    log(f"  main-site pages : {len(pages)}")
    log(f"  main-site posts : {len(posts)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
