#!/usr/bin/env python3
"""
Convert the source regulatory documents to plain text for the generator.

PDFs and .docx files are extracted once and cached as .txt beside the original.
Extraction is the step where section numbers get mangled, so the output is
checked for the citation patterns the articles depend on and the result is
reported rather than assumed.

Usage:
    python .github/scripts/extract_sources.py
    python .github/scripts/extract_sources.py --force    # re-extract everything
"""

import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SOURCE_DIR = os.path.join(os.path.dirname(ROOT), "source-docs")


def log(msg):
    print(f"[extract] {msg}", flush=True)


def from_docx(path):
    """Read a .docx without python-docx: it is a zip containing document.xml."""
    with zipfile.ZipFile(path) as zf:
        xml = zf.read("word/document.xml").decode("utf-8", "replace")
    # Paragraph and line breaks become newlines; everything else is dropped.
    xml = re.sub(r"</w:p>", "\n", xml)
    xml = re.sub(r"<w:br[^>]*/>", "\n", xml)
    xml = re.sub(r"<w:tab[^>]*/>", "\t", xml)
    text = re.sub(r"<[^>]+>", "", xml)
    text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    text = text.replace("&quot;", '"').replace("&apos;", "'")

    # Word leaves field codes behind in tables of contents. They are pure noise
    # that would otherwise be sent to the model on every single request.
    text = re.sub(r"PAGEREF\s+_Toc\d+\s*\\h", "", text)
    text = re.sub(r'TOC\s+\\o\s+"[^"]*"(\s+\\[a-z])*', "", text)
    text = re.sub(r"[ \t]{2,}", " ", text)

    return re.sub(r"\n{3,}", "\n\n", text).strip()


def from_pdf(path):
    try:
        import pdfplumber
    except ImportError:
        log("ERROR: pdfplumber is not installed — run: pip install pdfplumber")
        return None
    pages = []
    with pdfplumber.open(path) as pdf:
        for i, page in enumerate(pdf.pages, 1):
            txt = page.extract_text() or ""
            pages.append(txt)
    text = "\n\n".join(pages)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def quality_report(name, text):
    """Report on the patterns citations rely on, rather than assuming they survived."""
    checks = {
        "numbered provisions (e.g. '12.')": len(re.findall(r"^\s*\d{1,3}\.\s", text, re.M)),
        "sub-clauses (e.g. '(2)' or '(a)')": len(re.findall(r"\(\s*[0-9a-z]{1,3}\s*\)", text)),
        "'Regulation' references": len(re.findall(r"\bregulation\b", text, re.I)),
        "'Schedule' references": len(re.findall(r"\bschedule\b", text, re.I)),
        "Form references (Form A1 etc.)": len(re.findall(r"\bForm\s+[A-Z]?-?\d", text)),
    }
    log(f"  {name}: {len(text):,} chars (~{len(text)//4:,} tokens)")
    for label, count in checks.items():
        log(f"     {label}: {count}")
    if len(text) < 2000:
        log("     WARNING: suspiciously short — extraction may have failed")


def main(argv):
    force = "--force" in argv
    if not os.path.isdir(SOURCE_DIR):
        log(f"ERROR: {SOURCE_DIR} does not exist")
        return 1

    handled = 0
    for name in sorted(os.listdir(SOURCE_DIR)):
        path = os.path.join(SOURCE_DIR, name)
        stem, ext = os.path.splitext(name)
        ext = ext.lower()

        if ext == ".txt":
            with open(path, encoding="utf-8-sig", errors="replace") as fh:
                quality_report(name, fh.read())
            handled += 1
            continue

        if ext not in (".pdf", ".docx"):
            continue

        out = os.path.join(SOURCE_DIR, stem + ".txt")
        if os.path.exists(out) and not force:
            log(f"  {name}: already extracted (use --force to redo)")
            continue

        log(f"extracting {name} …")
        text = from_docx(path) if ext == ".docx" else from_pdf(path)
        if not text:
            log(f"  FAILED to extract {name}")
            continue

        with open(out, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        quality_report(os.path.basename(out), text)
        handled += 1

    log(f"done — {handled} document(s) ready")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
