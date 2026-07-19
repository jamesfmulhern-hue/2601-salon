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
    {
        "slug": "art_of_telling",
        "title": "The Art of Telling",
        "tag": "Ten Sessions",
        "blurb": "A salon in short story, poetry, and memoir. Ten Sundays across the three great narrative forms \u2014 the course that gave the salon its name, now on the shelf beside the others.",
        "hours": "10 sessions · 90 minutes each",
    },
]


def build():
    from _announcements import render_notice_block
    notices_band = render_notice_block()
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
{notices_band}
<div class="notice">
  <div class="label">A WELCOME</div>
  <p style="margin-bottom:0;">Professor Mulhern — a novelist, short story writer, poet, and essayist — offers the following free courses for adult readers and writers. Each course meets weekly for ninety minutes. Each is built around close reading and generous conversation.</p>
</div>

<div class="hero">
  <h1>The 2601 Salon</h1>
  <span class="subtitle">Free Courses</span>
  <p style="color:#E9D8A6;margin:14px auto 0;max-width:560px;font-size:1.02rem;">A literary salon for adult readers and writers, taught by James F. Mulhern — Professor of English and recipient of a Writing Fellowship at Exeter College, University of Oxford. Professor Mulhern is also a published novelist, short story writer, poet, and essayist.</p>
</div>

<div class="card" id="courses">
  <h2 style="text-align:center;margin-top:0;">The Courses</h2>
  <p style="text-align:center;color:var(--muted);margin-bottom:28px;">Click any course to see its full syllabus, readings, and sessions.</p>
  {''.join(cards)}
</div>

<div class="card" id="about">
  <h2>About This Salon</h2>
  <p>The 2601 Salon is a free literary program of Silver Current Press — a working catalog of the courses Professor Mulhern is prepared to teach for adult readers and writers. Every course meets weekly for ninety minutes. There are no grades, no quizzes, no fees, and no prerequisites — only an invitation to sit with serious books, to talk about them in plain language, and to improve one's own writing along the way. These courses are about both literature and the craft of writing.</p>
  <p>Each course is shaped the same way: a brief historical framing at the top of the hour, a passage read aloud, a guided discussion around four to six open questions, and an optional ten-minute writing prompt at the close. Any device with a browser suffices for in-class access to the readings. Writing in class, however, is always done by hand. We have found this matters.</p>
  <p>Readings are free. Most are in the public domain and are linked from each course page.</p>
  <h3>About the Instructor</h3>
  <p>James F. Mulhern is a Philadelphia novelist and Professor Emeritus of English. His novel <em>Give Them Unquiet Dreams</em> received a <strong>Kirkus starred review</strong> and was named a Kirkus Best Book of 2019. He held a fully funded Writing Fellowship at Exeter College, University of Oxford; was nominated for a Pushcart Prize; and was shortlisted for the Aesthetica Creative Writing Award. He served as Department Chair in both English and Social Studies and as an AP Consultant for the College Board and the National Math and Science Initiative. He is the founder of Silver Current Press, a Philadelphia literary imprint. Full biography at <a href="https://www.authorjamesmulhern.com">authorjamesmulhern.com</a>.</p>
</div>

<div class="card" id="formats">
  <h2>Formats &amp; Availability</h2>
  <p>Courses are offered in three formats, and Professor Mulhern will adapt any of the courses in this catalog to fit a partner venue's calendar and audience.</p>
  <ul>
    <li><strong>In person</strong> — at libraries, bookstores, community centers, universities, retirement communities, and literary nonprofits in the Philadelphia region and, on request, elsewhere in the Northeast.</li>
    <li><strong>Online</strong> — by Zoom or comparable platform, to any group of adult readers anywhere.</li>
    <li><strong>Hybrid</strong> — a combination of in-person sessions and online continuation, tailored to the host.</li>
  </ul>
  <p>Full sixteen-session courses, four-session workshops, single evening talks, and one-day masterclasses are all available. Please write with your calendar and I will propose a shape that fits.</p>
</div>

<div class="card" id="contact">
  <h2>How to Enroll or Book a Course</h2>
  <p><strong>Individual learners</strong> — if you would like to attend a course, express interest in a future session, or receive occasional announcements about new offerings, please write to me at <a href="mailto:jamesfmulhern@gmail.com">jamesfmulhern@gmail.com</a>. There is no formal enrollment.</p>
  <p><strong>Program directors, librarians, and venue partners</strong> — if you host adult programming and would like to bring a course to your community, please write to <a href="mailto:jamesfmulhern@gmail.com">jamesfmulhern@gmail.com</a>. The first offering at any new venue is free as a proof of concept; ongoing engagements are arranged at a modest honorarium. Please include the venue, an approximate audience size, and a proposed date window.</p>
  <p><strong>Silver Current Press</strong> · Philadelphia · <a href="https://silvercurrentpress.com">silvercurrentpress.com</a></p>
</div>

<div class="card" id="elsewhere">
  <h2>Elsewhere on the Web</h2>
  <p>The 2601 Salon is one of several sites that make up Professor Mulhern's teaching and publishing work. Anyone wanting the fuller picture — books, related courses, credentials, and background — can start here.</p>

  <h3>Author &amp; Books</h3>
  <ul>
    <li><a href="https://www.authorjamesmulhern.com">authorjamesmulhern.com</a> — the author site: reviews, awards, credentials, and news.</li>
    <li><a href="https://www.amazon.com/stores/James-Mulhern/author/B00HS4D2AQ">James Mulhern on Amazon</a> — all books, including <em>Give Them Unquiet Dreams</em>, <em>Molly Bonamici</em>, <em>Mia Bambina and Other Stories</em>, and the poetry chapbook <em>Crossings</em>.</li>
    <li><a href="https://www.kirkusreviews.com/book-reviews/james-mulhern/give-them-unquiet-dreams/">Kirkus starred review</a> of <em>Give Them Unquiet Dreams</em>, a Kirkus Best Book of 2019.</li>
    <li><a href="https://www.goodreads.com/book/show/50862422-give-them-unquiet-dreams">Give Them Unquiet Dreams on Goodreads</a></li>
    <li><a href="https://www.audible.com/pd/Give-Them-Unquiet-Dreams-Audiobook/B0CYTPQZSR">Give Them Unquiet Dreams on Audible</a></li>
  </ul>

  <h3>Related Courses</h3>
  <ul>
    <li><a href="https://art-of-telling.com">The Art of Telling</a> — the ten-session course that gave the salon its name.</li>
    <li><a href="https://companion.art-of-telling.com"><em>Because There Wasn't Time to Tell Everything</em></a> — the companion site to The Art of Telling. Expanded biographies, close readings, historical context, answers to every discussion question, craft essays, and a downloadable sixty-eight-page Word booklet for readers who want to go deeper.</li>
    <li><a href="https://chekhov-endings.silvercurrentpress.com">How Chekhov Ends</a> — a four-session close-reading workshop on the last paragraph of the modern short story.</li>
    <li><a href="https://joyces-sentences.silvercurrentpress.com">Joyce's Sentences</a> — a two-session close-reading weekend on <em>The Dead</em> and Molly Bloom's soliloquy.</li>
  </ul>

  <h3>The Mulhern Library</h3>
  <ul>
    <li><a href="https://shortstories.silvercurrentpress.com">The Mulhern Library — Short Stories</a> — a curated library of canonical short stories, with reading notes, discussion guides, and downloadable PDFs, suitable for salons, classrooms, and independent readers.</li>
  </ul>

  <h3>Publishing Guides for Writers</h3>
  <p style="font-size:0.94rem;color:var(--muted);margin-top:-6px;">Free student-facing guides for adult writers learning how contemporary publishing works. Each site includes a working guide, a downloadable PDF, model reading lists, and annotated craft studies from published work.</p>
  <ul>
    <li><a href="https://publishingpoetry.silvercurrentpress.com">Publishing Poetry</a> — how to submit poems and chapbooks to literary magazines, contests, and small presses.</li>
    <li><a href="https://submittingshortstories.silvercurrentpress.com">Submitting Short Stories</a> — the working submissions playbook for the short story: markets, cover letters, response times, and craft.</li>
    <li><a href="https://submittingmemoirs.silvercurrentpress.com">Submitting Memoirs</a> — a practical guide to essay, memoir excerpt, and full-manuscript submissions in creative nonfiction.</li>
  </ul>

  <h3>Press &amp; Publishing</h3>
  <ul>
    <li><a href="https://silvercurrentpress.com">Silver Current Press</a> — the Philadelphia literary imprint behind these courses.</li>
    <li><a href="https://shelfmediagroup.com/interview/interview-james-mulhern-author-of-molly-bonamici/">Shelf Media Group interview</a> on <em>Molly Bonamici</em>.</li>
  </ul>
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
        og_desc="Free literary courses for adult readers and writers, taught by James F. Mulhern. American Literature, Women in American Literature, Minority Voices, Jewish Writers, Irish Literature, Literature & American History, Poetry, Shakespeare's Sonnets & Speeches, Memoir, a Writers' Revision Workshop, The Writing Life, and The Art of Telling.",
    )
    with open("index.html", "w") as f:
        f.write(html)
    print("Built index.html")


if __name__ == "__main__":
    build()
