#!/usr/bin/env python3
"""
Build script for the Musings section of The 2601 Salon.

Reads markdown files from _content/musings/*.md, each with YAML-ish front
matter (title, date, slug, summary), and produces:
  - musings/<slug>.html  — one self-contained post page per markdown file
  - musings/index.html   — chronological landing page listing all posts

The landing page is INTENTIONALLY UNLINKED from the main site nav until the
user confirms they want it linked. Posts are reachable only by direct URL.

Run:  python3 _build_musings.py
"""

import os
import re
import html
import datetime
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
CONTENT_DIR = ROOT / "_content" / "musings"
OUT_DIR = ROOT / "musings"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def parse_front_matter(text: str) -> tuple[dict, str]:
    """Very small front matter parser: lines of 'key: value' until '---'."""
    meta = {}
    body = text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            block = text[3:end].strip()
            body = text[end + 4:].lstrip("\n")
            for line in block.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip().lower()] = v.strip().strip('"').strip("'")
    return meta, body


def md_to_html(md: str) -> str:
    """Minimal markdown → HTML for paragraphs, blockquotes, italics, em-dashes."""
    paragraphs = re.split(r"\n\s*\n", md.strip())
    out = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        if p.startswith(">"):
            inner = " ".join(line.lstrip("> ").strip() for line in p.splitlines())
            inner = inline(inner)
            out.append(f"<blockquote>{inner}</blockquote>")
        elif p.startswith("# "):
            out.append(f"<h1>{inline(p[2:].strip())}</h1>")
        elif p.startswith("## "):
            out.append(f"<h2>{inline(p[3:].strip())}</h2>")
        else:
            out.append(f"<p>{inline(p)}</p>")
    return "\n".join(out)


def inline(text: str) -> str:
    """Inline conversions: *italic*, **bold**, en/em dashes, smart quotes light."""
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    # preserve --, ---
    return text


SHELL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · Musings · The 2601 Salon</title>
<meta name="description" content="{summary}">
<meta name="robots" content="{robots}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Lora:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/styles.css">
<style>
  .musings-meta {{ color: var(--muted); font-size: 0.92rem; letter-spacing: 0.04em; margin-bottom: 1.6rem; }}
  .musings-back {{ display:inline-block; margin-top: 2.4rem; font-size: 0.9rem; color: var(--muted); }}
  .preview-banner {{ background: var(--bg-notice); border: 1px solid var(--gold); border-radius: 8px; padding: 10px 14px; margin: 14px 0 28px; font-size: 0.92rem; color: var(--navy); }}
</style>
</head>
<body>
<nav class="topnav">
  <div class="topnav-inner">
    <a class="brand" href="../index.html">2601 · Free Courses</a>
    <div class="links">
      <a href="../index.html#courses">Courses</a>
      <a href="../index.html#about">About</a>
      <a href="../index.html#contact">Contact</a>
    </div>
  </div>
</nav>
<main class="wrap">
{banner}
<article class="card">
  <span class="subtitle">Musings</span>
  <h1>{title}</h1>
  <div class="musings-meta">{date_human}</div>
  {body}
  <a class="musings-back" href="./index.html">← back to all musings</a>
</article>
</main>
</body>
</html>
"""

INDEX_SHELL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Musings · The 2601 Salon</title>
<meta name="description" content="Weekly literary reflections from Professor James F. Mulhern.">
<meta name="robots" content="{robots}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Lora:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/styles.css">
<style>
  .post-row {{ padding: 16px 0; border-bottom: 1px solid var(--border); }}
  .post-row:last-child {{ border-bottom: 0; }}
  .post-row .date {{ font-size: 0.85rem; color: var(--muted); letter-spacing: 0.06em; text-transform: uppercase; }}
  .post-row h3 {{ margin: 4px 0 6px; }}
  .post-row a {{ text-decoration: none; }}
  .post-row a:hover h3 {{ color: var(--maroon); }}
  .preview-banner {{ background: var(--bg-notice); border: 1px solid var(--gold); border-radius: 8px; padding: 10px 14px; margin: 14px 0 28px; font-size: 0.92rem; color: var(--navy); }}
</style>
</head>
<body>
<nav class="topnav">
  <div class="topnav-inner">
    <a class="brand" href="../index.html">2601 · Free Courses</a>
    <div class="links">
      <a href="../index.html#courses">Courses</a>
      <a href="../index.html#about">About</a>
      <a href="../index.html#contact">Contact</a>
    </div>
  </div>
</nav>
<main class="wrap">
{banner}
<div class="card">
  <span class="subtitle">Weekly Reflections</span>
  <h1>Musings</h1>
  <p style="color: var(--muted); margin-bottom: 2rem;">A weekly literary reflection from Professor Mulhern — published every Monday.</p>
  {rows}
</div>
</main>
</body>
</html>
"""

PREVIEW_BANNER = '<div class="preview-banner"><strong>Preview mode.</strong> This page is live but not yet linked from the main site navigation. Remove this banner and link from the homepage once you have approved the section.</div>'


def build():
    posts = []
    if CONTENT_DIR.exists():
        for md_path in sorted(CONTENT_DIR.glob("*.md"), reverse=True):
            text = md_path.read_text(encoding="utf-8")
            meta, body_md = parse_front_matter(text)
            slug = meta.get("slug") or md_path.stem
            title = meta.get("title", "Untitled")
            summary = meta.get("summary", "")
            date_str = meta.get("date", "")
            preview = meta.get("preview", "true").lower() != "false"
            robots = "noindex" if preview else "index,follow"
            banner = PREVIEW_BANNER if preview else ""

            try:
                d = datetime.date.fromisoformat(date_str)
                date_human = d.strftime("%A, %B %-d, %Y")
            except Exception:
                d = datetime.date.today()
                date_human = d.strftime("%A, %B %-d, %Y")

            body_html = md_to_html(body_md)

            out_path = OUT_DIR / f"{slug}.html"
            out_path.write_text(SHELL.format(
                title=html.escape(title),
                summary=html.escape(summary),
                robots=robots,
                banner=banner,
                date_human=date_human,
                body=body_html,
            ), encoding="utf-8")
            posts.append({
                "slug": slug,
                "title": title,
                "summary": summary,
                "date": d,
                "preview": preview,
            })

    # build index
    posts.sort(key=lambda p: p["date"], reverse=True)
    any_preview = any(p["preview"] for p in posts) or not posts
    robots = "noindex" if any_preview else "index,follow"
    rows_html = []
    if not posts:
        rows_html.append('<p style="color: var(--muted);"><em>No posts yet — the first one publishes Monday.</em></p>')
    for p in posts:
        rows_html.append(
            f'<div class="post-row">'
            f'<a href="./{p["slug"]}.html">'
            f'<div class="date">{p["date"].strftime("%A, %B %-d, %Y")}</div>'
            f'<h3>{html.escape(p["title"])}</h3>'
            f'<p style="color: var(--muted); margin: 0;">{html.escape(p["summary"])}</p>'
            f'</a></div>'
        )
    (OUT_DIR / "index.html").write_text(INDEX_SHELL.format(
        banner=PREVIEW_BANNER if any_preview else "",
        rows="\n".join(rows_html),
        robots=robots,
    ), encoding="utf-8")
    print(f"Built {len(posts)} musings post(s) → {OUT_DIR}")


if __name__ == "__main__":
    build()
