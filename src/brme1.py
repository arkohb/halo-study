"""BECE Religious and Moral Education - God and His creation; religious practices."""
from core import *
import draw

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}
A, B = "A. God, His creation & attributes", "B. Religious practices"

topic("creation", "God as Creator: the creation stories", A, [
  "All three religions studied in R.M.E. — Christianity, Islam and African Traditional Religion — "
  "teach that God is the Creator of the universe.",
  "<b>Christianity</b>: Genesis 1 and 2 describe God creating the heavens and the earth in six days and resting on "
  "the seventh; human beings were made in God's own image and given charge over creation.",
  "<b>Islam</b>: the Qur'an teaches that Allah created the heavens and the earth in six periods, and that He "
  "created the first human being, Adam, from clay and breathed life into him.",
  "<b>African Traditional Religion</b>: the Supreme Being — <i>Onyame</i> or <i>Nyame</i> (Akan), <i>Mawu</i> (Ewe), "
  "<i>Nyonmo</i> (Ga), <i>Naawuni</i> (Dagbani) — created the world, the lesser gods and human beings. "
  "Many communities keep their own account of how the first people came.",
  "The moral lesson common to all three is that creation is <b>God's property, not ours</b>: it is good, it is "
  "orderly, and we are caretakers who will answer for how we treat it.",
])
O("According to the Christian creation story, human beings were created",
  ["in the image of God", "before the plants", "on the first day", "from water only"],
  ["Genesis records that God made the heavens, the earth, the plants and animals first.",
   "Human beings were created <b>in the image of God</b>, on the sixth day."],
  ok=True)
O("In Islamic teaching, the first human being created by Allah was",
  ["Adam", "Ibrahim", "Musa", "Isa"],
  ["Ibrahim, Musa and Isa are prophets who came later.", "The first human being was <b>Adam</b>, created from clay."],
  ok=True)
O("The Akan name for the Supreme Being is",
  ["Onyame", "Mawu", "Nyonmo", "Naawuni"],
  ["Mawu is Ewe, Nyonmo is Ga and Naawuni is Dagbani.", "The Akan call the Supreme Being <b>Onyame (Nyame)</b>."],
  ok=True)
O("The main moral lesson taught by the creation stories is that human beings should",
  ["take good care of God's creation", "own the earth absolutely",
   "fear all animals", "worship the sun and moon"],
  ["We are placed in creation as caretakers, not owners.",
   "The lesson is that human beings should <b>take good care of God's creation</b>."],
  ok=True)
O("Which of the following is common to the creation stories of Christianity, Islam and African Traditional Religion?",
  ["God is the Creator of all things", "Creation took exactly seven days",
   "The world will never come to an end", "The world was created from water"],
  ["The details differ from one religion to another.",
   "What all three share is the teaching that <b>God is the Creator of all things</b>."],
  ok=True)
T("(a) Give an account of the creation story of any one of the three religions you have studied. "
  "(b) State three things that the creation stories teach us about God. "
  "(c) Give three ways in which pupils can show that they value God's creation.",
  ["(a) <b>Christianity</b> (Genesis 1–2): God created light on the first day; the sky on the second; land, sea and "
   "plants on the third; the sun, moon and stars on the fourth; fish and birds on the fifth; land animals and human "
   "beings on the sixth; and He rested on the seventh day, blessing it. He made human beings in His own image, male "
   "and female, and gave them charge over the earth. "
   "(A candidate may instead give the Islamic account — Allah created the heavens and the earth in six periods and "
   "formed Adam from clay — or a traditional account from his or her own community.)",
   "(b) God is <b>all-powerful</b>, for He created everything out of nothing; God is <b>orderly and wise</b>, for "
   "creation follows a pattern and each thing has its purpose; and God is <b>good and loving</b>, for He provided "
   "everything human beings need and declared creation good.",
   "(c) Pupils can <b>plant and water trees and keep the school compound clean</b>; <b>avoid wasting water, food and "
   "electricity</b>; <b>treat animals kindly and refuse to kill or trap them for sport</b>; and refuse to litter, "
   "burn bush or pollute streams."],
  marks=12, fig=draw.tree("GOD THE CREATOR", ["Christianity: Genesis — six days, rest on the seventh",
                                              "Islam: Qur'an — six periods, Adam from clay",
                                              "A.T.R.: the Supreme Being made the world and the first people"],
                          label="Creation in the three religions"))
extras("creation",
  plain="R.M.E. does not ask you to choose between the three religions; it asks you to know what each teaches and what "
        "moral lesson follows. On creation, all three agree on the essential point — God made it and we are answerable for how we treat it.",
  examples=[
    E("How would you answer a classmate who says the creation stories cannot all be true because the details differ?",
      "Step 1. Note what the stories agree on: one Creator, an orderly world, human beings with special responsibility.",
      "Step 2. Note that each story was told to a particular people in their own language and imagery.",
      "Step 3. In R.M.E. the examiner wants the <b>teaching and the moral lesson</b>, not a quarrel about details."),
    E("State the creation lesson behind a community rule that forbids farming on the banks of a river.",
      "Step 1. Traditionally the river is regarded as sacred, a gift of the Creator held in trust.",
      "Step 2. Farming to the water's edge causes erosion and silting, and the river dies.",
      "Step 3. So the rule expresses <b>stewardship</b> — looking after what God has given, for those coming after us.")])

topic("attributes", "The attributes of God", A, [
  "An attribute is a quality that belongs to God's nature.",
  "<b>Omnipotent</b> — all-powerful; <b>omniscient</b> — all-knowing; <b>omnipresent</b> — present everywhere; "
  "<b>eternal</b> — without beginning or end; <b>holy</b>; <b>merciful</b>; <b>just</b>; <b>loving</b>; "
  "<b>Creator</b> and <b>provider</b>.",
  "Christianity speaks of God as Father, holy and loving; Islam teaches the ninety-nine beautiful names of Allah, "
  "among them <i>Ar-Rahman</i> (the Most Gracious) and <i>Ar-Rahim</i> (the Most Merciful); "
  "African Traditional Religion gives the Supreme Being praise names such as <i>Otumfo</i> (the Powerful One) "
  "and <i>Odomankoma</i> (the Infinite Creator).",
  "Attributes are shown in daily life: rain and harvest show God the provider; healing shows God the merciful; "
  "conscience shows God the just.",
  "Knowing God's attributes should lead to reverence, trust in times of trouble, honesty even when no one is "
  "watching, and kindness towards others.",
])
O("The attribute of God which means 'all-knowing' is",
  ["omniscient", "omnipotent", "omnipresent", "eternal"],
  ["Omnipotent means all-powerful and omnipresent means everywhere.", "All-knowing is <b>omniscient</b>."],
  ok=True)
O("The belief that God is present everywhere at the same time is described as",
  ["omnipresence", "omnipotence", "omniscience", "holiness"],
  ["It is the attribute of being everywhere.", "That is <b>omnipresence</b>."],
  ok=True)
O("In Islam, Ar-Rahman and Ar-Rahim are names of Allah meaning",
  ["the Most Gracious and the Most Merciful", "the Creator and the Judge",
   "the Eternal and the Holy", "the Provider and the Protector"],
  ["They are the two names in the <i>basmala</i>, recited at the opening of almost every chapter of the Qur'an (every surah but one).",
   "They mean <b>the Most Gracious and the Most Merciful</b>."],
  ok=True)
O("A pupil who refuses to cheat in an examination even when no teacher is watching shows belief in God as",
  ["all-seeing and just", "a distant creator",
   "the provider of food", "the maker of the stars"],
  ["Behaviour in secret reveals what a person truly believes.",
   "It shows belief that God is <b>all-seeing and just</b>."],
  ok=True)
O("The Akan praise name 'Odomankoma' refers to God as",
  ["the Infinite Creator", "the God of war", "the god of the river", "the ancestor of the clan"],
  ["Traditional praise names describe the Supreme Being, not the lesser gods.",
   "<i>Odomankoma</i> describes God as <b>the Infinite Creator</b>."],
  ok=True)
T("(a) State five attributes of God. (b) Explain any three of them, giving an example of how each is seen in daily "
  "life. (c) State three ways in which belief in God's attributes should affect a pupil's behaviour.",
  ["(a) <b>Omnipotent, omniscient, omnipresent, eternal, holy, merciful, just, loving, Creator, provider</b> "
   "(any five).",
   "(b) <b>Omnipotent (all-powerful)</b> — nothing is too hard for God; believers point to creation itself and to "
   "recoveries from serious illness. "
   "<b>Omniscient (all-knowing)</b> — God knows our thoughts and our secret deeds, so wrongdoing cannot be hidden. "
   "<b>Merciful</b> — God forgives those who repent; believers see this in second chances and in answered prayer.",
   "(c) It should make a pupil <b>honest and sincere even in secret</b>, since God sees all; "
   "<b>humble and reverent</b>, since God is holy and far greater than we are; and "
   "<b>hopeful and persevering in difficulty</b>, trusting God's power and mercy — and <b>kind and forgiving</b> "
   "towards others, as God is to us."],
  marks=12)
extras("attributes",
  plain="Attributes are not words to recite but ideas with consequences. If God is all-seeing, cheating in secret makes no "
        "sense. If God is merciful, there is a way back after a wrong. Examiners reward answers that make that link.",
  examples=[
    E("Link each attribute to a behaviour: omniscient, merciful, just.",
      "Step 1. Omniscient → <b>honesty in secret</b>, because nothing is hidden.",
      "Step 2. Merciful → <b>forgiving others</b> and seeking forgiveness after wrongdoing.",
      "Step 3. Just → <b>fair dealing</b>, because every deed will be judged."),
    E("A boy says God cannot be both all-powerful and merciful, since a powerful God would simply punish sin at once. Respond.",
      "Step 1. Power means God is able to act; mercy means God chooses when and how.",
      "Step 2. All three religions teach that God gives time for repentance precisely because He is merciful.",
      "Step 3. So the two attributes <b>work together</b>: the delay is not weakness but patience.")])

topic("stewardship", "Caring for God's creation", A, [
  "Human beings are <b>stewards (caretakers)</b> of creation, not its owners. "
  "Christianity speaks of tending the garden; Islam of the human being as <i>khalifah</i> (trustee) on earth; "
  "African Traditional Religion of sacred groves, rivers and taboo days on which the land rests.",
  "Traditional practices that protect the environment: sacred groves where nobody may cut a tree, "
  "taboo days on which no one farms or fishes, closed seasons before a festival, and totems that forbid "
  "the killing of certain animals.",
  "Ways of caring for creation: planting trees, avoiding bush fires, keeping water bodies clean, "
  "proper disposal of waste, kindness to animals, and avoiding waste of food, water and power.",
  "Abuse of creation — galamsey, deforestation, pollution, cruelty to animals — brings suffering on "
  "the community itself, and all three religions treat it as a moral wrong, not merely a technical problem.",
  "Caring for creation is also caring for people: the person who pollutes a stream harms his neighbour.",
])
O("The teaching that human beings are caretakers of creation rather than its owners is known as",
  ["stewardship", "ownership", "inheritance", "dominion without limit"],
  ["A steward looks after property on behalf of its owner.", "The teaching is <b>stewardship</b>."],
  ok=True)
O("In Islamic teaching, the human being is described as the <i>khalifah</i> on earth, which means",
  ["God's trustee or representative", "the owner of the earth",
   "a wanderer on the earth", "the ruler of all religions"],
  ["The term carries responsibility, not possession.",
   "It means <b>God's trustee or representative</b>, answerable for how the earth is used."],
  ok=True)
O("A sacred grove in a traditional community helps the environment because",
  ["trees and animals there are never destroyed", "it is used as a refuse dump",
   "farmers are encouraged to clear it", "hunters are allowed in once a year"],
  ["The prohibition is what preserves it.",
   "In a sacred grove <b>trees and animals are never destroyed</b>, so the forest and its species survive."],
  ok=True)
O("Which of these practices shows poor stewardship of creation?",
  ["Dumping refuse into a river", "Planting trees on bare land",
   "Keeping a taboo day on the farm", "Separating waste for recycling"],
  ["The other three protect creation.",
   "<b>Dumping refuse into a river</b> destroys the water that others depend on."],
  ok=True)
O("A traditional taboo that forbids fishing on a particular day of the week helps by",
  ["allowing the fish to breed and multiply", "giving the gods something to eat",
   "making fish more expensive", "punishing lazy fishermen"],
  ["Rest days reduce the pressure on the stock.",
   "Such a taboo <b>allows the fish to breed and multiply</b>, so there is fish for the future — the same principle as a modern closed season."],
  ok=True)
T("(a) Explain the meaning of stewardship. (b) Give three traditional practices in Ghana that protect the "
  "environment, and explain how each works. (c) State four ways in which a pupil can care for God's creation.",
  ["(a) <b>Stewardship means that God is the owner of creation and human beings are caretakers who use it on His "
   "behalf and must answer to Him for how they treat it.</b>",
   "(b) <b>Sacred groves</b> — forest areas where felling trees and hunting are forbidden, so the trees, animals and "
   "the streams rising there are preserved. <b>Taboo days</b> — no farming or fishing on a stated day, which rests the "
   "land and allows fish stocks to recover. <b>Totems</b> — a clan forbids the killing of its totem animal, so that "
   "species is protected across the whole area. (Closed seasons before a festival have the same effect.)",
   "(c) Any four: <b>plant and water trees</b> at school and at home; <b>keep the compound and the streets clean and "
   "dispose of waste properly</b>; <b>avoid wasting water, food and electricity</b>; <b>refuse to start bush fires or "
   "to litter water bodies</b>; <b>treat animals kindly</b>; and <b>teach others</b> through a school environment club."],
  marks=12)
extras("stewardship",
  plain="Notice how closely religious teaching and good science agree here. A taboo day rests the land; a closed season "
        "lets fish breed; a sacred grove preserves a water catchment. The language is religious, but the effect is conservation.",
  examples=[
    E("A man cuts down the last trees around a stream to make charcoal. Give one religious and one practical objection.",
      "Step 1. Religious: he is destroying what God entrusted to the whole community, harming his neighbours for his own gain.",
      "Step 2. Practical: without the trees the banks erode, the stream silts up and dries, and everyone loses their water.",
      "Step 3. The two objections point the same way — <b>the wrong and the harm are the same act</b>."),
    E("How would you persuade a youth group to revive a neglected sacred grove?",
      "Step 1. Show what it once did: protected the stream, the herbs and the shade.",
      "Step 2. Involve the elders, so that the tradition and the rules are properly restored.",
      "Step 3. Add modern reasons — <b>water security, carbon, even eco-tourism income</b> — so that young people see it as their project, not only their grandfathers'.")])

topic("purpose", "The purpose of God's creation", A, [
  "All three religions teach that creation has a purpose and is not an accident.",
  "Human beings were created to <b>worship and serve God</b>, to <b>live in community</b> with one another, "
  "to <b>work and be productive</b>, and to <b>care for the rest of creation</b>.",
  "Each part of creation serves a purpose: plants give food, oxygen and medicine; animals give food, work and "
  "companionship; rain, soil and sunlight make farming possible; even insects pollinate crops.",
  "The special position of human beings lies in reason, conscience, speech and the freedom to choose — "
  "which is also why they are morally responsible.",
  "A sense of purpose shapes behaviour: work becomes service, not drudgery; talents are to be developed and used; "
  "and life is to be used for good rather than wasted.",
])
O("According to religious teaching, the chief purpose for which human beings were created is to",
  ["worship and serve God", "become rich",
   "rule over other human beings", "live without work"],
  ["Wealth and power are not given as purposes.",
   "The chief purpose is to <b>worship and serve God</b>, and to care for creation and one another."],
  ok=True)
O("What distinguishes human beings from the rest of creation in religious teaching is that they have",
  ["reason, conscience and freedom to choose", "the ability to move about",
   "the need for food and water", "the ability to reproduce"],
  ["Animals also move, eat and reproduce.",
   "Human beings have <b>reason, conscience and freedom to choose</b> — and therefore moral responsibility."],
  ok=True)
O("The belief that creation has a purpose should lead a pupil to",
  ["develop and use his talents for good", "wait for God to do everything",
   "despise manual work", "avoid responsibility"],
  ["Purpose calls for effort, not idleness.",
   "It should lead a pupil to <b>develop and use his talents for good</b>."],
  ok=True)
O("Which of the following shows that plants serve a purpose in creation?",
  ["They provide food, oxygen and medicine", "They occupy space on the land",
   "They are beautiful only", "They grow without help"],
  ["Beauty is a benefit, but not the main one.",
   "Plants <b>provide food, oxygen and medicine</b>, besides shade, timber and protection for the soil."],
  ok=True)
O("A person who wastes his life in idleness and drink fails chiefly because he",
  ["does not fulfil the purpose for which he was created", "has no money",
   "has no friends", "cannot read or write"],
  ["The deepest failure is not material.",
   "He <b>does not fulfil the purpose for which he was created</b> — to serve God, work and be useful to others."],
  ok=True)
T("(a) State four purposes for which God created human beings. (b) Give three ways in which other parts of creation "
  "serve human beings. (c) Explain three ways in which a J.H.S. pupil can begin to fulfil his purpose now.",
  ["(a) To <b>worship and serve God</b>; to <b>live together in community</b>, loving and helping one another; to "
   "<b>work and be productive</b>, developing the earth; and to <b>care for creation</b> as God's stewards. "
   "(Procreation — to be fruitful and multiply — is also accepted.)",
   "(b) <b>Plants</b> provide food, oxygen, medicine, timber and shade. <b>Animals</b> provide food, clothing, "
   "transport, work and companionship. <b>Soil, water, sunlight and rain</b> make farming, drinking, washing and "
   "energy possible. (Minerals provide materials and national income.)",
   "(c) By <b>working hard at school and developing his talents</b>, since the skills he gains are what he will use to "
   "serve others; by <b>serving at home, in school and in his religious body</b> — in the choir, as a prefect, in a "
   "clean-up — which trains him in responsibility; and by <b>living morally and caring for the environment</b>, "
   "keeping away from what destroys his health and his future."],
  marks=12)
extras("purpose",
  plain="Purpose is the bridge between the first two topics and the moral section of the syllabus. If we were created "
        "with reason and freedom, then how we use them matters — which is why R.M.E. moves from creation straight to character.",
  examples=[
    E("A pupil is good at drawing but says it is useless for the BECE. Advise him in terms of purpose.",
      "Step 1. A talent is part of what he was given, not an accident.",
      "Step 2. Drawing leads to real work — architecture, design, teaching, signwriting, animation.",
      "Step 3. So he should <b>keep developing it alongside his school work</b>, as a gift to be used, not buried."),
    E("Explain how the purpose of creation condemns cruelty to animals.",
      "Step 1. Animals were created with their own place and value in creation.",
      "Step 2. Human beings were given charge over them as stewards, not as tyrants.",
      "Step 3. So cruelty is an <b>abuse of trust</b>, and all three religions forbid it.")])

topic("worship", "Worship in the three religions", B, [
  "Worship is the reverence and honour given to God through prayer, praise, offerings and obedience.",
  "<b>Christianity</b>: worship in church, chiefly on Sunday — prayer, singing, Bible reading, preaching, offering, "
  "baptism and Holy Communion.",
  "<b>Islam</b>: <i>salat</i> five times a day (fajr, zuhr, asr, maghrib, isha), facing the Ka'bah in Mecca, "
  "preceded by <i>wudu</i> (ablution); congregational worship at the mosque on Friday (<i>Jumu'ah</i>).",
  "<b>African Traditional Religion</b>: prayer and <b>libation</b> poured with water or drink, offerings and "
  "sacrifices, drumming and dancing, observance of taboos, and festivals at shrines or in the family house; "
  "the Supreme Being may be prayed to directly, and in many communities also through the lesser gods and the ancestors, who are regarded as intermediaries.",
  "Moral value of worship: it builds reverence and gratitude, unites the community, teaches obedience and "
  "self-discipline, comforts the troubled, and restrains wrongdoing.",
])
O("The Muslim act of worship performed five times daily is called",
  ["salat", "zakat", "sawm", "hajj"],
  ["Zakat is almsgiving, sawm is fasting and hajj is the pilgrimage.", "The five daily prayers are <b>salat</b>."],
  ok=True)
O("Muslims face which direction in prayer?",
  ["Towards the Ka'bah in Mecca", "Towards the rising sun",
   "Towards Jerusalem", "Towards the nearest river"],
  ["The direction of prayer is called the <i>qiblah</i>.",
   "Muslims pray facing <b>the Ka'bah in Mecca</b>."],
  ok=True)
O("The pouring of water or drink on the ground with prayer in African Traditional Religion is called",
  ["libation", "baptism", "ablution", "communion"],
  ["Baptism and communion are Christian, and ablution is the washing before Muslim prayer.",
   "The traditional act is <b>libation</b>."],
  ok=True)
O("The washing performed by a Muslim before prayer is known as",
  ["wudu", "salat", "zakat", "sadaqah"],
  ["It is a ritual cleansing of parts of the body.", "It is called <b>wudu</b> (ablution)."],
  ok=True)
O("One moral value common to worship in all three religions is that it",
  ["teaches reverence and self-discipline", "makes worshippers wealthy",
   "removes the need to work", "guarantees long life"],
  ["Worship is not a means of gaining wealth or avoiding duty.",
   "It <b>teaches reverence and self-discipline</b>, and it binds the community together."],
  ok=True)
T("(a) Describe how worship is conducted in any one of the three religions you have studied. "
  "(b) State four items used in worship in African Traditional Religion and the purpose of each. "
  "(c) Give four moral benefits of worship.",
  ["(a) <b>Islam</b>: the worshipper first performs <i>wudu</i>, washing hands, mouth, nose, face, arms, head and "
   "feet. At the call to prayer (<i>adhan</i>) the congregation lines up facing the Ka'bah. The imam leads, and the "
   "worshippers recite from the Qur'an while standing, bowing (<i>ruku</i>), prostrating (<i>sujud</i>) and sitting. "
   "This is done five times a day, and on Friday the congregation gathers at the mosque for <i>Jumu'ah</i> with a "
   "sermon. (A Christian or traditional account is equally acceptable.)",
   "(b) <b>Water or drink</b> — poured as libation to invite God, the gods and the ancestors. "
   "<b>Drums and gongs</b> — to call the community and accompany songs of praise. "
   "<b>Animals or foodstuffs</b> — offered in sacrifice or thanksgiving. "
   "<b>Eggs, white clay and beads or white cloth</b> — used by the priest as symbols of purity and of the deity.",
   "(c) Worship <b>builds reverence for God and gratitude</b>; it <b>teaches obedience and self-discipline</b>, since "
   "it must be done at set times and in a set manner; it <b>unites the community</b> across family and class; and it "
   "<b>comforts and guides</b>, restraining people from wrongdoing because they are accountable to God."],
  marks=12)
extras("worship",
  plain="The forms of worship differ sharply — a mosque at dawn, a church on Sunday, libation at a family house — but the "
        "examiner is usually after the same two things: the correct details of one religion's practice, and the moral value that the practice builds.",
  examples=[
    E("Why does Islam require wudu before salat?",
      "Step 1. Prayer is standing before God, so cleanliness of body is a sign of respect.",
      "Step 2. The washing also prepares the mind, marking the change from ordinary activity to worship.",
      "Step 3. So wudu teaches <b>reverence, cleanliness and self-discipline</b> at the same time."),
    E("A pupil says libation is mere superstition. Explain its meaning to him respectfully.",
      "Step 1. In African Traditional Religion, libation is prayer: the words spoken matter more than the drink poured.",
      "Step 2. It calls on God, the gods and the ancestors, gives thanks, and asks for peace, rain, health and children.",
      "Step 3. Whatever a person's own faith, the right response is <b>to understand it as the prayer of a people</b>, and to discuss it with respect.")])

topic("prayer", "Prayer and its importance", B, [
  "Prayer is communication with God — adoration, confession, thanksgiving and petition.",
  "Christianity: the Lord's Prayer taught by Jesus; prayer may be private or in the congregation, in words or in song.",
  "Islam: the five obligatory daily prayers (<i>salat</i>), and voluntary personal prayer (<i>du'a</i>) "
  "which may be said at any time.",
  "African Traditional Religion: prayer through libation and at shrines, often led by the head of the family, "
  "an elder or a priest, on behalf of the whole community.",
  "Importance: it strengthens faith, brings peace of mind, gives thanks, asks forgiveness, "
  "and reminds the worshipper that he depends on God.",
  "Prayer is not a substitute for effort: the farmer prays for harvest and then weeds his farm; "
  "the pupil prays for success and then studies.",
])
O("The prayer taught by Jesus to his disciples is known as",
  ["the Lord's Prayer", "the Apostles' Creed", "the Beatitudes", "the Ten Commandments"],
  ["The Creed is a statement of belief and the Commandments are laws.",
   "The prayer Jesus taught is <b>the Lord's Prayer</b>."],
  ok=True)
O("In Islam, a voluntary personal prayer said at any time is called",
  ["du'a", "salat", "adhan", "zakat"],
  ["Salat is the obligatory prayer at fixed times and adhan is the call to prayer.",
   "Voluntary personal prayer is <b>du'a</b>."],
  ok=True)
O("In African Traditional Religion, prayer on behalf of the whole community is usually led by",
  ["the head of the family or a priest", "any child of the family",
   "a stranger passing by", "the youngest wife"],
  ["Authority to speak for the community rests with its recognised heads.",
   "It is led by <b>the head of the family, an elder or a priest</b>."],
  ok=True)
O("Which of the following is NOT a type of prayer?",
  ["Gossiping about others", "Thanksgiving", "Confession", "Petition"],
  ["Thanksgiving, confession and petition are all forms of prayer.",
   "<b>Gossiping about others</b> is not prayer — indeed all three religions condemn it."],
  ok=True)
O("A pupil who prays for success in the BECE should also",
  ["study hard and revise regularly", "wait for a miracle",
   "stop attending school", "copy from others in the exam"],
  ["Faith and effort belong together.",
   "He should <b>study hard and revise regularly</b> — prayer does not replace work."],
  ok=True)
T("(a) What is prayer? (b) State four types of prayer and give an example of each. "
  "(c) Give four reasons why prayer is important in the life of a believer.",
  ["(a) <b>Prayer is communication with God — speaking to Him in praise, thanksgiving, confession and request, "
   "and listening for His guidance.</b>",
   "(b) <b>Adoration or praise</b> — 'Great are you, Lord, Creator of heaven and earth.' "
   "<b>Thanksgiving</b> — thanking God for health, food, success in an examination. "
   "<b>Confession</b> — admitting a wrong and asking forgiveness. "
   "<b>Petition or intercession</b> — asking for something for oneself, or praying for a sick relative, for the school "
   "or for the nation.",
   "(c) Prayer <b>strengthens faith and the sense of God's presence</b>; it brings <b>peace of mind and courage</b> in "
   "trouble; it is the means of <b>asking and receiving forgiveness</b>, which keeps the conscience clear; it "
   "<b>expresses gratitude</b> and so guards against pride; and it <b>unites a family or congregation</b> that prays "
   "together."],
  marks=12)
extras("prayer",
  plain="Every religion in the syllabus prays, though in different words and postures. The examiner's favourite point is "
        "the balance: prayer and work go together — pray for the harvest, then pick up the hoe.",
  examples=[
    E("Give the four parts of a balanced prayer, with one line each.",
      "Step 1. Praise — 'Almighty God, Creator of all things.' Thanksgiving — 'Thank you for life and health today.'",
      "Step 2. Confession — 'Forgive me for the lie I told my mother.'",
      "Step 3. Petition — <b>'Help me to be honest, and bless my studies and my family.'</b>"),
    E("A sick man refuses medicine, saying prayer is enough. How does religious teaching answer him?",
      "Step 1. All three religions teach that God provides remedies as well as hearing prayer.",
      "Step 2. Refusing available help is not faith but neglect of the means God has given.",
      "Step 3. The balanced position is to <b>pray and take the medicine</b>, as the farmer prays and still weeds.")])

topic("festivals", "Religious festivals", B, [
  "A festival is a special occasion set aside to remember an important religious event, honour God or the "
  "ancestors, and renew the life of the community.",
  "<b>Christian</b>: Christmas (the birth of Jesus), Easter (his death and resurrection), "
  "Good Friday, Pentecost, Harvest.",
  "<b>Islamic</b>: Eid-ul-Fitr (the end of the fast of Ramadan), Eid-ul-Adha (the festival of sacrifice, "
  "recalling Ibrahim's obedience), Maulid-un-Nabi (the Prophet's birthday).",
  "<b>Traditional</b>: Homowo (Ga), Odwira and Akwasidae (Akan), Aboakyer (Effutu), Hogbetsotso (Anlo), "
  "Damba (Dagbamba), Bakatue (Elmina), Fetu Afahye (Cape Coast), Kundum, Yam festivals.",
  "Significance: thanksgiving to God, remembrance of history, purification and reconciliation, "
  "unity and home-coming, fund-raising for development, installation of chiefs, and attraction of tourists.",
  "Problems associated with some festivals: drunkenness, violence, extravagance and immorality — "
  "which are abuses, not purposes, of the festival.",
])
O("The Christian festival that celebrates the resurrection of Jesus Christ is",
  ["Easter", "Christmas", "Pentecost", "Harvest"],
  ["Christmas marks his birth and Pentecost the coming of the Holy Spirit.",
   "The resurrection is celebrated at <b>Easter</b>."],
  ok=True)
O("Eid-ul-Fitr is celebrated by Muslims to mark",
  ["the end of the fast of Ramadan", "the birth of the Prophet",
   "the pilgrimage to Mecca", "the revelation of the first verses of the Qur'an"],
  ["Eid-ul-Adha marks the sacrifice and Maulid the Prophet's birthday.",
   "Eid-ul-Fitr marks <b>the end of the fast of Ramadan</b>."],
  ok=True)
O("Homowo is a festival celebrated by the",
  ["Ga people", "Anlo people", "Effutu people", "Dagbamba"],
  ["Hogbetsotso is Anlo, Aboakyer is Effutu and Damba is Dagbamba.",
   "Homowo — which means 'hooting at hunger' — is celebrated by the <b>Ga people</b>."],
  ok=True)
O("Eid-ul-Adha reminds Muslims of the obedience of",
  ["Ibrahim", "Musa", "Isa", "Yusuf"],
  ["It recalls his readiness to sacrifice his son at God's command.",
   "The festival of sacrifice recalls the obedience of <b>Ibrahim</b>."],
  ok=True)
O("Which of the following is NOT a proper purpose of a religious festival?",
  ["Drunkenness and violence", "Thanksgiving to God",
   "Reconciliation among family members", "Raising funds for development"],
  ["The last three are among the real purposes.",
   "<b>Drunkenness and violence</b> are abuses that spoil festivals, not purposes of them."],
  ok=True)
T("(a) Name two festivals from each of the three religions you have studied. "
  "(b) Describe how any one traditional festival in Ghana is celebrated. "
  "(c) State four benefits of festivals to a community and two ways in which festivals are abused.",
  ["(a) <b>Christian</b>: Christmas, Easter (also Good Friday, Pentecost, Harvest). "
   "<b>Islamic</b>: Eid-ul-Fitr, Eid-ul-Adha (also Maulid-un-Nabi). "
   "<b>Traditional</b>: Homowo, Odwira (also Aboakyer, Hogbetsotso, Damba, Fetu Afahye, Bakatue).",
   "(b) <b>Homowo (Ga)</b>: a ban on drumming and noise-making is imposed during the planting season so that the crops "
   "may grow in peace. The ban is lifted with a ceremony; then comes the <i>Soobii</i> — the home-coming of citizens "
   "living elsewhere. On the festival day, the family heads sprinkle <i>kpokpoi</i> (the special festival food) and "
   "pour libation, remembering the famine their ancestors survived and 'hooting at hunger'. There is feasting, "
   "visiting of relatives, reconciliation of quarrels, and a durbar of chiefs. "
   "(An account of Odwira, Aboakyer or Hogbetsotso earns the same marks.)",
   "(c) Benefits: <b>thanksgiving to God and remembrance of the community's history</b>; <b>unity and reconciliation</b>, "
   "as citizens return home and quarrels are settled; <b>development funds raised at durbars</b> for schools and "
   "clinics; <b>preservation of culture and the attraction of tourists</b>, which brings income. "
   "Abuses: <b>drunkenness, violence and immorality</b>; and <b>extravagant spending</b> that leaves families in debt."],
  marks=12)
extras("festivals",
  plain="Festivals are where religion, culture and economics meet. Learn two festivals from each religion with their "
        "meaning, and be able to describe one traditional festival in order from start to finish — that description is a frequent theory question.",
  examples=[
    E("Why is a ban on drumming imposed before Homowo?",
      "Step 1. The ban falls in the planting season.",
      "Step 2. It protects a period of quiet for the crops, and for the spiritual preparation of the community.",
      "Step 3. Lifting it marks <b>the move from work and waiting to thanksgiving and celebration</b>."),
    E("Suggest three ways a town could reduce the abuses that spoil its annual festival.",
      "Step 1. The chiefs and religious leaders set and announce clear rules, including limits on alcohol at the durbar.",
      "Step 2. The assembly and police plan crowd control and deal firmly with violence.",
      "Step 3. <b>Give young people a real part in the programme</b> — sports, quizzes, clean-up, cultural competitions — so the celebration has content beyond drinking.")])

topic("obligations", "Religious duties: fasting, almsgiving & pilgrimage", B, [
  "<b>The five pillars of Islam</b>: <i>shahadah</i> (declaration of faith), <i>salat</i> (prayer), "
  "<i>zakat</i> (almsgiving), <i>sawm</i> (fasting in Ramadan) and <i>hajj</i> (pilgrimage to Mecca).",
  "<b>Fasting</b>: Muslims fast from dawn to sunset throughout Ramadan; Christians fast at Lent and at other times. "
  "Fasting teaches self-control, sympathy with the hungry and dependence on God.",
  "<b>Almsgiving</b>: <i>zakat</i> is a fixed yearly share of a Muslim's wealth given to the poor; "
  "<i>sadaqah</i> is voluntary charity. Christianity teaches tithes, offerings and care for the needy; "
  "African Traditional Religion teaches generosity to strangers and support for the bereaved.",
  "<b>Pilgrimage</b>: hajj to Mecca is required once in a lifetime of every Muslim who is able; "
  "Christians may visit the Holy Land; traditional worshippers visit shrines and ancestral homes.",
  "Moral value: these duties train self-discipline, compassion, humility and the habit of giving.",
])
O("The pillar of Islam that requires giving a fixed share of one's wealth to the poor is",
  ["zakat", "salat", "sawm", "hajj"],
  ["Salat is prayer, sawm is fasting and hajj is the pilgrimage.", "Compulsory almsgiving is <b>zakat</b>."],
  ok=True)
O("Muslims fast during the month of",
  ["Ramadan", "Shawwal", "Muharram", "Rajab"],
  ["Eid-ul-Fitr is celebrated in Shawwal, at the end of the fast.",
   "The fast is kept throughout <b>Ramadan</b>."],
  ok=True)
O("The pilgrimage to Mecca, required once in a lifetime of every able Muslim, is",
  ["hajj", "umrah", "zakat", "shahadah"],
  ["Umrah is the lesser, voluntary visit.", "The required pilgrimage is <b>hajj</b>."],
  ok=True)
O("The main moral lesson of fasting is that it teaches",
  ["self-control and sympathy for the hungry", "how to lose weight",
   "that food is unimportant", "how to avoid work"],
  ["Fasting is a spiritual discipline, not a diet.",
   "It teaches <b>self-control and sympathy for the hungry</b>, besides dependence on God."],
  ok=True)
O("The Christian season of fasting and self-denial before Easter is called",
  ["Lent", "Advent", "Pentecost", "Epiphany"],
  ["Advent comes before Christmas and Pentecost after Easter.",
   "The season of fasting before Easter is <b>Lent</b>."],
  ok=True)
T("(a) Name the five pillars of Islam. (b) Explain any three of them. "
  "(c) State four moral lessons that a pupil can learn from fasting and almsgiving.",
  ["(a) <b>Shahadah</b> (declaration of faith), <b>salat</b> (five daily prayers), <b>zakat</b> (almsgiving), "
   "<b>sawm</b> (fasting in Ramadan) and <b>hajj</b> (pilgrimage to Mecca).",
   "(b) <b>Shahadah</b> — the sincere declaration that there is no god but Allah and that Muhammad is His messenger; "
   "it is the foundation of being a Muslim. "
   "<b>Zakat</b> — a fixed annual share of one's surplus wealth given to the poor and needy; it purifies wealth and "
   "reduces inequality. "
   "<b>Sawm</b> — abstaining from food, drink and wrongdoing from dawn to sunset throughout Ramadan; it trains "
   "self-control and compassion.",
   "(c) <b>Self-discipline</b> — learning to say no to what one wants, which helps in study and in resisting peer "
   "pressure. <b>Compassion</b> — feeling hunger teaches sympathy for those who are hungry every day. "
   "<b>Generosity</b> — the habit of giving part of what one has, however little. "
   "<b>Humility and dependence on God</b> — recognising that food, wealth and life itself are gifts."],
  marks=12)
extras("obligations",
  plain="The religious duties in this topic all work the same way: they take an abstract virtue and give it a timetable. "
        "Charity becomes zakat with a fixed share; self-control becomes a month of fasting. That is why they form character and not merely opinion.",
  examples=[
    E("How can a pupil who is too young to pay zakat still practise its spirit?",
      "Step 1. The spirit of zakat is that part of what you have belongs to those who have less.",
      "Step 2. She can set aside a small, fixed part of her pocket money each week.",
      "Step 3. Then <b>give it deliberately — to a needy classmate's books, a collection for the sick, or a community clean-up</b>."),
    E("A man fasts all day but quarrels and cheats in the market. What does religious teaching say?",
      "Step 1. Fasting is abstaining from wrongdoing as well as from food.",
      "Step 2. Without the change of conduct, the hunger achieves nothing.",
      "Step 3. So his fast is <b>incomplete — the outward act without the inward discipline</b>.")])

topic("youth", "Religious youth organisations", B, [
  "Youth organisations train young people in faith, character, service and leadership.",
  "<b>Christian</b>: Scripture Union, Youth Fellowship, Boys' and Girls' Brigade, Catholic Youth Organisation, "
  "Methodist and Presbyterian youth guilds, Singing Bands, Student Christian Movement.",
  "<b>Islamic</b>: Muslim Students' Association, Ahlus-Sunnah youth wings, Tijaniyya and Ahmadiyya youth groups, "
  "Islamic study circles (<i>makaranta</i>).",
  "<b>Traditional</b>: Asafo companies, youth wings of festival committees, groups that keep drumming, "
  "dancing and the history of the community alive, and <i>nnoboa</i> work groups.",
  "Benefits: moral and spiritual growth, friendship with people of good character, leadership and public-speaking "
  "skills, talents developed (music, drama, sport), community service, and protection from bad company.",
  "A pupil should choose a group that strengthens, not distracts from, school work and family duties.",
])
O("Which of the following is a Christian youth organisation?",
  ["Scripture Union", "Muslim Students' Association", "Asafo company", "Tijaniyya youth wing"],
  ["The others are Islamic or traditional.", "<b>Scripture Union</b> is a Christian youth organisation."],
  ok=True)
O("The Asafo company in a traditional Ghanaian community is",
  ["a youth group that serves and defends the community", "a group of traders",
   "a church choir", "a political party"],
  ["Historically these were the fighting companies; today they organise communal work and festivals.",
   "It is <b>a youth group that serves and defends the community</b>."],
  ok=True)
O("A major benefit of belonging to a religious youth organisation is that it",
  ["builds character and leadership skills", "guarantees a job after school",
   "excuses a pupil from class", "provides money every week"],
  ["It offers formation, not payment or privilege.",
   "It <b>builds character and leadership skills</b>, and gives good company."],
  ok=True)
O("Before joining a youth group, a pupil should first consider whether it",
  ["will affect his school work and family duties", "has the loudest music",
   "has many rich members", "meets far from home"],
  ["The test is whether the group builds him up.",
   "He should consider whether it <b>will affect his school work and family duties</b>, and whether its teaching is sound."],
  ok=True)
O("Youth organisations help to reduce social vices among young people mainly because they",
  ["give young people good company and useful activity", "punish offenders severely",
   "report members to the police", "keep young people indoors"],
  ["Idleness and bad company are the roots of most youthful vices.",
   "They help by <b>giving young people good company and useful activity</b>."],
  ok=True)
T("(a) Name two religious youth organisations from each of the three religions. "
  "(b) State four activities of religious youth organisations. "
  "(c) Give four benefits a J.H.S. pupil derives from belonging to such an organisation.",
  ["(a) <b>Christian</b>: Scripture Union, Boys'/Girls' Brigade (also Youth Fellowship, Catholic Youth Organisation, "
   "Singing Band). <b>Islamic</b>: Muslim Students' Association, Ahmadiyya or Tijaniyya youth wing (also Islamic study "
   "circles). <b>Traditional</b>: Asafo company, festival or cultural youth group (also nnoboa work groups).",
   "(b) <b>Worship and study</b> — prayer meetings, Bible or Qur'an study, quizzes. "
   "<b>Community service</b> — clean-up exercises, visiting the sick and the aged, helping at funerals and festivals. "
   "<b>Talent development</b> — choir, drama, drumming, dancing, sports and debates. "
   "<b>Training and counselling</b> — leadership training, career and moral guidance, and camps or retreats.",
   "(c) <b>Moral and spiritual growth</b>, which strengthens him against temptation; <b>good friends and role "
   "models</b>, which keeps him from bad company; <b>leadership, organising and speaking skills</b> gained from holding "
   "office; and <b>discovery and development of talents</b> — with the discipline of service to others."],
  marks=12)
extras("youth",
  plain="This topic rewards local knowledge: name the groups that actually exist in your own school and town, and say "
        "what they do. The underlying point is always the same — young people become what their company and their activities make them.",
  examples=[
    E("A pupil's youth meetings run late and his grades are falling. What should he do?",
      "Step 1. Recognise that school work is itself a duty, not a rival to faith.",
      "Step 2. Speak to the group leader and his parents, and agree which meetings he will attend.",
      "Step 3. <b>Keep the commitment that fits his study timetable</b> — a well-run group will respect that, and a group that will not is not helping him."),
    E("Suggest a service project a school religious group could carry out in one term.",
      "Step 1. Choose something real and finishable: for example, repairing and painting the school's benches, or clearing a choked gutter.",
      "Step 2. Plan it — permission, materials, dates, tasks for each member.",
      "Step 3. <b>Do it, then report it at assembly</b>, so that others see service as normal rather than exceptional.")])

topic("rites", "Rites of passage", B, [
  "A rite of passage marks the movement of a person from one stage of life to another, and is observed in all "
  "three religions.",
  "<b>Birth and naming</b>: Christian baptism or christening and thanksgiving; Islamic <i>aqiqah</i> on the seventh "
  "day with the shaving of the head and the naming; traditional outdooring on the eighth day, when the child is "
  "shown the sky and given water and drink to teach truthfulness.",
  "<b>Puberty</b>: traditional rites such as <i>bragoro</i> (Akan) and <i>dipo</i> (Krobo) teach a girl hygiene, "
  "home-making, chastity and the duties of adulthood; confirmation and Islamic instruction classes play a "
  "comparable role.",
  "<b>Marriage</b>: knocking (<i>kokooko</i>), payment of the bride price and the joining of two families in "
  "traditional practice; the Christian wedding in church; the Islamic <i>nikah</i> with <i>mahr</i> and witnesses.",
  "<b>Death</b>: burial and funeral rites, mourning, final funeral rites, and remembrance of the dead. "
  "All three religions teach respect for the dead and comfort for the bereaved.",
  "Values taught: identity and belonging, responsibility, chastity before marriage, respect for elders, "
  "and the support of the community at every stage of life.",
])
O("The Islamic ceremony performed on the seventh day after the birth of a child is",
  ["aqiqah", "nikah", "hajj", "zakat"],
  ["Nikah is marriage and hajj the pilgrimage.",
   "The naming ceremony on the seventh day is <b>aqiqah</b>."],
  ok=True)
O("In traditional outdooring, giving the baby a drop of water and then a drop of drink teaches the child to",
  ["be truthful — to call water water, and drink drink", "enjoy palm wine",
   "grow quickly", "obey only the father"],
  ["The symbolism is moral instruction, not refreshment.",
   "It teaches the child <b>to be truthful — to call water water, and drink drink</b>."],
  ok=True)
O("Dipo is a puberty rite performed among the",
  ["Krobo", "Dagbamba", "Ga", "Nzema"],
  ["Bragoro is the Akan equivalent.", "<b>Dipo</b> is the puberty rite of the Krobo people."],
  ok=True)
O("The traditional ceremony in which a man's family formally asks for a woman's hand in marriage is called",
  ["knocking (kokooko)", "outdooring", "libation", "confirmation"],
  ["It is the first formal step before the marriage.", "It is called <b>knocking (kokooko)</b>."],
  ok=True)
O("One important value taught by puberty rites is",
  ["chastity before marriage", "early marriage for all girls",
   "refusal to go to school", "hatred of other tribes"],
  ["The traditional instruction is moral and practical.",
   "A central value is <b>chastity before marriage</b>, along with hygiene, home-making and respect for elders."],
  ok=True)
T("(a) Name the four main rites of passage. (b) Describe how a child is named in any one of the three religions. "
  "(c) State four values that rites of passage teach, and two ways in which such rites are sometimes abused.",
  ["(a) <b>Birth and naming; puberty; marriage; and death (funeral rites).</b>",
   "(b) <b>Traditional outdooring (Akan)</b>: on the eighth day, before dawn, the family gathers at the father's house. "
   "The child is taken outside and shown the sky, and libation is poured to thank God and the ancestors and to ask for "
   "long life. An elder places a drop of water on the child's tongue, saying 'when it is water, say water', and then a "
   "drop of drink, 'when it is drink, say drink' — teaching truthfulness. The child is then given a name, usually of a "
   "respected relative, and the family and guests present gifts and share a meal. "
   "(An account of Christian baptism/christening or Islamic aqiqah earns the same marks.)",
   "(c) Values: <b>identity and belonging</b> to a family, religion and community; <b>responsibility</b>, as each "
   "stage brings new duties; <b>chastity and self-control</b>, taught at puberty; <b>respect for elders and for the "
   "dead</b>; and the knowledge that <b>the community stands with the individual</b> in joy and grief. "
   "Abuses: <b>extravagant spending</b>, especially on funerals, which impoverishes families; and <b>harmful or "
   "degrading practices</b>, such as forced marriage, female genital mutilation and cruel widowhood rites, which must "
   "be abandoned."],
  marks=12)
extras("rites",
  plain="Rites of passage are the community's way of teaching: a ceremony says in one hour what a lecture could not say "
        "in a week. Learn one naming ceremony well enough to describe it in order, and note the moral meaning of each symbol — that is where the marks are.",
  examples=[
    E("Explain the meaning of two symbolic acts in a naming ceremony.",
      "Step 1. Showing the child the sky presents him to God and to the world, and asks for long life.",
      "Step 2. The water-and-drink test teaches that he must always <b>speak the truth and not confuse one thing with another</b>.",
      "Step 3. Naming him after a respected relative sets before him <b>an example to live up to</b>."),
    E("A family borrows heavily to hold an elaborate funeral. Comment from a moral standpoint.",
      "Step 1. Respect for the dead is a genuine religious duty.",
      "Step 2. But debt that cripples the living — school fees unpaid, farms sold — serves nobody, least of all the deceased.",
      "Step 3. The moral course is <b>a dignified funeral within the family's means</b>, and all three religions in Ghana now urge it.")])
