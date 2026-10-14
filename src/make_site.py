"""Turn the built app files into a complete static site for Netlify / GitHub."""
import os, re, shutil, json, time
from PIL import Image, ImageDraw, ImageFont

SITE = "site"
BRAND = {"paper": "#F7F2E7", "ink": "#17140E", "dark": "#0B0C0F",
         "gold": "#D99B16", "gold2": "#F0C24E",
         "bece": "#1F9E6B", "wassce": "#C2402D", "ink2": "#6B6252"}

PAGES = [
    ("bece.html", "bece.html", "BECE Core Six · Halo Study",
     "Free BECE practice for all six core subjects — Mathematics, English, Integrated Science, Social "
     "Studies, R.M.E. and Computing. 894 original questions with step-by-step solutions, plain-English notes, "
     "diagrams, the whole syllabus mapped, timed mock Paper 1 and a hands-on Lab."),
    ("wassce.html", "wassce.html", "WASSCE Core Four · Halo Study",
     "Free WASSCE practice for all four core subjects — Core Maths, English, Integrated Science and Social "
     "Studies. 886 original questions with step-by-step working, worked examples, diagrams, the whole syllabus "
     "mapped, timed mock Paper 1 and a hands-on Lab."),
]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{desc}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="{paper}" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="{dark}" media="(prefers-color-scheme: dark)">
<meta name="author" content="Bismark Arko-Ofori">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="share.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icons/icon-180.png">
<link rel="manifest" href="manifest.webmanifest">
<style>
html{{color-scheme:light dark}}
:root{{padding-top:env(safe-area-inset-top,0px); padding-bottom:env(safe-area-inset-bottom,0px)}}
img{{max-width:100%}}
[hidden]{{display:none!important}}
.sitefoot{{max-width:1100px; margin:0 auto; padding:26px 16px 40px; font-size:13px; color:var(--ink-2);
  display:flex; flex-wrap:wrap; gap:6px 16px; align-items:center; border-top:1px solid var(--rule)}}
.sitefoot a{{color:var(--accent); font-weight:600; text-decoration:none}}
.sitefoot a:hover{{text-decoration:underline}}
.sitefoot .sep{{opacity:.5}}
</style>
"""

FOOT = """<footer class="sitefoot">
  <a href="./index.html">Halo Study home</a><span class="sep">·</span>
  <a href="bece.html">BECE (JHS)</a><span class="sep">·</span>
  <a href="wassce.html">WASSCE (SHS)</a>
  <span style="flex:1 1 100%">Original practice questions written to the Ghanaian syllabus — not
  reproductions of past BECE or WASSCE papers. Your progress is stored only in this browser, and the two
  levels are kept separately.</span>
</footer>
"""

SW_REG = """<script>
if ('serviceWorker' in navigator) {
  window.addEventListener('load', function () {
    navigator.serviceWorker.register('sw.js').catch(function(){});
  });
}
</script>
"""


def build_pages():
    for src, out, title, desc in PAGES:
        html = open(src, encoding="utf-8").read()
        cut = html.index("<header")
        head_part, body_part = html[:cut], html[cut:]
        doc = (HEAD.format(desc=desc, title=title, paper=BRAND["paper"], dark=BRAND["dark"])
               + head_part.strip() + "\n</head>\n<body>\n"
               + body_part.rstrip() + "\n" + FOOT + SW_REG + "</body>\n</html>\n")
        open(os.path.join(SITE, out), "w", encoding="utf-8").write(doc)
        print("  %-14s %4d KB   %s" % (out, len(doc) // 1024, title))
    shutil.copy("landing.html", os.path.join(SITE, "index.html"))
    print("  %-14s %4d KB   %s" % ("index.html", os.path.getsize(f"{SITE}/index.html") // 1024,
                                   "Halo Study — choose BECE or WASSCE"))


def icons():
    """The Halo mark: a gold tile with a dark ring - a halo."""
    os.makedirs(f"{SITE}/icons", exist_ok=True)
    for size in (180, 192, 512):
        img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        d.rounded_rectangle([0, 0, size - 1, size - 1], radius=size * 0.24, fill=BRAND["gold2"])
        d.rounded_rectangle([0, 0, size - 1, size * 0.52], radius=size * 0.24, fill=BRAND["gold"])
        w = size * 0.085
        pad = size * 0.26
        d.ellipse([pad, pad, size - pad, size - pad], outline=BRAND["ink"], width=int(w))
        img.save(f"{SITE}/icons/icon-{size}.png")
    size = 512
    img = Image.new("RGBA", (size, size), BRAND["dark"])
    d = ImageDraw.Draw(img)
    pad = size * 0.32
    d.ellipse([pad, pad, size - pad, size - pad], outline=BRAND["gold2"], width=int(size * 0.075))
    img.save(f"{SITE}/icons/icon-maskable-512.png")

    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="Halo Study">\n'
           '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
           '<stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>\n'
           '<rect width="64" height="64" rx="15" fill="url(#g)"/>\n'
           '<circle cx="32" cy="32" r="15" fill="none" stroke="%s" stroke-width="5.5"/>\n</svg>\n'
           % (BRAND["gold2"], BRAND["gold"], BRAND["ink"]))
    open(f"{SITE}/favicon.svg", "w").write(svg)
    print("  icons/        4 PNG icons + favicon.svg")


def share_image():
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), BRAND["paper"])
    d = ImageDraw.Draw(img)
    for x in range(0, W, 40):
        d.line([(x, 0), (x, H)], fill="#EBE3D2")
    for y in range(0, H, 40):
        d.line([(0, y), (W, y)], fill="#EBE3D2")
    # kente band across the top
    x = 0
    pattern = [(BRAND["gold2"], 26), (BRAND["ink"], 12), ("#C2402D", 20),
               (BRAND["ink"], 12), ("#1F9E6B", 20), (BRAND["ink"], 12)]
    while x < W:
        for col, wid in pattern:
            d.rectangle([x, 0, x + wid, 16], fill=col)
            x += wid

    def font(sz, bold=False):
        for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSerif%s.ttf" % ("-Bold" if bold else ""),
                  "/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if bold else "")):
            if os.path.exists(p):
                return ImageFont.truetype(p, sz)
        return ImageFont.load_default()

    d.rounded_rectangle([80, 110, 152, 182], radius=18, fill=BRAND["gold2"])
    d.ellipse([98, 128, 134, 164], outline=BRAND["ink"], width=7)
    d.text((172, 118), "Halo Study", font=font(62, True), fill=BRAND["ink"])
    d.text((176, 192), "BECE  ·  WASSCE  ·  Ghana", font=font(30), fill=BRAND["ink2"])
    d.text((80, 282), "1,780 practice questions, worked step by step", font=font(44, True), fill=BRAND["ink"])
    d.text((80, 352), "10 subjects · 278 topics · timed mock papers · a hands-on Lab",
           font=font(32), fill=BRAND["ink2"])
    d.rounded_rectangle([80, 430, 400, 492], radius=31, fill=BRAND["bece"])
    d.text((126, 446), "BECE  ·  6 subjects", font=font(28, True), fill="#FFFFFF")
    d.rounded_rectangle([424, 430, 760, 492], radius=31, fill=BRAND["wassce"])
    d.text((470, 446), "WASSCE · 4 subjects", font=font(28, True), fill="#FFFFFF")
    d.text((80, 536), "Original practice written to the Ghanaian syllabus — not past papers",
           font=font(26), fill=BRAND["ink2"])
    img.save(f"{SITE}/share.png")
    print("  share.png     social preview card")


def support_files(version):
    manifest = {
        "name": "Halo Study — BECE & WASSCE practice", "short_name": "Halo Study",
        "description": "Practice questions, worked solutions and mock papers for the BECE and the WASSCE.",
        "start_url": "./", "scope": "./", "display": "standalone",
        "background_color": BRAND["paper"], "theme_color": BRAND["gold2"], "orientation": "portrait-primary",
        "icons": [
            {"src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
            {"src": "icons/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
        ],
        "shortcuts": [
            {"name": "BECE practice", "url": "bece.html"},
            {"name": "WASSCE practice", "url": "wassce.html"},
        ],
    }
    open(f"{SITE}/manifest.webmanifest", "w").write(json.dumps(manifest, indent=2))

    open(f"{SITE}/sw.js", "w").write('''/* Halo Study - offline support.
   HTML is network-first (so updates arrive), everything else cache-first. */
const VERSION = '%s';
const CACHE = 'halo-study-' + VERSION;
const ASSETS = ['./', './index.html', './bece.html', './wassce.html',
  './manifest.webmanifest', './favicon.svg', './icons/icon-192.png', './icons/icon-512.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting()).catch(() => {}));
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys()
    .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;            // fonts etc. - leave to the browser

  const isPage = req.mode === 'navigate' || (req.headers.get('accept') || '').includes('text/html');
  if (isPage) {
    e.respondWith(fetch(req)
      .then(res => { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); return res; })
      .catch(() => caches.match(req).then(r => r || caches.match('./index.html'))));
  } else {
    e.respondWith(caches.match(req).then(r => r || fetch(req).then(res => {
      const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); return res;
    })));
  }
});
''' % version)

    open(f"{SITE}/netlify.toml", "w").write('''# Netlify configuration - static site, no build step.

[build]
  publish = "."
  command = ""

# Pretty URLs: /bece instead of /bece.html
[[redirects]]
  from = "/bece"
  to = "/bece.html"
  status = 200
[[redirects]]
  from = "/wassce"
  to = "/wassce.html"
  status = 200
# old links from the previous version keep working
[[redirects]]
  from = "/maths"
  to = "/wassce.html"
  status = 301
[[redirects]]
  from = "/maths.html"
  to = "/wassce.html"
  status = 301
[[redirects]]
  from = "/english.html"
  to = "/wassce.html"
  status = 301
[[redirects]]
  from = "/science.html"
  to = "/wassce.html"
  status = 301
[[redirects]]
  from = "/social.html"
  to = "/wassce.html"
  status = 301

[[headers]]
  for = "/*"
  [headers.values]
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
    Permissions-Policy = "geolocation=(), microphone=(), camera=()"

# HTML: always revalidate, so students get updates as soon as you redeploy
[[headers]]
  for = "/*.html"
  [headers.values]
    Cache-Control = "public, max-age=0, must-revalidate"

[[headers]]
  for = "/sw.js"
  [headers.values]
    Cache-Control = "public, max-age=0, must-revalidate"

# Icons and the share image rarely change
[[headers]]
  for = "/icons/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
''')

    open(f"{SITE}/robots.txt", "w").write("User-agent: *\nAllow: /\n\nSitemap: /sitemap.xml\n")
    pages = ["", "bece.html", "wassce.html"]
    today = time.strftime("%Y-%m-%d")
    urls = "".join("  <url><loc>https://REPLACE-WITH-YOUR-DOMAIN/%s</loc><lastmod>%s</lastmod></url>\n"
                   % (p, today) for p in pages)
    open(f"{SITE}/sitemap.xml", "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + urls + "</urlset>\n")

    open(f"{SITE}/404.html", "w").write('''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found &middot; Halo Study</title>
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<style>
  body{margin:0; min-height:100vh; display:grid; place-items:center; background:%(paper)s;
    color:%(ink)s; font-family:system-ui,-apple-system,Segoe UI,sans-serif; text-align:center; padding:24px}
  h1{font-size:28px; margin:0 0 8px}
  p{color:%(ink2)s; margin:0 0 20px}
  a{display:inline-block; background:%(gold)s; color:#1B1812; text-decoration:none;
    padding:11px 24px; border-radius:999px; font-weight:700}
  @media (prefers-color-scheme: dark){
    body{background:%(dark)s; color:#F2EDE1}
  }
</style></head>
<body><main>
  <h1>That page is not here</h1>
  <p>The link may be old or mistyped.</p>
  <a href="/">Go to Halo Study</a>
</main></body></html>
''' % {"paper": BRAND["paper"], "ink": BRAND["ink"], "ink2": BRAND["ink2"],
       "gold": BRAND["gold2"], "dark": BRAND["dark"]})
    print("  manifest, sw.js, netlify.toml, robots.txt, sitemap.xml, 404.html")


def repo_files(version):
    open(f"{SITE}/.gitignore", "w").write(
        "__pycache__/\n*.pyc\n.DS_Store\n.netlify/\nnode_modules/\n*.zip\nsrc/bank_*.json\n")

    open(f"{SITE}/README.md", "w").write('''# Halo Study — BECE & WASSCE practice

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

Content © %(year)s Bismark Arko-Ofori. Build %(version)s.
''' % {"year": time.strftime("%Y"), "version": version})

    os.makedirs(f"{SITE}/src", exist_ok=True)
    keep = ["core.py", "draw.py", "extras_pack.py", "syllabus.py", "syllabus_bece.py",
            "dump.py", "dump_bece.py", "audit_dump.py", "test_site.py",
            "build_subject.py", "build_hub.py", "build_two.py", "hudify.py", "make_site.py",
            "hud_css.txt", "hud_js.txt", "hub.html", "template.html", "landing.html",
            "part1.py", "part2.py", "part3.py", "ext_maths.py", "ext2_maths.py",
            "eng1.py", "eng2.py", "eng3.py", "ext_eng.py", "ext2_eng.py",
            "sci1.py", "sci2.py", "sci3.py", "ext_sci.py", "ext2_sci.py",
            "sst1.py", "sst2.py", "sst3.py", "ext_sst.py", "ext2_sst.py",
            "bmat1.py", "bmat2.py", "beng1.py", "beng2.py",
            "bsci1.py", "bsci2.py", "bsci3.py", "bsst1.py", "bsst2.py", "bsst3.py",
            "brme1.py", "brme2.py", "bcomp1.py", "bcomp2.py"]
    for f in keep:
        if os.path.exists(f):
            shutil.copy(f, f"{SITE}/src/{f}")
    open(f"{SITE}/src/requirements.txt", "w").write("sympy>=1.12\npillow>=10.0\n")
    open(f"{SITE}/src/build.sh", "w").write('''#!/usr/bin/env bash
# Rebuild both level apps and refresh the site folder.
set -e
cd "$(dirname "$0")"

# ---- question banks (every answer is checked here; the build stops on an error) ----
python3 dump.py maths   part1,part2,part3,ext_maths,ext2_maths
python3 dump.py english eng1,eng2,eng3,ext_eng,ext2_eng
python3 dump.py science sci1,sci2,sci3,ext_sci,ext2_sci
python3 dump.py social  sst1,sst2,sst3,ext_sst,ext2_sst

python3 dump_bece.py bmaths     bmat1,bmat2
python3 dump_bece.py benglish   beng1,beng2
python3 dump_bece.py bscience   bsci1,bsci2,bsci3
python3 dump_bece.py bsocial    bsst1,bsst2,bsst3
python3 dump_bece.py brme       brme1,brme2
python3 dump_bece.py bcomputing bcomp1,bcomp2

# ---- theme the shell, build both apps, then the site ----
python3 hudify.py
python3 build_two.py
python3 make_site.py
echo "Done. Commit and push, or drag the site folder to Netlify."
''')
    os.chmod(f"{SITE}/src/build.sh", 0o755)
    print("  README.md, .gitignore, src/ (python source + build.sh)")


if __name__ == "__main__":
    version = time.strftime("%Y.%m.%d-%H%M")   # new cache name on every build
    if os.path.exists(SITE):
        shutil.rmtree(SITE)
    os.makedirs(SITE, exist_ok=True)
    print("Building site/ …")
    build_pages()
    icons()
    share_image()
    support_files(version)
    repo_files(version)
    total = sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(SITE) for f in fs)
    print("site/ ready — %.1f MB in total" % (total / 1024 / 1024))
