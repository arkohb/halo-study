"""BECE English Language - vocabulary, comprehension, composition and oral English."""
from core import *
import draw

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}
B, C, D, X = "B. Vocabulary & usage", "C. Comprehension & summary", "D. Composition", "E. Oral English"

# ------------------------------------------------------------------ synonyms / antonyms
topic("synant", "Synonyms & antonyms", B, [
  "A <b>synonym</b> means nearly the same (big / large); an <b>antonym</b> means the opposite (big / small).",
  "Read the whole sentence before choosing — the best synonym is the one that fits the <i>context</i>.",
  "Many antonyms are made with prefixes: happy → unhappy, possible → impossible, legal → illegal, "
  "regular → irregular, obey → disobey.",
  "Learn words in families: brave, courageous, fearless, bold — and their opposites: cowardly, timid, afraid.",
])
O("Choose the word that is nearest in meaning to the underlined word: The chief was <u>furious</u> when he heard the news.",
  ["very angry", "surprised", "worried", "pleased"],
  ["<i>Furious</i> is a strong word for anger.", "The nearest in meaning is <b>very angry</b>."],
  ok=True)
O("Choose the opposite of the underlined word: The bridge was <u>permanent</u>.",
  ["temporary", "strong", "modern", "narrow"],
  ["<i>Permanent</i> means lasting for ever.", "Its opposite is <b>temporary</b>, meaning lasting only for a short time."],
  ok=True)
O("Choose the word nearest in meaning to <u>scarce</u>.",
  ["rare", "plenty", "cheap", "useless"],
  ["<i>Scarce</i> means hard to find because there is very little of it.", "The closest word is <b>rare</b>."],
  ok=True)
O("The opposite of <u>generous</u> is",
  ["mean", "kind", "wealthy", "careless"],
  ["A generous person gives freely.", "Someone who will not give is <b>mean</b> (or stingy)."],
  ok=True)
O("Choose the word nearest in meaning to the underlined word: The old man walked with a <u>feeble</u> step.",
  ["weak", "quick", "proud", "heavy"],
  ["<i>Feeble</i> describes something lacking strength.", "The nearest meaning is <b>weak</b>."],
  ok=True)
T("For each word below, give (i) one synonym and (ii) one antonym: (a) brave (b) honest (c) increase (d) ancient.",
  ["(a) brave — synonym: <b>courageous</b>; antonym: <b>cowardly</b>.",
   "(b) honest — synonym: <b>truthful</b>; antonym: <b>dishonest</b>.",
   "(c) increase — synonym: <b>rise</b>; antonym: <b>decrease</b> (or reduce).",
   "(d) ancient — synonym: <b>old</b>; antonym: <b>modern</b>.",
   "In the exam, write only one word for each — a list of guesses loses the mark."],
  marks=8)
extras("synant",
  plain="Synonym questions reward wide reading more than any rule. A good habit: whenever you meet a new word, write it in "
        "a notebook with one word that means the same and one that means the opposite. Three new words a day is about a thousand a year.",
  examples=[
    E("Choose the nearest meaning: The crowd <u>dispersed</u> after the match.",
      "Step 1. Picture the scene — a crowd after a match.",
      "Step 2. <i>Dispersed</i> describes people moving away in all directions.",
      "Step 3. The nearest meaning is <b>scattered</b> (or broke up)."),
    E("Give the opposite of 'obedient' using a prefix.",
      "Step 1. Many opposites are formed with the prefixes un-, in-, im-, ir- or dis-.",
      "Step 2. The word <i>obedient</i> takes dis-.",
      "Step 3. The opposite is <b>disobedient</b>.")])

# ------------------------------------------------------------------ idioms
topic("idioms", "Idioms & proverbs", B, [
  "An idiom is a group of words whose meaning cannot be worked out from the single words: "
  "<i>to pass away</i> means to die.",
  "Never change the words of an idiom — it is 'to kick the bucket', not 'to kick the basket'.",
  "Common ones: to put up with (tolerate), to look down on (despise), to give up (stop trying), "
  "to break the news (announce bad news), to turn a deaf ear (refuse to listen), in hot water (in trouble).",
  "Proverbs teach a lesson in one sentence. Many Ghanaian proverbs have close English equivalents.",
])
O("What does the idiom 'to turn a deaf ear' mean?",
  ["to refuse to listen", "to become deaf", "to listen carefully", "to whisper"],
  ["The expression has nothing to do with real deafness.",
   "It means <b>to refuse to listen</b> to advice or complaints."],
  ok=True)
O("The expression 'to be in hot water' means to be",
  ["in trouble", "very ill", "taking a bath", "working hard"],
  ["Hot water here stands for difficulty.", "The idiom means to be <b>in trouble</b>."],
  ok=True)
O("'Kofi has put up with his noisy neighbours for years.' The underlined idiom means he has",
  ["tolerated them", "fought them", "reported them", "moved away from them"],
  ["'Put up with' means to bear something unpleasant without complaining.",
   "So Kofi has <b>tolerated them</b>."],
  ok=True)
O("The proverb 'A stitch in time saves nine' teaches us to",
  ["solve small problems early", "learn to sew", "save our money", "work slowly"],
  ["One stitch now prevents a big tear later.",
   "The lesson is to <b>solve small problems early</b>, before they grow."],
  ok=True)
O("'When the headmaster entered, the pupils took to their heels.' The underlined idiom means they",
  ["ran away", "stood up", "kept quiet", "started laughing"],
  ["'To take to one's heels' pictures somebody running so fast you see only their heels.",
   "It means they <b>ran away</b>."],
  ok=True)
T("Use each of the following idioms in a sentence of your own that shows its meaning clearly: "
  "(a) to break the news (b) to look down on (c) to give up (d) once in a blue moon.",
  ["(a) <b>The doctor asked the pastor to break the news of the accident to the family.</b> (= to announce bad news)",
   "(b) <b>We should never look down on people because they are poor.</b> (= to despise)",
   "(c) <b>Although the work was hard, she refused to give up.</b> (= to stop trying)",
   "(d) <b>My uncle visits us once in a blue moon.</b> (= very rarely)",
   "A sentence earns the mark only if the meaning is clear from the context, so avoid 'He gave up.' on its own."],
  marks=8)
extras("idioms",
  plain="Idioms are the fingerprints of a language. They cannot be translated word for word, which is exactly why "
        "examiners like them. The safest way to learn one is inside a full sentence, not as a list — your ear then remembers it.",
  examples=[
    E("What does 'to let the cat out of the bag' mean? Use it in a sentence.",
      "Step 1. There is no real cat — the idiom is about a secret.",
      "Step 2. It means to reveal a secret, usually by accident.",
      "Step 3. <b>We wanted to surprise mother, but my little sister let the cat out of the bag.</b>"),
    E("Match the Ghanaian proverb 'The ruin of a nation begins in the homes of its people' with an English equivalent.",
      "Step 1. The proverb says that what happens in families decides the fate of the whole country.",
      "Step 2. Look for an English proverb about small beginnings leading to big results.",
      "Step 3. A close equivalent is <b>'Charity begins at home'</b> — both point to the family as the starting place.")])

# ------------------------------------------------------------------ word formation
topic("vocab", "Word formation & vocabulary in context", B, [
  "A <b>prefix</b> goes in front and changes the meaning: un-, dis-, im-, re-, pre-, mis-, over-.",
  "A <b>suffix</b> goes at the end and often changes the part of speech: -ness, -ment, -tion, -ful, -less, -ly, -able.",
  "Noun from verb: enjoy → enjoyment, decide → decision, arrive → arrival, succeed → success.",
  "Adjective from noun: care → careful / careless, hope → hopeful / hopeless, danger → dangerous.",
  "In the exam, read the sentence and ask what part of speech is missing before choosing the ending.",
])
O("Choose the correct noun form: We all enjoyed the ______ of the festival. (celebrate)",
  ["celebration", "celebrating", "celebrated", "celebrative"],
  ["The gap comes after 'the', so a noun is needed.", "The noun from <i>celebrate</i> is <b>celebration</b>."],
  ok=True)
O("The opposite of 'possible', formed with a prefix, is",
  ["impossible", "unpossible", "dispossible", "nonpossible"],
  ["Before words beginning with p, the prefix in- becomes im-.", "So the opposite is <b>impossible</b>."],
  ok=True)
O("Choose the correct word: His ______ to the school was a new library. (contribute)",
  ["contribution", "contributing", "contributed", "contributor"],
  ["After 'his' we need a noun naming the thing given.",
   "<b>Contribution</b> is the thing; 'contributor' would be the person."],
  ok=True)
O("A person who cannot read or write is",
  ["illiterate", "unliterate", "disliterate", "misliterate"],
  ["Before words beginning with l, the prefix in- becomes il-.", "So the word is <b>illiterate</b>."],
  ok=True)
O("Choose the correct adjective: The road is very ______ at night. (danger)",
  ["dangerous", "dangerful", "dangering", "endanger"],
  ["After 'very' we need an adjective.", "The adjective from <i>danger</i> is <b>dangerous</b>."],
  ok=True)
T("Give the correct form of the word in brackets. (a) The ______ of the new road took two years. (construct) "
  "(b) He answered the question ______. (correct) (c) Her ______ surprised everybody. (kind) "
  "(d) The teacher praised the ______ of the class. (behave)",
  ["(a) After 'the' a noun is needed: <b>construction</b>.",
   "(b) The word describes how he answered — an adverb: <b>correctly</b>.",
   "(c) After 'her' a noun is needed: <b>kindness</b>.",
   "(d) After 'the' a noun is needed: <b>behaviour</b>."],
  marks=8)
extras("vocab",
  plain="One root word can give you a whole family: <i>care</i> → careful, careless, carefully, carelessness. Learning the "
        "family instead of the single word doubles your vocabulary quickly — and the exam question is nearly always 'which member of the family fits this gap?'",
  examples=[
    E("Fill the gap: The manager showed great ______ in dealing with the crowd. (patient)",
      "Step 1. 'Great ______' tells us a noun is needed.",
      "Step 2. The noun from the adjective <i>patient</i> is formed with -ce.",
      "Step 3. <b>Patience</b> — 'The manager showed great patience.'"),
    E("Make the opposite of each word with a prefix: agree, legal, regular, understand.",
      "Step 1. Choose the right prefix for each: dis-, il-, ir-, mis-.",
      "Step 2. agree → disagree;  legal → illegal.",
      "Step 3. regular → irregular;  understand → <b>misunderstand</b>.")])

# ------------------------------------------------------------------ confusables
topic("confuse", "Spelling & commonly confused words", B, [
  "<i>Their</i> (belonging to them) / <i>there</i> (place) / <i>they're</i> (they are).",
  "<i>Your</i> (belonging to you) / <i>you're</i> (you are). <i>Its</i> (belonging to it) / <i>it's</i> (it is).",
  "<i>Advice</i> (noun) / <i>advise</i> (verb). <i>Practice</i> (noun) / <i>practise</i> (verb). "
  "<i>Effect</i> (noun, a result) / <i>affect</i> (verb, to influence).",
  "<i>Lose</i> (to misplace) / <i>loose</i> (not tight). <i>Than</i> (comparison) / <i>then</i> (time). "
  "<i>Accept</i> (to receive) / <i>except</i> (apart from).",
  "Spelling rules: i before e except after c (believe, receive); drop the e before -ing (hope → hoping); "
  "double the consonant after a short vowel (stop → stopping).",
])
O("Choose the correct word: ______ going to miss the bus if you don't hurry.",
  ["You're", "Your", "Yours", "You are're"],
  ["The sentence needs 'you are', and the short form of that is <b>you're</b>.",
   "<i>Your</i> would wrongly mean 'belonging to you'."],
  ok=True)
O("The doctor's ______ was that I should rest.",
  ["advice", "advise", "advised", "advises"],
  ["After 'the doctor's' we need a noun.", "The noun is spelt with a c: <b>advice</b>. ('Advise' is the verb.)"],
  ok=True)
O("Choose the correct word: Be careful not to ______ your money.",
  ["lose", "loose", "loss", "losing"],
  ["The verb meaning 'to misplace' is <b>lose</b>, with one o.",
   "<i>Loose</i> is an adjective meaning 'not tight'."],
  ok=True)
O("Everybody came to the meeting ______ Kofi, who was ill.",
  ["except", "accept", "expect", "exempt"],
  ["The sense is 'apart from', and that word is <b>except</b>.",
   "<i>Accept</i> would mean to receive something."],
  ok=True)
O("Which word is correctly spelt?",
  ["receive", "recieve", "receve", "ressieve"],
  ["The rule is 'i before e except after c', and here the letters follow c.",
   "So the correct spelling is <b>receive</b>."],
  ok=True)
T("Choose the correct word in each pair and write out the sentence. "
  "(a) The pupils left (their / there) books at home. (b) This bag is heavier (than / then) that one. "
  "(c) The medicine had a good (effect / affect) on her. (d) We must (practice / practise) every evening.",
  ["(a) <b>The pupils left their books at home.</b> (belonging to them)",
   "(b) <b>This bag is heavier than that one.</b> (a comparison)",
   "(c) <b>The medicine had a good effect on her.</b> (a noun — a result)",
   "(d) <b>We must practise every evening.</b> (a verb takes the s spelling)"],
  marks=8)
extras("confuse",
  plain="These pairs cost more marks in the BECE than any grammar rule, because they slip past when you write quickly. "
        "The cure is a test you can do in your head: replace the word with its full form — if 'they are' or 'it is' fits, use the apostrophe form.",
  examples=[
    E("Choose: (It's / Its) raining, and the cat has hurt (it's / its) paw.",
      "Step 1. Test the first gap: 'It is raining' makes sense, so use <b>it's</b>.",
      "Step 2. Test the second: 'the cat has hurt it is paw' is nonsense, so we need the possessive.",
      "Step 3. <b>It's raining, and the cat has hurt its paw.</b>"),
    E("Why is 'begining' wrong?",
      "Step 1. The verb is <i>begin</i>, which ends in a short vowel plus a single consonant.",
      "Step 2. Such words double the final consonant before -ing.",
      "Step 3. The correct spelling is <b>beginning</b> — with two n's.")])

# ------------------------------------------------------------------ figures of speech
topic("figspeech", "Figures of speech", B, [
  "<b>Simile</b>: a comparison using <i>like</i> or <i>as</i> — as brave as a lion.",
  "<b>Metaphor</b>: a comparison without like or as — the chief is a lion in battle.",
  "<b>Personification</b>: giving human qualities to things — the wind whispered.",
  "<b>Hyperbole</b>: deliberate exaggeration — I have told you a thousand times.",
  "<b>Alliteration</b>: repeated beginning sounds — the silent silver sea. "
  "<b>Onomatopoeia</b>: words that imitate sounds — buzz, crash, hiss.",
])
O("'The baby's skin is as soft as silk.' This is an example of",
  ["a simile", "a metaphor", "personification", "hyperbole"],
  ["The comparison uses the word 'as'.", "A comparison with like or as is a <b>simile</b>."],
  ok=True)
O("'The angry sea swallowed the little boat.' This is an example of",
  ["personification", "a simile", "alliteration", "onomatopoeia"],
  ["The sea is given human feelings ('angry') and a human action ('swallowed').",
   "That is <b>personification</b>."],
  ok=True)
O("'My father is a rock.' This figure of speech is",
  ["a metaphor", "a simile", "hyperbole", "irony"],
  ["The father is being called a rock directly, with no 'like' or 'as'.",
   "A direct comparison of this kind is a <b>metaphor</b>."],
  ok=True)
O("'I have told you a million times to shut the gate!' This is",
  ["hyperbole", "a simile", "a metaphor", "personification"],
  ["Nobody has literally spoken a million times — the exaggeration is deliberate.",
   "Deliberate exaggeration is <b>hyperbole</b>."],
  ok=True)
O("'The buzzing bees flew between the big bushes.' Which figure of speech is used in 'big bushes, buzzing bees'?",
  ["alliteration", "a simile", "hyperbole", "a metaphor"],
  ["The b sound is repeated at the beginning of several words.", "That repetition is <b>alliteration</b>."],
  ok=True)
T("Name the figure of speech in each sentence and explain your answer in one line. "
  "(a) The old lorry groaned up the hill. (b) Her smile was like the morning sun. "
  "(c) The books weigh a ton. (d) The fire crackled and hissed.",
  ["(a) <b>Personification</b> — the lorry is given the human action of groaning.",
   "(b) <b>Simile</b> — her smile is compared to the sun using 'like'.",
   "(c) <b>Hyperbole</b> — the weight is exaggerated for effect.",
   "(d) <b>Onomatopoeia</b> — 'crackled' and 'hissed' imitate the sounds themselves.",
   "Always give the reason: naming the figure alone usually earns only half the marks."],
  marks=8)
extras("figspeech",
  plain="Figures of speech make writing come alive, and using one or two in your composition lifts the language mark. The "
        "simplest test for the two commonest: if you can see the word <i>like</i> or <i>as</i>, it is a simile; if the comparison is made directly, it is a metaphor.",
  examples=[
    E("Turn this plain sentence into a simile and then into a metaphor: 'The boy ran fast.'",
      "Step 1. Simile — add 'like' or 'as': <b>The boy ran like the wind.</b>",
      "Step 2. Metaphor — make the comparison direct: <b>The boy was a streak of lightning down the track.</b>",
      "Step 3. Notice how much more the reader can picture in each new version."),
    E("Identify and explain the figure of speech: 'Time is a thief.'",
      "Step 1. Time is being called a thief, with no 'like' or 'as'.",
      "Step 2. That makes it a metaphor.",
      "Step 3. The meaning: <b>time takes away our years and chances without our noticing</b>.")])

# ------------------------------------------------------------------ comprehension
PASS1 = ('<div class="passage"><span class="lbl">Passage</span>'
         '<p>Adjoa had looked forward to the Saturday market for the whole week. Her grandmother had promised that if she '
         'helped at the stall from morning until noon, she could keep whatever she earned from selling the oranges she had '
         'picked herself. By Friday evening she had already decided how to spend it: a new exercise book, a pencil, and, if '
         'anything remained, a bottle of cold Fanta.</p>'
         '<p>The market was louder than she had expected. Traders called out their prices over one another, a radio shouted '
         'highlife music from somewhere behind the tomato sellers, and a stubborn goat stood in the middle of the path '
         'refusing to move for anyone. Adjoa set out her oranges in neat pyramids and waited. For almost an hour, nobody '
         'stopped. The women who passed glanced at her small table and walked on to the big sellers at the gate.</p>'
         '<p>Then her grandmother leaned across and said quietly, "You are waiting for the market to come to you. Stand up. '
         'Greet the people. Tell them your oranges are sweet, and let them taste one." Adjoa felt shy, but she stood up and '
         'did as she was told. She cut one orange into pieces and offered them to a woman carrying a baby. The woman tasted, '
         'smiled, and bought six. By noon the pyramids were gone.</p>'
         '<p>Walking home, Adjoa counted her money twice. She had earned more than she had hoped, but it was not the money '
         'she kept thinking about. It was the moment she had stood up.</p></div>')

topic("comp", "Comprehension", C, [
  "Read the passage through once for the general sense before you look at the questions.",
  "Then read each question and go back to the exact lines that answer it. Never answer from memory.",
  "Answer in your own words where you can, and in complete sentences. Lifting whole sentences loses marks.",
  "For 'what does this word mean as used in the passage', give a word that could replace it in that very sentence.",
  "Check the marks: one mark usually wants one point, so four marks wants four separate points.",
])
O(PASS1 + "Why had Adjoa looked forward to the Saturday market?",
  ["She would keep the money from the oranges she had picked herself.",
   "She wanted to listen to the highlife music.",
   "Her grandmother had promised to buy her a Fanta.",
   "She wanted to see the goat in the market."],
  ["The first paragraph says her grandmother promised she 'could keep whatever she earned from selling the oranges "
   "she had picked herself'.",
   "So the answer is that <b>she would keep the money from the oranges she had picked herself</b>."],
  ok=True)
O(PASS1 + "Why did nobody stop at Adjoa's table for almost an hour?",
  ["She sat quietly and waited for customers to come to her.",
   "Her oranges were not sweet.", "Her prices were too high.", "The goat blocked the way to her table."],
  ["The grandmother's words explain it: 'You are waiting for the market to come to you.'",
   "So it was because <b>she sat quietly and waited for customers to come to her</b>."],
  ok=True)
O(PASS1 + "The word <u>stubborn</u>, as used in the passage, means",
  ["refusing to change or move", "very large", "dangerous", "lost"],
  ["The goat 'stood in the middle of the path refusing to move for anyone'.",
   "So <i>stubborn</i> here means <b>refusing to change or move</b>."],
  ok=True)
O(PASS1 + "What finally made the woman with the baby buy six oranges?",
  ["She was given a piece to taste.", "Adjoa reduced the price.",
   "The grandmother called her over.", "The other sellers had closed."],
  ["Adjoa 'cut one orange into pieces and offered them to a woman carrying a baby. The woman tasted, smiled, and bought six.'",
   "So <b>she was given a piece to taste</b>."],
  ok=True)
O(PASS1 + "'It was the moment she had stood up.' This suggests that Adjoa valued most",
  ["the courage she had found", "the money she had counted",
   "the exercise book she would buy", "her grandmother's praise"],
  ["The last paragraph contrasts the money with something she valued more.",
   "Standing up was the moment she overcame her shyness, so she valued <b>the courage she had found</b>."],
  ok=True)
T(PASS1 + "Answer the following questions on the passage. "
  "(a) How long had Adjoa agreed to help at the stall? "
  "(b) Give two details that show the market was noisy. "
  "(c) What advice did the grandmother give, in your own words? "
  "(d) Why does the writer say the pyramids were gone by noon? "
  "(e) Give another word or phrase for each of these as used in the passage: (i) glanced (ii) remained.",
  ["(a) From <b>morning until noon</b>.",
   "(b) Any two of: <b>traders called out their prices over one another</b>; <b>a radio shouted highlife music</b>; "
   "the general shouting behind the tomato sellers.",
   "(c) She told Adjoa to <b>stop sitting quietly and instead greet customers, speak to them about her oranges and let "
   "them taste one</b> — in other words, to go after the buyers instead of waiting for them.",
   "(d) Because <b>she had sold all her oranges</b> once she began offering tastes and greeting people.",
   "(e) (i) glanced = <b>looked quickly</b>;  (ii) remained = <b>was left</b>.",
   "Notice that each answer is a complete statement in the candidate's own words, not a copied sentence."],
  marks=12)
extras("comp",
  plain="Comprehension is not a memory test — the answers are all in front of you. The skill is locating them. Read once "
        "for the story, then treat each question as a search: find the line, understand it, and rewrite it in your own words.",
  examples=[
    E("A passage says: 'The clerk hesitated before signing, turning the paper over twice.' Question: What does the "
      "writer suggest about the clerk?",
      "Step 1. Underline the clue words: 'hesitated', 'turning the paper over twice'.",
      "Step 2. Both show delay and doubt rather than confidence.",
      "Step 3. Answer in your own words: <b>The clerk was uncertain and not willing to sign at once.</b>"),
    E("A question is worth 4 marks and asks 'Why was the town deserted?'. How should you answer?",
      "Step 1. Four marks nearly always means four separate reasons or points.",
      "Step 2. Search the passage for each distinct reason and number them in your rough work.",
      "Step 3. Write <b>four short, separate statements</b> — not one long sentence repeating the same point.")])

# ------------------------------------------------------------------ summary
topic("summ", "Summary writing", C, [
  "A summary answers one set question — not 'what is the passage about' but, for example, "
  "'state the problems faced by the farmers'.",
  "Read the question first, then hunt only for points that answer it. Ignore everything else, however interesting.",
  "Write each point as one short, complete sentence in your own words. Do not copy whole sentences.",
  "Do not add your own opinions, examples or explanations, and do not repeat the same point in new words.",
  "Keep to the number of points or words asked for.",
])
O("The first thing to do in a summary question is to",
  ["read the question so that you know what to look for", "count the words in the passage",
   "copy the first sentence of each paragraph", "write an introduction of your own"],
  ["A summary is always a summary <i>of something particular</i>.",
   "So you must <b>read the question so that you know what to look for</b> before you start underlining."],
  ok=True)
O("Which of the following must NOT appear in a summary?",
  ["your own opinion about the passage", "a point in your own words",
   "a complete sentence", "the main idea of a paragraph"],
  ["A summary reports only what the passage says.",
   "<b>Your own opinion about the passage</b> earns no marks and may lose them."],
  ok=True)
O("In a summary, each point should be written",
  ["as one short sentence in your own words", "as a single word",
   "exactly as it appears in the passage", "as a question"],
  ["Points must be complete and in your own words to show you have understood.",
   "So write each <b>as one short sentence in your own words</b>."],
  ok=True)
O("If the question asks for four points and you write seven, the examiner will usually",
  ["mark only the first four", "mark the best four", "mark all seven", "give no marks at all"],
  ["Examiners mark in order and stop when the required number is reached.",
   "So the examiner will usually <b>mark only the first four</b> — which is why the weak points must be left out."],
  ok=True)
O("Repeating the same point in different words in a summary",
  ["wastes time and earns no extra mark", "doubles the mark",
   "shows a wide vocabulary", "is required for emphasis"],
  ["Each separate point is credited once.",
   "Saying it twice <b>wastes time and earns no extra mark</b>."],
  ok=True)
T("Read this short passage and, in four sentences, state the reasons given for the poor results in the school.<br>"
  "<i>The school had done badly for three years running. Many of the classrooms had no roofs, so lessons stopped whenever "
  "it rained. There were only two teachers for six classes, and one of them was often absent. The pupils had no textbooks "
  "of their own and copied everything from the board. Worst of all, most of the children walked more than eight kilometres "
  "to school and arrived too tired to concentrate.</i>",
  ["Find the points that answer the question and nothing else. There are four:",
   "1. <b>Lessons were interrupted whenever it rained because the classrooms had no roofs.</b>",
   "2. <b>There were too few teachers — only two for six classes — and one was often absent.</b>",
   "3. <b>The pupils had no textbooks and had to copy all their work from the board.</b>",
   "4. <b>Most children were too tired to concentrate after walking more than eight kilometres to school.</b>",
   "Note what was left out: 'the school had done badly for three years' is the problem, not a reason, so it earns no mark."],
  marks=8)
extras("summ",
  plain="Summary is the part of Paper 2 where careful readers gain easy marks. The method never changes: read the question, "
        "underline only the points that answer it, then rewrite each one in a short sentence of your own. Everything else in the passage is a distraction.",
  examples=[
    E("A passage lists the duties of a prefect. The question asks for three duties. How do you prepare your answer?",
      "Step 1. Underline every place where a duty is mentioned, and number them in the margin.",
      "Step 2. Cross out anything that is a quality (honesty, courage) rather than a duty.",
      "Step 3. Write the <b>three clearest duties as three separate sentences</b> in your own words."),
    E("The passage says: 'Because the river was polluted, the villagers had to walk to the next town for drinking water.' "
      "Summarise this in your own words.",
      "Step 1. Identify the single point: polluted river → long walk for water.",
      "Step 2. Replace the writer's words with your own.",
      "Step 3. <b>The villagers had to travel to another town for clean water because their river was dirty.</b>")])

# ------------------------------------------------------------------ letters
topic("letter", "Letter writing", D, [
  "<b>Informal letter</b> (to a friend or relative): one address — your own — at the top right, "
  "then the date, then 'Dear Ama,' and a friendly ending such as 'Your friend,' or 'Yours sincerely,' "
  "followed by your first name.",
  "<b>Formal letter</b> (to the headmaster, a company, a newspaper): your address top right, "
  "the receiver's address on the left, the date, 'Dear Sir,' a <b>heading (subject)</b> in capitals, "
  "then the body, and 'Yours faithfully,' with your full name.",
  "Three paragraphs is the safe plan: why you are writing, the details, what you want to happen.",
  "Keep the tone right: a formal letter has no slang, no contractions (do not write 'don't') and no jokes.",
  "Marks are given for content, organisation, expression and mechanical accuracy — layout alone is not enough.",
])
O("In a formal letter, which closing is correct after 'Dear Sir,'?",
  ["Yours faithfully,", "Yours sincerely,", "Your friend,", "Yours lovingly,"],
  ["When the letter opens with 'Dear Sir' (the name is not used), the correct closing is <b>Yours faithfully</b>.",
   "'Yours sincerely' goes with a named person, such as 'Dear Mr Mensah'."],
  ok=True)
O("A letter to the District Chief Executive about a broken bridge should include",
  ["a heading stating the subject", "a joke to attract attention",
   "the writer's nickname", "the address of a friend"],
  ["A formal letter states its business immediately through a heading.",
   "So it should include <b>a heading stating the subject</b>, such as 'REPAIR OF THE BROKEN BRIDGE AT ADOM'."],
  ok=True)
O("Which of these is suitable for an informal letter but NOT for a formal one?",
  ["I can't wait to see you again!", "I am writing to inform you of the matter.",
   "I shall be grateful for your assistance.", "The problem has lasted for three months."],
  ["Formal letters avoid contractions and excited exclamations.",
   "<b>I can't wait to see you again!</b> belongs only in a friendly letter."],
  ok=True)
O("In an informal letter, how many addresses are written?",
  ["one — the writer's own", "two — the writer's and the receiver's",
   "none", "three — including the school's"],
  ["Only a formal letter carries the receiver's address.", "An informal letter has <b>one — the writer's own</b>."],
  ok=True)
O("The best first paragraph of a formal letter",
  ["states clearly why you are writing", "describes the weather",
   "greets the reader's family", "apologises for writing"],
  ["A formal reader wants the business at once.",
   "So the opening paragraph <b>states clearly why you are writing</b>."],
  ok=True)
T("Write a letter to the headmaster of your school complaining about the poor state of the school toilets and "
  "suggesting two ways the problem can be solved. (Plan and model answer follows.)",
  ["<b>Layout</b>: your address at the top right; under it, the date; on the left, 'The Headmaster, Osei Memorial J.H.S., "
   "P.O. Box 24, Nsawam'; then 'Dear Sir,'; then the heading in capitals.",
   "<b>Heading</b>: POOR STATE OF THE SCHOOL TOILETS.",
   "<b>Paragraph 1 (purpose)</b>: I am writing, on behalf of the pupils of Form 3B, to draw your attention to the poor "
   "condition of the school toilets.",
   "<b>Paragraph 2 (details)</b>: Three of the six cubicles have no doors, the taps have not worked since last term, and "
   "the smell reaches the nearest classroom. Many pupils now walk home at break, and some stay away from school on market days.",
   "<b>Paragraph 3 (suggestions)</b>: I humbly suggest, first, that the broken doors and taps be repaired before the next "
   "term begins, and secondly, that each class be given a weekly cleaning duty supervised by a prefect, so that the "
   "toilets are kept clean once they are repaired.",
   "<b>Closing</b>: I shall be grateful for your kind consideration. / Yours faithfully, / <i>(signature)</i> / "
   "KWABENA ASARE (Form 3B).",
   "Check before you submit: no contractions, no slang, every paragraph on one idea, and the heading in capitals."],
  marks=30, fig=draw.letterfig(label="Layout of a formal letter"))
extras("letter",
  plain="Letters carry the biggest single block of marks in English Paper 2, and the layout is the easy part — learn it "
        "once and it is yours for ever. The marks that separate candidates come from the three-paragraph plan and from keeping the right tone throughout.",
  examples=[
    E("How should a letter to a friend who has lost his father begin and end?",
      "Step 1. It is informal, so only your own address and the date appear at the top.",
      "Step 2. Begin with sympathy, not with news about yourself: 'Dear Kofi, I was very sad to hear about the death of your father.'",
      "Step 3. End warmly: <b>'Your friend, Yaw.'</b> Never 'Yours faithfully' to a friend."),
    E("Write a suitable heading for a letter asking the assembly to provide street lights in your town.",
      "Step 1. A heading is short, capitalised and names the business exactly.",
      "Step 2. Avoid vague headings such as 'A REQUEST'.",
      "Step 3. <b>PROVISION OF STREET LIGHTS AT ANKAASE TOWNSHIP</b>")])

# ------------------------------------------------------------------ narrative / descriptive
topic("narrative", "Story & descriptive composition", D, [
  "Plan for five minutes before you write: beginning, middle (the problem), end (how it was settled).",
  "Write in the past tense for a story, and keep the same person throughout (I … or he/she …).",
  "Show rather than tell: instead of 'I was afraid', write 'my hands would not keep still'.",
  "Use your five senses in a description — what you saw, heard, smelt, touched and tasted.",
  "Leave three minutes at the end to check spelling, full stops and capital letters. Those marks are free.",
])
O("The best way to begin a story composition is with",
  ["a sentence that makes the reader curious", "an explanation of the title",
   "an apology for your English", "a list of the characters"],
  ["Examiners reward an opening that pulls the reader in.",
   "So begin with <b>a sentence that makes the reader curious</b>, such as 'I had never heard the town so quiet.'"],
  ok=True)
O("A story composition should normally be written in the",
  ["past tense", "present continuous tense", "future tense", "imperative"],
  ["A story tells what happened, so it is told in the <b>past tense</b>.",
   "Changing tense in the middle is one of the commonest faults."],
  ok=True)
O("Which sentence shows, rather than tells, that a boy was nervous?",
  ["He read the same line four times without seeing it.", "He was very nervous indeed.",
   "He felt nervousness.", "The boy's nervousness was great."],
  ["Showing means giving the detail and letting the reader draw the conclusion.",
   "<b>He read the same line four times without seeing it</b> shows the nervousness through action."],
  ok=True)
O("In a descriptive composition about a market, the best detail to include is",
  ["the smell of smoked fish and the shouting of traders", "a definition of the word market",
   "the history of trade in Ghana", "a list of all the goods sold in Ghana"],
  ["Description works through the senses and through particular things.",
   "<b>The smell of smoked fish and the shouting of traders</b> lets the reader hear and smell the place."],
  ok=True)
O("The last paragraph of a story should",
  ["bring the events to a clear end", "introduce a new character",
   "explain the moral in ten lines", "repeat the first paragraph"],
  ["A story needs a settled ending, not a new problem.",
   "So the final paragraph should <b>bring the events to a clear end</b> — a single closing line of reflection is enough."],
  ok=True)
T("Write a story that ends with the words: '… and from that day I never kept quiet about a bully again.' "
  "(Plan and model opening follows.)",
  ["<b>Plan.</b> Paragraph 1: set the scene — the bus stop after school, a boy called Nii who always took the younger "
   "pupils' money. Paragraph 2: the day he took Abena's chop money and she said nothing. Paragraph 3: my own fear — "
   "I knew, and I said nothing either. Paragraph 4: the turning point — Abena stopped coming to school, and the class "
   "teacher asked why. Paragraph 5: I spoke, what followed, and the closing line.",
   "<b>Model opening.</b> The bus stop was always loudest at half past three, which is why nobody heard anything. I was "
   "standing behind the kiosk with my bag on my shoulder when I saw Nii stretch out his hand towards Abena, and I saw "
   "her give him the coins her mother had counted into her palm that morning.",
   "<b>Model closing.</b> My voice shook so much that the teacher asked me to begin again. But I began again, and I "
   "finished — and from that day I never kept quiet about a bully again.",
   "<b>Marking.</b> The examiner awards marks for content (a real story with a clear problem), organisation (paragraphs "
   "that follow one another), expression (varied sentences, some figurative language) and mechanical accuracy "
   "(spelling, punctuation, tense). The given last line must appear <b>exactly</b> as set, at the very end."],
  marks=30)
extras("narrative",
  plain="A story composition is marked on four things: content, organisation, expression and accuracy. You can gain all "
        "four with a simple, true-sounding story told in order — a complicated plot usually loses marks. One problem, one solution, five paragraphs.",
  examples=[
    E("Turn this flat sentence into one that shows the scene: 'The village was very hot.'",
      "Step 1. Ask what you would see, hear or feel in that heat.",
      "Step 2. Choose two particular details.",
      "Step 3. <b>By ten o'clock the goats had crowded under the mango tree, and the sand burned through the soles of my sandals.</b>"),
    E("You are asked to write about 'The most useful lesson I have learnt'. How do you plan it in five minutes?",
      "Step 1. Choose one small, real event — not three.",
      "Step 2. Jot five paragraph labels: the day, what I did wrong, what happened, what I understood, how I behave now.",
      "Step 3. Write one line under each label, then start writing. <b>The plan is what keeps the essay organised.</b>")])

# ------------------------------------------------------------------ article / report
topic("article", "Articles, reports & speeches", D, [
  "An <b>article</b> for a newspaper or magazine needs a title, your name as the writer, and paragraphs with one idea each.",
  "A <b>report</b> (for example of a school event) answers what, where, when, who and how, in the past tense, "
  "and ends with a recommendation or conclusion.",
  "A <b>speech</b> begins with the vocatives — the people you are addressing — in order of seniority: "
  "'Mr Chairman, the Headmaster, members of staff, fellow pupils, …'.",
  "A <b>debate</b> states your stand clearly and gives at least three reasons, each with an example, "
  "and finishes by restating the stand.",
  "Keep to the audience: a speech is spoken, so short sentences and direct address ('you will agree with me') work well.",
])
O("A speech at a school gathering should begin with",
  ["the vocatives, in order of seniority", "a joke about the chairman",
   "the writer's address", "the date and the time"],
  ["A spoken address opens by greeting those present in order of rank.",
   "So it begins with <b>the vocatives</b>: 'Mr Chairman, the Headmistress, members of staff, fellow pupils …'"],
  ok=True)
O("A report on your school's sports day should be written in the",
  ["past tense", "present tense", "future tense", "imperative"],
  ["A report tells what has already happened.", "So it is written in the <b>past tense</b>."],
  ok=True)
O("Which of these is essential in a debate?",
  ["a clear stand, for or against the motion", "a long story about your family",
   "the address of your school", "a drawing to illustrate your point"],
  ["A debate is an argument, and the audience must know which side you are on.",
   "So you need <b>a clear stand, for or against the motion</b>, stated in the first paragraph."],
  ok=True)
O("The main difference between an article and a report is that a report",
  ["records events that have happened", "is always shorter",
   "needs no paragraphs", "must contain a story"],
  ["An article may argue or discuss, while a report is a record.",
   "So a report <b>records events that have happened</b>, usually for someone who was not there."],
  ok=True)
O("A good title for an article on keeping the town clean is",
  ["Our Town, Our Responsibility", "Composition", "An Article for the Newspaper", "Cleanliness"],
  ["A title should be short, interesting and point to the argument.",
   "<b>Our Town, Our Responsibility</b> does all three; 'Cleanliness' alone is flat and the others are not titles at all."],
  ok=True)
T("Write an article for your school magazine on the topic: 'The dangers of mobile phone addiction among pupils.' "
  "(Plan and model paragraphs follow.)",
  ["<b>Title and by-line.</b> SCREENS BEFORE BOOKS: THE PHONE HABIT THAT IS COSTING US OUR GRADES — by Esi Agyeman, Form 3A.",
   "<b>Paragraph 1 (the point).</b> Open with a fact or a scene: 'At nine o'clock last Tuesday, I counted eleven of my "
   "classmates still online. By seven the next morning, nine of them had not finished their mathematics assignment.'",
   "<b>Paragraph 2 (first danger — school work).</b> Hours spent scrolling are hours taken from study and sleep, and "
   "tired pupils cannot concentrate in class.",
   "<b>Paragraph 3 (second danger — health).</b> Long screen time strains the eyes, keeps pupils awake at night, and "
   "replaces the games and walks that keep the body strong.",
   "<b>Paragraph 4 (third danger — behaviour and safety).</b> Pupils meet strangers online, share what they should not "
   "share, and copy behaviour they do not understand.",
   "<b>Paragraph 5 (what should be done).</b> Suggest two practical things: agreed phone-free hours for homework, and "
   "a school talk each term on using phones wisely.",
   "<b>Closing line.</b> 'The phone is a good servant but a poor master — let us keep it in that place.'",
   "<b>Marking.</b> Content (clear, separate dangers), organisation (one idea per paragraph), expression (varied "
   "sentences and a strong title) and accuracy (spelling and punctuation)."],
  marks=30)
extras("article",
  plain="These three forms differ mainly in who is listening. An article is read by strangers, so it needs a title that "
        "attracts them. A report is read by someone who was not there, so it needs facts in order. A speech is heard, so it needs greetings and short sentences.",
  examples=[
    E("Write the opening vocatives for a speech at your school's speech and prize-giving day.",
      "Step 1. List those present in order of seniority.",
      "Step 2. Begin with the chairman, then the guest of honour, then the head, then staff, then pupils.",
      "Step 3. <b>'Mr Chairman, our Guest of Honour, the Headmistress, members of staff, invited guests, fellow pupils, good morning.'</b>"),
    E("You are reporting your school's inter-house athletics. What five facts must appear in the first paragraph?",
      "Step 1. A report answers what, where, when, who and how.",
      "Step 2. So: the event (inter-house athletics), the place (the school field), the date, who took part (the four houses), "
      "and the result.",
      "Step 3. <b>'The annual inter-house athletics competition of Osei Memorial J.H.S. took place on the school field on "
      "Friday, 12 June 2026, with all four houses taking part. Red House won with 148 points.'</b>")])

# ------------------------------------------------------------------ oral english
topic("oral", "Oral English", X, [
  "Paper 1 includes a few questions on sounds. You must match words that share the <b>same sound</b>, not the same spelling.",
  "Vowel sounds: <i>bit</i> /ɪ/ versus <i>beat</i> /iː/; <i>cat</i> /æ/ versus <i>cart</i> /ɑː/; "
  "<i>full</i> /ʊ/ versus <i>fool</i> /uː/.",
  "Consonant traps: <i>ship</i> /ʃ/ versus <i>sip</i> /s/; <i>thin</i> /θ/ versus <i>then</i> /ð/; "
  "<i>van</i> /v/ versus <i>fan</i> /f/.",
  "Silent letters: <b>k</b>nee, <b>w</b>rite, lam<b>b</b>, ho<b>u</b>r, lis<b>t</b>en, is<b>l</b>and.",
  "<b>Stress</b> is the syllable said with more force: TA-ble, be-GIN, pho-TO-gra-pher. "
  "Some words change meaning with stress: a RE-cord (noun) but to re-CORD (verb).",
  "Rhyme means the ending sounds the same: <i>fight</i> rhymes with <i>kite</i>, not with <i>eight</i>… but <i>eight</i> rhymes with <i>late</i>.",
])
O("Which word has the same vowel sound as the underlined part of <u>ea</u>t?",
  ["feet", "bet", "bit", "bat"],
  ["The vowel in <i>eat</i> is the long /iː/ sound.", "<b>Feet</b> has the same long /iː/ sound; 'bit' is the short /ɪ/."],
  ok=True)
O("Which word rhymes with <u>right</u>?",
  ["kite", "rig", "ring", "rich"],
  ["Rhyme depends on the sound of the ending, not the spelling.",
   "<i>Right</i> and <b>kite</b> both end in the /aɪt/ sound."],
  ok=True)
O("In which word is the letter k silent?",
  ["knife", "kite", "kick", "basket"],
  ["English drops the k sound before n at the beginning of a word.",
   "So the k is silent in <b>knife</b> (also knee, knock, know)."],
  ok=True)
O("Which word is stressed on the second syllable?",
  ["begin", "table", "pencil", "window"],
  ["Say each word aloud and feel which part is stronger.",
   "<i>TA-ble, PEN-cil, WIN-dow</i> are stressed first; <b>be-GIN</b> is stressed on the second syllable."],
  ok=True)
O("Which word has the same consonant sound as the underlined part of <u>sh</u>oe?",
  ["sugar", "soap", "chair", "zebra"],
  ["The sound in <i>shoe</i> is /ʃ/.",
   "<b>Sugar</b> begins with that same /ʃ/ sound, although it is spelt with s."],
  ok=True)
T("(a) Give two words in which the letter w is silent. (b) Say which syllable is stressed in each of these words: "
  "photograph, photographer, important. (c) Give one word that rhymes with each of: tough, break.",
  ["(a) Any two of: <b>write</b>, <b>wrong</b>, <b>wrist</b>, <b>sword</b>, <b>answer</b>, <b>two</b>.",
   "(b) <b>PHO-to-graph</b> (first), <b>pho-TO-gra-pher</b> (second), <b>im-POR-tant</b> (second). "
   "Notice how the stress moves when the ending changes.",
   "(c) <i>tough</i> rhymes with <b>stuff</b> (both end /ʌf/); <i>break</i> rhymes with <b>cake</b> (both end /eɪk/).",
   "Spelling is a poor guide here — always say the words aloud."],
  marks=8)
extras("oral",
  plain="Oral English looks hard on paper because English spelling and English sound do not match. The trick is to say the "
        "words quietly to yourself and listen, rather than compare letters. <i>Sugar</i> starts with the sound of <i>sh</i>; <i>eight</i> rhymes with <i>late</i>.",
  examples=[
    E("Which of these words does not belong: cough, rough, tough, though?",
      "Step 1. Say each one aloud: /kɒf/, /rʌf/, /tʌf/, /ðəʊ/.",
      "Step 2. Three of them end in the f sound.",
      "Step 3. <b>Though</b> is the odd one out — the gh is silent."),
    E("The word 'present' can be said in two ways. Explain.",
      "Step 1. Stressed on the first syllable, PRE-sent, it is a noun or adjective — a gift, or 'he is present'.",
      "Step 2. Stressed on the second, pre-SENT, it is a verb — to give or to show something.",
      "Step 3. So <b>the stress changes the part of speech</b>: 'He will pre-SENT the PRE-sent.'")],
  fig=draw.flow(["Say the word aloud", "Listen to the sound, not the spelling",
                 "Match the sound (sugar = sh)", "Mark the stressed syllable"],
                label="How to answer an oral English question"))
