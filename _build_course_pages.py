"""Build each course page in the Art of Telling pattern:
three collapsible sections (Important Info, The Sessions, The Readings),
with sessions shown as a grid of buttons that each open just one session inline."""
import os
import re
import sys
import markdown
from _partials import page

CONTENT_DIR = "_content"
OUT_DIR = "courses"
WHITEBOARD_URL = "https://whiteboard.silvercurrentpress.com"

COURSES = {
    "american_lit": {
        "title": "Survey of American Literature",
        "subtitle": "Sixteen Sessions",
        "desc": "A free 16-week community course in American literature for residents of 2601.",
    },
    "poetry": {
        "title": "Reading Poetry: A Beginner's Welcome",
        "subtitle": "Sixteen Sessions",
        "desc": "A free 16-week beginners' poetry course for residents of 2601.",
    },
    "memoir": {
        "title": "The Personal Essay & Memoir",
        "subtitle": "Sixteen Sessions",
        "desc": "A free 16-week course on personal essay and memoir for residents of 2601.",
    },
    "shakespeare": {
        "title": "Shakespeare's Sonnets & Famous Speeches",
        "subtitle": "Sixteen Sessions",
        "desc": "A free 16-week course on Shakespeare's sonnets and most famous monologues for residents of 2601.",
    },
    "women_writers": {
        "title": "Women in American Literature",
        "subtitle": "Sixteen Sessions",
        "desc": "A free 16-week course on American women writers, for residents of 2601.",
    },
    "minority_voices": {
        "title": "Minority Voices in American Literature",
        "subtitle": "Sixteen Sessions",
        "desc": "A free 16-week course on Black, Latinx, Asian American, Native American, and immigrant American voices, for residents of 2601.",
    },
    "jewish_writers": {
        "title": "Jewish Writers: A Literary Tradition",
        "subtitle": "Sixteen Sessions",
        "desc": "A free 16-week course on Jewish American and international Jewish literature, for residents of 2601.",
    },
    "irish_lit": {
        "title": "The Irish Literary Imagination",
        "subtitle": "Sixteen Sessions",
        "desc": "A free 16-week course on Irish literature, for residents of 2601.",
    },
    "revision_workshop": {
        "title": "The Craft of Revision — A Writers' Workshop",
        "subtitle": "Sixteen Sessions",
        "desc": "A free 16-week writers' workshop on revision, for residents of 2601.",
    },
    "lit_and_history": {
        "title": "Literature & American History — A Cross-Reading",
        "subtitle": "Sixteen Sessions",
        "desc": "A free 16-week course pairing primary historical documents with the literary works that answer them, for residents of 2601.",
    },
    "writing_life": {
        "title": "The Writing Life: Getting Published",
        "subtitle": "Sixteen Sessions",
        "desc": "The literary magazine scene, cover letters and queries, agents, small presses, contests \u2014 the practical work of becoming a published writer, taught by a working writer and former editor.",
    },
}

# Sections that belong in each of the three top-level collapsibles.
# These match the H2 headings we typically find inside the syllabi.
SECTION_BUCKETS = {
    "info": {
        "label": "Important Information & Course Materials",
        # Match by case-insensitive substring of the H2 text.
        "match_patterns": [
            "an invitation", "welcome", "what this course is", "what this course is not",
            "course details", "what to expect", "a few promises", "a few asks",
            "schedule at a glance", "workshop norms", "a note on readings",
            "literary terms glossary", "glossary", "reading companion", "about me",
        ],
    },
    "sessions": {
        "label": "The Sessions",
        "match_patterns": ["the sessions"],
    },
    "readings": {
        "label": "All the Readings",
        "match_patterns": ["all course readings", "all the readings", "all course resources"],
    },
}


def md_to_html(md_text):
    """Convert markdown text to HTML, preserving headings + ids."""
    return markdown.markdown(
        md_text,
        extensions=["extra", "sane_lists", "smarty", "toc"],
        output_format="html5",
    )


def split_into_sections(md_text):
    """Walk the markdown and return a list of (level, title, body_md) tuples.
    Level 2 = top-level section, Level 3 = subsection (typically Session N)."""
    md_text = re.sub(r"^# .*$", "", md_text, count=1, flags=re.MULTILINE).strip()
    # Split on H2 boundaries while preserving them
    parts = re.split(r"\n(?=## )", md_text)
    sections = []
    for part in parts:
        m = re.match(r"^## (.+?)\s*\n(.*)", part, flags=re.DOTALL)
        if not m:
            continue
        title = m.group(1).strip()
        body = m.group(2).strip()
        # Determine the H3 boundary. In the AOT six-tab format, each session
        # ("### Session N — ...") contains its own H3 subsections
        # (### Main Points of the Lesson, ### Reading, ### Critical Reception,
        # ### In-Class Practice, ### Discussion Questions, ### Homework).
        # Those inner H3s must NOT be treated as separate sessions, so when a
        # body contains "### Session" headings we split only on those and keep
        # the inner H3s inside each session body. Otherwise we fall back to
        # splitting on every H3 (the older bold-label / plain layouts).
        if re.search(r"(?m)^### Session\b", body):
            split_pat = r"\n(?=### Session\b)"
            session_mode = True
        else:
            split_pat = r"\n(?=### )"
            session_mode = False
        subs = re.split(split_pat, body)
        # First chunk is the body before any H3 boundary
        first_is_heading = subs[0].startswith("### Session") if session_mode else subs[0].startswith("### ")
        lead = subs[0].strip() if not first_is_heading else ""
        subsections = []
        for sub in subs:
            is_boundary = sub.startswith("### Session") if session_mode else sub.startswith("### ")
            if is_boundary:
                m3 = re.match(r"^### (.+?)\s*\n(.*)", sub, flags=re.DOTALL)
                if m3:
                    subsections.append((m3.group(1).strip(), m3.group(2).strip()))
        sections.append({"title": title, "lead_md": lead, "subs": subsections})
    return sections


def bucket_for_section(title):
    t = title.lower()
    for bucket, info in SECTION_BUCKETS.items():
        for pat in info["match_patterns"]:
            if pat in t:
                return bucket
    # Default: info bucket (covers anything we forgot)
    return "info"


def render_session_button(idx, sub_title, sub_id):
    """A clickable navy session button (grid item) that toggles the detail panel."""
    return (
        f'<a class="session-btn" href="#{sub_id}" '
        f'data-target="session-panel-{idx}">{sub_title}</a>'
    )


def render_session_panel(idx, sub_id, sub_title, sub_body_html):
    """The detail panel for one session, hidden by default."""
    return (
        f'<div class="session-panel" id="session-panel-{idx}" data-anchor="{sub_id}">'
        f'<div class="session-panel-inner">'
        f'<a class="session-close" href="#sessions-top">‹ Close</a>'
        f'<h3 id="{sub_id}">{sub_title}</h3>'
        f'{sub_body_html}'
        f'</div></div>'
    )


def build_course(slug):
    md_path = os.path.join(CONTENT_DIR, f"{slug}.md")
    if not os.path.exists(md_path):
        print(f"  [skip] {slug}: content not yet written")
        return False
    meta = COURSES[slug]
    with open(md_path) as f:
        md_text = f.read()

    sections = split_into_sections(md_text)

    # Group sections into the three buckets
    buckets = {"info": [], "sessions": [], "readings": []}
    for sec in sections:
        buckets[bucket_for_section(sec["title"])].append(sec)

    # -------- Render "Important Information" bucket --------
    info_inner = []
    for sec in buckets["info"]:
        # Build the section as a clickable inner collapsible (like AOT's "Welcome", "Syllabus")
        inner_body_md = sec["lead_md"]
        # If this section has subsections (rare for info), inline them
        for sub_title, sub_body_md in sec["subs"]:
            inner_body_md += f"\n\n#### {sub_title}\n\n{sub_body_md}"
        inner_html = md_to_html(inner_body_md)
        sec_id = re.sub(r"[^a-z0-9]+", "-", sec["title"].lower()).strip("-")
        info_inner.append(
            f'<details class="info-item" id="{sec_id}">'
            f'<summary><span>{sec["title"]}</span><span class="chev">▾</span></summary>'
            f'<div class="info-body">{inner_html}</div>'
            f'</details>'
        )
    info_block = (
        '<details class="topbar" id="topbar-info">'
        '<summary><span>Important Information & Course Materials</span>'
        '<span class="chev">▾</span></summary>'
        '<div class="topbar-body">'
        + "".join(info_inner)
        + '</div></details>'
    )

    # -------- Render "The Sessions" bucket --------
    sessions_buttons = []
    sessions_panels = []
    # Sessions live as ### subsections under the H2 "The Sessions"
    all_sessions = []
    for sec in buckets["sessions"]:
        all_sessions.extend(sec["subs"])
    for idx, (sub_title, sub_body_md) in enumerate(all_sessions, start=1):
        sub_id = re.sub(r"[^a-z0-9]+", "-", sub_title.lower()).strip("-")
        sub_html = md_to_html(sub_body_md)
        sessions_buttons.append(render_session_button(idx, sub_title, sub_id))
        sessions_panels.append(render_session_panel(idx, sub_id, sub_title, sub_html))

    sessions_block = (
        '<details class="topbar" id="topbar-sessions">'
        '<summary><span>The Sessions</span><span class="chev">▾</span></summary>'
        '<div class="topbar-body" id="sessions-top">'
        '<div class="session-grid">'
        + "".join(sessions_buttons)
        + '</div>'
        '<div class="session-panels">'
        + "".join(sessions_panels)
        + '</div>'
        '</div></details>'
    ) if sessions_buttons else ""

    # -------- Render "The Readings" bucket --------
    readings_inner = []
    for sec in buckets["readings"]:
        readings_inner.append(md_to_html(sec["lead_md"]))
        for sub_title, sub_body_md in sec["subs"]:
            readings_inner.append(f"<h4>{sub_title}</h4>" + md_to_html(sub_body_md))
    readings_block = (
        '<details class="topbar" id="topbar-readings">'
        '<summary><span>All the Readings</span><span class="chev">▾</span></summary>'
        '<div class="topbar-body">'
        + "".join(readings_inner)
        + '</div></details>'
    ) if readings_inner else ""

    # -------- Compose page body --------
    from _announcements import render_notice_block
    notices_band = render_notice_block()
    body = f"""
{notices_band}

<div class="hero">
  <h1>{meta['title']}</h1>
  <span class="subtitle">{meta['subtitle']}</span>
  <p style="color:#E9D8A6;margin:14px auto 0;max-width:540px;font-size:1.0rem;">
    A free literary course for the residents of 2601 · taught by James F. Mulhern
  </p>
</div>

<div style="text-align:center;margin:-12px 0 26px;">
  <a href="../index.html" style="color:var(--maroon);font-weight:600;text-decoration:none;">‹ Back to all courses</a>
</div>

<h2 class="prompt-h">What would you like to see?</h2>
<p class="prompt-sub">Click any button below.</p>

<div class="topbars">
  {info_block}
  {sessions_block}
  {readings_block}
</div>

<a class="cta-btn" href="{WHITEBOARD_URL}" target="_blank" rel="noopener">Open the Whiteboard →</a>

<hr class="rule">
<p style="text-align:center;color:var(--muted);"><a href="../index.html" style="color:var(--navy);font-weight:600;text-decoration:none;">‹ Back to the 2601 Salon</a></p>

<script>
// Session button → open its panel, scroll the panel into view, close others
document.querySelectorAll('.session-btn').forEach(btn => {{
  btn.addEventListener('click', (e) => {{
    e.preventDefault();
    const target = document.getElementById(btn.dataset.target);
    if (!target) return;
    // Close other open panels
    document.querySelectorAll('.session-panel.open').forEach(p => {{
      if (p !== target) p.classList.remove('open');
    }});
    target.classList.add('open');
    // Scroll the panel into view, accounting for sticky header
    setTimeout(() => target.scrollIntoView({{ behavior: 'smooth', block: 'start' }}), 50);
    // Update URL hash
    history.replaceState(null, '', '#' + target.dataset.anchor);
  }});
}});
document.querySelectorAll('.session-close').forEach(btn => {{
  btn.addEventListener('click', (e) => {{
    e.preventDefault();
    const panel = btn.closest('.session-panel');
    if (panel) panel.classList.remove('open');
    document.getElementById('sessions-top')?.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
  }});
}});
// If page loads with a hash that matches a session anchor, open that panel
const hash = window.location.hash.replace('#', '');
if (hash) {{
  const target = document.querySelector(`.session-panel[data-anchor="${{hash}}"]`);
  if (target) {{
    document.getElementById('topbar-sessions')?.setAttribute('open', '');
    target.classList.add('open');
    setTimeout(() => target.scrollIntoView({{ behavior: 'smooth', block: 'start' }}), 200);
  }}
}}
</script>
"""
    html = page(
        meta["title"],
        body,
        course_running_head=meta["title"],
        og_desc=meta["desc"],
    )
    out_path = os.path.join(OUT_DIR, f"{slug}.html")
    with open(out_path, "w") as f:
        f.write(html)
    print(f"  [ok]   {slug}: {len(html):,} bytes · {len(all_sessions)} sessions")
    return True


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    slugs = sys.argv[1:] if len(sys.argv) > 1 else list(COURSES)
    for slug in slugs:
        build_course(slug)


if __name__ == "__main__":
    main()
