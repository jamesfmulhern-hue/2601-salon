"""Build the catalog landing page (index.html)."""
from _partials import home_page

# Final 10-course catalog, ordered as the user would naturally browse:
# strongest/most-personal foundations first, then specialties, then workshop.
COURSES = [
    {
        "slug": "american_lit",
        "title": "Survey of American Literature",
        "tag": "Sixteen Sessions",
        "blurb": "A chronological journey from Indigenous voices and Puritan sermons to contemporary American writing — read slowly, together.",
        "hours": "16 sessions · 90 minutes each",
    },
    {
        "slug": "women_writers",
        "title": "Women in American Literature",
        "tag": "Sixteen Sessions",
        "blurb": "From Anne Bradstreet and Phillis Wheatley to Toni Morrison and Joy Harjo — a chronological reading of the women whose work makes the American canon whole.",
        "hours": "16 sessions · 90 minutes each",
    },
    {
        "slug": "minority_voices",
        "title": "Minority Voices in American Literature",
        "tag": "Sixteen Sessions",
        "blurb": "Black, Latinx, Asian American, Native American, and immigrant voices — from Frederick Douglass to Ocean Vuong — read with the close attention they have always deserved.",
        "hours": "16 sessions · 90 minutes each",
    },
    {
        "slug": "jewish_writers",
        "title": "Jewish Writers: A Literary Tradition",
        "tag": "Sixteen Sessions",
        "blurb": "Sholem Aleichem, Kafka, Singer, Primo Levi, Celan, Bellow, Malamud, Ozick, Paley, Amichai — a literature older than empires, read together.",
        "hours": "16 sessions · 90 minutes each",
    },
    {
        "slug": "irish_lit",
        "title": "The Irish Literary Imagination",
        "tag": "Sixteen Sessions",
        "blurb": "Sixteen weeks of Irish writing — from the Táin and Swift to Yeats, Joyce, Heaney, Boland, and the contemporary moment. Personal territory for your instructor.",
        "hours": "16 sessions · 90 minutes each",
    },
    {
        "slug": "lit_and_history",
        "title": "Literature & American History — A Cross-Reading",
        "tag": "Sixteen Sessions",
        "blurb": "Each week pairs a primary historical document with the literary work answering it — the Declaration with Douglass, the 14th Amendment with Du Bois, the Pentagon Papers with O'Brien.",
        "hours": "16 sessions · 90 minutes each",
    },
    {
        "slug": "poetry",
        "title": "Reading Poetry: A Beginner's Welcome",
        "tag": "Sixteen Sessions",
        "blurb": "An unhurried introduction to poetry for anyone who has ever felt locked out of it. We read aloud, we sit with the lines, and we discover that a poem is not a code to crack.",
        "hours": "16 sessions · 90 minutes each",
    },
    {
        "slug": "shakespeare",
        "title": "Shakespeare's Sonnets & Famous Speeches",
        "tag": "Sixteen Sessions",
        "blurb": "Sixteen sonnets paired with sixteen of Shakespeare's most famous monologues — short, self-contained texts read aloud and discussed. No full plays, no homework dread.",
        "hours": "16 sessions · 90 minutes each",
    },
    {
        "slug": "memoir",
        "title": "The Personal Essay & Memoir",
        "tag": "Sixteen Sessions",
        "blurb": "Writing from a life — your own. We read masters of the form and we write by hand, in scene, with candor and craft.",
        "hours": "16 sessions · 90 minutes each",
    },
    {
        "slug": "revision_workshop",
        "title": "The Craft of Revision — A Writers' Workshop",
        "tag": "Sixteen Sessions",
        "blurb": "Bring your pages. We will read them aloud, cut them, sharpen them, and send them out.",
        "hours": "16 sessions · 90 minutes each",
    },
    {
        "slug": "writing_life",
        "title": "The Writing Life: Getting Published",
        "tag": "Sixteen Sessions",
        "blurb": "The literary magazine scene, cover letters and queries, agents, small presses, contests \u2014 the practical work of becoming a published writer, taught by a working writer and former editor.",
        "hours": "16 sessions · 90 minutes each",
    },
]


def build():
    cards = []
    for c in COURSES:
        cards.append(f"""
<a class="menu-btn" href="courses/{c['slug']}.html">
  <span>{c['title']}<br><span style="font-size:0.78rem;letter-spacing:0.14em;text-transform:uppercase;color:var(--gold);font-family:Lora,serif;font-weight:600;">{c['tag']}</span></span>
  <span class="chev">›</span>
</a>
<p style="margin:-6px 0 22px;padding:0 6px;color:var(--muted);font-size:0.98rem;">{c['blurb']}</p>
""".strip())

    body = f"""
<div class="notice">
  <div class="label">A NOTE TO MY NEIGHBORS</div>
  <p style="margin-bottom:0;">Professor Mulhern — your neighbor in A Tower, and a novelist, short story writer, poet, and essayist — is willing to teach the following eleven free courses for the residents of 2601. Each meets weekly in the community room. Each is built around close reading and generous conversation.</p>
</div>

<div class="hero">
  <h1>The 2601 Salon</h1>
  <span class="subtitle">Eleven Free Courses</span>
  <p style="color:#E9D8A6;margin:14px auto 0;max-width:560px;font-size:1.02rem;">A literary salon for the residents of our building, taught by James F. Mulhern — Professor of English, recipient of a Writing Fellowship at Exeter College, University of Oxford, and your neighbor in A Tower. Professor Mulhern is also a published novelist, short story writer, poet, and essayist.</p>
</div>

<div class="card" id="courses">
  <h2 style="text-align:center;margin-top:0;">The Courses</h2>
  <p style="text-align:center;color:var(--muted);margin-bottom:28px;">Click any course to see its full syllabus, readings, and sessions.</p>
  {''.join(cards)}
</div>

<div class="card" id="about">
  <h2>About This Salon</h2>
  <p>The 2601 Salon is a free, building-wide literary program. Every course meets weekly in the community room for ninety minutes. There are no grades, no quizzes, no fees, and no prerequisites — only an invitation to sit together with serious books, to talk about them in plain language, and to improve our own writing along the way. These courses are about both literature and the craft of writing.</p>
  <p>Each course is shaped the same way: a brief historical framing at the top of the hour, a passage read aloud, a guided discussion around four to six open questions, and an optional ten-minute writing prompt at the close. A laptop is required for in-class access to the readings. Writing in class, however, is always done by hand. We have found this matters.</p>
  <p>Readings are free. Most are in the public domain and are linked from each course page.</p>
  <h3>About Your Instructor</h3>
  <p>James F. Mulhern is a Professor of English, a former Department Chair in both English and Social Studies, an AP Consultant for the College Board and the National Math and Science Initiative, and the recipient of a fully funded Writing Fellowship at Exeter College, University of Oxford — a grant that brought together writers selected from around the world. He is a published novelist, short story writer, poet, and essayist, with editorial experience at major publishing houses in Boston, New York City, and Amherst, Massachusetts.</p>
</div>

<div class="card" id="contact">
  <h2>How to Join</h2>
  <p style="margin-bottom:0;">To express interest in a course, please email Professor Mulhern at <a href="mailto:jamesfmulhern@gmail.com">jamesfmulhern@gmail.com</a>.</p>
</div>

<hr class="rule">

<div class="card" style="text-align:center;background:transparent;border:none;box-shadow:none;">
  <p style="font-family:'Cormorant Garamond',serif;font-size:1.4rem;color:var(--navy);font-style:italic;">"A book is a heart that only beats in the chest of another."</p>
  <p style="color:var(--muted);font-size:0.92rem;">— Rebecca Solnit</p>
</div>
"""
    html = home_page(
        "The 2601 Salon · Free Literary Courses",
        body,
        og_desc="Ten free literary courses for the residents of 2601 — taught by James F. Mulhern. American Literature, Women in American Literature, Minority Voices, Jewish Writers, Irish Literature, Literature & American History, Poetry, Shakespeare's Sonnets & Speeches, Memoir, and a Writers' Revision Workshop.",
    )
    with open("index.html", "w") as f:
        f.write(html)
    print("Built index.html")


if __name__ == "__main__":
    build()
