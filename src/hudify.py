"""Turn hub.html into the HUD-themed, Lab-equipped, level-aware shell: hub_hud.html."""
import re, sys

src = open("hub.html").read()
css = open("hud_css.txt").read()
js = open("hud_js.txt").read()
n = 0


def sub(old, new, count=1):
    global src, n
    assert src.count(old) >= count, "anchor not found:\n" + old[:160]
    src = src.replace(old, new, count)
    n += 1


# ---- fonts + stylesheet -------------------------------------------------
src = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^"]*">',
             '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
             '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
             'family=Space+Grotesk:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700'
             '&family=IBM+Plex+Mono:wght@400;500&display=swap">', src, count=1)
n += 1
src = re.sub(r'<style>.*?</style>', lambda m: "<style>\n" + css + "</style>", src, count=1, flags=re.S)
n += 1

# ---- title / header ----------------------------------------------------
src = re.sub(r'^<title>.*?</title>', '<title>__HUBTITLE__</title>', src, count=1, flags=re.M)
n += 1
sub("""    <h1>WASSCE Core Four</h1>
    <span class="sub" id="subline"></span>""",
    """    <h1>__HUBTITLE__</h1>
    <span class="sub" id="subline"></span>
    __SWITCH__""")

# ---- Lab tab + view ----------------------------------------------------
# the hub's mock tab label is fixed text, not a token - normalise it first
src = src.replace('data-view="mock">Mock Paper 1</button>', 'data-view="mock">__MOCKTAB__</button>')
n += 1
sub("""    <button class="tab" role="tab" id="tab-mock" aria-selected="false" data-view="mock">__MOCKTAB__</button>""",
    """    <button class="tab" role="tab" id="tab-lab" aria-selected="false" data-view="lab">Lab</button>
    <button class="tab" role="tab" id="tab-mock" aria-selected="false" data-view="mock">__MOCKTAB__</button>""")
sub("""  <section id="view-syllabus" hidden></section>""",
    """  <section id="view-syllabus" hidden></section>
  <section id="view-lab" hidden></section>""")

# ---- keys and exam name ------------------------------------------------
sub("var KEY = 'wassce-core-four-v1';",
    "var KEY = '__KEY__';\nvar EXAM = '__EXAM__';")

# ---- step-by-step solutions -------------------------------------------
sub("""  sol.innerHTML = '<span class="lbl">'+SUB.cfg.objSolLabel+'</span><ol><li>'+q.sol.join('</li><li>')+'</li></ol>'
      + '<p style="margin:10px 0 0"><b>Answer: '+LETTERS[q.ans]+'</b> &nbsp;<span class="note">'+q.opts[q.ans]+'</span></p>'
      + (q.tip ? '<p class="tip">'+q.tip+'</p>' : '');""",
    """  fillSol(sol, SUB.cfg.objSolLabel, q.sol,
      '<p style="margin:10px 0 0"><b>Answer: '+LETTERS[q.ans]+'</b> &nbsp;<span class="note">'+q.opts[q.ans]+'</span></p>'
      + (q.tip ? '<p class="tip">'+q.tip+'</p>' : ''));""")

sub("""  sol.innerHTML = '<span class="lbl">'+S.cfg.thySolLabel+'</span><ol><li>'+q.sol.join('</li><li>')+'</li></ol>'
      + (q.tip ? '<p class="tip">'+q.tip+'</p>' : '');""",
    """  fillSol(sol, S.cfg.thySolLabel, q.sol, (q.tip ? '<p class="tip">'+q.tip+'</p>' : ''));""")

# ---- answer feedback ---------------------------------------------------
sub("""      paint(i,true); sol.hidden=false; if(solRef) solRef.classList.add('on');
      refreshSide(); refreshChips();""",
    """      paint(i,true); sol.hidden=false; if(solRef) solRef.classList.add('on');
      feedback(card, i===q.ans, buttons[i]);
      refreshSide(); refreshChips();""")

# ---- navigation: lab + view transition --------------------------------
sub("""  ['home','topics','syllabus','mock','progress'].forEach(function(n){
    document.getElementById('view-'+n).hidden = (n!==name);
    document.getElementById('tab-'+n).setAttribute('aria-selected', n===name ? 'true':'false');
  });""",
    """  ['home','topics','syllabus','lab','mock','progress'].forEach(function(n){
    var sec = document.getElementById('view-'+n);
    sec.hidden = (n!==name);
    document.getElementById('tab-'+n).setAttribute('aria-selected', n===name ? 'true':'false');
    if (n===name && !reduced()){ sec.classList.remove('viewin'); void sec.offsetWidth; sec.classList.add('viewin'); }
  });
  if (name==='lab') drawLab();""")

# ---- rank chip on the dashboard ---------------------------------------
sub("""  var bar = el('div','lvlbar','<i></i>');
  hero.appendChild(bar);""",
    """  hero.appendChild(el('div','rankline',
      '<span class="rankchip"><i></i>' + rankOf(t.level) + ' \\u00b7 Level ' + t.level + '</span>'
      + '<span class="note">' + t.points + ' XP earned</span>'));
  var bar = el('div','lvlbar','<i></i>');
  hero.appendChild(bar);""")

# ---- exam-neutral wording ---------------------------------------------
sub("""  sc.innerHTML = '<p><b>Know someone writing WASSCE?</b> Send them this page — it is free, '
    + 'works offline, and needs no sign-in.</p>';""",
    """  sc.innerHTML = '<p><b>Know someone writing the ' + EXAM + '?</b> Send them this page \\u2014 it is free, '
    + 'works offline, and needs no sign-in.</p>';""")
sub("""    var data = {title: document.title, text: 'Free WASSCE practice — questions, worked answers and mock papers.',
                url: location.href};""",
    """    var data = {title: document.title, text: 'Free ' + EXAM + ' practice \\u2014 questions, worked answers and mock papers.',
                url: location.href};""")
sub("""  v.appendChild(el('div','lbl sec-h','Across all four subjects'));""",
    """  v.appendChild(el('div','lbl sec-h','Across all ' + SUBJECTS.length + ' subjects'));""")
sub("""    + '<p class="note" style="margin:8px 0 0">All ' + n + ' items of the WAEC syllabus for this subject, in order. '""",
    """    + '<p class="note" style="margin:8px 0 0">All ' + n + ' items of the ' + EXAM + ' syllabus for this subject, in order. '""")

# ---- topic intro: illustration up front, then "use it in real life" ----
sub("""function topicIntro(t, panel){
  if (t.plain) panel.appendChild(el('div','plain','<span class="lbl">In plain words</span>'+t.plain));
  panel.appendChild(el('div','facts','<span class="lbl">Key facts</span><ul><li>'+t.notes.join('</li><li>')+'</li></ul>'));
  if (t.fig) panel.appendChild(figWrap(t.fig));""",
    """function topicIntro(t, panel){
  if (t.plain) panel.appendChild(el('div','plain','<span class="lbl">In plain words</span>'+t.plain));
  if (t.fig) panel.appendChild(figWrap(t.fig, t.figcap));
  panel.appendChild(el('div','facts','<span class="lbl">Key facts</span><ul><li>'+t.notes.join('</li><li>')+'</li></ul>'));
  if (t.apply) panel.appendChild(el('div','applybox',
      '<div class="ic">\u2713</div><div class="bd"><span class="lbl">Use it in real life</span><br>'+t.apply+'</div>'));""")

sub("""function figWrap(svg){ var d = el('div','figwrap'); d.innerHTML = svg; return d; }""",
    """function figWrap(svg, cap){
  var d = el('div','figwrap'); d.innerHTML = svg;
  if (cap) d.appendChild(el('div','figcap', cap));
  return d;
}""")

# ---- the lab + HUD helpers --------------------------------------------
sub("""show(start);
})();""",
    js + """
show(start);
})();""")

open("hub_hud.html", "w").write(src)
print("hub_hud.html written:", len(src) // 1024, "KB,", n, "patches applied")
for tok in ["__HUBTITLE__", "__SWITCH__", "__KEY__", "__EXAM__", "__MOCKTAB__", "__BANK__"]:
    print("  token", tok, "x", src.count(tok))
