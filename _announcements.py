"""Shared announcement renderer — used by both home and course-page builders.

Single source: /home/user/workspace/courses_2601/_content/_announcements.md

Entries are separated by lines containing only `---`. Each entry starts with
`posted: <human date>` on the first line, then a blank line, then the body
(plain text + simple inline HTML allowed). Newest first.
"""
import os, re

ANN_PATH = os.path.join(os.path.dirname(__file__), "_content", "_announcements.md")


def _parse_entries(text: str):
    # Drop everything up to (and including) the first --- separator (preamble)
    parts = re.split(r'^---\s*$', text, flags=re.MULTILINE)
    entries = []
    # First part is preamble; the rest alternate: entry, separator-aftermath, entry, ...
    for chunk in parts[1:]:
        chunk = chunk.strip()
        if not chunk:
            continue
        # First line must be `posted: ...`
        m = re.match(r'^posted:\s*(.+?)\s*\n', chunk, flags=re.IGNORECASE)
        if not m:
            continue
        posted = m.group(1).strip()
        body = chunk[m.end():].strip()
        if not body:
            continue
        entries.append({"posted": posted, "body": body})
    return entries


def render_notice_block(heading: str = "Notices &amp; Announcements") -> str:
    """Return an HTML string with the entire Notices band, ready to drop into a page.

    If there are no announcements, returns an empty string (band hidden entirely).
    """
    if not os.path.exists(ANN_PATH):
        return ""
    with open(ANN_PATH) as f:
        entries = _parse_entries(f.read())
    if not entries:
        return ""

    cards = []
    for e in entries:
        cards.append(
            '<div class="notice-card">'
            f'<div class="date">Posted {e["posted"]}</div>'
            f'<div class="body">{e["body"]}</div>'
            '</div>'
        )

    return (
        '<section class="notices-band" aria-label="Notices and announcements">'
        f'<div class="notices-heading">{heading}</div>'
        + "".join(cards)
        + '</section>'
    )
