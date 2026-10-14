"""Write a readable text dump of every bank for review, and run automated sanity checks."""
import json, os, re, sys
from collections import Counter

LEVELS = {
    "BECE": [("bmaths", "Mathematics"), ("benglish", "English Language"), ("bscience", "Integrated Science"),
             ("bsocial", "Social Studies"), ("brme", "Religious & Moral Education"), ("bcomputing", "Computing")],
    "WASSCE": [("maths", "Core Mathematics"), ("english", "English Language"),
               ("science", "Integrated Science"), ("social", "Social Studies")],
}
LET = "ABCD"
os.makedirs("audit", exist_ok=True)


SUP = {"0": "\u2070", "1": "\u00b9", "2": "\u00b2", "3": "\u00b3", "4": "\u2074", "5": "\u2075",
       "6": "\u2076", "7": "\u2077", "8": "\u2078", "9": "\u2079", "-": "\u207b", "\u2212": "\u207b",
       "+": "\u207a", "n": "\u207f", "a": "\u1d43", "b": "\u1d47", "m": "\u1d50", "x": "\u02e3"}
SUB = {"0": "\u2080", "1": "\u2081", "2": "\u2082", "3": "\u2083", "4": "\u2084", "5": "\u2085",
       "6": "\u2086", "7": "\u2087", "8": "\u2088", "9": "\u2089"}


def _sup(m):
    t = m.group(1)
    return "".join(SUP.get(ch, "^" + ch) for ch in t) if all(ch in SUP for ch in t) else "^(" + t + ")"


def _sub(m):
    t = m.group(1)
    return "".join(SUB.get(ch, "_" + ch) for ch in t) if all(ch in SUB for ch in t) else "_(" + t + ")"


def plain(s):
    """Render the app's HTML as readable text WITHOUT losing maths: superscripts, fractions,
    vectors, surds and < > all survive, so a reviewer sees what a student sees."""
    if not isinstance(s, str):
        return s
    s = re.sub(r'<svg[\s\S]*?</svg>', '[diagram]', s)
    # stacked fractions, vectors/matrices, surds
    s = re.sub(r'<span class="fr"><span>(.*?)</span><span>(.*?)</span></span>', r'(\1)/(\2)', s)
    s = re.sub(r'<span class="mx">(.*?)</span>', lambda m: "[" + m.group(1) + "]", s)
    s = re.sub(r'<span class="mr">(.*?)</span>', lambda m: m.group(1).strip() + "; ", s)
    s = re.sub('\u221a<span class="ov">(.*?)</span>', '\u221a(\\1)', s)
    s = re.sub(r'<sup>(.*?)</sup>', _sup, s)
    s = re.sub(r'<sub>(.*?)</sub>', _sub, s)
    s = re.sub(r'<br\s*/?>', ' / ', s)
    s = re.sub(r'</(p|div|h\d|tr)>', r'</\1>\n   ', s)
    s = re.sub(r'<span class="lbl">(.*?)</span>', r'[\1] ', s)
    s = re.sub(r'</t[dh]>', ' | ', s)
    s = re.sub(r'<li>', ' \u2022 ', s)
    # only strip things that really are tags (< followed by a letter or /)
    s = re.sub(r'</?[A-Za-z][^>]*>', '', s)
    s = (s.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
          .replace("&nbsp;", " ").replace("&middot;", "\u00b7"))
    s = re.sub(r'\[\s*;\s*', '[', s)
    s = re.sub(r';\s*\]', ']', s)
    s = re.sub(r'[ \t]+', ' ', s)
    return re.sub(r'\n\s*\n+', '\n', s).strip()


def dump(level, sid, name):
    bank = json.load(open("bank_%s.json" % sid))
    out = ["# %s %s — full content for review" % (level, name), ""]
    byt = {}
    for q in bank["questions"]:
        byt.setdefault(q["topic"], []).append(q)
    for t in bank["topics"]:
        out.append("## TOPIC [%s] %s   (section: %s)" % (t["id"], t["name"], t["section"]))
        out.append("PLAIN WORDS: " + plain(t.get("plain", "")))
        for i, n in enumerate(t["notes"], 1):
            out.append("KEY FACT %d: %s" % (i, plain(n)))
        if t.get("apply"):
            out.append("USE IT: " + plain(t["apply"]))
        if t.get("figcap"):
            out.append("FIGURE CAPTION: " + plain(t["figcap"]))
        for j, e in enumerate(t.get("examples", []), 1):
            out.append("WORKED EXAMPLE %d: %s" % (j, plain(e["q"])))
            for s in e["steps"]:
                out.append("    " + plain(s))
        for q in byt.get(t["id"], []):
            if q["type"] == "obj":
                out.append("Q[%s] %s" % (q["id"], plain(q["q"])))
                for k, o in enumerate(q["opts"]):
                    out.append("   %s%s %s" % (LET[k], "*" if k == q["ans"] else ".", plain(o)))
                out.append("   KEY: %s" % LET[q["ans"]])
                for s in q["sol"]:
                    out.append("   WHY: " + plain(s))
            else:
                out.append("T[%s] (%s marks) %s" % (q["id"], q.get("marks", "?"), plain(q["q"])))
                for s in q["sol"]:
                    out.append("   ANS: " + plain(s))
        out.append("")
    path = "audit/%s_%s.md" % (level.lower(), sid)
    open(path, "w", encoding="utf-8").write("\n".join(out))
    return path, bank


def checks(level, sid, name, bank):
    bad = []
    qs = bank["questions"]
    obj = [q for q in qs if q["type"] == "obj"]
    # 1. duplicate stems
    stems = Counter(plain(q["q"]).lower() for q in qs)
    for s, n in stems.items():
        if n > 1:
            bad.append("DUPLICATE STEM x%d: %s" % (n, s[:90]))
    # 2. option problems
    for q in obj:
        opts = [plain(o) for o in q["opts"]]
        if len(set(opts)) != 4:
            bad.append("%s: options not distinct after stripping markup" % q["id"])
        if any(not o for o in opts):
            bad.append("%s: empty option" % q["id"])
        lens = [len(o) for o in opts]
        others = [lens[i] for i in range(4) if i != q["ans"]]
        if lens[q["ans"]] == max(lens) and lens[q["ans"]] > 60 and lens[q["ans"]] > 1.7 * (sum(others) / 3.0):
            bad.append("%s: the key is much longer than the distractors (give-away)" % q["id"])
        if any(o.lower() in ("all of the above", "none of the above") for o in opts):
            bad.append("%s: 'all/none of the above' is not used in WAEC objectives" % q["id"])
    # 3. answer key spread
    c = Counter(q["ans"] for q in obj)
    worst = max(c.values()) / float(len(obj))
    if worst > 0.33:
        bad.append("key spread skewed: %s of %d" % (dict(c), len(obj)))
    # 4. solutions present and non-trivial
    for q in qs:
        if not q["sol"] or any(not plain(s) for s in q["sol"]):
            bad.append("%s: empty solution line" % q["id"])
        if q["type"] == "obj" and len(q["sol"]) < 2:
            bad.append("%s: only one line of working" % q["id"])
    # 5. theory marks sensible
    for q in qs:
        if q["type"] == "thy":
            m = q.get("marks")
            if not m or m < 4 or m > 60:
                bad.append("%s: odd mark allocation (%s)" % (q["id"], m))
    # 6. balanced tags
    void = {"br", "img", "line", "circle", "path", "polygon", "rect", "text", "polyline", "ellipse", "marker"}
    for q in qs:
        for s in [q["q"]] + q["sol"] + (q["opts"] if q["type"] == "obj" else []):
            if not isinstance(s, str):
                continue
            op = [x for x in re.findall(r'<(\w+)[^>]*?(?<!/)>', s) if x not in void]
            cl = re.findall(r'</(\w+)>', s)
            if sorted(op) != sorted(cl):
                bad.append("%s: unbalanced HTML in '%s'" % (q["id"], plain(s)[:50]))
    # 7. every topic has both types and enough objectives
    for t in bank["topics"]:
        tq = [q for q in qs if q["topic"] == t["id"]]
        if sum(1 for q in tq if q["type"] == "obj") < 4:
            bad.append("topic %s has fewer than 4 objectives" % t["id"])
        if not any(q["type"] == "thy" for q in tq):
            bad.append("topic %s has no theory question" % t["id"])
    return bad


if __name__ == "__main__":
    total_bad = 0
    for level, subs in LEVELS.items():
        for sid, name in subs:
            path, bank = dump(level, sid, name)
            bad = checks(level, sid, name, bank)
            total_bad += len(bad)
            size = os.path.getsize(path) // 1024
            print("%-8s %-24s %3d topics %4d questions  dump %3d KB  %s"
                  % (level, name, len(bank["topics"]), len(bank["questions"]), size,
                     "OK" if not bad else "%d issues" % len(bad)))
            for b in bad[:12]:
                print("      - " + b)
    print("\nautomated issues found:", total_bad)
