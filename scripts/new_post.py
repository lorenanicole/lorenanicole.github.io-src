#!/usr/bin/env python3
"""
new_post.py — Scaffold a new lorenamesa.com blog post.

Usage:
    python3 scripts/new_post.py <source.md> [--images img1.png img2.png ...]

Works with two source types:
  A) A file that already has Pelican front matter (Title:, Date:, Slug: ...)
     — just copies it into content/articles/ and copies images.
  B) A raw Substack/artifact export with no front matter
     — strips header noise (H1, byline, image caption, subtitle, hr)
     — prompts you for the missing meta fields interactively.

Example (A) — already has front matter (e.g. the canonical Download):
    python3 scripts/new_post.py ~/Downloads/my-post.md \\
        --images ~/Downloads/hero-1200x630.png

Example (B) — raw Substack export:
    python3 scripts/new_post.py ~/Downloads/substack-export.md
"""

import argparse
import re
import shutil
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = REPO_ROOT / "content" / "articles"
IMAGES_DIR   = REPO_ROOT / "content" / "images"


def slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s).strip("-")
    return s


def parse_front_matter(lines: list) -> tuple:
    """Parse Pelican 'Key: Value' headers from top of file.
    Returns (meta_dict, body_lines)."""
    meta = {}
    i = 0
    for i, line in enumerate(lines):
        m = re.match(r"^([A-Za-z_][A-Za-z_0-9]*)\s*:\s*(.+)$", line)
        if m:
            meta[m.group(1).lower()] = m.group(2).strip()
        elif line.strip() == "" and meta:
            break
        else:
            break
    return meta, lines[i + 1:] if meta else lines


def strip_substack_header(lines: list) -> list:
    """Remove Substack noise from top: H1, byline, image alt, subtitle, hr."""
    patterns = [
        r"^# .+",
        r"^Oct \d+, \d+.*@.+",
        r"^\[image:.+?\]\\?$",
        r"^\*Subtitle.+?\*$",
        r"^---$",
        r"^$",
    ]
    i = 0
    while i < len(lines):
        if any(re.match(p, lines[i].strip()) for p in patterns):
            i += 1
        else:
            break
    return lines[i:]


def prompt(field: str, default: str = "") -> str:
    hint = f" [{default}]" if default else ""
    val = input(f"  {field}{hint}: ").strip()
    return val or default


def main():
    parser = argparse.ArgumentParser(description="Scaffold a new Pelican blog post.")
    parser.add_argument("source", help="Source markdown file")
    parser.add_argument("--images", nargs="*", default=[], help="Images to copy into content/images/")
    args = parser.parse_args()

    source = Path(args.source).expanduser().resolve()
    if not source.exists():
        sys.exit(f"Error: file not found: {source}")

    lines = source.read_text(encoding="utf-8").splitlines()
    meta, body_lines = parse_front_matter(lines)

    if not meta.get("title"):
        # Raw export path
        body_lines = strip_substack_header(lines)
        print("\nNo Pelican front matter detected — please fill in:\n")
        meta["title"]    = prompt("Title")
        meta["date"]     = prompt("Date (YYYY-MM-DD)", str(date.today()))
        meta["slug"]     = prompt("Slug", slugify(meta["title"]))
        meta["author"]   = prompt("Author", "Lorena Mesa")
        meta["category"] = prompt("Category", "Python")
        meta["tags"]     = prompt("Tags (comma-separated)")
        meta["summary"]  = prompt("Summary")
        meta["og_image"] = prompt("Og_image (e.g. images/hero-1200x630.png)", "")
    else:
        meta.setdefault("slug", slugify(meta["title"]))

    slug = meta["slug"]
    body = "\n".join(body_lines).replace("&#91;", "[").replace("&#93;", "]")

    header = [
        f"Title: {meta.get('title','')}",
        f"Date: {meta.get('date', str(date.today()))}",
        f"Author: {meta.get('author','Lorena Mesa')}",
        f"Category: {meta.get('category','Python')}",
        f"Tags: {meta.get('tags','')}",
        f"Slug: {slug}",
        f"Summary: {meta.get('summary','')}",
    ]
    if meta.get("og_image"):
        header.append(f"Og_image: {meta['og_image']}")

    out_path = ARTICLES_DIR / f"{slug}.md"
    out_path.write_text("\n".join(header) + "\n\n" + body.strip() + "\n", encoding="utf-8")
    print(f"\n✅ Article: {out_path.relative_to(REPO_ROOT)}")

    for img_str in args.images:
        img = Path(img_str).expanduser().resolve()
        if not img.exists():
            print(f"  ⚠️  Not found, skipping: {img}")
            continue
        shutil.copy2(img, IMAGES_DIR / img.name)
        print(f"✅ Image:   content/images/{img.name}")

    print(f"""
✅ Done. Preview at http://localhost:8001 after running:
  pelican -r -l -s pelicanconf_dev.py -o output -p 8001
""")


if __name__ == "__main__":
    main()
