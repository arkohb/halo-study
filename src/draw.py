"""Small SVG diagram library. Every figure is theme-aware (colours come from CSS tokens)."""
import math

ARROW = ('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5.5" markerHeight="5.5" '
         'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="dah"/></marker></defs>')


def _svg(w, h, body, label):
    return (f'<svg viewBox="0 0 {w} {h}" class="dia" role="img" aria-label="{label}" '
            f'style="width:min(100%,{min(int(w * 1.15), 520)}px)">'
            f'{ARROW}{body}</svg>')


def _wrap(s, width=16):
    words, lines, cur = s.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= width or not cur:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines[:3]


def _txt(x, y, s, cls="dtxt", anchor="middle", size=None):
    st = f' style="font-size:{size}px"' if size else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" text-anchor="{anchor}"{st}>{s}</text>'


def _boxtext(cx, cy, s, cls="dtxt", width=16, lh=12, size=None):
    ls = _wrap(s, width)
    y0 = cy - (len(ls) - 1) * lh / 2 + 3.5
    return "".join(_txt(cx, y0 + i * lh, t, cls, size=size) for i, t in enumerate(ls))


def _arrow(x1, y1, x2, y2, cls="dline"):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="{cls}" marker-end="url(#ah)"/>'


# ---------------------------------------------------------------- generic
def flow(items, label="Flow chart", note=None):
    """Boxes left to right with arrows between them."""
    bw, gap, h = 104, 26, 58
    w = len(items) * bw + (len(items) - 1) * gap + 20
    top = 24 if note else 14
    g = []
    if note:
        g.append(_txt(w / 2, 15, note, "dmut", size=12))
    for i, it in enumerate(items):
        x = 10 + i * (bw + gap)
        g.append(f'<rect x="{x}" y="{top}" width="{bw}" height="{h}" rx="7" class="dbox"/>')
        g.append(_boxtext(x + bw / 2, top + h / 2, it, "dtxt", 14, 15, 13))
        if i:
            g.append(_arrow(x - gap + 3, top + h / 2, x - 4, top + h / 2))
    return _svg(w, top + h + 14, "".join(g), label)


def cyclefig(items, centre="", label="Cycle diagram"):
    """Items arranged round a circle with arrows showing the cycle."""
    w = h = 260
    cx, cy, r = w / 2, h / 2, 82
    g = [f'<circle cx="{cx}" cy="{cy}" r="{r}" class="ddash"/>']
    if centre:
        g.append(_boxtext(cx, cy, centre, "dmut", 14))
    n = len(items)
    for i, it in enumerate(items):
        ang = -math.pi / 2 + i * 2 * math.pi / n
        x, y = cx + r * math.cos(ang), cy + r * math.sin(ang)
        g.append(f'<rect x="{x-46:.1f}" y="{y-17:.1f}" width="92" height="34" rx="7" class="dfill"/>')
        g.append(_boxtext(x, y, it, "dtxt", 14, 13, 12.5))
        a1 = ang + 0.42
        a2 = ang + 2 * math.pi / n - 0.42
        g.append(f'<path d="M{cx + (r+22)*math.cos(a1):.1f},{cy + (r+22)*math.sin(a1):.1f} '
                 f'A{r+22},{r+22} 0 0 1 {cx + (r+22)*math.cos(a2):.1f},{cy + (r+22)*math.sin(a2):.1f}" '
                 f'class="dline" marker-end="url(#ah)"/>')
    return _svg(w, h, "".join(g), label)


def tree(root, kids, label="Structure diagram", sub=None):
    """One box on top, a row of boxes underneath, joined by lines."""
    bw, gap = 104, 16
    w = max(len(kids) * bw + (len(kids) - 1) * gap + 20, 260)
    g = [f'<rect x="{w/2-70:.1f}" y="10" width="140" height="42" rx="7" class="dfill"/>',
         _boxtext(w / 2, 31, root, "dtxt", 17, 14, 13)]
    y2 = 92
    for i, kd in enumerate(kids):
        x = (w - (len(kids) * bw + (len(kids) - 1) * gap)) / 2 + i * (bw + gap)
        g.append(f'<rect x="{x:.1f}" y="{y2}" width="{bw}" height="50" rx="7" class="dbox"/>')
        g.append(_boxtext(x + bw / 2, y2 + 25, kd, "dtxt", 15, 14, 12.5))
        g.append(f'<path d="M{w/2},52 L{w/2},72 L{x+bw/2:.1f},72 L{x+bw/2:.1f},{y2}" class="dline"/>')
        if sub and sub[i]:
            g.append(_txt(x + bw / 2, y2 + 66, sub[i], "dmut"))
    return _svg(w, y2 + (78 if sub else 60), "".join(g), label)


def venn2(a_label, b_label, only_a, both, only_b, outside=None, label="Venn diagram"):
    w, h = 300, 190
    g = [f'<rect x="6" y="6" width="{w-12}" height="{h-12}" rx="6" class="dbox"/>',
         f'<circle cx="118" cy="95" r="62" class="dfill" fill-opacity="0.45"/>',
         f'<circle cx="182" cy="95" r="62" class="dfill" fill-opacity="0.45"/>',
         _txt(78, 30, a_label, "dtxt"), _txt(224, 30, b_label, "dtxt"),
         _txt(88, 100, str(only_a), "dtxt"), _txt(150, 100, str(both), "dtxt"), _txt(212, 100, str(only_b), "dtxt")]
    if outside is not None:
        g.append(_txt(w - 24, h - 16, str(outside), "dmut"))
        g.append(_txt(20, 22, "U", "dmut"))
    return _svg(w, h, "".join(g), label)


def venn3(labels, vals, label="Venn diagram"):
    """vals: [A only, B only, C only, AB, BC, AC, ABC, outside]"""
    w, h = 300, 250
    A, B, C = labels
    g = [f'<rect x="6" y="6" width="{w-12}" height="{h-12}" rx="6" class="dbox"/>', _txt(20, 22, "U", "dmut"),
         '<circle cx="118" cy="105" r="66" class="dfill" fill-opacity="0.4"/>',
         '<circle cx="182" cy="105" r="66" class="dfill" fill-opacity="0.4"/>',
         '<circle cx="150" cy="160" r="66" class="dfill" fill-opacity="0.4"/>',
         _txt(70, 42, A, "dtxt"), _txt(232, 42, B, "dtxt"), _txt(150, 238, C, "dtxt"),
         _txt(92, 92, str(vals[0])), _txt(208, 92, str(vals[1])), _txt(150, 208, str(vals[2])),
         _txt(150, 88, str(vals[3])), _txt(184, 150, str(vals[4])), _txt(116, 150, str(vals[5])),
         _txt(150, 130, str(vals[6])), _txt(w - 26, h - 18, str(vals[7]), "dmut")]
    return _svg(w, h, "".join(g), label)


def numline(lo, hi, seg=None, marks=(), label="Number line"):
    """seg = (a, b, closed_a, closed_b); use None for an open end (arrow)."""
    w, h = 320, 70
    pad = 24
    sx = lambda v: pad + (v - lo) / (hi - lo) * (w - 2 * pad)
    g = [f'<line x1="{pad}" y1="36" x2="{w-pad}" y2="36" class="dline" marker-end="url(#ah)"/>']
    for v in range(math.ceil(lo), math.floor(hi) + 1):
        g.append(f'<line x1="{sx(v):.1f}" y1="31" x2="{sx(v):.1f}" y2="41" class="dline"/>')
        g.append(_txt(sx(v), 56, str(v).replace("-", "−"), "dmut"))
    if seg:
        a, b, ca, cb = seg
        xa, xb = sx(a if a is not None else lo), sx(b if b is not None else hi)
        g.append(f'<line x1="{xa:.1f}" y1="36" x2="{xb:.1f}" y2="36" class="dacc" stroke-width="4"/>')
        if a is not None:
            g.append(f'<circle cx="{xa:.1f}" cy="36" r="5" class="{"dsolidpt" if ca else "dopenpt"}"/>')
        if b is not None:
            g.append(f'<circle cx="{xb:.1f}" cy="36" r="5" class="{"dsolidpt" if cb else "dopenpt"}"/>')
    for (v, t) in marks:
        g.append(f'<circle cx="{sx(v):.1f}" cy="36" r="4" class="dsolidpt"/>')
        g.append(_txt(sx(v), 20, t, "dtxt"))
    return _svg(w, h, "".join(g), label)


def barfig(data, label="Bar chart", ylab=""):
    """data: [(name, value), ...]"""
    w, h = 320, 200
    pad_l, pad_b, top = 34, 34, 16
    mx = max(v for _, v in data) or 1
    bw = (w - pad_l - 14) / len(data)
    g = [f'<line x1="{pad_l}" y1="{top}" x2="{pad_l}" y2="{h-pad_b}" class="dline"/>',
         f'<line x1="{pad_l}" y1="{h-pad_b}" x2="{w-8}" y2="{h-pad_b}" class="dline"/>']
    if ylab:
        g.append(_txt(8, top + 4, ylab, "dmut", "start"))
    for i, (nm, v) in enumerate(data):
        bh = (h - pad_b - top) * v / mx
        x = pad_l + i * bw + bw * 0.18
        g.append(f'<rect x="{x:.1f}" y="{h-pad_b-bh:.1f}" width="{bw*0.64:.1f}" height="{bh:.1f}" class="dfill"/>')
        g.append(_txt(x + bw * 0.32, h - pad_b - bh - 5, str(v), "dmut"))
        g.append(_txt(x + bw * 0.32, h - pad_b + 14, nm, "dmut"))
    return _svg(w, h, "".join(g), label)


def piefig(data, label="Pie chart"):
    """data: [(name, value), ...] — sectors with their angles."""
    w, h = 320, 220
    cx, cy, r = 110, 108, 84
    total = sum(v for _, v in data)
    ang = -90
    g = []
    for i, (nm, v) in enumerate(data):
        sweep = 360 * v / total
        a1, a2 = math.radians(ang), math.radians(ang + sweep)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
        large = 1 if sweep > 180 else 0
        op = 0.25 + 0.6 * (i / max(1, len(data) - 1))
        g.append(f'<path d="M{cx},{cy} L{x1:.1f},{y1:.1f} A{r},{r} 0 {large} 1 {x2:.1f},{y2:.1f} Z" '
                 f'class="dfill" fill-opacity="{op:.2f}"/>')
        mid = math.radians(ang + sweep / 2)
        g.append(_txt(cx + (r + 16) * math.cos(mid), cy + (r + 16) * math.sin(mid) + 3, f"{round(sweep)}°", "dmut"))
        g.append(f'<rect x="216" y="{26+i*22}" width="11" height="11" class="dfill" fill-opacity="{op:.2f}"/>')
        g.append(_txt(233, 36 + i * 22, nm, "dmut", "start"))
        ang += sweep
    return _svg(w, h, "".join(g), label)


def pyramidfig(levels, label="Pyramid diagram"):
    """levels: top first."""
    w, h = 300, 40 + 44 * len(levels)
    g = []
    n = len(levels)
    for i, t in enumerate(levels):
        half = 42 + i * (100 / n)
        y = 20 + i * 44
        g.append(f'<polygon points="{150-half:.0f},{y+40} {150+half:.0f},{y+40} '
                 f'{150+half-100/n/2:.0f},{y} {150-half+100/n/2:.0f},{y}" class="dfill" fill-opacity="{0.2+0.18*i:.2f}"/>')
        g.append(_txt(150, y + 25, t, "dtxt"))
    return _svg(w, h, "".join(g), label)


# ---------------------------------------------------------------- maths
def tri(a="", b="", c="", A="", B="", C="", right=False, label="Triangle"):
    """Triangle with vertices A (left), B (right), C (top). a,b,c are side labels."""
    w, h = 300, 190
    P = {"A": (40, 150), "B": (250, 150), "C": (170, 40)}
    g = [f'<polygon points="40,150 250,150 170,40" class="dfill" fill-opacity="0.25"/>',
         '<polyline points="40,150 250,150 170,40 40,150" class="dacc"/>']
    if right:
        g.append('<polyline points="232,150 232,132 250,132" class="dline"/>')
    g += [_txt(30, 162, A or "A"), _txt(258, 162, B or "B"), _txt(172, 32, C or "C"),
          _txt(145, 166, c or "", "dmut"), _txt(220, 90, a or "", "dmut"), _txt(92, 88, b or "", "dmut")]
    return _svg(w, h, "".join(g), label)


def circlefig(kind, angles=None, label="Circle diagram"):
    w, h = 300, 240
    cx, cy, r = 150, 118, 88
    g = [f'<circle cx="{cx}" cy="{cy}" r="{r}" class="dacc"/>']
    P = lambda deg: (cx + r * math.cos(math.radians(deg)), cy - r * math.sin(math.radians(deg)))
    if kind == "centre":
        A, B, C = P(210), P(330), P(80)
        g += [f'<line x1="{A[0]:.0f}" y1="{A[1]:.0f}" x2="{cx}" y2="{cy}" class="dline"/>',
              f'<line x1="{B[0]:.0f}" y1="{B[1]:.0f}" x2="{cx}" y2="{cy}" class="dline"/>',
              f'<line x1="{A[0]:.0f}" y1="{A[1]:.0f}" x2="{C[0]:.0f}" y2="{C[1]:.0f}" class="dline"/>',
              f'<line x1="{B[0]:.0f}" y1="{B[1]:.0f}" x2="{C[0]:.0f}" y2="{C[1]:.0f}" class="dline"/>',
              f'<circle cx="{cx}" cy="{cy}" r="3" class="dsolidpt"/>',
              _txt(cx, cy - 10, "O", "dmut"), _txt(A[0] - 12, A[1] + 6, "A"), _txt(B[0] + 12, B[1] + 6, "B"),
              _txt(C[0], C[1] - 8, "C"),
              _txt(cx, cy + 26, (angles or ["2x", "x"])[0], "dtxt"),
              _txt(C[0], C[1] + 26, (angles or ["2x", "x"])[1], "dtxt")]
    elif kind == "cyclic":
        pts = [P(150), P(40), P(320), P(215)]
        g += ['<polyline points="' + " ".join(f"{p[0]:.0f},{p[1]:.0f}" for p in pts + [pts[0]]) + '" class="dline"/>']
        for lb, p, dy in zip("ABCD", pts, (-8, -8, 16, 16)):
            g.append(_txt(p[0], p[1] + dy, lb))
        g += [_txt(pts[0][0] + 16, pts[0][1] + 20, (angles or ["a", "b"])[0], "dtxt"),
              _txt(pts[2][0] - 16, pts[2][1] - 16, (angles or ["a", "b"])[1], "dtxt")]
    elif kind == "tangent":
        T = P(270)
        g += [f'<line x1="40" y1="{T[1]:.0f}" x2="260" y2="{T[1]:.0f}" class="dacc"/>',
              f'<line x1="{cx}" y1="{cy}" x2="{T[0]:.0f}" y2="{T[1]:.0f}" class="dline"/>',
              '<polyline points="' + f'{T[0]-16:.0f},{T[1]} {T[0]-16:.0f},{T[1]-16:.0f} {T[0]:.0f},{T[1]-16:.0f}' + '" class="dline"/>',
              f'<circle cx="{cx}" cy="{cy}" r="3" class="dsolidpt"/>',
              _txt(cx - 12, cy, "O"), _txt(T[0] + 6, T[1] + 16, "T"), _txt(70, T[1] + 18, "tangent", "dmut")]
    return _svg(w, h, "".join(g), label)


def sectorfig(angle=72, rlabel="r", label="Sector of a circle"):
    w, h = 280, 210
    cx, cy, r = 110, 130, 86
    a2 = math.radians(angle)
    x2, y2 = cx + r * math.cos(-a2 + 0), cy + r * math.sin(-a2)
    g = [f'<path d="M{cx},{cy} L{cx+r},{cy} A{r},{r} 0 {1 if angle>180 else 0} 0 {x2:.1f},{y2:.1f} Z" class="dfill"/>',
         f'<path d="M{cx+30},{cy} A30,30 0 0 0 {cx+30*math.cos(a2):.1f},{cy-30*math.sin(a2):.1f}" class="dline"/>',
         _txt(cx + 46, cy - 12, f"{angle}°", "dtxt"),
         _txt(cx + r / 2, cy + 16, rlabel, "dmut"),
         _txt(cx + 70, cy - 74, "arc", "dmut")]
    return _svg(w, h, "".join(g), label)


def solidfig(kind, labels=(), label="Solid shape"):
    w, h = 280, 200
    g = []
    if kind == "cylinder":
        g = ['<ellipse cx="110" cy="42" rx="56" ry="18" class="dfill"/>',
             '<path d="M54,42 L54,150 A56,18 0 0 0 166,150 L166,42" class="dfill"/>',
             '<ellipse cx="110" cy="42" rx="56" ry="18" class="dacc"/>',
             '<line x1="110" y1="42" x2="166" y2="42" class="ddash"/>',
             _txt(140, 20, labels[0] if labels else "r", "dmut"),
             '<line x1="186" y1="42" x2="186" y2="150" class="dline"/>',
             _txt(200, 100, labels[1] if len(labels) > 1 else "h", "dmut")]
    elif kind == "cone":
        g = ['<path d="M110,26 L54,138 A56,18 0 0 0 166,138 Z" class="dfill"/>',
             '<ellipse cx="110" cy="138" rx="56" ry="18" class="dacc"/>',
             '<line x1="110" y1="26" x2="110" y2="138" class="ddash"/>',
             '<line x1="110" y1="138" x2="166" y2="138" class="ddash"/>',
             _txt(100, 92, labels[1] if len(labels) > 1 else "h", "dmut"),
             _txt(140, 132, labels[0] if labels else "r", "dmut"),
             _txt(150, 80, labels[2] if len(labels) > 2 else "l", "dmut")]
    elif kind == "sphere":
        g = ['<circle cx="110" cy="100" r="66" class="dfill"/>',
             '<ellipse cx="110" cy="100" rx="66" ry="18" class="ddash"/>',
             '<line x1="110" y1="100" x2="176" y2="100" class="dline"/>',
             _txt(142, 92, labels[0] if labels else "r", "dmut")]
    elif kind == "cuboid":
        g = ['<polygon points="40,60 150,60 190,34 80,34" class="dfill"/>',
             '<rect x="40" y="60" width="110" height="80" class="dfill"/>',
             '<polygon points="150,60 190,34 190,114 150,140" class="dfill" fill-opacity="0.35"/>',
             _txt(95, 155, labels[0] if labels else "l", "dmut"),
             _txt(24, 104, labels[1] if len(labels) > 1 else "h", "dmut"),
             _txt(178, 134, labels[2] if len(labels) > 2 else "w", "dmut")]
    return _svg(w, h, "".join(g), label)


def compass(rays, label="Bearings diagram"):
    """rays: [(bearing_degrees, text, length_fraction)] measured clockwise from north."""
    w, h = 300, 260
    cx, cy = 140, 140
    g = [f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="30" class="dline" marker-end="url(#ah)"/>',
         _txt(cx, 22, "N", "dtxt"),
         f'<circle cx="{cx}" cy="{cy}" r="3" class="dsolidpt"/>']
    for brg, t, fr in rays:
        L = 100 * fr
        a = math.radians(90 - brg)
        x, y = cx + L * math.cos(a), cy - L * math.sin(a)
        g.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" class="dacc"/>')
        g.append(_txt(x + (12 if x >= cx else -12), y + 4, t, "dtxt"))
        r2 = 34
        g.append(f'<path d="M{cx},{cy-r2} A{r2},{r2} 0 {1 if brg>180 else 0} 1 '
                 f'{cx + r2*math.cos(a):.1f},{cy - r2*math.sin(a):.1f}" class="dline"/>')
        g.append(_txt(cx + (r2 + 14) * math.cos(math.radians(90 - brg / 2)),
                      cy - (r2 + 14) * math.sin(math.radians(90 - brg / 2)) + 4, f"{brg:03d}°", "dmut"))
    return _svg(w, h, "".join(g), label)


# ---------------------------------------------------------------- science
def cellfig(kind="plant", label="Cell diagram"):
    w, h = 320, 210
    if kind == "plant":
        g = ['<rect x="24" y="24" width="270" height="160" rx="10" class="dfill"/>',
             '<rect x="34" y="34" width="250" height="140" rx="8" class="dbox"/>',
             '<ellipse cx="110" cy="100" rx="26" ry="22" class="dfill" fill-opacity="0.8"/>',
             _txt(110, 104, "nucleus", "dmut"),
             '<rect x="160" y="70" width="96" height="62" rx="8" class="dbox"/>',
             _txt(208, 104, "vacuole", "dmut"),
             '<ellipse cx="78" cy="146" rx="22" ry="11" class="dfill" fill-opacity="0.9"/>',
             _txt(78, 168, "chloroplast", "dmut"),
             _txt(150, 18, "cell wall (outer) · cell membrane (inner)", "dmut"),
             _txt(150, 200, "cytoplasm fills the rest of the cell", "dmut")]
    else:
        g = ['<ellipse cx="160" cy="104" rx="130" ry="76" class="dfill"/>',
             '<ellipse cx="150" cy="100" rx="30" ry="25" class="dbox"/>',
             _txt(150, 104, "nucleus", "dmut"),
             '<ellipse cx="236" cy="132" rx="22" ry="11" class="dbox"/>',
             _txt(236, 136, "mitochondrion", "dmut", size=8),
             _txt(160, 22, "cell membrane (no cell wall)", "dmut"),
             _txt(160, 196, "cytoplasm — no chloroplasts, no large vacuole", "dmut")]
    return _svg(w, h, "".join(g), label)


def raysfig(kind="reflect", label="Light diagram"):
    w, h = 320, 200
    if kind == "reflect":
        g = ['<line x1="30" y1="150" x2="290" y2="150" class="dacc"/>',
             '<line x1="160" y1="150" x2="160" y2="40" class="ddash"/>',
             _txt(160, 32, "normal", "dmut"),
             '<line x1="60" y1="55" x2="160" y2="150" class="dline" marker-end="url(#ah)"/>',
             '<line x1="160" y1="150" x2="260" y2="55" class="dline" marker-end="url(#ah)"/>',
             _txt(84, 48, "incident ray", "dmut"), _txt(246, 48, "reflected ray", "dmut"),
             _txt(140, 116, "i", "dtxt"), _txt(182, 116, "r", "dtxt"),
             _txt(160, 176, "i = r  (plane mirror)", "dmut")]
    elif kind == "refract":
        g = ['<rect x="30" y="100" width="260" height="76" rx="4" class="dfill" fill-opacity="0.35"/>',
             '<line x1="30" y1="100" x2="290" y2="100" class="dacc"/>',
             '<line x1="160" y1="30" x2="160" y2="170" class="ddash"/>',
             '<line x1="70" y1="34" x2="160" y2="100" class="dline" marker-end="url(#ah)"/>',
             '<line x1="160" y1="100" x2="205" y2="172" class="dline" marker-end="url(#ah)"/>',
             _txt(92, 28, "ray in air", "dmut"), _txt(240, 140, "bends towards", "dmut"),
             _txt(240, 156, "the normal", "dmut"), _txt(62, 120, "water / glass", "dmut", "start")]
    else:  # lens
        g = ['<path d="M160,40 Q196,100 160,160 Q124,100 160,40 Z" class="dfill"/>',
             '<line x1="20" y1="100" x2="300" y2="100" class="ddash"/>',
             '<line x1="20" y1="60" x2="160" y2="60" class="dline" marker-end="url(#ah)"/>',
             '<line x1="160" y1="60" x2="250" y2="100" class="dline" marker-end="url(#ah)"/>',
             '<line x1="20" y1="140" x2="160" y2="140" class="dline" marker-end="url(#ah)"/>',
             '<line x1="160" y1="140" x2="250" y2="100" class="dline" marker-end="url(#ah)"/>',
             f'<circle cx="250" cy="100" r="4" class="dsolidpt"/>',
             _txt(258, 92, "F", "dtxt"), _txt(60, 52, "parallel rays", "dmut"),
             _txt(160, 182, "convex (converging) lens", "dmut")]
    return _svg(w, h, "".join(g), label)


def circuitfig(label="Series circuit"):
    w, h = 300, 180
    g = ['<rect x="40" y="40" width="220" height="100" rx="4" class="dline"/>',
         # cell
         '<line x1="130" y1="40" x2="130" y2="26" class="dline"/>',
         '<line x1="118" y1="34" x2="142" y2="34" class="dline" stroke-width="3"/>',
         '<line x1="124" y1="46" x2="136" y2="46" class="dline"/>',
         _txt(150, 22, "cell (V)", "dmut", "start"),
         # resistor
         '<rect x="236" y="70" width="48" height="26" rx="3" class="dfill" transform="rotate(90 260 83)"/>',
         _txt(274, 88, "R", "dtxt", "start"),
         # ammeter
         '<circle cx="150" cy="140" r="14" class="dbox"/>', _txt(150, 144, "A", "dtxt"),
         _txt(150, 168, "current I flows round the loop", "dmut")]
    return _svg(w, h, "".join(g), label)


def leverfig(cls=1, label="Lever diagram"):
    w, h = 300, 166
    g = ['<rect x="30" y="70" width="240" height="10" rx="3" class="dfill"/>']
    pos = {1: (150, 60, 240), 2: (50, 230, 130), 3: (50, 240, 150)}
    fx, lx, ex = pos[cls]
    g += [f'<polygon points="{fx-14},108 {fx+14},108 {fx},82" class="dfill"/>',
          _txt(fx, 126, "fulcrum", "dmut"),
          f'<line x1="{lx}" y1="66" x2="{lx}" y2="26" class="dline" marker-end="url(#ah)"/>', _txt(lx, 20, "load", "dmut"),
          f'<line x1="{ex}" y1="82" x2="{ex}" y2="124" class="dline" marker-end="url(#ah)"/>', _txt(ex, 140, "effort", "dmut")]
    names = {1: "1st class — see-saw, scissors", 2: "2nd class — wheelbarrow, bottle opener", 3: "3rd class — tongs, forearm"}
    g.append(_txt(150, 156, names[cls], "dmut"))
    return _svg(w, h, "".join(g), label)


# ---------------------------------------------------------------- english / social
def letterfig(label="Formal letter layout"):
    w, h = 300, 320
    g = ['<rect x="18" y="12" width="264" height="296" rx="6" class="dbox"/>']
    rows = [("Your address", 40, "end"), ("Date", 62, "end"),
            ("The District Chief Executive", 96, "start"), ("(receiver's address)", 112, "start"),
            ("Dear Sir / Madam,", 148, "start"), ("TITLE IN CAPITALS", 176, "start"),
            ("Yours faithfully,", 262, "start"), ("YOUR FULL NAME", 284, "start")]
    for t, y, anch in rows:
        x = 264 if anch == "end" else 36
        g.append(_txt(x, y, t, "dtxt" if t.isupper() or t.startswith("Dear") else "dmut", anch))
    g.append('<rect x="36" y="192" width="228" height="56" rx="4" class="dfill" fill-opacity="0.35"/>')
    g.append(_txt(150, 224, "Body: 3 or 4 paragraphs", "dmut"))
    return _svg(w, h, "".join(g), label)


# ================================================================ animated figures
# The CSS classes used here (dmarch, dpulse, dbob, drise, dspin, dp-*) are defined in the
# theme stylesheet, and the global prefers-reduced-motion rule switches every one of them off.

def animflow(items, label="Flow chart", note=None, colour=True):
    """Like flow(), but the arrows march and each box fades in after the one before it."""
    bw, gap, h = 108, 28, 60
    w = len(items) * bw + (len(items) - 1) * gap + 20
    top = 26 if note else 14
    g = []
    if note:
        g.append(_txt(w / 2, 16, note, "dmut", size=12))
    for i, it in enumerate(items):
        x = 10 + i * (bw + gap)
        cls = "dfill" if (colour and i in (0, len(items) - 1)) else "dbox"
        g.append(f'<rect x="{x}" y="{top}" width="{bw}" height="{h}" rx="8" class="{cls} dstep" '
                 f'style="animation-delay:{i * 0.28:.2f}s"/>')
        g.append(_boxtext(x + bw / 2, top + h / 2, it, "dtxt", 15, 15, 13))
        if i:
            g.append(f'<line x1="{x - gap + 3:.0f}" y1="{top + h / 2:.0f}" x2="{x - 5:.0f}" y2="{top + h / 2:.0f}" '
                     f'class="dacc dmarch" marker-end="url(#ah)"/>')
    return _svg(w, top + h + 16, "".join(g), label)


def animcycle(items, centre="", label="Cycle diagram"):
    """A cycle whose arrows flow round and round."""
    w = h = 300
    cx = cy = 150
    R = 96
    n = len(items)
    g = []
    for i in range(n):
        a0 = math.radians(-90 + i * 360 / n)
        a1 = math.radians(-90 + (i + 1) * 360 / n)
        x0, y0 = cx + R * math.cos(a0), cy + R * math.sin(a0)
        x1, y1 = cx + R * math.cos(a1), cy + R * math.sin(a1)
        mx, my = cx + (R + 26) * math.cos(a0), cy + (R + 26) * math.sin(a0)
        # arc from this node to the next
        g.append(f'<path d="M{x0:.1f},{y0:.1f} A{R},{R} 0 0 1 {x1:.1f},{y1:.1f}" class="dacc dmarch" '
                 f'marker-end="url(#ah)" fill="none"/>')
        g.append(f'<circle cx="{x0:.1f}" cy="{y0:.1f}" r="9" class="dfill dpulse" '
                 f'style="animation-delay:{i * 0.4:.2f}s"/>')
        g.append(_boxtext(mx, my, items[i], "dtxt", 13, 13, 12))
    if centre:
        g.append(_boxtext(cx, cy, centre, "dmut", 12, 14, 12))
    return _svg(w, h, "".join(g), label)


def particles(state="solid", label=None):
    """The particle model of matter, animated: solid, liquid or gas."""
    w, h = 300, 170
    titles = {"solid": "SOLID - packed in a pattern, only vibrating",
              "liquid": "LIQUID - touching but free to slide",
              "gas": "GAS - far apart, moving fast in all directions"}
    g = ['<rect x="16" y="14" width="268" height="118" rx="8" class="dbox"/>']
    import random as _r
    rnd = _r.Random({"solid": 1, "liquid": 2, "gas": 3}[state])
    if state == "solid":
        pts = [(46 + c * 32, 32 + r * 24) for r in range(4) for c in range(7)]
    elif state == "liquid":
        pts = [(40 + c * 30 + (6 if r % 2 else 0), 56 + r * 26) for r in range(3) for c in range(8)][:22]
    else:
        pts = [(34 + rnd.random() * 232, 24 + rnd.random() * 96) for _ in range(14)]
    cls = {"solid": "dp-solid", "liquid": "dp-liq", "gas": "dp-gas"}[state]
    for i, (x, y) in enumerate(pts):
        g.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" class="dsolidpt {cls}" '
                 f'style="animation-delay:-{(i % 9) * 0.23:.2f}s"/>')
    g.append(_txt(150, 152, titles[state], "dmut"))
    return _svg(w, h, "".join(g), label or ("Particles in a " + state))


def phscale(value=7, name="", label="The pH scale"):
    """pH 0-14 with a pointer, and what the colour means."""
    w, h = 320, 150
    x0, x1, y = 24, 296, 60
    g = []
    cols = ["#D03A2B", "#E0603A", "#E89A3C", "#E8C83C", "#BFD040", "#6FC06A", "#3BAF7A",
            "#2FA8A0", "#2E8FB8", "#2E6FC0", "#3A52B8", "#4A3FAE", "#5A33A0", "#6B2A92", "#7A2288"]
    bw = (x1 - x0) / 15
    for i, c in enumerate(cols):
        g.append(f'<rect x="{x0 + i * bw:.1f}" y="{y}" width="{bw + .6:.1f}" height="26" fill="{c}"/>')
        if i % 2 == 0:
            g.append(_txt(x0 + i * bw + bw / 2, y + 44, str(i), "dmut", size=10))
    px = x0 + (value + 0.5) * bw
    g.append(f'<polygon points="{px - 9:.1f},{y - 6} {px + 9:.1f},{y - 6} {px:.1f},{y + 6}" class="dsolidpt dbob"/>')
    word = "acidic" if value < 7 else ("neutral" if value == 7 else "basic (alkaline)")
    g.append(_txt(150, 26, (name + " - " if name else "") + "pH " + str(value) + ", " + word, "dtxt"))
    g.append(_txt(60, 124, "acids turn blue litmus RED", "dmut"))
    g.append(_txt(250, 124, "bases turn red litmus BLUE", "dmut"))
    return _svg(w, h, "".join(g), label)


def plantfig(label="Photosynthesis"):
    """A leaf taking in light, water and carbon dioxide and giving out oxygen."""
    w, h = 320, 210
    g = ['<circle cx="48" cy="40" r="20" class="dfill dpulse"/>', _txt(48, 45, "sun", "dmut"),
         '<path d="M118,150 C118,96 160,70 214,70 C214,124 172,150 118,150 Z" class="dfill"/>',
         '<path d="M118,150 L214,70" class="dacc"/>',
         _txt(150, 186, "leaf (chlorophyll)", "dmut")]
    for i in range(3):
        g.append(f'<line x1="{66 + i * 10}" y1="{54 + i * 6}" x2="{120 + i * 10}" y2="{100 + i * 6}" '
                 f'class="dacc dmarch"/>')
    g.append(_txt(78, 112, "light", "dmut"))
    g.append('<line x1="34" y1="178" x2="112" y2="150" class="dline dmarch" marker-end="url(#ah)"/>')
    g.append(_txt(14, 200, "water from the roots", "dmut", "start"))
    g.append('<line x1="286" y1="150" x2="218" y2="120" class="dline dmarch" marker-end="url(#ah)"/>')
    g.append(_txt(312, 170, "carbon dioxide", "dmut", "end"))
    for i in range(4):
        g.append(f'<circle cx="{196 + i * 14}" cy="62" r="5" class="dsolidpt drise" '
                 f'style="animation-delay:-{i * 0.6:.1f}s"/>')
    g.append(_txt(312, 28, "oxygen out", "dtxt", "end"))
    return _svg(w, h, "".join(g), label)


def labware(kind="filter", label=None):
    """Simple apparatus drawings for the practicals."""
    w, h = 300, 200
    if kind == "filter":
        g = ['<polygon points="96,40 204,40 156,110 144,110" class="dbox"/>',
             '<polygon points="104,46 196,46 152,104 148,104" class="dfill" fill-opacity="0.5"/>',
             '<rect x="144" y="110" width="12" height="26" class="dbox"/>',
             '<path d="M112,140 L112,186 Q150,196 188,186 L188,140 Z" class="dbox"/>',
             '<path d="M112,164 L112,186 Q150,196 188,186 L188,164 Z" class="dfill"/>',
             f'<circle cx="150" cy="148" r="3" class="dsolidpt drise" style="animation-delay:-.3s"/>',
             _txt(236, 60, "residue stays", "dmut", "end"), _txt(150, 36, "filter paper in a funnel", "dmut"),
             _txt(150, 178, "filtrate", "dmut")]
    elif kind == "evaporate":
        g = ['<path d="M96,96 Q150,140 204,96 Z" class="dbox"/>',
             '<path d="M104,100 Q150,130 196,100 Z" class="dfill"/>',
             '<polygon points="140,150 160,150 150,134" class="dfill dpulse"/>',
             _txt(150, 174, "heat gently", "dmut")]
        for i in range(3):
            g.append(f'<circle cx="{126 + i * 24}" cy="86" r="5" class="dsolidpt drise" '
                     f'style="animation-delay:-{i * .7:.1f}s"/>')
        g.append(_txt(150, 40, "water leaves as vapour, salt stays", "dmut"))
    elif kind == "distil":
        g = ['<path d="M52,120 Q86,160 120,120 Z" class="dbox"/>',
             '<path d="M58,124 Q86,150 114,124 Z" class="dfill"/>',
             '<rect x="86" y="70" width="10" height="52" class="dbox"/>',
             '<rect x="96" y="66" width="120" height="16" rx="8" class="dbox"/>',
             '<rect x="96" y="66" width="120" height="16" rx="8" class="dfill dmarch" fill-opacity="0.35"/>',
             '<path d="M214,82 L214,120 Q240,132 262,120 L262,82 Z" class="dbox"/>',
             '<path d="M214,104 L214,120 Q240,132 262,120 L262,104 Z" class="dfill"/>',
             _txt(86, 174, "salt water, heated", "dmut"), _txt(156, 56, "condenser", "dmut"),
             _txt(238, 152, "pure water", "dmut")]
    else:  # magnet
        g = ['<rect x="60" y="60" width="40" height="80" rx="8" class="dfill"/>', _txt(80, 106, "N", "dtxt"),
             '<rect x="200" y="60" width="40" height="80" rx="8" class="dbox"/>', _txt(220, 106, "iron", "dmut")]
        for i in range(5):
            g.append(f'<circle cx="{118 + i * 16}" cy="{86 + (i % 3) * 14}" r="4" class="dsolidpt dmarch"/>')
        g.append(_txt(150, 172, "iron filings jump to the magnet; sulphur stays", "dmut"))
    return _svg(w, h, "".join(g), label or ("Apparatus: " + kind))


def reflectfig(angle=40, label="Reflection at a plane mirror"):
    """Incident and reflected rays with equal angles, drawn to the angle given."""
    w, h = 300, 180
    cx, cy = 150, 130
    L = 100
    a = math.radians(angle)
    ix, iy = cx - L * math.sin(a), cy - L * math.cos(a)
    rx, ry = cx + L * math.sin(a), cy - L * math.cos(a)
    g = ['<line x1="30" y1="130" x2="270" y2="130" class="dacc"/>',
         '<rect x="30" y="131" width="240" height="8" class="dfill" fill-opacity="0.45"/>',
         f'<line x1="{cx}" y1="130" x2="{cx}" y2="26" class="ddash"/>', _txt(cx + 22, 32, "normal", "dmut"),
         f'<line x1="{ix:.1f}" y1="{iy:.1f}" x2="{cx}" y2="{cy}" class="dline dmarch" marker-end="url(#ah)"/>',
         f'<line x1="{cx}" y1="{cy}" x2="{rx:.1f}" y2="{ry:.1f}" class="dacc dmarch" marker-end="url(#ah)"/>',
         f'<path d="M{cx - 34 * math.sin(a):.1f},{cy - 34 * math.cos(a):.1f} A34,34 0 0 1 {cx},{cy - 34}" class="dline"/>',
         f'<path d="M{cx},{cy - 34} A34,34 0 0 1 {cx + 34 * math.sin(a):.1f},{cy - 34 * math.cos(a):.1f}" class="dline"/>',
         _txt(cx - 46, cy - 46, "i = " + str(angle) + "°", "dtxt"),
         _txt(cx + 46, cy - 46, "r = " + str(angle) + "°", "dtxt"),
         _txt(150, 162, "angle of incidence = angle of reflection", "dmut")]
    return _svg(w, h, "".join(g), label)
