"""Build both level apps from hub_hud.html: wassce.html and bece.html."""
import json, re, sys

DISC = ("They are <b>not</b> reproductions of past papers — for those, use WAEC's own e-learning portal "
        "and the past-question booklets sold by WAEC Ghana.")

LEVELS = {
 "wassce": {
  "out": "wassce.html",
  "title": "WASSCE Core Four",
  "key": "wassce-core-four-v2",
  "exam": "WASSCE",
  "subjects": [
   ("maths", "Core Maths", "#D14A76", "bank_maths.json",
    "{n} original practice questions with full working — WAEC Core Mathematics syllabus. Not official past papers.",
    dict(objSolLabel="Working", objSolBtn="working", thySolLabel="Worked solution", thySolBtn="worked solution",
         mockTab="Mock Paper 1", mockN=50, mockMins=90, quickN=20, quickMins=30,
         mockBlurb="50 objective questions in 1 hour 30 minutes — the shape of WAEC Paper 1. "
                   "Questions are drawn at random from every topic, and the paper is marked the moment you submit.",
         paperNote="Paper 1 is 50 marks out of the 150 for the whole subject.",
         theoryNote="Work each question on paper first, then reveal the steps one at a time. "
                    "In Paper 2 you must show your working to earn method marks. The mark shown on a question is for the work it asks for \u2014 in the real Paper 2, Section A questions carry about 8 marks each and Section B questions about 15.",
         about="<b>About these questions.</b> Original practice questions written to the WAEC Core Mathematics syllabus "
               "and to the format of Paper 1 (50 objectives, 1½ h) and Paper 2 (13 theory questions, 2½ h). " + DISC)),
   ("english", "English", "#5A67D8", "bank_english.json",
    "{n} original practice questions with model answers — WAEC English Language syllabus. Not official past papers.",
    dict(objSolLabel="Explanation", objSolBtn="explanation", thySolLabel="Model answer", thySolBtn="model answer",
         mockTab="Mock Paper 1", mockN=80, mockMins=60, quickN=20, quickMins=15,
         mockBlurb="80 objective questions in 1 hour — the shape of WAEC Paper 1 (lexis and structure).",
         paperNote="Paper 1 carries 40 of the 170 marks for English Language.",
         theoryNote="Write your answer out in full before you reveal the model. Paper 2 rewards complete sentences in your own words. The essay is marked out of 50 (Content 10, Organisation 10, Expression 20, Mechanical Accuracy 10); the comprehension passage carries about 20 and the summary 10.",
         about="<b>About these questions.</b> Original practice questions written to the WAEC English Language syllabus and to "
               "the format of Paper 1 (80 objectives, 1 h), Paper 2 (essay, comprehension and summary, 2 h) and Paper 3 "
               "(test of orals, 45 min). The passages were written for this app. " + DISC)),
   ("science", "Integrated Science", "#1AA189", "bank_science.json",
    "{n} original practice questions with full explanations — WAEC Integrated Science syllabus. Not official past papers.",
    dict(objSolLabel="Explanation", objSolBtn="explanation", thySolLabel="Answer guide", thySolBtn="answer guide",
         mockTab="Mock Paper 1", mockN=50, mockMins=60, quickN=20, quickMins=25,
         mockBlurb="50 objective questions in 1 hour — the shape of WAEC Paper 1, drawn from all five syllabus themes.",
         paperNote="Paper 1 carries 50 of the 190 marks for Integrated Science.",
         theoryNote="Answer on paper first, then compare. In Paper 2, points must be stated in full sentences, and labelled diagrams earn marks. Each of the Paper 2 essay questions carries 15 marks, so aim for that much substance in a full answer.",
         about="<b>About these questions.</b> Original practice questions written to the WAEC Integrated Science syllabus and to "
               "the format of Paper 1 (50 objectives, 1 h), Paper 2 (six essays, answer four, 1½ h) and Paper 3 (practical, 2 h). " + DISC)),
   ("social", "Social Studies", "#C08028", "bank_social.json",
    "{n} original practice questions with answer guides — WASSCE Social Studies syllabus. Not official past papers.",
    dict(objSolLabel="Explanation", objSolBtn="explanation", thySolLabel="Answer guide", thySolBtn="answer guide",
         mockTab="Mock Paper 1", mockN=50, mockMins=50, quickN=20, quickMins=20,
         mockBlurb="50 objective questions in 50 minutes — the shape of WAEC Paper 1, drawn from all three sections.",
         paperNote="Paper 1 carries 50 marks; Paper 2 carries 100 (five essays at 20 marks each).",
         theoryNote="Plan four or five points, then write each as a paragraph: state the point, explain it, give a Ghanaian example. Every Paper 2 essay carries 20 marks, which is roughly four or five developed points.",
         about="<b>About these questions.</b> Original practice questions written to the WASSCE Social Studies syllabus and to the "
               "format of Paper 1 (50 objectives) and Paper 2 (three sections, five essays). " + DISC)),
  ],
 },

 "bece": {
  "out": "bece.html",
  "title": "BECE Core Six",
  "key": "bece-core-six-v1",
  "exam": "BECE",
  "subjects": [
   ("bmaths", "Mathematics", "#0FA8BF", "bank_bmaths.json",
    "{n} original practice questions with full working — the complete JHS mathematics syllabus. Not official past papers.",
    dict(objSolLabel="Working", objSolBtn="working", thySolLabel="Worked solution", thySolBtn="worked solution",
         mockTab="Mock Paper 1", mockN=40, mockMins=60, quickN=15, quickMins=20,
         mockBlurb="40 objective questions in 1 hour — the exact shape of BECE Paper 1. "
                   "Questions are drawn at random from all 30 topics, and the paper is marked the moment you submit.",
         paperNote="BECE Mathematics Paper 1 is 40 objectives in 1 hour (40 marks); Paper 2 is 6 questions, answer 4, in 1 hour (60 marks).",
         theoryNote="Work each question on paper first, then reveal the steps one at a time. "
                    "In Paper 2 the method marks are given for the working, not just the answer. Each of the six Paper 2 questions carries 15 marks; the mark shown here is for the work this question asks for.",
         about="<b>About these questions.</b> Original practice questions written to the Ghanaian JHS mathematics curriculum and to "
               "the BECE format: Paper 1 (40 objectives, 1 h, 40 marks) and Paper 2 (six questions, answer four, 1 h, 60 marks). " + DISC)),
   ("benglish", "English Language", "#6A5CFF", "bank_benglish.json",
    "{n} original practice questions with model answers — JHS English Language, including oral English. Not official past papers.",
    dict(objSolLabel="Explanation", objSolBtn="explanation", thySolLabel="Model answer", thySolBtn="model answer",
         mockTab="Mock Paper 1", mockN=40, mockMins=50, quickN=15, quickMins=20,
         mockBlurb="40 objective questions in 50 minutes — the shape of BECE Paper 1 (35 on grammar and lexis, 5 on oral English).",
         paperNote="BECE English Paper 1 is 40 objectives in 50 minutes (40 marks); Paper 2 is essay, comprehension and grammar in 1 hour 10 minutes (60 marks).",
         theoryNote="Write the whole answer out before you reveal the model. Marks come from content, organisation, expression and accuracy. In Paper 2 the essay carries 30 marks, the comprehension 20 and the grammar section 10.",
         about="<b>About these questions.</b> Original practice questions written to the Ghanaian JHS English syllabus and to the BECE "
               "format: Paper 1 (40 objectives in 50 minutes, five of them on oral English) and Paper 2 (Part A essay, "
               "Part B comprehension, Part C grammar, 1 h 10 min). The passages were written for this app. " + DISC)),
   ("bscience", "Integrated Science", "#12B57A", "bank_bscience.json",
    "{n} original practice questions with full explanations — the five JHS science strands. Not official past papers.",
    dict(objSolLabel="Explanation", objSolBtn="explanation", thySolLabel="Answer guide", thySolBtn="answer guide",
         mockTab="Mock Paper 1", mockN=40, mockMins=45, quickN=15, quickMins=18,
         mockBlurb="40 objective questions in 45 minutes — the shape of BECE Paper 1, drawn from all five science strands.",
         paperNote="BECE Science Paper 1 is 40 objectives in 45 minutes; Paper 2 is Section A (compulsory) plus three of four questions in Section B, 1 h 25 min.",
         theoryNote="Answer on paper first. In Paper 2, state points in full sentences and label every diagram \u2014 labels carry marks. Section A is 40 marks of short answers; each Section B question carries 20.",
         about="<b>About these questions.</b> Original practice questions written to the Ghanaian JHS science curriculum and to the BECE "
               "format: Paper 1 (40 objectives, 45 min) and Paper 2 (Section A compulsory, 40 marks; Section B answer three of four, "
               "60 marks; 1 h 25 min). " + DISC)),
   ("bsocial", "Social Studies", "#D9892A", "bank_bsocial.json",
    "{n} original practice questions with answer guides — environment, governance and development. Not official past papers.",
    dict(objSolLabel="Explanation", objSolBtn="explanation", thySolLabel="Answer guide", thySolBtn="answer guide",
         mockTab="Mock Paper 1", mockN=40, mockMins=45, quickN=15, quickMins=18,
         mockBlurb="40 objective questions in 45 minutes — the shape of BECE Paper 1, drawn from all three sections of the syllabus.",
         paperNote="BECE Social Studies Paper 1 is 40 objectives in 45 minutes (40 marks); Paper 2 is three questions out of five in 1 hour.",
         theoryNote="Plan four or five points, then write each as a paragraph: state it, explain it, and give a Ghanaian example. Each of the Paper 2 questions carries 20 marks, which is about four developed points.",
         about="<b>About these questions.</b> Original practice questions written to the Ghanaian JHS social studies curriculum and to "
               "the BECE format: Paper 1 (40 objectives, 45 min, 40 marks) and Paper 2 (answer three of five questions, 1 h). " + DISC)),
   ("brme", "Religious & Moral Ed.", "#E0557F", "bank_brme.json",
    "{n} original practice questions with answer guides — Christianity, Islam and African Traditional Religion. Not official past papers.",
    dict(objSolLabel="Explanation", objSolBtn="explanation", thySolLabel="Answer guide", thySolBtn="answer guide",
         mockTab="Mock Paper 1", mockN=40, mockMins=45, quickN=15, quickMins=18,
         mockBlurb="40 objective questions in 45 minutes — the shape of BECE Paper 1, drawn from all four strands.",
         paperNote="BECE R.M.E. Paper 1 is 40 objectives in 45 minutes (40 marks); Paper 2 is Section A (compulsory) plus two of four in Section B, 1 hour.",
         theoryNote="Answer in full sentences, and always end with the moral lesson \u2014 that sentence is often worth the mark. In Paper 2, Section A is compulsory and each Section B question carries 20 marks.",
         about="<b>About these questions.</b> Original practice questions written to the Ghanaian JHS R.M.E. curriculum and to the BECE "
               "format: Paper 1 (40 objectives, 45 min, 40 marks) and Paper 2 (Section A compulsory plus two of four questions in "
               "Section B, 1 h, 60 marks). Each religion is presented as its own adherents teach it. " + DISC)),
   ("bcomputing", "Computing", "#2E7FE0", "bank_bcomputing.json",
    "{n} original practice questions with full explanations — hardware, software, networks and algorithms. Not official past papers.",
    dict(objSolLabel="Explanation", objSolBtn="explanation", thySolLabel="Answer guide", thySolBtn="answer guide",
         mockTab="Mock Paper 1", mockN=40, mockMins=45, quickN=15, quickMins=18,
         mockBlurb="40 objective questions in 45 minutes — the shape of BECE Paper 1, drawn from every strand of the course.",
         paperNote="BECE Computing Paper 1 is 40 objectives in 45 minutes; Paper 2 has a compulsory section plus three of four questions, 1 h 15 min (60 marks).",
         theoryNote="Write the steps or the labels in full. For a flowchart, name the symbol you are using at each stage. Paper 2 is 60 marks: a compulsory section plus three of four questions.",
         about="<b>About these questions.</b> Original practice questions written to the Ghanaian JHS computing curriculum and to the "
               "BECE format: Paper 1 (40 objectives, 45 min) and Paper 2 (a compulsory section plus three of four questions, "
               "1 h 15 min, 60 marks). " + DISC)),
  ],
 },
}

shell = open("hub_hud.html").read()
SWITCH = ('<a class="swap" href="./index.html" title="Choose a different examination">'
          '◀ Switch exam</a>')

for level in (sys.argv[1:] or ["wassce", "bece"]):
    spec = LEVELS[level]
    subjects, nobj, nthy, ntop, nsyl = [], 0, 0, 0, 0
    for sid, name, dot, path, sub, cfg in spec["subjects"]:
        bank = json.load(open(path))
        qs = bank["questions"]
        o = sum(1 for q in qs if q["type"] == "obj")
        nobj += o; nthy += len(qs) - o; ntop += len(bank["topics"])
        nsyl += sum(len(s["items"]) for s in bank["syllabus"])
        cfg = dict(cfg); cfg["key"] = spec["key"] + "-" + sid; cfg["subjectName"] = name
        subjects.append({"id": sid, "name": name, "dot": dot, "sub": sub.format(n=len(qs)),
                         "cfg": cfg, "topics": bank["topics"], "questions": qs, "syllabus": bank["syllabus"]})
        print("  %-22s %3d topics  %3d obj  %3d theory" % (name, len(bank["topics"]), o, len(qs) - o))
    data = json.dumps({"subjects": subjects}, ensure_ascii=False)
    assert "</script" not in data
    html = (shell.replace("__HUBTITLE__", spec["title"])
                 .replace("__SWITCH__", SWITCH)
                 .replace("__KEY__", spec["key"])
                 .replace("__EXAM__", spec["exam"])
                 .replace("__MOCKTAB__", "Mock Paper 1")
                 .replace("__BANK__", data))
    for tok in ["__HUBTITLE__", "__SWITCH__", "__KEY__", "__EXAM__", "__MOCKTAB__", "__BANK__"]:
        assert tok not in html, tok
    open(spec["out"], "w").write(html)
    print("%s: %d topics, %d objective, %d theory, %d syllabus items → %s (%d KB)"
          % (spec["title"], ntop, nobj, nthy, nsyl, spec["out"], len(html) // 1024))
