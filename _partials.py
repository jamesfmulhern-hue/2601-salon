"""Shared HTML scaffolding for every course page."""

GOOGLE_FONTS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Lora:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
""".strip()

def topnav(path_prefix=""):
    """Render the top nav. `path_prefix` is "" for the home page and "../" for course pages."""
    return f"""
<nav class="topnav">
  <div class="topnav-inner">
    <a class="brand" href="{path_prefix}index.html">2601 · Free Courses</a>
    <div class="links">
      <a href="{path_prefix}index.html#courses">Courses</a>
      <a href="{path_prefix}index.html#about">About</a>
      <a href="{path_prefix}index.html#contact">Contact</a>
    </div>
  </div>
</nav>
""".strip()

# Back-compat default (home page)
TOPNAV = topnav("")

FOOTER = """
<footer>
  <div class="sig">— James F. Mulhern</div>
  <div>Free literary courses for the residents of 2601 · Philadelphia · 2026</div>
  <div style="margin-top:6px;font-size:0.82rem;">All readings are free to access. All sessions are free to attend.</div>
</footer>
""".strip()


def page(title, body_html, course_running_head=None, og_desc=""):
    """Wrap a page in the standard shell (used for course pages, in /courses/ subdir)."""
    running_head = course_running_head or title
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · 2601 Free Courses</title>
<meta name="description" content="{og_desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{og_desc}">
{GOOGLE_FONTS}
<link rel="stylesheet" href="../assets/styles.css">
</head>
<body>
{topnav("../")}
<main class="wrap" data-running-head="{running_head}">
{body_html}
</main>
{FOOTER}
</body>
</html>
"""


def home_page(title, body_html, og_desc=""):
    """Home/index variant (CSS path is shorter)."""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{og_desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{og_desc}">
{GOOGLE_FONTS}
<link rel="stylesheet" href="assets/styles.css">
</head>
<body>
{topnav("")}
<main class="wrap">
{body_html}
</main>
{FOOTER}
</body>
</html>
"""
