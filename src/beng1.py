"""BECE English Language - Section A: Grammar and structure."""
from core import *
import draw

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}
A = "A. Grammar & structure"

# ------------------------------------------------------------------ nouns
topic("nouns", "Nouns: types, number & possession", A, [
  "<b>Common</b> noun: boy, town. <b>Proper</b> noun (capital letter): Kofi, Accra. "
  "<b>Collective</b>: a flock of birds. <b>Abstract</b> (ideas you cannot touch): honesty, fear.",
  "Countable nouns have a plural (book → books). Uncountable nouns do not: <i>information</i>, <i>advice</i>, "
  "<i>furniture</i>, <i>luggage</i>, <i>equipment</i>.",
  "Irregular plurals: child → children, tooth → teeth, mouse → mice, sheep → sheep, knife → knives, roof → roofs.",
  "Possession: singular noun takes 's (the boy's bag); plural ending in -s takes only ' (the boys' bags).",
])
O("Choose the correct plural: The dentist examined my ______.",
  ["teeth", "tooths", "teeths", "tooth's"],
  ["<i>Tooth</i> has an irregular plural.", "The plural is <b>teeth</b> — never 'tooths' or 'teeths'."],
  ok=True)
O("Which of these is an abstract noun?",
  ["courage", "soldier", "mountain", "basket"],
  ["An abstract noun names something you cannot see or touch — an idea, quality or feeling.",
   "<b>Courage</b> is a quality, so it is abstract. The others are things you can point at."],
  ok=True)
O("The bags belonging to the girls are here. Rewrite the underlined part: the ______ bags are here.",
  ["girls'", "girl's", "girls", "girls's"],
  ["There is more than one girl, so the plural <i>girls</i> already ends in -s.",
   "A plural ending in -s takes only an apostrophe after it: <b>girls'</b> bags."],
  ok=True)
O("Choose the correct form: She gave me some useful ______ about the examination.",
  ["information", "informations", "information's", "an information"],
  ["<i>Information</i> is uncountable in English.",
   "Uncountable nouns have no plural and take no 'a/an', so the answer is <b>information</b>."],
  ok=True)
O("A group of cattle is called",
  ["a herd", "a flock", "a swarm", "a shoal"],
  ["Collective nouns are fixed by usage: a flock of sheep or birds, a swarm of bees, a shoal of fish.",
   "Cattle go together in <b>a herd</b>."],
  ok=True)
T("Rewrite the following sentences correctly. (a) The childrens toys are missing. (b) He gave us two advices. "
  "(c) The womens meeting ended late. (d) My uncle bought three new furnitures.",
  ["(a) The plural of <i>child</i> is <i>children</i>, and possession needs an apostrophe: "
   "<b>The children's toys are missing.</b>",
   "(b) <i>Advice</i> is uncountable: <b>He gave us two pieces of advice.</b>",
   "(c) <b>The women's meeting ended late.</b> (<i>Women</i> is already plural, so add 's.)",
   "(d) <i>Furniture</i> is uncountable: <b>My uncle bought three new pieces of furniture.</b>"],
  marks=8)
extras("nouns",
  plain="A noun is a naming word — a person, place, thing, animal or idea. Two things trip students up in the exam: "
        "irregular plurals (child → children) and uncountable nouns like <i>information</i>, <i>advice</i>, <i>luggage</i> and "
        "<i>furniture</i>, which never take -s and never take 'a'.",
  examples=[
    E("Why is 'He gave me many advices' wrong, and how do we fix it?",
      "Step 1. <i>Advice</i> is uncountable — you cannot count it one by one.",
      "Step 2. Uncountable nouns take 'much', not 'many', and have no plural -s.",
      "Step 3. Correct version: <b>He gave me much advice</b> or <b>He gave me many pieces of advice</b>."),
    E("Put the apostrophe in the right place: the boys school bags (there are several boys).",
      "Step 1. Ask: who owns the bags? The boys — more than one.",
      "Step 2. The plural <i>boys</i> already ends in -s, so add only an apostrophe.",
      "Step 3. <b>The boys' school bags.</b> (If it were one boy: the boy's school bag.)")],
  fig=draw.tree("NOUNS", ["Common: boy, town", "Proper: Kofi, Accra", "Collective: herd, flock", "Abstract: honesty, fear"],
                label="Types of noun"))

# ------------------------------------------------------------------ pronouns
topic("pronouns", "Pronouns", A, [
  "Subject pronouns: I, we, you, he, she, it, they. Object pronouns: me, us, you, him, her, it, them.",
  "After a preposition, use the object form: <i>between you and <b>me</b></i>, not 'between you and I'.",
  "Reflexive pronouns: myself, yourself, himself, herself, itself, ourselves, yourselves, themselves "
  "(there is no such word as 'hisself' or 'theirselves').",
  "A pronoun must agree with the noun it replaces: <i>Every pupil must bring <b>his or her</b> book.</i>",
])
O("This is a secret between you and ______.",
  ["me", "I", "myself", "mine"],
  ["<i>Between</i> is a preposition, and a preposition is followed by an object pronoun.",
   "The object form of 'I' is <b>me</b>."],
  ok=True)
O("The headmaster himself opened the gate. The underlined word is a ______ pronoun.",
  ["reflexive (emphatic)", "relative", "possessive", "demonstrative"],
  ["<i>Himself</i> refers back to the headmaster and adds emphasis.",
   "That is a <b>reflexive (emphatic)</b> pronoun."],
  ok=True)
O("The girl ______ won the prize is my sister.",
  ["who", "which", "whose", "whom"],
  ["We need a relative pronoun for a person acting as the subject of 'won'.",
   "<b>Who</b> is used for people as subject; <i>whom</i> would be the object form and <i>which</i> is for things."],
  ok=True)
O("Kofi and ______ are going to the market.",
  ["I", "me", "myself", "mine"],
  ["The two people are doing the action, so we need a subject pronoun.",
   "Test it by dropping 'Kofi and': 'I am going', not 'me am going'. So the answer is <b>I</b>."],
  ok=True)
O("Every candidate must bring ______ own pen.",
  ["his or her", "their", "theirs", "them"],
  ["<i>Every candidate</i> is singular, so the pronoun must be singular too.",
   "In formal examination English the accepted form is <b>his or her</b>."],
  ok=True)
T("Correct the pronoun errors in these sentences. (a) Me and my brother went to town. "
  "(b) The teacher gave the books to Ama and I. (c) The boys washed theirselves. (d) Who did you give the letter to?",
  ["(a) The subject form is needed, and politeness puts the other person first: <b>My brother and I went to town.</b>",
   "(b) After 'to' we need the object form: <b>The teacher gave the books to Ama and me.</b>",
   "(c) There is no word 'theirselves': <b>The boys washed themselves.</b>",
   "(d) 'Give' takes an object, so the object form is needed: <b>Whom did you give the letter to?</b> "
   "(or, more formally, 'To whom did you give the letter?')"],
  marks=8)
extras("pronouns",
  plain="A pronoun stands in place of a noun so that we do not repeat it: <i>Ama said Ama lost Ama's pen</i> becomes "
        "<i>Ama said she lost her pen</i>. The exam tests one thing above all — subject form (I, he, she, they) versus object "
        "form (me, him, her, them).",
  examples=[
    E("Is it 'Ama is taller than me' or 'Ama is taller than I'?",
      "Step 1. Finish the sentence in your head: 'Ama is taller than I <u>am</u>.'",
      "Step 2. Because 'am' is understood, the subject form fits.",
      "Step 3. The formal, examination-correct answer is <b>Ama is taller than I</b>, though 'than me' is common in speech."),
    E("Choose the right word: The letter was addressed to my father and (I / me).",
      "Step 1. Drop the other person: 'The letter was addressed to ___'.",
      "Step 2. You would say 'to me', not 'to I'.",
      "Step 3. So the answer is <b>me</b>.")])

# ------------------------------------------------------------------ verbs
topic("verbs", "Verbs & tenses", A, [
  "Simple present for habits (<i>he walks to school</i>); present continuous for now (<i>he is walking</i>).",
  "Simple past for a finished time (<i>I saw him yesterday</i>); present perfect for a time not stated "
  "(<i>I have seen him</i>). Never use 'have' with a stated past time.",
  "Irregular verbs: go-went-gone, see-saw-seen, write-wrote-written, eat-ate-eaten, break-broke-broken, "
  "take-took-taken, drink-drank-drunk.",
  "After <i>did</i>, <i>does</i>, <i>can</i>, <i>will</i>, <i>must</i> and <i>to</i>, use the plain form: "
  "<i>He did not <b>go</b></i>, not 'did not went'.",
])
O("I ______ my uncle last Saturday.",
  ["visited", "have visited", "visit", "had visited"],
  ["'Last Saturday' is a finished, stated past time.", "A stated past time takes the simple past: <b>visited</b>."],
  ok=True)
O("She has already ______ her lunch.",
  ["eaten", "ate", "eat", "eating"],
  ["After 'has' we need the past participle (the third form).",
   "eat - ate - <b>eaten</b>, so the answer is <b>eaten</b>."],
  ok=True)
O("He did not ______ to school yesterday.",
  ["go", "went", "gone", "going"],
  ["After the helper 'did' the main verb stays in its plain form.", "So it is <b>go</b>, never 'did not went'."],
  ok=True)
O("By the time we arrived, the match ______.",
  ["had started", "has started", "starts", "is starting"],
  ["One past action happened before another past action, so we need the past perfect.",
   "The past perfect is 'had + past participle': <b>had started</b>."],
  ok=True)
O("Water ______ at 100 °C.",
  ["boils", "is boiling", "boiled", "has boiled"],
  ["A general truth takes the simple present tense.",
   "With the singular subject 'water', the verb takes -s: <b>boils</b>."],
  ok=True)
T("Fill each gap with the correct form of the verb in brackets. "
  "(a) My father ______ (travel) to Tamale every month. (b) Look! The baby ______ (cry). "
  "(c) They ______ (write) the test before the bell rang. (d) I ______ (not see) him since January.",
  ["(a) A regular habit takes the simple present: <b>travels</b> (singular subject, so -s).",
   "(b) 'Look!' points to something happening now, so the present continuous: <b>is crying</b>.",
   "(c) The writing finished before another past event, so the past perfect: <b>had written</b>.",
   "(d) 'since January' goes with the present perfect: <b>have not seen</b>."],
  marks=8)
extras("verbs",
  plain="The verb is the action or state word, and its <b>tense</b> tells us when. Two clues decide nearly every question: "
        "a stated past time (yesterday, last week, in 2019) demands the simple past, while <i>since</i>, <i>for</i>, "
        "<i>already</i>, <i>just</i> and <i>yet</i> demand the present perfect.",
  examples=[
    E("Why is 'I have seen him yesterday' wrong?",
      "Step 1. 'Yesterday' names a finished past time.",
      "Step 2. The present perfect (have seen) is for a time that is <b>not</b> stated.",
      "Step 3. Correct it as <b>I saw him yesterday</b>, or as <b>I have seen him</b> (no time given)."),
    E("Choose the right form: She (don't / doesn't) like noise.",
      "Step 1. The subject 'she' is third person singular.",
      "Step 2. Third person singular takes <i>does</i>, not <i>do</i>.",
      "Step 3. So: <b>She doesn't like noise.</b>")],
  fig=draw.flow(["Stated past time → simple past (I went)",
                 "No time stated → present perfect (I have gone)",
                 "Earlier of two past actions → past perfect (I had gone)"],
                label="Choosing a past tense"))

# ------------------------------------------------------------------ adjectives
topic("adjectives", "Adjectives & comparison", A, [
  "An adjective describes a noun: a <b>tall</b> boy, <b>three</b> books, <b>Ghanaian</b> food.",
  "Short adjectives: add -er / -est (tall, taller, tallest). Longer ones use more / most "
  "(beautiful, more beautiful, most beautiful).",
  "Irregular: good-better-best, bad-worse-worst, little-less-least, many/much-more-most, far-farther/further-farthest.",
  "Use the comparative for two things and the superlative for three or more. Never write 'more taller' or 'most tallest'.",
  "Order of adjectives: opinion → size → age → shape → colour → origin → material (a lovely small old round brown Ghanaian wooden stool).",
])
O("Of the three boys, Kwame is the ______.",
  ["tallest", "taller", "more tall", "most tall"],
  ["Three or more items need the superlative form.",
   "<i>Tall</i> is short, so the superlative is <b>tallest</b>."],
  ok=True)
O("This mango is ______ than that one.",
  ["sweeter", "sweetest", "more sweeter", "most sweet"],
  ["Two things are compared, so we need the comparative.", "The comparative of <i>sweet</i> is <b>sweeter</b>."],
  ok=True)
O("My result is ______ than yours.",
  ["better", "gooder", "best", "more good"],
  ["<i>Good</i> is irregular: good - better - best.", "Comparing two results needs <b>better</b>."],
  ok=True)
O("Choose the correct order: She bought a ______ table.",
  ["small round wooden", "wooden round small", "round wooden small", "wooden small round"],
  ["English puts adjectives in the order size → shape → material.",
   "So: <b>small round wooden</b> table."],
  ok=True)
O("Which of the underlined words is an adjective? 'The <u>careful</u> driver drove <u>slowly</u> along the <u>narrow</u> road.'",
  ["careful and narrow", "slowly only", "careful and slowly", "narrow and slowly"],
  ["Adjectives describe nouns: <i>careful</i> describes 'driver' and <i>narrow</i> describes 'road'.",
   "<i>Slowly</i> describes the verb 'drove', so it is an adverb.",
   "The adjectives are therefore <b>careful and narrow</b>."],
  ok=True)
T("Rewrite each sentence correctly. (a) She is the most cleverest girl in the class. (b) This is more better than that. "
  "(c) Of the two roads, this one is the shortest. (d) He is the taller of all the pupils.",
  ["(a) Never double the superlative: <b>She is the cleverest girl in the class.</b>",
   "(b) <i>Better</i> is already comparative: <b>This is better than that.</b>",
   "(c) Only two roads are compared, so use the comparative: <b>Of the two roads, this one is the shorter.</b>",
   "(d) 'All the pupils' is more than two, so use the superlative: <b>He is the tallest of all the pupils.</b>"],
  marks=8)
extras("adjectives",
  plain="Adjectives describe. The whole topic turns on one simple test: how many things are being compared? Two → "
        "comparative (-er / more). Three or more → superlative (-est / most). And you never use both -er and 'more' together.",
  examples=[
    E("Complete: Of all the subjects, I find Mathematics the ______ (difficult).",
      "Step 1. 'All the subjects' means more than two, so use the superlative.",
      "Step 2. <i>Difficult</i> is a long adjective, so it takes 'most' rather than -est.",
      "Step 3. Answer: <b>most difficult</b>."),
    E("Which is correct: 'He is more intelligent than his brother' or 'He is intelligenter'?",
      "Step 1. Count the syllables: in-tel-li-gent has four.",
      "Step 2. Long adjectives form the comparative with 'more'.",
      "Step 3. So <b>He is more intelligent than his brother</b> is correct.")])

# ------------------------------------------------------------------ adverbs
topic("adverbs", "Adverbs", A, [
  "An adverb tells us <i>how</i>, <i>when</i>, <i>where</i> or <i>how often</i> something happens.",
  "Many adverbs of manner end in -ly: quickly, carefully, badly. But <i>fast</i>, <i>hard</i>, <i>late</i> and "
  "<i>early</i> are the same as adjectives.",
  "Careful: <i>hardly</i> means 'almost not', which is quite different from <i>hard</i>. "
  "<i>Lately</i> means 'recently', not 'in a late manner'.",
  "Adverbs of frequency (always, often, never, usually) go before the main verb but after 'is/are/was/were'.",
])
O("The pupils answered the questions ______.",
  ["correctly", "correct", "correctness", "more correct"],
  ["The word describes <i>how</i> they answered, so an adverb is needed.",
   "The adverb formed from 'correct' is <b>correctly</b>."],
  ok=True)
O("He drives very ______.",
  ["fast", "fastly", "faster", "fastest"],
  ["<i>Fast</i> is both an adjective and an adverb — there is no word 'fastly'.",
   "So the answer is <b>fast</b>."],
  ok=True)
O("She ______ comes late to school.",
  ["never", "not", "no", "nothing"],
  ["We need an adverb of frequency before the main verb.", "<b>Never</b> fits: 'She never comes late to school.'"],
  ok=True)
O("I could ______ hear what the teacher said because of the noise.",
  ["hardly", "hard", "hardest", "harder"],
  ["The meaning is 'almost not', and that is <b>hardly</b>.",
   "'Hard' would mean with force, which does not fit here."],
  ok=True)
O("In the sentence 'The old man walked slowly into the room', the adverb is",
  ["slowly", "old", "walked", "room"],
  ["<i>Slowly</i> tells us how he walked, so it modifies the verb.",
   "<i>Old</i> is an adjective, <i>walked</i> is the verb and <i>room</i> is a noun. The adverb is <b>slowly</b>."],
  ok=True)
T("Use the adverb form of the word in brackets to complete each sentence. "
  "(a) He spoke ______ (angry) to the stranger. (b) The train arrived ______ (late). "
  "(c) She writes very ______ (good). (d) They have ______ (recent) moved to Takoradi.",
  ["(a) angry → <b>angrily</b> (y changes to i before -ly).",
   "(b) <i>Late</i> does not change: <b>late</b>. ('Lately' would wrongly mean 'recently'.)",
   "(c) <i>Good</i> is irregular — its adverb is <b>well</b>.",
   "(d) recent → <b>recently</b>."],
  marks=8)
extras("adverbs",
  plain="If a describing word is pointing at a <b>noun</b>, it is an adjective; if it is pointing at a <b>verb</b>, it is an "
        "adverb. 'He is a careful driver' (adjective) but 'He drives carefully' (adverb). Watch the traps: good → well, fast → fast, hard → hard.",
  examples=[
    E("Choose the correct word: She sings (good / well).",
      "Step 1. The word describes how she sings — a verb — so an adverb is needed.",
      "Step 2. The adverb of <i>good</i> is not 'goodly'; it is <i>well</i>.",
      "Step 3. Answer: <b>She sings well.</b>"),
    E("Explain the difference between 'He worked hard' and 'He hardly worked'.",
      "Step 1. <i>Hard</i> as an adverb means with much effort.",
      "Step 2. <i>Hardly</i> means almost not at all.",
      "Step 3. So the first man worked a great deal; the second <b>did almost no work</b> — opposite meanings.")])

# ------------------------------------------------------------------ prepositions
topic("prepos", "Prepositions", A, [
  "A preposition shows a relationship of place, time or direction: in, on, at, to, from, under, between, among.",
  "Time: <i>at</i> 6 o'clock, <i>on</i> Monday, <i>in</i> June, <i>in</i> 2026.",
  "<b>Between</b> two things, <b>among</b> three or more.",
  "Fixed pairs you must learn: afraid <i>of</i>, good <i>at</i>, married <i>to</i>, listen <i>to</i>, depend <i>on</i>, "
  "congratulate <i>on</i>, insist <i>on</i>, prefer <i>to</i>, different <i>from</i>, arrive <i>at</i> (a place).",
])
O("The meeting will take place ______ Monday.",
  ["on", "in", "at", "to"],
  ["Days of the week take <i>on</i>.", "So: <b>on</b> Monday. (Use 'at' for clock times and 'in' for months and years.)"],
  ok=True)
O("The sweets were shared ______ the five children.",
  ["among", "between", "within", "along"],
  ["There are more than two children.", "Use <b>among</b> for three or more, and 'between' for exactly two."],
  ok=True)
O("She is very good ______ Mathematics.",
  ["at", "in", "on", "with"],
  ["'Good' is followed by <i>at</i> when we talk about a skill or subject.", "So: good <b>at</b> Mathematics."],
  ok=True)
O("The children are afraid ______ snakes.",
  ["of", "from", "with", "about"],
  ["The fixed expression is 'afraid of'.", "So: afraid <b>of</b> snakes."],
  ok=True)
O("We arrived ______ the airport at noon.",
  ["at", "to", "in", "on"],
  ["<i>Arrive</i> takes 'at' for a place or point, and 'in' only for large areas such as countries or cities.",
   "So: arrived <b>at</b> the airport."],
  ok=True)
T("Fill each gap with a suitable preposition. (a) He congratulated me ______ my success. "
  "(b) This book is different ______ that one. (c) We must depend ______ ourselves. "
  "(d) The teacher insisted ______ silence. (e) I prefer rice ______ yam.",
  ["(a) <b>on</b> — congratulate somebody on something.",
   "(b) <b>from</b> — different from (not 'different than' in examination English).",
   "(c) <b>on</b> — depend on.",
   "(d) <b>on</b> — insist on.",
   "(e) <b>to</b> — prefer one thing to another, never 'prefer than'."],
  marks=10)
extras("prepos",
  plain="Prepositions are small words with big consequences, and most of them cannot be reasoned out — they must be "
        "learned as pairs. Keep a page in your notebook headed 'verb + preposition' and add to it every week: listen to, depend on, insist on, prefer to.",
  examples=[
    E("Choose: The pen is ______ the table. (on / in / at)",
      "Step 1. The pen is resting on a flat surface.",
      "Step 2. <i>On</i> is used for surfaces, <i>in</i> for inside something enclosed.",
      "Step 3. Answer: <b>on</b> the table."),
    E("Correct this sentence: I am married with a teacher.",
      "Step 1. The fixed expression is 'married to somebody'.",
      "Step 2. 'Married with' is a common error borrowed from other languages.",
      "Step 3. Correct version: <b>I am married to a teacher.</b>")])

# ------------------------------------------------------------------ conjunctions
topic("conj", "Conjunctions & connectors", A, [
  "Joining words of equal weight: and, but, or, so, for, yet.",
  "Joining a dependent clause: because, although, unless, while, since, if, when, after, before.",
  "Pairs that must stay together: either … or, neither … nor, both … and, not only … but also.",
  "Do not double up: use 'Although he was tired, he worked' OR 'He was tired but he worked' — never 'Although … but …'.",
])
O("______ he was tired, he finished the work.",
  ["Although", "But", "Because", "Unless"],
  ["The two ideas contrast: being tired usually stops work, but he finished it.",
   "<b>Although</b> introduces a contrast. (Note we do not add 'but' later in the same sentence.)"],
  ok=True)
O("Neither the teacher ______ the pupils were in class.",
  ["nor", "or", "and", "either"],
  ["<i>Neither</i> is always paired with <i>nor</i>.", "So: neither the teacher <b>nor</b> the pupils."],
  ok=True)
O("You will fail ______ you work hard.",
  ["unless", "if", "because", "although"],
  ["<i>Unless</i> means 'if … not', which is the sense required.",
   "'You will fail <b>unless</b> you work hard' = you will fail if you do not work hard."],
  ok=True)
O("He was absent ______ he was ill.",
  ["because", "although", "unless", "so that"],
  ["The second part gives the reason for the first.", "<b>Because</b> introduces a reason."],
  ok=True)
O("Not only did she pass, ______ she came first.",
  ["but also", "and also", "or", "nor"],
  ["The fixed pair is 'not only … but also'.", "So the answer is <b>but also</b>."],
  ok=True)
T("Join each pair of sentences into one, using the word in brackets. "
  "(a) It rained heavily. We went to school. (although) "
  "(b) He ran fast. He missed the bus. (but) "
  "(c) Study hard. You will pass. (so that) "
  "(d) She was not in class. Her brother was not in class. (neither … nor)",
  ["(a) <b>Although it rained heavily, we went to school.</b>",
   "(b) <b>He ran fast, but he missed the bus.</b>",
   "(c) <b>Study hard so that you will pass.</b>",
   "(d) <b>Neither she nor her brother was in class.</b> (With 'neither … nor', the verb agrees with the nearer subject.)"],
  marks=8)
extras("conj",
  plain="Conjunctions are the joints of a sentence. Short sentences joined well read like good English; joined badly they "
        "read like a list. The marks are lost on the pairs — <i>neither</i> must take <i>nor</i>, and <i>although</i> must never be followed later by <i>but</i>.",
  examples=[
    E("Why is 'Although he was poor, but he was honest' wrong?",
      "Step 1. <i>Although</i> already shows the contrast.",
      "Step 2. Adding <i>but</i> shows the same contrast twice.",
      "Step 3. Write either <b>Although he was poor, he was honest</b> or <b>He was poor, but he was honest</b>."),
    E("Join with 'either … or': He will travel today. He will travel tomorrow.",
      "Step 1. The two choices are 'today' and 'tomorrow'.",
      "Step 2. Put <i>either</i> before the first choice and <i>or</i> before the second.",
      "Step 3. <b>He will travel either today or tomorrow.</b>")])

# ------------------------------------------------------------------ concord
topic("concord", "Concord (agreement)", A, [
  "A singular subject takes a singular verb: <i>The boy <b>is</b></i>. A plural subject takes a plural verb: <i>The boys <b>are</b></i>.",
  "Words between the subject and the verb do not change the agreement: "
  "<i>The box <b>of</b> pencils <b>is</b> on the table</i> (box is the subject).",
  "<i>Each</i>, <i>every</i>, <i>either</i>, <i>neither</i>, <i>everybody</i>, <i>nobody</i>, <i>one of</i> are all singular.",
  "With 'either … or' and 'neither … nor', the verb agrees with the subject <b>nearer</b> to it.",
  "Uncountable nouns (news, mathematics, furniture, information) take a singular verb: <i>The news <b>is</b> good</i>.",
])
O("The box of pencils ______ on the table.",
  ["is", "are", "were", "have"],
  ["The subject is 'the box', not 'pencils' — 'of pencils' only describes the box.",
   "A singular subject takes a singular verb: <b>is</b>."],
  ok=True)
O("Each of the pupils ______ a textbook.",
  ["has", "have", "are having", "having"],
  ["<i>Each</i> is singular, even when followed by 'of the pupils'.", "So the verb is singular: <b>has</b>."],
  ok=True)
O("Neither the boys nor their teacher ______ present.",
  ["was", "were", "are", "have"],
  ["With 'neither … nor', the verb agrees with the nearer subject, which is 'their teacher' (singular).",
   "So the verb is <b>was</b>."],
  ok=True)
O("Mathematics ______ my favourite subject.",
  ["is", "are", "were", "have been"],
  ["Although it ends in -s, <i>mathematics</i> is the name of one subject and is treated as singular.",
   "So: Mathematics <b>is</b> my favourite subject."],
  ok=True)
O("The news about the floods ______ disturbing.",
  ["is", "are", "were", "have been"],
  ["<i>News</i> is uncountable and takes a singular verb.", "So: The news <b>is</b> disturbing."],
  ok=True)
T("Correct the errors of concord. (a) One of the girls have lost her bag. (b) There is many reasons for his failure. "
  "(c) Every pupil in the three classes were present. (d) My trousers is torn.",
  ["(a) The subject is 'one', which is singular: <b>One of the girls has lost her bag.</b>",
   "(b) The real subject is 'many reasons', which is plural: <b>There are many reasons for his failure.</b>",
   "(c) <i>Every pupil</i> is singular: <b>Every pupil in the three classes was present.</b>",
   "(d) <i>Trousers</i> is treated as plural: <b>My trousers are torn.</b>"],
  marks=8)
extras("concord",
  plain="Concord means the subject and the verb must match in number. The exam hides the subject behind extra words — "
        "'The <u>list</u> of names <u>is</u> on the board' — so train yourself to cross out everything between the subject and the verb before choosing.",
  examples=[
    E("Choose the right verb: The quality of the shoes (is / are) poor.",
      "Step 1. Find the subject: 'the quality'. 'Of the shoes' merely describes it.",
      "Step 2. 'Quality' is singular.",
      "Step 3. So: <b>The quality of the shoes is poor.</b>"),
    E("Choose the right verb: Either the driver or the passengers (was / were) at fault.",
      "Step 1. 'Either … or' makes the verb agree with the nearer subject.",
      "Step 2. The nearer subject is 'the passengers', which is plural.",
      "Step 3. So: <b>Either the driver or the passengers were at fault.</b>")])

# ------------------------------------------------------------------ articles
topic("articles", "Articles & determiners", A, [
  "<i>A</i> before a consonant sound, <i>an</i> before a vowel sound. Judge by the <b>sound</b>: "
  "a university, an hour, an honest man, a one-cedi coin.",
  "<i>The</i> points to something particular, or to something already mentioned.",
  "No article with most proper nouns, meals, games or languages: <i>He plays football after school.</i>",
  "Countable determiners: many, few, a few. Uncountable: much, little, a little. "
  "<i>Few</i> means 'hardly any'; <i>a few</i> means 'some'.",
])
O("He waited for ______ hour at the station.",
  ["an", "a", "the", "one of"],
  ["The word 'hour' begins with a vowel <i>sound</i> because the h is silent.",
   "So we use <b>an</b> hour."],
  ok=True)
O("My brother is ______ university student.",
  ["a", "an", "the", "some"],
  ["Although 'university' begins with the letter u, it is pronounced 'yu' — a consonant sound.",
   "So we use <b>a</b> university student."],
  ok=True)
O("There is only ______ water left in the barrel.",
  ["a little", "a few", "few", "many"],
  ["<i>Water</i> is uncountable, so it takes 'little / a little', not 'few'.",
   "<b>A little</b> means a small amount is left."],
  ok=True)
O("______ sun rises in the east.",
  ["The", "A", "An", "Some"],
  ["There is only one sun, and unique things take 'the'.", "So: <b>The</b> sun rises in the east."],
  ok=True)
O("Very ______ pupils passed the difficult test.",
  ["few", "little", "much", "a little"],
  ["<i>Pupils</i> is countable and plural, so it takes 'few'.",
   "<b>Few</b> (meaning hardly any) fits the sense of a difficult test."],
  ok=True)
T("Insert a, an, the or nothing (—) in each gap. (a) ___ honest man never fears. (b) He is ___ best pupil in ___ class. "
  "(c) We play ___ football every evening. (d) She bought ___ umbrella and ___ raincoat.",
  ["(a) <b>An</b> honest man never fears. (The h in 'honest' is silent.)",
   "(b) He is <b>the</b> best pupil in <b>the</b> class. (A superlative takes 'the'.)",
   "(c) We play <b>—</b> football every evening. (No article before the names of games.)",
   "(d) She bought <b>an</b> umbrella and <b>a</b> raincoat."],
  marks=8)
extras("articles",
  plain="A/an introduce something for the first time; <i>the</i> points to something we already know about. The one rule "
        "to drill is that a/an follows the <b>sound</b>, not the letter: an hour, a university, an X-ray, a European.",
  examples=[
    E("Why do we say 'a European' but 'an Englishman'?",
      "Step 1. 'European' begins with a 'yu' sound, which is a consonant sound.",
      "Step 2. 'Englishman' begins with a clear 'e' vowel sound.",
      "Step 3. So: <b>a European</b> but <b>an Englishman</b> — judged by sound, not spelling."),
    E("Explain the difference between 'few friends' and 'a few friends'.",
      "Step 1. <i>Few</i> is negative in feeling — hardly any.",
      "Step 2. <i>A few</i> is positive — a small number, but some.",
      "Step 3. 'He has few friends' sounds lonely; <b>'He has a few friends' means he has some</b>.")])

# ------------------------------------------------------------------ question tags
topic("qtags", "Question tags", A, [
  "A question tag is a short question added to a statement: <i>You are coming, <b>aren't you?</b></i>",
  "Positive statement → negative tag. Negative statement → positive tag.",
  "The tag repeats the helping verb and uses a <b>pronoun</b>: Ama is late, isn't <b>she</b>?",
  "If there is no helping verb, use do / does / did: <i>He came late, didn't he?</i>",
  "Special cases: I am … , aren't I?  Let's go, shall we?  Open the door, will you?  Nobody came, did they?",
])
O("You are coming with us, ______?",
  ["aren't you", "are you", "isn't it", "don't you"],
  ["The statement is positive, so the tag must be negative.",
   "Repeat the helping verb 'are' with the pronoun 'you': <b>aren't you</b>."],
  ok=True)
O("She didn't finish the work, ______?",
  ["did she", "didn't she", "does she", "is she"],
  ["The statement is negative, so the tag is positive.", "Repeat the helper 'did': <b>did she</b>."],
  ok=True)
O("Let's start the meeting, ______?",
  ["shall we", "will we", "do we", "aren't we"],
  ["A suggestion beginning <i>Let's</i> does not follow the usual positive-negative tag rule.",
   "After 'let's' the fixed tag is <b>shall we</b>."],
  ok=True)
O("I am right, ______?",
  ["aren't I", "am not I", "amn't I", "isn't it"],
  ["A positive statement takes a negative tag, but <i>I am</i> has no neat negative short form.",
   "English has no tag 'am not I', so by convention we use <b>aren't I</b>."],
  ok=True)
O("Kofi passed the examination, ______?",
  ["didn't he", "did he", "isn't he", "hasn't he"],
  ["There is no helping verb in the statement, so use did.",
   "The statement is positive, so the tag is negative: <b>didn't he</b>."],
  ok=True)
T("Add the correct question tag to each statement. (a) Nobody told you the truth, ______? "
  "(b) Everything is ready, ______? (c) You have never been to Kumasi, ______? "
  "(d) Open the window, ______?",
  ["(a) 'Nobody' is negative in meaning, so the tag is positive, and the pronoun is 'they': <b>did they?</b>",
   "(b) 'Everything' takes the pronoun 'it', and the positive statement takes a negative tag: <b>isn't it?</b>",
   "(c) 'Never' makes the statement negative, so the tag is positive: <b>have you?</b>",
   "(d) A command takes the tag <b>will you?</b>"],
  marks=8)
extras("qtags",
  plain="A question tag turns a statement into a check: 'It's hot, isn't it?' Two rules cover nearly every question — "
        "swap positive for negative, and reuse the helping verb with a pronoun. Learn the four odd ones by heart: aren't I, shall we, will you, did they.",
  examples=[
    E("Add a tag: He can swim, ______?",
      "Step 1. The statement is positive, so the tag must be negative.",
      "Step 2. The helping verb is 'can', and the pronoun is 'he'.",
      "Step 3. <b>can't he?</b>"),
    E("Add a tag: There is no water in the tank, ______?",
      "Step 1. 'No water' makes the statement negative, so the tag is positive.",
      "Step 2. In tags, 'there' is repeated as the subject.",
      "Step 3. <b>is there?</b>")])

# ------------------------------------------------------------------ reported speech
topic("reported", "Reported (indirect) speech", A, [
  "Reporting someone's words moves the tense one step back: am/is → was, are → were, will → would, "
  "can → could, have → had, simple past → past perfect.",
  "Pronouns change to fit the new speaker: I → he/she, we → they, my → his/her.",
  "Time and place words change: now → then, today → that day, tomorrow → the next day, "
  "yesterday → the previous day, here → there, this → that.",
  "Questions are reported with <i>asked … if/whether</i> (yes-no) or with the question word, and the word order becomes that of a statement.",
  "Commands are reported with <i>told … to</i> / <i>ordered … to</i>; requests with <i>asked … to</i>.",
])
O("'I am tired,' said Ama. In reported speech: Ama said that she ______ tired.",
  ["was", "is", "has been", "were"],
  ["The reporting verb 'said' is past, so the present 'am' moves back to the past.",
   "'I' also becomes 'she': Ama said that she <b>was</b> tired."],
  ok=True)
O("'Where do you live?' the teacher asked. The teacher asked where ______.",
  ["I lived", "do I live", "did I live", "I live"],
  ["A reported question takes statement word order, with no 'do'.",
   "The present 'live' moves back to the past: the teacher asked where <b>I lived</b>."],
  ok=True)
O("'Close the door,' the master said. The master ______ close the door.",
  ["told us to", "said us to", "told us", "said to"],
  ["Commands are reported with 'told somebody to + verb'.",
   "So the master <b>told us to</b> close the door."],
  ok=True)
O("'I will travel tomorrow,' he said. He said that he ______ travel ______.",
  ["would … the next day", "will … tomorrow", "would … tomorrow", "will … the next day"],
  ["'Will' moves back to 'would', and 'tomorrow' becomes 'the next day'.",
   "So: He said that he <b>would</b> travel <b>the next day</b>."],
  ok=True)
O("'Did you see the film?' she asked. She asked ______ seen the film.",
  ["whether I had", "if I have", "did I have", "whether I was"],
  ["A yes-no question is reported with if or whether.",
   "The simple past 'did see' moves back to the past perfect: she asked <b>whether I had</b> seen the film."],
  ok=True)
T("Report the following. (a) 'I am going to the market now,' mother said. "
  "(b) 'Have you finished your homework?' father asked me. (c) 'Don't play on the road,' the teacher warned the children. "
  "(d) 'We bought this yesterday,' they said.",
  ["(a) <b>Mother said that she was going to the market then.</b> (am → was; now → then)",
   "(b) <b>Father asked me whether I had finished my homework.</b> (have → had; word order becomes a statement)",
   "(c) <b>The teacher warned the children not to play on the road.</b> (negative command → not to + verb)",
   "(d) <b>They said that they had bought that the previous day.</b> (bought → had bought; this → that; yesterday → the previous day)"],
  marks=10)
extras("reported",
  plain="Reporting speech is a three-step mechanical change: move the tense one step into the past, change the pronouns to "
        "suit the new speaker, and shift the time and place words. Do the three steps in that order every time and the sentence comes out right.",
  examples=[
    E("Report: 'I can swim very well,' the boy said.",
      "Step 1. Tense: 'can' moves back to 'could'.",
      "Step 2. Pronoun: 'I' becomes 'he'.",
      "Step 3. <b>The boy said that he could swim very well.</b>"),
    E("Report: 'Please help me,' the old woman said to the boy.",
      "Step 1. A request is reported with 'asked … to'.",
      "Step 2. 'Me' becomes 'her' (the old woman).",
      "Step 3. <b>The old woman asked the boy to help her.</b>")],
  fig=draw.flow(["Step 1: tense back one step (is → was)",
                 "Step 2: change the pronouns (I → he/she)",
                 "Step 3: shift time and place (now → then)"],
                label="Turning direct speech into reported speech"))

# ------------------------------------------------------------------ voice
topic("voice", "Active & passive voice", A, [
  "Active: the subject does the action — <i>The boy kicked the ball.</i>",
  "Passive: the thing acted upon comes first — <i>The ball was kicked by the boy.</i>",
  "To change to the passive: object becomes the subject, add the right form of 'be', use the past participle, "
  "and put the old subject after 'by' (or leave it out).",
  "Keep the tense: kicks → is kicked; kicked → was kicked; will kick → will be kicked; has kicked → has been kicked.",
  "The passive is useful when the doer is unknown or unimportant: <i>The window was broken.</i>",
])
O("Change to the passive: The teacher punished the boy.",
  ["The boy was punished by the teacher.", "The boy is punished by the teacher.",
   "The boy had punished the teacher.", "The teacher was punished by the boy."],
  ["The object 'the boy' becomes the subject.",
   "'Punished' is simple past, so use 'was + punished': <b>The boy was punished by the teacher.</b>"],
  ok=True)
O("Change to the active: The letter was written by Ama.",
  ["Ama wrote the letter.", "Ama has written the letter.", "The letter wrote Ama.", "Ama writes the letter."],
  ["The doer is Ama, so she becomes the subject.",
   "'Was written' is past, so the active verb is 'wrote': <b>Ama wrote the letter.</b>"],
  ok=True)
O("Change to the passive: They are building a new school.",
  ["A new school is being built.", "A new school is built.", "A new school was being built.", "A new school has built."],
  ["The tense is present continuous, so the passive is 'is being + built'.",
   "The doer 'they' is vague and can be dropped: <b>A new school is being built.</b>"],
  ok=True)
O("Change to the passive: Someone has stolen my bicycle.",
  ["My bicycle has been stolen.", "My bicycle is stolen.", "My bicycle was stolen by someone.",
   "My bicycle had been stolen."],
  ["The present perfect 'has stolen' becomes 'has been stolen'.",
   "'Someone' adds nothing, so we leave it out: <b>My bicycle has been stolen.</b>"],
  ok=True)
O("Which of these sentences is in the passive voice?",
  ["The food was eaten by the children.", "The children ate the food.",
   "The children are eating the food.", "The children will eat the food."],
  ["In the passive, the subject receives the action and the verb includes a form of 'be' plus a past participle.",
   "<b>The food was eaten by the children</b> is the passive one."],
  ok=True)
T("Rewrite these sentences in the passive voice. (a) The carpenter is making a table. "
  "(b) Our class will plant trees tomorrow. (c) The headmistress has announced the results. "
  "(d) People speak English all over the world.",
  ["(a) <b>A table is being made by the carpenter.</b>",
   "(b) <b>Trees will be planted by our class tomorrow.</b>",
   "(c) <b>The results have been announced by the headmistress.</b>",
   "(d) <b>English is spoken all over the world.</b> ('People' is unimportant, so it is left out.)"],
  marks=8)
extras("voice",
  plain="Voice is about who comes first in the sentence. Active puts the doer first; passive puts the receiver first. The "
        "change is mechanical: swap the two nouns, add the correct form of <i>be</i>, and use the third form of the verb — keeping the tense exactly as it was.",
  examples=[
    E("Change to the passive: The driver had repaired the car.",
      "Step 1. Object 'the car' becomes the subject.",
      "Step 2. 'Had repaired' is past perfect, so the passive is 'had been repaired'.",
      "Step 3. <b>The car had been repaired by the driver.</b>"),
    E("Why is the passive used in 'The bridge was destroyed in the storm'?",
      "Step 1. We do not know, or do not care, who or what did it.",
      "Step 2. The passive lets us leave the doer out altogether.",
      "Step 3. It also puts the important thing — <b>the bridge</b> — at the front of the sentence.")])

# ------------------------------------------------------------------ sentences
topic("sentence", "Sentences, phrases & clauses", A, [
  "A <b>phrase</b> has no verb of its own: <i>in the morning</i>, <i>under the big tree</i>.",
  "A <b>clause</b> has a subject and a verb. A main clause can stand alone; a subordinate clause cannot.",
  "Sentence types by structure: <b>simple</b> (one clause), <b>compound</b> (two main clauses joined by and/but/or), "
  "<b>complex</b> (a main clause plus a subordinate clause).",
  "Sentence types by purpose: statement, question, command (imperative), exclamation.",
])
O("'After the rain' is an example of a",
  ["phrase", "main clause", "subordinate clause", "compound sentence"],
  ["There is no subject-and-verb pair in 'after the rain'.", "A group of words with no verb is a <b>phrase</b>."],
  ok=True)
O("'He slept early because he was tired' is a ______ sentence.",
  ["complex", "simple", "compound", "compound-complex"],
  ["There is one main clause ('He slept early') and one subordinate clause ('because he was tired').",
   "A main clause plus a subordinate clause makes a <b>complex</b> sentence."],
  ok=True)
O("'Ama cooked the rice and Kofi washed the plates' is a ______ sentence.",
  ["compound", "simple", "complex", "interrogative"],
  ["Each half can stand on its own, and they are joined by 'and'.",
   "Two main clauses joined by a coordinating conjunction make a <b>compound</b> sentence."],
  ok=True)
O("'Shut the gate at once!' is a/an",
  ["imperative sentence", "interrogative sentence", "declarative sentence", "exclamatory sentence"],
  ["The sentence gives an order, and the subject 'you' is understood.",
   "A sentence that gives a command is <b>imperative</b>."],
  ok=True)
O("In the sentence 'The girl who won the race is my cousin', the underlined part 'who won the race' is a",
  ["subordinate (relative) clause", "phrase", "main clause", "compound subject"],
  ["It has a subject ('who') and a verb ('won'), so it is a clause, but it cannot stand alone.",
   "It describes 'the girl', so it is a <b>subordinate (relative) clause</b>."],
  ok=True)
T("(a) Write one sentence of your own that is simple, one that is compound and one that is complex, and label each. "
  "(b) Say whether each of these is a phrase or a clause: (i) on the table (ii) when the bell rang (iii) a very tall man.",
  ["(a) Simple: <b>The baby slept.</b> (one subject and one verb)",
   "Compound: <b>The baby slept, but the dog barked.</b> (two main clauses joined by 'but')",
   "Complex: <b>The baby slept after the dog stopped barking.</b> (main clause + subordinate clause)",
   "(b) (i) <b>phrase</b> — no verb. (ii) <b>clause</b> — it has the subject 'the bell' and the verb 'rang'. "
   "(iii) <b>phrase</b> — no verb."],
  marks=9)
extras("sentence",
  plain="To tell a phrase from a clause, look for a verb with its own subject: if you find one, it is a clause. To name a "
        "sentence type, count the clauses that could stand alone: one → simple, two joined by and/but/or → compound, one plus a dependent one → complex.",
  examples=[
    E("Is 'Because he was late' a sentence?",
      "Step 1. It has a subject ('he') and a verb ('was'), so it is a clause.",
      "Step 2. But 'because' makes it dependent — it leaves the reader waiting.",
      "Step 3. It is a <b>subordinate clause, not a complete sentence</b>. It needs a main clause: 'Because he was late, he missed the bus.'"),
    E("Name the type: 'Although it was raining, the farmers went to the farm and worked hard.'",
      "Step 1. 'Although it was raining' is subordinate.",
      "Step 2. 'The farmers went to the farm' and '(they) worked hard' are joined by 'and'.",
      "Step 3. There is both subordination and coordination, so it is a <b>compound-complex</b> sentence.")])

# ------------------------------------------------------------------ punctuation
topic("punct", "Punctuation & capital letters", A, [
  "Capital letters: the first word of a sentence, names of people, places, days, months, "
  "nationalities, titles and the pronoun I.",
  "Full stop ends a statement; question mark ends a question; exclamation mark shows strong feeling.",
  "Commas separate items in a list, mark off a name being addressed, and follow an opening subordinate clause.",
  "Apostrophes show possession (Kofi's bag) or a missing letter (don't = do not). <i>It's</i> = it is; "
  "<i>its</i> = belonging to it.",
  "Quotation marks enclose the exact words spoken, and the comma goes inside: <i>'I am ready,' he said.</i>",
])
O("Which sentence is correctly punctuated?",
  ["\"Where are you going?\" asked Ama.", "\"Where are you going\"? asked Ama.",
   "\"where are you going?\" asked Ama.", "\"Where are you going?\" Asked Ama."],
  ["The question mark belongs to the spoken words, so it goes inside the quotation marks.",
   "The speech begins with a capital, and 'asked' continues the same sentence in lower case.",
   "So: <b>\"Where are you going?\" asked Ama.</b>"],
  ok=True)
O("Choose the correctly punctuated sentence.",
  ["We bought rice, beans, oil and sugar.", "We bought rice beans oil and sugar.",
   "We bought, rice, beans, oil and sugar.", "We bought rice; beans; oil and sugar."],
  ["Items in a list are separated by commas, with 'and' before the last item.",
   "So: <b>We bought rice, beans, oil and sugar.</b>"],
  ok=True)
O("Which word correctly completes the sentence? The dog wagged ______ tail.",
  ["its", "it's", "its'", "it is"],
  ["We need the possessive form, meaning 'belonging to it', which is <b>its</b> — with no apostrophe.",
   "<i>It's</i> would mean 'it is', which makes no sense here."],
  ok=True)
O("Which sentence uses capital letters correctly?",
  ["My friend Kwesi lives in Cape Coast and speaks Fante.",
   "My friend kwesi lives in cape coast and speaks fante.",
   "My Friend Kwesi lives in Cape Coast and speaks fante.",
   "my friend Kwesi lives in Cape Coast and speaks Fante."],
  ["Names of people, towns and languages all take capital letters, and the sentence must begin with one.",
   "'Friend' is a common noun, so it stays in lower case: <b>My friend Kwesi lives in Cape Coast and speaks Fante.</b>"],
  ok=True)
O("The shortened form of 'cannot' is",
  ["can't", "cant", "ca'nt", "can'not"],
  ["The apostrophe stands where letters have been removed — here 'no'.", "So the correct short form is <b>can't</b>."],
  ok=True)
T("Rewrite the following passage, putting in the correct punctuation and capital letters.<br>"
  "<i>on monday ama kofi and i travelled to kumasi we visited the manhyia palace and bought kente cloth "
  "what a wonderful day it was</i>",
  ["<b>On Monday, Ama, Kofi and I travelled to Kumasi.</b> (capital at the start; day, names and the pronoun I; "
   "commas in the list; full stop at the end)",
   "<b>We visited the Manhyia Palace and bought kente cloth.</b> (a place name takes capitals)",
   "<b>What a wonderful day it was!</b> (strong feeling takes an exclamation mark)"],
  marks=10)
extras("punct",
  plain="Punctuation marks are the road signs of writing: they tell the reader where to pause, stop and change voice. In "
        "the BECE, marks are lost most often on three things — the comma in a list, the apostrophe in possession, and the comma that must sit inside the quotation marks.",
  examples=[
    E("Punctuate: ama said i will come tomorrow",
      "Step 1. The spoken words are 'I will come tomorrow', so they need quotation marks.",
      "Step 2. A comma separates 'Ama said' from the speech, and the speech starts with a capital.",
      "Step 3. <b>Ama said, \"I will come tomorrow.\"</b>"),
    E("Choose the right word: (Their / There / They're) books are on the table.",
      "Step 1. The sentence shows possession — the books belong to them.",
      "Step 2. <i>There</i> shows place and <i>they're</i> means 'they are'.",
      "Step 3. So: <b>Their books are on the table.</b>")])
