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
    {
        "slug": "chekhov_endings",
        "title": "How Chekhov Ends",
        "tag": "Four Sessions",
        "blurb": "A close-reading workshop on the last paragraph of the modern short story. Four Chekhov stories, read slowly, with attention to the ending Chekhov taught fiction how to make.",
        "hours": "4 sessions · 90 minutes each",
    },
    {
        "slug": "joyces_sentences",
        "title": "Joyce's Sentences",
        "tag": "Two Sessions",
        "blurb": "A close-reading weekend on the last pages of The Dead and on Molly Bloom's soliloquy at the end of Ulysses. Two of the most famous passages in modern English prose, read aloud and slowly.",
        "hours": "2 sessions · 90 minutes each",
    },
    {
        "slug": "emerson",
        "title": "Reading Emerson",
        "tag": "Four Sessions",
        "blurb": "Four Emerson essays read slowly \u2014 Nature, Self-Reliance, The American Scholar, and Circles. The founding voice of American thought, at the pace he asks to be read.",
        "hours": "4 sessions · 90 minutes each",
    },
    {
        "slug": "dickinson",
        "title": "Reading Dickinson",
        "tag": "Four Sessions",
        "blurb": "Emily Dickinson at close range \u2014 the dashes, the slant rhymes, the small rooms that hold whole universes. Twenty-four of her finest poems, unhurried.",
        "hours": "4 sessions · 90 minutes each",
    },
    {
        "slug": "thoreau",
        "title": "Reading Thoreau",
        "tag": "Four Sessions",
        "blurb": "Walden and Civil Disobedience, read as literature and as challenge. Three sessions in the cabin at the pond, one in the Concord jail.",
        "hours": "4 sessions · 90 minutes each",
    },
    {
        "slug": "whitman",
        "title": "Reading Whitman",
        "tag": "Four Sessions",
        "blurb": "Song of Myself in three unhurried passes, then the Civil War poems that gave Whitman his deepest music. Read aloud, always.",
        "hours": "4 sessions · 90 minutes each",
    },
    {
        "slug": "presidential_speeches",
        "title": "The Presidential Speech",
        "tag": "Six Sessions",
        "blurb": "Six great American speeches close-read for their craft, rhetorical devices, and historical context. Washington's Farewell, Lincoln's Second Inaugural, FDR, JFK, Dr. King, and Reagan on the Challenger.",
        "hours": "6 sessions · 90 minutes each",
    },
    {
        "slug": "2601_essays",
        "title": "Our Building, Our Story: Writing the Life of 2601",
        "tag": "Ten Sessions · For 2601 Residents",
        "blurb": "A course written for our own building — craft fundamentals, the ethics of writing about real neighbors, and the arrival, portrait, happy, hard, and funniest-experience essays that become a shared, publishable resident anthology.",
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
  <span>{c['title']}<br><span style="font-size:0.78rem;letter-spacing:0.14em;text-transform:uppercase;color:var(--gold-on-dark);font-family:Lora,serif;font-weight:600;">{c['tag']}</span></span>
  <span class="chev">›</span>
</a>
<p style="margin:-6px 0 22px;padding:0 6px;color:var(--muted);font-size:0.98rem;">{c['blurb']}</p>
""".strip())

    body = f"""
{notices_band}
<div class="notice">
  <div class="label">A WELCOME</div>
  <p style="margin-bottom:0;">Professor Mulhern — a novelist, short story writer, poet, and essayist — offers the following courses for adult readers and writers. Each course meets weekly for ninety minutes. Each is built around close reading and generous conversation.</p>
</div>

<style>
.network-toc {{
  background: #FBF7EC;
  border: 1px solid rgba(184,137,58,0.35);
  border-radius: 3px;
  padding: 28px 32px;
  margin: 24px 0;
}}
.network-toc h2 {{
  margin-top: 0;
  text-align: center;
  color: var(--navy);
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-weight: 600;
}}
.network-toc .lede {{
  text-align: center;
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-style: italic;
  color: var(--muted);
  max-width: 60ch;
  margin: 0 auto 20px;
}}
.network-toc details {{
  border-bottom: 1px solid rgba(184,137,58,0.25);
  padding: 10px 0;
}}
.network-toc details:last-child {{ border-bottom: none; }}
.network-toc details > summary {{
  cursor: pointer;
  list-style: none;
  padding: 6px 0;
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-size: 1.15rem;
  font-weight: 600;
  color: var(--navy);
  display: flex;
  align-items: baseline;
  gap: 12px;
}}
.network-toc details > summary::-webkit-details-marker {{ display: none; }}
.network-toc details > summary::before {{
  content: "\\25B8";
  color: var(--gold);
  font-size: 0.9em;
  transition: transform .2s ease;
  display: inline-block;
  width: 14px;
}}
.network-toc details[open] > summary::before {{
  content: "\\25BE";
}}
.network-toc summary .toc-count {{
  margin-left: auto;
  font-family: 'Outfit', system-ui, sans-serif;
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--gold);
  font-weight: 500;
}}
.network-toc ul {{
  list-style: none;
  padding-left: 28px;
  margin: 8px 0 14px;
}}
.network-toc ul li {{
  padding: 6px 0;
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-size: 1rem;
  line-height: 1.5;
}}
.network-toc ul li a {{ color: var(--maroon); border-bottom: 1px dotted rgba(107,31,42,0.35); }}
.network-toc ul li a:hover {{ color: var(--gold); border-bottom-color: var(--gold); }}
.network-toc ul li .note {{
  color: var(--muted);
  font-size: 0.94rem;
  font-style: italic;
}}
.network-toc .toc-actions {{
  text-align: center;
  margin-top: 18px;
  font-family: 'Outfit', system-ui, sans-serif;
  font-size: 0.75rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}}
.network-toc .toc-actions a {{
  color: var(--gold);
  border: none;
  margin: 0 12px;
  cursor: pointer;
}}
</style>

<div class="card network-toc" id="toc">
  <h2>Table of Contents</h2>
  <p class="lede">One nested map of the whole teaching and publishing network. Click any heading to expand.</p>

  <div class="toc-actions">
    <a href="#" onclick="document.querySelectorAll('.network-toc details').forEach(d=>d.open=true);return false;">Expand All</a>
    <a href="#" onclick="document.querySelectorAll('.network-toc details').forEach(d=>d.open=false);return false;">Collapse All</a>
  </div>
  <script>
    // When any TOC summary is toggled, scroll the summary line back into view
    // at the top of the viewport so users don't lose their place after clicking.
    document.querySelectorAll('.network-toc details').forEach(function(det) {{
      det.querySelector('summary').addEventListener('click', function(e) {{
        // wait for the toggle to complete before scrolling
        setTimeout(function() {{
          const rect = det.getBoundingClientRect();
          // Only scroll if the summary is above or too far below the visible area
          const target = window.scrollY + rect.top - 20;
          window.scrollTo({{ top: target, behavior: 'smooth' }});
        }}, 50);
      }});
    }});
  </script>

  <details open>
    <summary>For Program Partners <span class="toc-count">Instructor portfolio</span></summary>
    <ul>
      <li><a href="partners.html">Bring a Course to Your Venue</a> <span class="note">— the instructor portfolio: credentials, full catalog, formats, sample materials, and how to schedule. The single URL to share with any program director, librarian, or venue partner.</span></li>
    </ul>
  </details>

  <details open>
    <summary>The Salon <span class="toc-count">19 courses</span></summary>
    <ul>
      <li><a href="courses/american_lit.html">Survey of American Literature</a></li>
      <li><a href="courses/women_writers.html">Women in American Literature</a></li>
      <li><a href="courses/minority_voices.html">Minority Voices in American Literature</a></li>
      <li><a href="courses/jewish_writers.html">Jewish Writers: A Literary Tradition</a></li>
      <li><a href="courses/irish_lit.html">The Irish Literary Imagination</a></li>
      <li><a href="courses/lit_and_history.html">Literature &amp; American History — A Cross-Reading</a></li>
      <li><a href="courses/poetry.html">Reading Poetry: A Beginner's Welcome</a></li>
      <li><a href="courses/shakespeare.html">Shakespeare's Sonnets &amp; Famous Speeches</a></li>
      <li><a href="courses/memoir.html">The Personal Essay &amp; Memoir</a></li>
      <li><a href="courses/revision_workshop.html">The Craft of Revision — A Writers' Workshop</a></li>
      <li><a href="courses/writing_life.html">The Writing Life: Getting Published</a></li>
      <li><a href="courses/art_of_telling.html">The Art of Telling</a> <span class="note">— a salon in short story, poetry, and memoir</span></li>
      <li><a href="courses/emerson.html">Reading Emerson</a> <span class="note">— four essays close-read</span></li>
      <li><a href="courses/dickinson.html">Reading Dickinson</a> <span class="note">— the poems, close-read</span></li>
      <li><a href="courses/thoreau.html">Reading Thoreau</a> <span class="note">— Walden and Civil Disobedience</span></li>
      <li><a href="courses/whitman.html">Reading Whitman</a> <span class="note">— Leaves of Grass and the Civil War poems</span></li>
      <li><a href="courses/chekhov_endings.html">How Chekhov Ends</a> <span class="note">— four sessions on the last paragraph</span></li>
      <li><a href="courses/joyces_sentences.html">Joyce's Sentences</a> <span class="note">— The Dead and Molly Bloom</span></li>
      <li><a href="courses/presidential_speeches.html">The Presidential Speech</a> <span class="note">— rhetoric, craft, and history</span></li>
    </ul>
  </details>

  <details>
    <summary>Companion Course Sites <span class="toc-count">Deep-dive workshops</span></summary>
    <ul>
      <li><a href="https://art-of-telling.com">The Art of Telling</a> <span class="note">— the ten-session salon site</span></li>
      <li><a href="https://companion.art-of-telling.com">Because There Wasn't Time to Tell Everything</a> <span class="note">— companion volume with expanded readings, discussion answers, and craft essays</span></li>
      <li><a href="courses/chekhov_endings.html">How Chekhov Ends</a> <span class="note">— a four-session close-reading workshop on the last paragraph of the modern short story</span></li>
      <li><a href="courses/joyces_sentences.html">Joyce's Sentences</a> <span class="note">— a two-session close-reading weekend on <em>The Dead</em> and Molly Bloom's soliloquy</span></li>
    </ul>
  </details>

  <details>
    <summary>The Mulhern Library <span class="toc-count">Reading resources</span></summary>
    <ul>
      <li><a href="https://shortstories.silvercurrentpress.com">Short Stories</a> <span class="note">— a curated library with reading notes, discussion guides, and downloadable PDFs</span></li>
    </ul>
  </details>

  <details>
    <summary>Course Tools <span class="toc-count">In-class instruments</span></summary>
    <ul>
      <li><a href="https://whiteboard.silvercurrentpress.com">The Whiteboard</a> <span class="note">— the live classroom whiteboard used inside sessions for shared writing, close-reading marks, and instructor notes</span></li>
    </ul>
  </details>

  <details>
    <summary>Publishing Guides for Writers <span class="toc-count">Field guides</span></summary>
    <ul>
      <li><a href="https://publishingpoetry.silvercurrentpress.com">Publishing Poetry</a> <span class="note">— poems and chapbooks to literary magazines, contests, and small presses</span></li>
      <li><a href="https://submittingshortstories.silvercurrentpress.com">Submitting Short Stories</a> <span class="note">— the working submissions playbook for the short story</span></li>
      <li><a href="https://submittingmemoirs.silvercurrentpress.com">Submitting Memoirs</a> <span class="note">— essay, memoir excerpt, and full-manuscript submissions in creative nonfiction</span></li>
    </ul>
  </details>

  <details>
    <summary>The Author <span class="toc-count">Books and background</span></summary>
    <ul>
      <li><a href="https://www.authorjamesmulhern.com">authorjamesmulhern.com</a> <span class="note">— reviews, awards, credentials, and news</span></li>
      <li><a href="https://jamesfmulhern-hue.github.io/press-kit/">Press Packet</a> <span class="note">— for journalists, program directors, and event bookers</span></li>
      <li><a href="philosophy-of-writing.html">Philosophy of Writing</a> <span class="note">— the author statement under every course here</span></li>
      <li><a href="thin-places.html">Thin Places</a> <span class="note">— a craft essay on permeability, recurrence, and the writing life</span></li>
      <li><a href="https://www.kirkusreviews.com/book-reviews/james-mulhern/give-them-unquiet-dreams/">Kirkus Starred Review</a> <span class="note">— <em>Give Them Unquiet Dreams</em>, a Kirkus Best Book of 2019</span></li>
      <li><a href="https://shelfmediagroup.com/interview/interview-james-mulhern-author-of-molly-bonamici/">Shelf Media Group Interview</a> <span class="note">— on <em>Molly Bonamici</em></span></li>
    </ul>
  </details>

  <details>
    <summary>The Books <span class="toc-count">8 titles</span></summary>
    <ul>
      <li><em>Give Them Unquiet Dreams</em> <span class="note">— novel, 2019; Kirkus starred review; Kirkus Best Book of 2019</span></li>
      <li><em>Molly Bonamici</em> <span class="note">— novel, 2016; dark comic mystery of Boston and South Florida</span></li>
      <li><em>A Prayer for Home</em> <span class="note">— novelette, 2016; praised by <em>The Missouri Review</em></span></li>
      <li><em>Assumptions and Other Stories</em> <span class="note">— story collection, 2016</span></li>
      <li><em>About Aiden: Selected Stories</em> <span class="note">— 2018; a compact selection of the Aiden stories</span></li>
      <li><em>Blindfolded and Other Stories</em> <span class="note">— story collection</span></li>
      <li><em>Crossings</em> <span class="note">— poetry chapbook; shortlisted, Aesthetica Creative Writing Award 2021</span></li>
      <li><a href="https://www.amazon.com/stores/James-Mulhern/author/B00HS4D2AQ">See the full catalog on Amazon</a></li>
    </ul>
  </details>

  <details>
    <summary>The Press <span class="toc-count">Publishing home</span></summary>
    <ul>
      <li><a href="https://silvercurrentpress.com">Silver Current Press</a> <span class="note">— the Philadelphia literary imprint behind these courses</span></li>
    </ul>
  </details>
</div>

<div class="hero">
  <h1>The 2601 Salon</h1>
  <span class="subtitle">A Literary Salon</span>
  <p style="color:#E9D8A6;margin:14px auto 0;max-width:560px;font-size:1.02rem;">A literary salon for adult readers and writers, taught by James F. Mulhern — Professor of English and recipient of a Writing Fellowship at Exeter College, University of Oxford. Professor Mulhern is also a published novelist, short story writer, poet, and essayist.</p>
</div>

<div class="card" id="courses">
  <h2 style="text-align:center;margin-top:0;">The Courses</h2>
  <p style="text-align:center;color:var(--muted);margin-bottom:28px;">Click any course to see its full syllabus, readings, and sessions.</p>
  {''.join(cards)}
</div>

<div class="card" id="about">
  <h2>About This Salon</h2>
  <p>The 2601 Salon is a literary program of Silver Current Press — a working catalog of the courses Professor Mulhern is prepared to teach for adult readers and writers. Every course meets weekly for ninety minutes. There are no grades, no quizzes, and no prerequisites — only an invitation to sit with serious books, to talk about them in plain language, and to improve one's own writing along the way. These courses are about both literature and the craft of writing.</p>
  <p>Each course is shaped the same way: a brief historical framing at the top of the hour, a passage read aloud, a guided discussion around four to six open questions, and an optional ten-minute writing prompt at the close. Any device with a browser suffices for in-class access to the readings. Writing in class, however, is always done by hand. We have found this matters.</p>
  <p>Readings are open-access. Most are in the public domain and are linked from each course page; the remainder are available as free digital borrows through the Internet Archive.</p>
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
  <p><strong>Program directors, librarians, and venue partners</strong> — if you host adult programming and would like to bring a course to your community, please write to <a href="mailto:jamesfmulhern@gmail.com">jamesfmulhern@gmail.com</a>. Please include the venue, an approximate audience size, and a proposed date window; terms are set to fit the host.</p>
  <p><strong>Silver Current Press</strong> · Philadelphia · <a href="https://silvercurrentpress.com">silvercurrentpress.com</a></p>
</div>

<div class="card" id="elsewhere">
  <h2>Elsewhere on the Web</h2>
  <p>The 2601 Salon is one of several sites that make up Professor Mulhern's teaching and publishing work. Anyone wanting the fuller picture — books, philosophy of writing, press packet, related courses, and background — can start here.</p>

  <h3>Author &amp; Press</h3>
  <ul>
    <li><a href="https://www.authorjamesmulhern.com">authorjamesmulhern.com</a> — the author site: reviews, awards, credentials, and news.</li>
    <li><a href="https://jamesfmulhern-hue.github.io/press-kit/">Press Packet</a> — for journalists, program directors, and event bookers: Kirkus starred review, high-resolution author photo, cover images, bio in three lengths, contact.</li>
    <li><a href="philosophy-of-writing.html">Philosophy of Writing</a> — the author statement that sits under every course in this salon.</li>
    <li><a href="thin-places.html">Thin Places</a> — a craft essay on thin psychological boundaries, recurrence, and why the same images keep returning in a body of work.</li>
    <li><a href="https://www.kirkusreviews.com/book-reviews/james-mulhern/give-them-unquiet-dreams/">Kirkus starred review</a> of <em>Give Them Unquiet Dreams</em>, a Kirkus Best Book of 2019.</li>
    <li><a href="https://shelfmediagroup.com/interview/interview-james-mulhern-author-of-molly-bonamici/">Shelf Media Group interview</a> on <em>Molly Bonamici</em>.</li>
  </ul>

  <h3>The Books</h3>
  <p style="font-size:0.94rem;color:var(--muted);margin-top:-6px;">Novels, story collections, and poetry. Full catalog on Amazon; the pieces below are the ones a new reader is most likely to want to start with.</p>
  <ul>
    <li><em>Give Them Unquiet Dreams</em> (novel, 2019) — <strong>Kirkus starred review</strong>; Kirkus Best Book of 2019; also available on <a href="https://www.audible.com/pd/Give-Them-Unquiet-Dreams-Audiobook/B0CYTPQZSR">Audible</a> and <a href="https://www.goodreads.com/book/show/50862422-give-them-unquiet-dreams">Goodreads</a>.</li>
    <li><em>Molly Bonamici</em> (novel, 2016) — a dark comic mystery of Boston and South Florida; five-star review from <em>Readers' Favorite</em>; positively critiqued by <em>Kirkus Reviews</em>.</li>
    <li><em>A Prayer for Home</em> (novelette, 2016) — praised by <em>The Missouri Review</em> for its “well-written, complex characters… and fantastic voice.”</li>
    <li><em>Assumptions and Other Stories</em> (story collection, 2016) — five-star review from <em>Readers' Favorite</em>.</li>
    <li><em>About Aiden: Selected Stories</em> (2018) — a compact selection of the Aiden stories.</li>
    <li><em>Blindfolded and Other Stories</em> (story collection).</li>
    <li><em>Crossings</em> (poetry chapbook) — poetry shortlisted for the Aesthetica Creative Writing Award 2021.</li>
    <li><a href="https://www.amazon.com/stores/James-Mulhern/author/B00HS4D2AQ">See the full catalog on Amazon</a> — including individual short stories, teaching guides, and back issues.</li>
  </ul>

  <h3>Related Courses</h3>
  <ul>
    <li><a href="https://art-of-telling.com">The Art of Telling</a> — the ten-session course that gave the salon its name.</li>
    <li><a href="https://companion.art-of-telling.com"><em>Because There Wasn't Time to Tell Everything</em></a> — the companion site to The Art of Telling. Expanded biographies, close readings, historical context, answers to every discussion question, craft essays, and a downloadable sixty-eight-page Word booklet for readers who want to go deeper.</li>
    <li><a href="courses/chekhov_endings.html">How Chekhov Ends</a> — a four-session close-reading workshop on the last paragraph of the modern short story.</li>
    <li><a href="courses/joyces_sentences.html">Joyce's Sentences</a> — a two-session close-reading weekend on <em>The Dead</em> and Molly Bloom's soliloquy.</li>
  </ul>

  <h3>The Mulhern Library</h3>
  <ul>
    <li><a href="https://shortstories.silvercurrentpress.com">The Mulhern Library — Short Stories</a> — a curated library of canonical short stories, with reading notes, discussion guides, and downloadable PDFs, suitable for salons, classrooms, and independent readers.</li>
  </ul>

  <h3>Publishing Guides for Writers</h3>
  <p style="font-size:0.94rem;color:var(--muted);margin-top:-6px;">Student-facing guides for adult writers learning how contemporary publishing works. Each site includes a working guide, a downloadable PDF, model reading lists, and annotated craft studies from published work.</p>
  <ul>
    <li><a href="https://publishingpoetry.silvercurrentpress.com">Publishing Poetry</a> — how to submit poems and chapbooks to literary magazines, contests, and small presses.</li>
    <li><a href="https://submittingshortstories.silvercurrentpress.com">Submitting Short Stories</a> — the working submissions playbook for the short story: markets, cover letters, response times, and craft.</li>
    <li><a href="https://submittingmemoirs.silvercurrentpress.com">Submitting Memoirs</a> — a practical guide to essay, memoir excerpt, and full-manuscript submissions in creative nonfiction.</li>
  </ul>

  <h3>Press &amp; Publishing</h3>
  <ul>
    <li><a href="https://silvercurrentpress.com">Silver Current Press</a> — the Philadelphia literary imprint behind these courses; services, catalog, and production notes.</li>
    <li><a href="https://jamesfmulhern-hue.github.io/press-kit/">Press Kit</a> — for journalists, program directors, and event bookers: high-resolution author photo, Kirkus starred review, cover images, bio in three lengths, contact.</li>
    <li><a href="https://shelfmediagroup.com/interview/interview-james-mulhern-author-of-molly-bonamici/">Shelf Media Group interview</a> on <em>Molly Bonamici</em>.</li>
  </ul>
</div>

<hr class="rule">

<div class="card" id="use-of-materials">
  <h2>About the Use of These Materials</h2>
  <p>Everything on this site — course descriptions, reading lists, syllabi, discussion questions, session pages, revision checklists, and The Mulhern Library — was written and designed by James F. Mulhern for Silver Current Press.</p>
  <p><strong>Readers are always welcome</strong> to read, print, share, and quote these pages for their own study and enjoyment. That is what the site is for.</p>
  <p>Teachers, program directors, and institutions who would like to use any of it in a classroom, syllabus, publication, or paid program are asked to write first — a short email is enough. The answer will almost always be a warm yes, with a note on attribution. Please contact Professor Mulhern at <a href="mailto:jamesfmulhern@gmail.com">jamesfmulhern@gmail.com</a>.</p>
</div>

<hr class="rule">

<div class="card" style="text-align:center;background:transparent;border:none;box-shadow:none;">
  <p style="font-family:'Cormorant Garamond',serif;font-size:1.4rem;color:var(--navy);font-style:italic;">"A book is a heart that only beats in the chest of another."</p>
  <p style="color:var(--muted);font-size:0.92rem;">— Rebecca Solnit</p>
</div>
"""
    html = home_page(
        "The 2601 Salon · Literary Courses",
        body,
        og_desc="Literary courses for adult readers and writers, taught by James F. Mulhern. American Literature, Women in American Literature, Minority Voices, Jewish Writers, Irish Literature, Literature & American History, Poetry, Shakespeare's Sonnets & Speeches, Memoir, a Writers' Revision Workshop, The Writing Life, and The Art of Telling.",
    )
    with open("index.html", "w") as f:
        f.write(html)
    print("Built index.html")


if __name__ == "__main__":
    build()
