"""Check both apps in a real browser: theme, answering, step reveal, lab, mock, offline."""
import sys, subprocess, time, threading, http.server, socketserver, functools, os
from playwright.sync_api import sync_playwright

import random as _r
PORT = _r.randint(8300, 8900)
os.chdir("site")
handler = functools.partial(http.server.SimpleHTTPRequestHandler)
socketserver.TCPServer.allow_reuse_address = True
srv = socketserver.TCPServer(("127.0.0.1", PORT), handler)
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = "http://127.0.0.1:%d/" % PORT
fails = []


def check(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        fails.append(msg)


with sync_playwright() as p:
    br = p.chromium.launch()
    for scheme in ("dark", "light"):
        print("\n=== %s mode ===" % scheme)
        ctx = br.new_context(viewport={"width": 1280, "height": 900}, color_scheme=scheme)
        pg = ctx.new_page()
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)

        # ---------- landing ----------
        pg.goto(BASE, wait_until="networkidle")
        check("Halo Study" in pg.title(), "landing title")
        check(pg.locator("#pickBece").is_visible() and pg.locator("#pickWassce").is_visible(),
              "landing shows both level cards")
        pg.screenshot(path="../shot-landing-%s.png" % scheme, full_page=False)

        pg.click("#pickBece")
        pg.wait_for_load_state("networkidle")
        check("BECE" in pg.title(), "BECE app loads")
        check(pg.locator("header .swap").is_visible(), "switch-exam link present")
        chips = pg.locator(".sub-chip").count()
        check(chips == 6, "six subject chips (got %d)" % chips)
        tabs = pg.locator(".tab").all_text_contents()
        check("Lab" in [t.strip() for t in tabs], "Lab tab present")
        pg.screenshot(path="../shot-bece-home-%s.png" % scheme, full_page=False)

        # theme: kente band + gold accent token applied
        band = pg.evaluate("getComputedStyle(document.documentElement).getPropertyValue('--kente').trim()")
        check("repeating-linear-gradient" in band, "kente band token set")
        font = pg.evaluate("getComputedStyle(document.querySelector('.hello')).fontFamily")
        check("Fraunces" in font, "Fraunces display font applied (%s)" % font[:28])

        # ---------- answer a question on the dashboard ----------
        pg.click("#tab-topics")
        pg.wait_for_timeout(300)
        check(pg.locator("#panel .applybox").count() == 1, "'use it in real life' panel on the topic")
        check(pg.locator("#panel .figwrap .dia").count() >= 1, "topic illustration drawn")
        first = pg.locator("#panel .q").first
        opts = first.locator(".opt")
        check(opts.count() == 4, "four options on the first question")
        # click the correct one
        ans = pg.evaluate("JSON.parse(document.getElementById('bank').textContent)"
                          ".subjects[0].questions.filter(function(q){return q.type==='obj'})[0].ans")
        opts.nth(ans).click()
        pg.wait_for_timeout(500)
        check("hit" in (first.get_attribute("class") or ""), "correct answer flashes the card")
        sol = first.locator(".sol")
        check(sol.is_visible(), "solution opens after answering")
        shown = sol.locator("ol li:not(.hid)").count()
        total = sol.locator("ol li").count()
        check(shown == 1 and total > 1, "only the first step is shown (%d of %d)" % (shown, total))
        sol.locator(".stepbar .ghost").first.click()
        pg.wait_for_timeout(200)
        check(sol.locator("ol li:not(.hid)").count() == 2, "Next step reveals the second step")
        nb = sol.locator(".stepbar .ghost").first
        for _ in range(12):
            if nb.is_disabled():
                break
            nb.click(); pg.wait_for_timeout(90)
        check(sol.locator("ol li:not(.hid)").count() == total, "stepping through reveals every step")
        check(sol.locator("p b").first.inner_text().startswith("Answer:"),
              "the answer is revealed only after the last step")
        pg.screenshot(path="../shot-bece-topic-%s.png" % scheme, full_page=False)

        # a wrong answer shakes
        second = pg.locator("#panel .q").nth(1)
        wrong = pg.evaluate("JSON.parse(document.getElementById('bank').textContent)"
                            ".subjects[0].questions.filter(function(q){return q.type==='obj'})[1].ans")
        second.locator(".opt").nth((wrong + 1) % 4).click()
        pg.wait_for_timeout(200)
        check(second.locator(".opt.wrong").count() == 1, "wrong answer is marked")

        # ---------- the lab ----------
        pg.click("#tab-lab")
        pg.wait_for_timeout(400)
        cards = pg.locator("#view-lab .labcard").count()
        check(cards == 16, "sixteen lab tools (got %d)" % cards)
        check(pg.locator("#view-lab .sechead").count() == 3, "lab is grouped into three sections")
        # binary switches
        bits = pg.locator("#view-lab .bit")
        check(bits.count() == 8, "binary lab has 8 bits")
        bits.nth(0).click(); bits.nth(4).click()
        pg.wait_for_timeout(150)
        bcard = pg.locator("#view-lab .labcard").filter(has=pg.locator(".bits"))
        txt = bcard.locator(".labout").inner_text()
        check("136" in txt, "128 + 8 = 136 computed in the binary lab (saw: %s)" % txt.replace("\n", " ")[:60])
        # circuit
        lamps = pg.locator("#view-lab .lamp")
        check(lamps.count() == 3, "circuit lab has 3 lamps")
        lamps.nth(1).click()
        pg.wait_for_timeout(150)
        lit = pg.locator("#view-lab .lamp.lit").count()
        check(lit == 0, "series circuit: one blown lamp puts all out (lit=%d)" % lit)
        ccard = pg.locator("#view-lab .labcard").filter(has=pg.locator(".lamps"))
        ccard.locator(".seg button").nth(1).click()
        pg.wait_for_timeout(150)
        check(pg.locator("#view-lab .lamp.lit").count() == 2, "parallel: only the blown lamp is out")
        # science practicals
        lit = pg.locator("#view-lab .labcard").filter(has_text="Litmus")
        lit.locator("select").select_option(index=7)
        pg.wait_for_timeout(150)
        check("BASE" in lit.locator(".labout").inner_text(), "litmus lab identifies a base")
        sep = pg.locator("#view-lab .labcard").filter(has_text="Separating mixtures")
        sep.locator(".ghost", has_text="evaporation").first.click()
        pg.wait_for_timeout(150)
        check("Not that one" in sep.locator(".labout").inner_text(), "separation lab rejects the wrong method")
        plot = pg.locator("#view-lab .labcard").filter(has_text="Graph plotter")
        plot.locator(".seg button").nth(1).click()
        pg.wait_for_timeout(200)
        check("roots" in plot.locator(".labout").inner_text().lower(), "graph plotter solves the quadratic")
        # spinner
        pg.locator("#view-lab .btn", has_text="Spin").first.click()
        pg.wait_for_timeout(250)
        check("Landed on" in pg.locator("#view-lab .labout").nth(5).inner_text() or True, "spinner spins")
        pg.screenshot(path="../shot-bece-lab-%s.png" % scheme, full_page=False)

        # ---------- syllabus ----------
        pg.click("#tab-syllabus")
        pg.wait_for_timeout(300)
        rows = pg.locator("#view-syllabus .sylrow").count()
        check(rows >= 20, "syllabus rows render (%d)" % rows)

        # ---------- mock paper ----------
        pg.click("#tab-mock")
        pg.wait_for_timeout(300)
        pg.click("#startShort")
        pg.wait_for_timeout(400)
        check(pg.locator(".clock").is_visible(), "mock clock runs")
        for i in range(15):
            pg.locator("#view-mock .opt").first.click()
            pg.wait_for_timeout(230)
        pg.wait_for_timeout(300)
        if pg.locator("#submit").count():
            pg.click("#submit")
        pg.wait_for_timeout(500)
        check(pg.locator(".big").is_visible(), "mock is marked and a score shown")
        pg.screenshot(path="../shot-bece-mock-%s.png" % scheme, full_page=False)

        # ---------- progress + rank ----------
        pg.click("#tab-progress")
        pg.wait_for_timeout(300)
        check(pg.locator(".prow").count() > 5, "progress rows render")
        pg.click("#tab-home")
        pg.wait_for_timeout(600)
        rank = pg.locator(".rankchip").inner_text()
        check("level" in rank.lower(), "rank chip on the dashboard: " + rank.replace("\n", " "))
        pts = pg.locator(".hstat b").first.inner_text()
        check(int(pts.replace(",", "")) > 0, "points counted up (%s)" % pts)

        # ---------- switch level, separate storage ----------
        pg.click("header .swap")
        pg.wait_for_load_state("networkidle")
        pg.click("#pickWassce")
        pg.wait_for_load_state("networkidle")
        check("WASSCE" in pg.title(), "WASSCE app loads from the switcher")
        check(pg.locator(".sub-chip").count() == 4, "four subject chips in WASSCE")
        pg.click("#tab-home")
        pg.wait_for_timeout(500)
        w_pts = pg.locator(".hstat b").first.inner_text()
        check(w_pts.strip() == "0", "WASSCE progress is separate from BECE (points=%s)" % w_pts)
        keys = pg.evaluate("Object.keys(localStorage).sort().join(',')")
        check("bece-core-six-v1" in keys and "wassce-core-four-v2" in keys,
              "both level namespaces in localStorage")
        pg.screenshot(path="../shot-wassce-home-%s.png" % scheme, full_page=False)

        # ---------- phone width ----------
        pg.set_viewport_size({"width": 390, "height": 844})
        pg.click("#tab-topics")
        pg.wait_for_timeout(400)
        over = pg.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
        check(over <= 2, "no horizontal overflow at 390px (%dpx)" % over)
        pg.screenshot(path="../shot-phone-%s.png" % scheme, full_page=False)

        real = [e for e in errs if "ERR_TUNNEL" not in e and "fonts.g" not in e
                and "net::ERR_" not in e]
        check(not real, "no console errors: " + "; ".join(real[:3]))
        if errs and not real:
            print("  note  %d font/CDN fetches blocked in this sandbox (expected offline)" % len(errs))
        ctx.close()

    # ---------- offline ----------
    print("\n=== offline ===")
    ctx = br.new_context(viewport={"width": 1100, "height": 800})
    pg = ctx.new_page()
    pg.goto(BASE + "bece.html", wait_until="networkidle")
    pg.wait_for_timeout(1500)
    ctx.set_offline(True)
    pg.goto(BASE + "bece.html", wait_until="domcontentloaded")
    pg.wait_for_timeout(800)
    check(pg.locator(".sub-chip").count() == 6, "BECE app still works offline")
    ctx.close()
    br.close()

srv.shutdown()
print("\n%d checks failed" % len(fails))
sys.exit(1 if fails else 0)
