# The 2601 Salon — Free Literary Courses

Source for **[salon.silvercurrentpress.com](https://salon.silvercurrentpress.com)** — free literature courses for residents of 2601 in Philadelphia, taught by James F. Mulhern.

Eleven courses, sixteen sessions each, with reading lists, critical reception, discussion questions, and homework — all readings free online.

## How this repo works

- `_content/` — markdown source for the eleven course syllabi and instructor companions
- `_build_home.py`, `_build_course_pages.py`, `_partials.py` — Python build scripts
- `assets/styles.css` — site styling
- `index.html`, `courses/*.html` — built HTML output served by Cloudflare Pages

To rebuild: `python3 _build_home.py && python3 _build_course_pages.py`

Cloudflare Pages auto-deploys on every push to `main`.

---

Runs alongside [The Art of Telling](https://art-of-telling.com) under the [Silver Current Press](https://silvercurrentpress.com) imprint. Whiteboard: [whiteboard.silvercurrentpress.com](https://whiteboard.silvercurrentpress.com).
