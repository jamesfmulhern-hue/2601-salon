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
    <a class="brand" href="{path_prefix}index.html">The 2601 Salon</a>
    <div class="links">
      <a href="{path_prefix}partners.html">For Partners</a>
      <a href="{path_prefix}index.html#toc">Table of Contents</a>
      <a href="{path_prefix}index.html#courses">Courses</a>
      <a href="{path_prefix}index.html#formats">Formats</a>
      <a href="{path_prefix}philosophy-of-writing.html">Philosophy</a>
      <a href="{path_prefix}index.html#contact">Enroll or Book</a>
    </div>
  </div>
</nav>
""".strip()

# Back-compat default (home page)
TOPNAV = topnav("")

FOOTER = """
<footer>
  <div class="sig">— James F. Mulhern</div>
  <div>Literary courses for adult readers and writers · Philadelphia</div>
  <div style="margin-top:14px;padding-top:12px;border-top:1px solid rgba(184,137,58,0.25);font-size:0.78rem;line-height:1.55;max-width:780px;margin-left:auto;margin-right:auto;color:var(--muted);">
    &copy; James F. Mulhern &amp; Silver Current Press. All rights reserved.
    Individual readers are welcome to enjoy, print, and share these materials for personal use.
    For classroom, institutional, or commercial use — including reuse of syllabi, reading lists, discussion questions, or course design —
    please write to <a href="mailto:jamesfmulhern@gmail.com" style="color:var(--gold);">jamesfmulhern@gmail.com</a> for permission.
  </div>
</footer>
""".strip()


def page(title, body_html, course_running_head=None, og_desc="", slug=None):
    """Wrap a page in the standard shell (used for course pages, in /courses/ subdir)."""
    running_head = course_running_head or title
    canonical = f"https://salon.silvercurrentpress.com/courses/{slug}.html" if slug else ""
    course_ld = ""
    if slug:
        course_ld = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "{title}",
  "description": "{og_desc}",
  "url": "{canonical}",
  "provider": {{
    "@type": "Organization",
    "name": "Silver Current Press",
    "url": "https://silvercurrentpress.com"
  }},
  "instructor": {{
    "@type": "Person",
    "name": "James F. Mulhern",
    "jobTitle": "Professor Emeritus of English; Novelist",
    "url": "https://www.authorjamesmulhern.com"
  }},
  "inLanguage": "en",
  "availableLanguage": "en",
  "educationalLevel": "adult continuing education",
  "audience": {{
    "@type": "EducationalAudience",
    "educationalRole": "adult learner"
  }},
  "courseMode": ["onsite", "online"],
  "hasCourseInstance": {{
    "@type": "CourseInstance",
    "courseMode": ["onsite", "online"],
    "instructor": {{
      "@type": "Person",
      "name": "James F. Mulhern"
    }}
  }}
}}
</script>'''
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · The 2601 Salon</title>
<meta name="description" content="{og_desc}">
<meta name="author" content="James F. Mulhern">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="The 2601 Salon">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{og_desc}">
{course_ld}
{GOOGLE_FONTS}
<link rel="stylesheet" href="../assets/styles.css">
</head>
<body>
{topnav("../")}
<main class="wrap" data-running-head="{running_head}">
{f'<div class="partner-band"><span class="partner-band-text"><strong>For program partners:</strong> This course can be brought to any adult reading audience — in person or on Zoom. See the <a href="../partners.html">partners page</a> or download a <a href="../flyers/{slug}_flyer.pdf">one-page flyer for this course</a>.</span></div>' if slug else ''}
{body_html}
</main>
{FOOTER}
</body>
</html>
"""


def home_page(title, body_html, og_desc="", canonical_path="/"):
    """Home/index variant (CSS path is shorter)."""
    canonical = f"https://salon.silvercurrentpress.com{canonical_path}"
    org_ld = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "EducationalOrganization",
  "name": "The 2601 Salon",
  "alternateName": "Silver Current Press — Literary Courses",
  "description": "A working catalog of literary courses for adult readers and writers, taught by James F. Mulhern — Kirkus-starred novelist, Oxford Writing Fellow, and Professor Emeritus of English. American Literature, Women in American Literature, Minority Voices, Jewish Writers, Irish Literature, Literature & American History, Poetry, Shakespeare’s Sonnets & Speeches, Memoir, Revision, The Writing Life, and The Art of Telling.",
  "url": "https://salon.silvercurrentpress.com/",
  "logo": "https://salon.silvercurrentpress.com/assets/logo.png",
  "parentOrganization": {
    "@type": "Organization",
    "name": "Silver Current Press",
    "url": "https://silvercurrentpress.com"
  },
  "founder": {
    "@type": "Person",
    "name": "James F. Mulhern",
    "jobTitle": "Professor Emeritus of English; Novelist; Founder, Silver Current Press",
    "url": "https://www.authorjamesmulhern.com",
    "alumniOf": {
      "@type": "CollegeOrUniversity",
      "name": "Exeter College, University of Oxford"
    },
    "award": [
      "Kirkus Starred Review — Give Them Unquiet Dreams",
      "Kirkus Best Book of 2019",
      "Pushcart Prize Nomination, Fiction, 2017",
      "Aesthetica Creative Writing Award Shortlist, Poetry, 2021",
      "Fully Funded Writing Fellowship, Exeter College, University of Oxford"
    ],
    "sameAs": [
      "https://www.authorjamesmulhern.com",
      "https://www.amazon.com/stores/James-Mulhern/author/B00HS4D2AQ",
      "https://www.goodreads.com/author/show/1356345.James_Mulhern",
      "https://silvercurrentpress.com"
    ]
  },
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Philadelphia",
    "addressRegion": "PA",
    "addressCountry": "US"
  },
  "areaServed": [
    {"@type": "City", "name": "Philadelphia"},
    {"@type": "Country", "name": "United States"},
    {"@type": "Place", "name": "Online (Zoom, worldwide)"}
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "course inquiries and partnerships",
    "email": "jamesfmulhern@gmail.com"
  },
  "offers": {
    "@type": "Offer",
    "availability": "https://schema.org/InStock",
    "priceCurrency": "USD",
    "description": "Terms are set to fit the host venue; first offering at a new venue is often at no cost as a proof of concept."
  },
  "knowsAbout": [
    "American literature", "women writers", "minority voices in American literature",
    "Jewish literary tradition", "Irish literature", "literature and history",
    "poetry for beginners", "Shakespeare", "memoir", "personal essay",
    "revision workshop", "getting published", "the art of telling",
    "close reading", "creative writing", "literary craft", "salon teaching"
  ]
}
</script>"""
    keywords = "literary courses, adult creative writing, memoir workshop, poetry for beginners, close reading, Shakespeare course, American literature course, Irish literature course, Jewish writers course, women writers course, minority voices, revision workshop, getting published, literary salon, Philadelphia writing course, Zoom literature course, James F. Mulhern, Silver Current Press, Kirkus starred review, Oxford writing fellowship, professor emeritus, adult continuing education, lifelong learning, OLLI course, library workshop, bookstore author event, program partner, book club leader, literature lecture series, memoir consulting"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{og_desc}">
<meta name="keywords" content="{keywords}">
<meta name="author" content="James F. Mulhern">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="The 2601 Salon">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{og_desc}">
{org_ld}
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
