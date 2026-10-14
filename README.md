# Halo Study — BECE & WASSCE practice

Free practice for Ghana's two school-leaving examinations, as plain static HTML — no build step,
no server, no database, no sign-in. Students land on `index.html`, pick their examination, and the
choice is remembered.

## What is in it

### BECE (JHS) — `bece.html`

| Subject | Topics | Questions |
|---|---|---|
| Mathematics | 30 | 180 |
| English Language | 25 | 150 |
| Integrated Science | 28 | 168 |
| Social Studies | 25 | 150 |
| Religious & Moral Education | 23 | 138 |
| Computing | 18 | 108 |
| **Total** | **149** | **894** |

### WASSCE (SHS core) — `wassce.html`

| Subject | Topics | Questions |
|---|---|---|
| Core Mathematics | 32 | 244 |
| English Language | 24 | 204 |
| Integrated Science | 38 | 228 |
| Social Studies | 35 | 210 |
| **Total** | **129** | **886** |

Every topic carries plain-English notes, key facts, two worked examples, and both objective and
theory questions. Each app also has:

* **step-by-step solutions** — the working is revealed one step at a time, with the answer last;
* **the whole syllabus mapped** — 331 syllabus lines in all, each linking to the topic that covers it;
* **timed mock Paper 1** in the real shape and time for each subject, marked on submission, with the
  weakest topics named;
* **the Lab** — sixteen hands-on tools in three groups:
  *Mathematics* — graph plotter, number line, fraction bars, Pythagoras explorer, Venn builder,
  speed/distance/time, probability spinner;
  *Science practicals* — litmus and pH, separating mixtures, food tests, states of matter,
  photosynthesis, reflection of light, series-or-parallel circuit;
  *Computing and English* — binary switches, sentence builder;
* **points, ranks, streaks and badges**, to make daily practice stick.

Progress lives in the student's own browser (localStorage), separately for each level — nothing is
uploaded anywhere.

## Files

```
index.html      Halo Study home - choose BECE or WASSCE (remembers the choice)
bece.html       BECE Core Six   - six subjects in one app
wassce.html     WASSCE Core Four - four core subjects in one app
404.html        not-found page
sw.js           service worker: the apps work offline after the first visit
manifest.webmanifest + icons/   installable on a phone's home screen
netlify.toml    Netlify settings (publish ".", pretty URLs, old-link redirects, cache headers)
sitemap.xml     edit REPLACE-WITH-YOUR-DOMAIN once you have your domain
src/            the Python source that generates everything (optional)
```

## Deploy on Netlify

**Option 1 — drag and drop (fastest).**
Open <https://app.netlify.com/drop> and drag this whole folder onto the page. It is live in seconds.

**Option 2 — from GitHub (recommended, so every push redeploys).**

1. Create a repository on GitHub and push this folder:
   ```bash
   git init
   git add .
   git commit -m "Halo Study: BECE and WASSCE practice apps"
   git branch -M main
   git remote add origin https://github.com/arkohb/YOUR-REPO.git
   git push -u origin main
   ```
2. In Netlify: **Add new site → Import an existing project → GitHub**, choose the repo.
3. Build settings — Netlify reads `netlify.toml`, so just confirm:
   - Build command: *(empty)*
   - Publish directory: `.`
4. Deploy. Every later `git push` redeploys automatically.

### Custom domain
Netlify → **Domain settings → Add a domain**. Point your domain's DNS at Netlify, then edit
`sitemap.xml` and replace `REPLACE-WITH-YOUR-DOMAIN`.

## Deploy on GitHub Pages instead

Settings → Pages → Source: *Deploy from a branch* → `main` / root. Every path in the site is
relative, so it also works from a project sub-path such as `https://arkohb.github.io/halo-study/`.
(`netlify.toml` is simply ignored there.)

## Updating the content

The HTML files are generated. To change questions, edit the Python in `src/` and rebuild:

```bash
cd src
pip install -r requirements.txt
./build.sh            # rebuilds every page into the site folder
```

`src/` holds one module per block of content:

* WASSCE — `part*.py` (maths), `eng*.py`, `sci*.py`, `sst*.py`, `ext*.py` (notes and worked examples),
  `syllabus.py`
* BECE — `bmat*.py`, `beng*.py`, `bsci*.py`, `bsst*.py`, `brme*.py`, `bcomp*.py`, `syllabus_bece.py`
* shared — `core.py` (the question helpers and the answer checker), `draw.py` (the SVG diagram
  library), `extras_pack.py` (one illustration and one "use it in real life" note per topic),
  `hub.html` (the app shell), `hud_css.txt` / `hud_js.txt` (the Halo theme and the Lab),
  `hudify.py` (applies them), `build_two.py` (builds both level apps), `make_site.py` (builds the site)
* checks — `audit_dump.py` (writes a readable dump of every bank to `audit/` and runs the content
  checks), `test_site.py` (drives both apps in a real browser)

The build **fails loudly** if a mathematics or science answer does not check out, if a syllabus item
points at a missing topic, if a topic is missing from the syllabus, or if any topic lacks notes,
objective questions or theory questions.

## Quality checks

Three layers run on every build, and all three must pass:

1. **The answer checker** (`core.py`). Every objective question is authored with the correct option
   first and, wherever the answer is computable, an independently computed value; the build asserts
   that exactly one option matches it. Options are then shuffled deterministically, and the keys are
   evened out across A–D so no letter is over-represented.
2. **The content audit** (`python3 src/audit_dump.py`). It writes a plain-text dump of every bank to
   `audit/` and checks for duplicate stems, options that are not distinct, keys that give themselves
   away by being much longer than the distractors, skewed answer-key spread, missing or single-line
   working, unbalanced HTML, odd mark allocations, and topics without enough questions. It currently
   reports **0 issues** across all ten banks.
3. **The browser suite** (`python3 src/test_site.py`). 83 checks in light and dark mode, plus an
   offline reload and a 390px phone-width overflow check.

Every explanation, key fact and worked example was also read through subject by subject against
WAEC marking practice, and the mark allocations shown on theory questions follow the real papers
(for example the WASSCE English essay is marked out of 50: Content 10, Organisation 10,
Expression 20, Mechanical Accuracy 10).

## About the questions

These are **original** practice questions written to the Ghanaian syllabus and to the format of the
papers. They are **not** reproductions of past BECE or WASSCE papers. For the real papers, use WAEC's
own e-learning portal and the past-question booklets sold by WAEC Ghana.

Content © 2026 Bismark Arko-Ofori. Build 2026.10.14-2136.
