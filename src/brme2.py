"""BECE Religious and Moral Education - religious leaders and the moral life."""
from core import *
import draw

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}
C, D = "C. Religious leaders", "D. The moral life"

topic("jesus", "Jesus Christ", C, [
  "Christians believe Jesus Christ is the Son of God and the Saviour of the world. "
  "He was born in <b>Bethlehem</b>; his mother was <b>Mary</b> and Joseph, a carpenter, cared for him.",
  "He was baptised by <b>John the Baptist</b> in the River Jordan, was tempted in the wilderness, "
  "and then began to teach, calling <b>twelve disciples</b>.",
  "His teaching: the Sermon on the Mount and the Beatitudes, the parables (the Good Samaritan, the Prodigal Son, "
  "the Sower, the Talents), the two great commandments — love God, and love your neighbour as yourself — "
  "and the Lord's Prayer.",
  "His works: healing the sick, feeding the five thousand, calming the storm, raising the dead, "
  "forgiving sinners and welcoming the poor, children and outcasts.",
  "He was crucified at Calvary, and Christians believe he rose on the third day and ascended into heaven.",
  "Moral lessons from his life: humility, love and compassion, forgiveness, obedience to God, service to others, "
  "courage in standing for truth, and concern for the weak.",
])
O("Jesus Christ was born in",
  ["Bethlehem", "Nazareth", "Jerusalem", "Galilee"],
  ["He grew up in Nazareth and died in Jerusalem.", "He was born in <b>Bethlehem</b>."],
  ok=True)
O("Jesus was baptised by",
  ["John the Baptist", "Peter", "Paul", "Joseph"],
  ["Peter and Paul were later followers; Joseph was his guardian.",
   "He was baptised by <b>John the Baptist</b> in the River Jordan."],
  ok=True)
O("The number of disciples Jesus chose was",
  ["twelve", "seven", "ten", "seventy"],
  ["He later sent out seventy as well, but the inner group was smaller.",
   "He chose <b>twelve</b> disciples."],
  ok=True)
O("The parable of the Good Samaritan teaches Christians to",
  ["help anyone in need, whoever he is", "give money only to relatives",
   "avoid travelling alone", "respect only priests"],
  ["The point of the story is that the despised foreigner proved the true neighbour.",
   "It teaches us to <b>help anyone in need, whoever he is</b>."],
  ok=True)
O("The two greatest commandments according to the teaching of Jesus are to love",
  ["God and your neighbour", "your family and your tribe",
   "your country and your chief", "yourself and your friends"],
  ["He summed up the whole law in two.",
   "They are to love <b>God and your neighbour</b> as yourself."],
  ok=True)
T("(a) Give an account of the birth and early life of Jesus Christ. (b) State four works of Jesus. "
  "(c) Give four moral lessons a pupil can learn from the life of Jesus Christ.",
  ["(a) Jesus was born in <b>Bethlehem</b> of <b>Mary</b>, who was betrothed to <b>Joseph</b> a carpenter. "
   "Christians believe his birth was announced by an angel; shepherds visited him in a manger, and wise men from the "
   "east brought gifts of gold, frankincense and myrrh. To escape Herod the family fled to Egypt, and later settled in "
   "<b>Nazareth</b>, where he grew up and worked as a carpenter. At twelve he was found in the temple discussing with "
   "the teachers, and at about thirty he was baptised by John the Baptist and began his ministry.",
   "(b) Any four: <b>healed the sick</b> — the blind, lepers, the paralysed; <b>fed the five thousand</b> with five "
   "loaves and two fish; <b>calmed a storm</b> on the Sea of Galilee; <b>raised the dead</b>, such as Lazarus; "
   "<b>forgave sinners</b> and welcomed outcasts and children; cast out evil spirits.",
   "(c) <b>Humility</b> — though honoured, he washed his disciples' feet and was born in a stable; "
   "<b>love and compassion</b> — he cared for the sick, the poor and the rejected; "
   "<b>forgiveness</b> — he forgave even those who crucified him, which teaches us to let go of revenge; "
   "<b>obedience to God and courage for the truth</b> — he spoke against hypocrisy and kept to his mission at the cost "
   "of his life. (Service to others and prayerfulness are equally acceptable.)"],
  marks=12)
extras("jesus",
  plain="For R.M.E. you need the facts of Jesus' life in order — birth, baptism, ministry, death and resurrection — and, "
        "just as important, the moral lesson behind each story. Examiners reward 'the parable teaches…' far more than retelling the story at length.",
  examples=[
    E("What moral lesson does the parable of the Prodigal Son teach?",
      "Step 1. The younger son wastes his inheritance and returns home in disgrace.",
      "Step 2. The father welcomes him with joy instead of punishment.",
      "Step 3. The lessons: <b>God forgives the truly repentant, and we should forgive and welcome back those who wrong us</b> — and the elder brother warns us against jealousy."),
    E("A classmate from another tribe is being mocked. Apply the teaching of Jesus.",
      "Step 1. The Good Samaritan shows that a neighbour is anyone in need, not only one's own people.",
      "Step 2. The command is to love your neighbour as yourself.",
      "Step 3. So the pupil should <b>stand with the classmate, speak up, and report the bullying</b> rather than laugh along.")])

topic("muhammad", "Prophet Muhammad", C, [
  "Muslims believe Muhammad is the last of God's prophets. He was born in <b>Mecca</b> about 570 CE. "
  "His father <b>Abdullah</b> died before his birth and his mother <b>Aminah</b> when he was six; he was brought up "
  "by his grandfather Abdul Muttalib and then by his uncle <b>Abu Talib</b>.",
  "As a young man he worked as a shepherd and a trader and became known as <i>Al-Amin</i>, 'the trustworthy'. "
  "He married <b>Khadijah</b>.",
  "At about forty, while meditating in the cave of <b>Hira</b>, he received the first revelation of the Qur'an "
  "through the angel <b>Jibril</b> (Gabriel).",
  "He preached the oneness of Allah, kindness to the poor, orphans and slaves, and honesty in trade. "
  "Persecution in Mecca led to the <b>Hijra</b>, the migration to Medina in <b>622 CE</b>, "
  "from which the Islamic calendar is counted.",
  "In Medina he built the first mosque, made a treaty binding the community together, and later returned to Mecca "
  "in peace. He died in Medina in 632 CE.",
  "Moral lessons: honesty, trustworthiness, patience under persecution, humility, forgiveness of enemies, "
  "kindness to the weak and tolerance of other faiths.",
])
O("Prophet Muhammad was born in",
  ["Mecca", "Medina", "Jerusalem", "Cairo"],
  ["He migrated to Medina later in life.", "He was born in <b>Mecca</b>."],
  ok=True)
O("The angel through whom the Qur'an was revealed to Prophet Muhammad is",
  ["Jibril", "Mikail", "Israfil", "Izrail"],
  ["The other angels have different offices in Islamic teaching.",
   "The revelation came through <b>Jibril</b> (Gabriel)."],
  ok=True)
O("The migration of Prophet Muhammad and his followers from Mecca to Medina is called the",
  ["Hijra", "Hajj", "Umrah", "Jihad"],
  ["Hajj and umrah are pilgrimages.", "The migration is the <b>Hijra</b>, which took place in 622 CE."],
  ok=True)
O("Before he received the call to prophethood, Muhammad was known among his people as Al-Amin, which means",
  ["the trustworthy", "the wealthy", "the strongest", "the scholar"],
  ["The title described his character in business and in daily dealing.",
   "<i>Al-Amin</i> means <b>the trustworthy</b>."],
  ok=True)
O("A chief moral lesson from the life of Prophet Muhammad is",
  ["honesty and patience in the face of difficulty", "the use of force to spread belief",
   "the pursuit of wealth above all", "avoiding the poor"],
  ["His life is remembered for character, not for coercion or riches.",
   "It teaches <b>honesty and patience in the face of difficulty</b>, with kindness to the weak."],
  ok=True)
T("(a) Give an account of the early life of Prophet Muhammad. (b) Describe how he received his first revelation. "
  "(c) Give four moral lessons from his life.",
  ["(a) He was born in <b>Mecca</b> about 570 CE into the Quraysh tribe. His father <b>Abdullah</b> died before he was "
   "born, and his mother <b>Aminah</b> died when he was about six. He was cared for by his grandfather <b>Abdul "
   "Muttalib</b>, and after his death by his uncle <b>Abu Talib</b>. He worked as a shepherd and later as a trader, "
   "earning such a reputation for honesty that he was called <b>Al-Amin</b>, the trustworthy. He married <b>Khadijah</b>, "
   "a widow whose trade he had managed, and was known for settling disputes fairly — he helped place the sacred stone "
   "during the repair of the Ka'bah.",
   "(b) At about the age of forty he often went to meditate in the cave of <b>Hira</b> on Mount Nur, outside Mecca. "
   "There the angel <b>Jibril</b> appeared to him and commanded him to 'Read!' He protested that he could not read, "
   "but the angel repeated the command, and the first verses of the Qur'an were revealed. He returned home trembling, "
   "and Khadijah comforted him and became the first to accept his message.",
   "(c) <b>Honesty and trustworthiness</b> — he was trusted with other people's goods long before he was a prophet; "
   "<b>patience and perseverance</b> — he bore insult, boycott and exile without abandoning his mission; "
   "<b>forgiveness</b> — on returning to Mecca in triumph he pardoned those who had persecuted him; "
   "<b>humility and kindness to the weak</b> — he mended his own sandals, ate with the poor and defended orphans, "
   "widows and slaves."],
  marks=12)
extras("muhammad",
  plain="Keep four facts and four dates straight — Mecca, Hira, the Hijra of 622 to Medina, and his death in 632 — and "
        "then concentrate on character. The reason he was believed in Mecca was that his honesty was already famous.",
  examples=[
    E("Why is the Hijra so important that the Islamic calendar counts from it?",
      "Step 1. In Mecca the believers were a persecuted minority.",
      "Step 2. In Medina they could worship openly and organise themselves as a community under agreed rules.",
      "Step 3. So the Hijra marks <b>the beginning of the Muslim community (ummah)</b>, not merely a journey."),
    E("How can a trader today follow the example of Al-Amin?",
      "Step 1. Use correct weights and measures and state defects in goods honestly.",
      "Step 2. Keep promises about delivery and repayment, even at a loss.",
      "Step 3. The reward is the same as his: <b>a reputation that brings customers, and a clear conscience</b>.")])

topic("tradleaders", "Traditional religious leaders", C, [
  "In African Traditional Religion, worship is led by recognised office-holders: "
  "the <b>traditional priest</b> (<i>okomfo</i>, <i>bosomfo</i>), the <b>chief</b> as custodian of the land "
  "and the stools, the <b>linguist</b> (<i>okyeame</i>), the <b>queen mother</b>, "
  "and the <b>head of the family</b> who pours libation for the household.",
  "Duties of a priest: pouring libation and praying for the community, performing sacrifices, interpreting the will "
  "of the deity, healing with herbs, settling disputes, teaching taboos, and guarding the shrine and the groves.",
  "<b>Okomfo Anokye</b> was the renowned Asante priest who, with Osei Tutu, united the Asante states; "
  "tradition says he brought down the <b>Golden Stool (Sika Dwa Kofi)</b> as the soul of the nation, "
  "and laid down laws that bound the union together.",
  "Qualities expected of traditional leaders: truthfulness, purity, discipline, patience, courage, "
  "impartiality and knowledge of custom and herbs.",
  "Moral lessons: leadership is service; the leader must be morally clean; unity is built on shared symbols and "
  "agreed rules; and knowledge must be used to heal and reconcile, not to exploit people.",
])
O("The Akan word for a traditional priest is",
  ["okomfo", "okyeame", "ohemaa", "odikro"],
  ["<i>Okyeame</i> is the linguist, <i>ohemaa</i> the queen mother and <i>odikro</i> a village chief.",
   "A traditional priest is an <b>okomfo</b>."],
  ok=True)
O("Okomfo Anokye is remembered chiefly for",
  ["helping to unite the Asante states and bringing the Golden Stool",
   "leading the Asante army against the invaders at Feyiase",
   "founding the shrine at Larteh and the Akuapem state",
   "serving as the first Asantehene of the united Asante nation"],
  ["He was a priest and statesman of the seventeenth century.",
   "He is remembered for <b>helping to unite the Asante states and bringing the Golden Stool</b>."],
  ok=True)
O("The Golden Stool of the Asante is regarded as",
  ["the soul of the nation", "the property of one family",
   "an ordinary chair for the chief", "a gift from the British"],
  ["It is never sat upon and is kept with great reverence.",
   "It is regarded as <b>the soul of the Asante nation</b>."],
  ok=True)
O("Which of the following is a duty of a traditional priest?",
  ["Pouring libation and praying for the community", "Collecting income tax",
   "Conducting elections", "Teaching mathematics in school"],
  ["Each office has its own functions.",
   "A priest's duties include <b>pouring libation and praying for the community</b>, offering sacrifice, healing and interpreting the deity's will."],
  ok=True)
O("The okyeame in a traditional court serves as",
  ["the spokesman of the chief", "the chief's bodyguard",
   "the keeper of the treasury", "the leader of the Asafo company"],
  ["Words addressed to a chief pass through him.",
   "The <i>okyeame</i> is <b>the spokesman (linguist) of the chief</b>."],
  ok=True)
T("(a) Name four leaders in African Traditional Religion and state one duty of each. "
  "(b) Give an account of the work of Okomfo Anokye. "
  "(c) State four qualities expected of a traditional religious leader.",
  ["(a) <b>The traditional priest (okomfo)</b> — leads worship at the shrine, prays, offers sacrifice and heals. "
   "<b>The chief</b> — custodian of the land and the stools; he performs rites for the whole state and presides at "
   "festivals. <b>The queen mother (ohemaa)</b> — advises the chief, nominates candidates for the stool and cares for "
   "the moral training of the women and girls. <b>The head of the family (abusuapanin)</b> — pours libation for the "
   "household, keeps the family property and settles family disputes. "
   "(The linguist, okyeame, and the Asafo leader are equally acceptable.)",
   "(b) <b>Okomfo Anokye</b> was a famous priest of the Asante in the seventeenth century, a contemporary and friend "
   "of <b>Osei Tutu</b>. Tradition holds that at a great gathering at Kumasi he brought down from the sky the "
   "<b>Golden Stool (Sika Dwa Kofi)</b>, declaring it the soul of the Asante nation, so that the separate states "
   "accepted one allegiance. He is credited with laying down laws and taboos binding the union, with planting the "
   "sword at Kumasi, where it is still shown today, and with using his skill in herbs and divination for the welfare of the state. His work shows the "
   "use of religion in <b>nation building</b>.",
   "(c) <b>Truthfulness and honesty</b>, since the community relies on his word; <b>moral purity and "
   "self-discipline</b>, including the observance of taboos; <b>patience and impartiality</b> in settling disputes; "
   "and <b>courage with sound knowledge of custom and herbs</b>, so that he can guide and heal rather than deceive."],
  marks=12)
extras("tradleaders",
  plain="Traditional leaders combine the roles that other societies separate: priest, judge, doctor and historian. The "
        "moral point the syllabus draws out is that such authority rests on character — a priest or chief known to be dishonest loses the community's trust at once.",
  examples=[
    E("How does the story of the Golden Stool show the use of religion in nation building?",
      "Step 1. The separate Asante states each had its own stool and loyalty.",
      "Step 2. One sacred object, accepted by all, gave them a shared identity above their separate interests.",
      "Step 3. So religion supplied <b>a symbol of unity that politics alone could not provide</b> — and the union held for centuries."),
    E("A man claiming priestly powers demands large sums to 'remove a curse'. How should the community judge him?",
      "Step 1. Genuine traditional office is held by appointment and training, and is accountable to the elders.",
      "Step 2. Demanding heavy payment for fear-based claims is exploitation, condemned in all three religions.",
      "Step 3. The community should <b>refuse, report him, and consult the recognised elders and health services</b>.")])

topic("leaderlessons", "Moral lessons from religious leaders", C, [
  "The leaders studied in R.M.E. share a pattern: a humble beginning, a call, resistance and suffering, "
  "patient service, and a lasting influence.",
  "<b>Common virtues</b>: obedience to God, honesty, humility, courage, patience, forgiveness, compassion for the "
  "poor and weak, and self-denial.",
  "Other figures the syllabus mentions include Moses (courage and leadership of his people out of slavery), "
  "Abraham/Ibrahim (faith and obedience), Joseph/Yusuf (purity and forgiveness) "
  "and the early Ghanaian religious leaders who built schools, clinics and churches.",
  "Modern application: a prefect, a teacher, a chief or a president is judged by the same virtues — "
  "service rather than self-interest.",
  "The lesson for a pupil is that character is formed in small things: punctuality, honesty in small sums, "
  "keeping a promise, admitting a fault.",
])
O("One virtue common to Jesus Christ, Prophet Muhammad and the great traditional leaders is",
  ["service to others", "love of wealth", "hatred of enemies", "refusal to work"],
  ["All three traditions remember their leaders for what they gave, not what they gained.",
   "The common virtue is <b>service to others</b>."],
  ok=True)
O("The life of Prophet Ibrahim (Abraham) is remembered chiefly as an example of",
  ["faith and obedience to God", "skill in trade", "military strength", "wealth and luxury"],
  ["Both Christians and Muslims honour him for one quality above all.",
   "He is remembered for <b>faith and obedience to God</b>."],
  ok=True)
O("Which of these actions best shows that a school prefect has learnt from the example of religious leaders?",
  ["Serving fairly even when it costs him friends", "Using his position to settle scores",
   "Taking money from juniors", "Giving orders and doing no work himself"],
  ["Leadership modelled on these examples is service, not privilege.",
   "<b>Serving fairly even when it costs him friends</b> shows the lesson has been learnt."],
  ok=True)
O("The suffering endured by religious leaders in the course of their mission teaches us",
  ["patience and perseverance in doing good", "that doing good is useless",
   "to avoid all difficulty", "to keep our beliefs secret"],
  ["Their persistence, not their comfort, is what is remembered.",
   "It teaches <b>patience and perseverance in doing good</b>."],
  ok=True)
O("A pupil builds good character mainly by",
  ["practising honesty and responsibility in small daily matters", "reading about famous people only",
   "waiting until he is an adult", "joining the loudest group in class"],
  ["Character is a habit, and habits are built by repetition.",
   "It is built by <b>practising honesty and responsibility in small daily matters</b>."],
  ok=True)
T("(a) State four virtues common to the religious leaders you have studied. "
  "(b) For each of two leaders, give one incident from his life and the lesson it teaches. "
  "(c) Explain three ways in which a J.H.S. pupil can imitate these leaders in school.",
  ["(a) <b>Obedience to God; honesty and trustworthiness; humility; patience under suffering; forgiveness; "
   "compassion for the poor and weak; courage for the truth; service to others</b> (any four).",
   "(b) <b>Jesus Christ</b> — he washed his disciples' feet at the Last Supper, though he was their master. "
   "Lesson: <b>true greatness lies in humble service</b>. "
   "<b>Prophet Muhammad</b> — when he returned to Mecca in triumph he forgave those who had driven him out. "
   "Lesson: <b>forgiveness is stronger than revenge</b>. "
   "(Okomfo Anokye uniting the Asante states — unity and the use of one's gifts for the common good — is equally acceptable.)",
   "(c) By <b>serving without reward</b> — helping a weaker classmate, cleaning the classroom, carrying out duties as a "
   "prefect fairly; by <b>telling the truth and keeping promises</b>, even when it is costly, as in refusing to help a "
   "friend cheat; and by <b>bearing difficulty patiently</b> — a hard subject, a long walk to school, a family "
   "hardship — without giving up, and by forgiving those who offend him."],
  marks=12)
extras("leaderlessons",
  plain="This topic is the hinge of the syllabus: it turns the history of religious leaders into questions about your own "
        "conduct. In the exam, always end an answer about a leader with 'the lesson for us today is…' — that sentence is often worth the mark.",
  examples=[
    E("Choose one incident from the life of a religious leader and apply it to examination malpractice.",
      "Step 1. Muhammad was called Al-Amin because people could trust him with their property.",
      "Step 2. A candidate who cheats gains a mark but loses that trustworthiness.",
      "Step 3. The lesson: <b>a result obtained dishonestly is worth less than the character it costs</b>."),
    E("Why does R.M.E. study leaders from three different religions together?",
      "Step 1. Ghana is a country of many faiths living side by side.",
      "Step 2. Studying all three builds knowledge and mutual respect instead of suspicion.",
      "Step 3. And the moral virtues they teach <b>largely agree</b>, which gives the nation a common moral language.")])

# ------------------------------------------------------------------ moral life
topic("obedience", "Obedience, discipline & authority", D, [
  "Obedience is doing willingly what a lawful authority requires. Discipline is the self-control that makes "
  "obedience a habit rather than a fear of punishment.",
  "Authorities to be obeyed: God, parents, teachers, prefects, chiefs, the police and the laws of the land.",
  "All three religions command respect for parents and lawful authority: the commandment to honour your father and mother (the Fifth in the numbering used by most churches in Ghana, the Fourth in the Catholic numbering), "
  "the Qur'an's command of kindness to parents, and the traditional duty of respect for elders.",
  "Benefits of obedience and discipline: peace and order at home and school, personal safety, "
  "progress in studies, trust and responsibility, and success in later life.",
  "Obedience is not blind: a pupil must refuse an instruction to steal, cheat, lie or harm another, "
  "and should report it to a trusted adult.",
])
O("Obedience may best be described as",
  ["willingly doing what lawful authority requires", "doing whatever one is told by anybody",
   "acting only out of fear of punishment", "obeying only one's friends"],
  ["The key words are 'willingly' and 'lawful'.",
   "Obedience is <b>willingly doing what lawful authority requires</b>."],
  ok=True)
O("A pupil who is told by an older boy to steal chalk from the office should",
  ["refuse and report the matter", "obey because the boy is older",
   "obey and keep it secret", "do it but return the chalk later"],
  ["Obedience does not extend to wrongdoing.",
   "He should <b>refuse and report the matter</b> to a teacher he trusts."],
  ok=True)
O("Self-discipline is important in a pupil's life because it",
  ["helps him do what is right without being watched", "makes him popular in class",
   "removes the need for teachers", "makes examinations easier to cheat in"],
  ["Discipline is internal, not imposed.",
   "It <b>helps him do what is right without being watched</b> — which is the mark of character."],
  ok=True)
O("Which of the following shows indiscipline in a school?",
  ["Coming late and refusing to do assignments", "Taking part in the school clean-up",
   "Asking a teacher a question", "Helping a weak classmate"],
  ["The other three are good conduct.",
   "<b>Coming late and refusing to do assignments</b> is indiscipline."],
  ok=True)
O("Respect for parents is taught",
  ["in all three religions studied", "in Christianity only",
   "in Islam only", "in African Traditional Religion only"],
  ["Each tradition states it in its own words.",
   "Respect for parents is taught <b>in all three religions studied</b>."],
  ok=True)
T("(a) State four authorities a pupil should obey and one duty owed to each. "
  "(b) Give four benefits of discipline to a pupil. "
  "(c) Explain, with an example, why obedience should not be blind.",
  ["(a) <b>God</b> — worship Him and keep His commands. <b>Parents</b> — respect them, help at home and heed their "
   "advice. <b>Teachers and prefects</b> — attend punctually, do assignments and keep school rules. "
   "<b>The state and its laws</b> — obey traffic laws, respect public property and report crime.",
   "(b) Discipline <b>produces order and peace</b> at home and in school; it <b>improves academic work</b>, since the "
   "disciplined pupil studies regularly without being forced; it <b>earns trust and responsibility</b>, such as "
   "appointment as a prefect; and it <b>protects a pupil from vices</b> — theft, drugs, premarital sex — and so secures "
   "his future.",
   "(c) Obedience is owed to <b>lawful</b> authority and not to wrongdoing. For example, if a senior pupil or even an "
   "adult tells a pupil to carry a parcel he knows contains stolen goods, or to lie to a teacher, he must <b>refuse "
   "and report it</b>. All three religions put obedience to God and conscience above obedience to any human being who "
   "commands evil."],
  marks=12)
extras("obedience",
  plain="Obedience and discipline are the difference between being managed and managing yourself. The second is what the "
        "syllabus is after: a pupil who works when the teacher is absent has learnt it; one who works only when watched has not.",
  examples=[
    E("A prefect tells a pupil to beat a junior for coming late. What should he do?",
      "Step 1. The instruction is unlawful — a pupil has no right to punish another physically.",
      "Step 2. Carrying it out would make him guilty too.",
      "Step 3. He should <b>decline and report it to a teacher</b>, which is both obedient to the school's real rules and morally right."),
    E("Give three habits that show self-discipline in a candidate preparing for the BECE.",
      "Step 1. A fixed study timetable, kept even when friends are playing.",
      "Step 2. Going to bed and rising at set times, and limiting phone use.",
      "Step 3. <b>Doing every assignment honestly and on time</b> — the habit that makes the exam itself unremarkable.")])

topic("honesty", "Honesty, truthfulness & integrity", D, [
  "Honesty is being truthful in word and upright in action; integrity is being the same person in public and "
  "in private.",
  "Forms of dishonesty: lying, stealing, cheating in examinations, false weights and measures, bribery, "
  "forgery, plagiarism and breaking promises.",
  "All three religions condemn dishonesty: the Commandments forbid stealing and false witness; "
  "the Qur'an commands just dealing and honest measure; traditional religion treats theft and perjury as "
  "offences against the ancestors and the whole community.",
  "Benefits of honesty: trust and good reputation, peace of mind, lasting success, promotion and responsibility, "
  "and a community in which business and public life can function.",
  "Consequences of dishonesty: loss of trust and friends, punishment and disgrace, cancellation of results, "
  "imprisonment, and the slow corruption of the whole society.",
])
O("Integrity means",
  ["being the same honest person in public and in private", "being well known in the community",
   "having a good certificate", "having many friends"],
  ["Reputation is what others think; integrity is what one actually is.",
   "Integrity means <b>being the same honest person in public and in private</b>."],
  ok=True)
O("Which of the following is an act of dishonesty?",
  ["Using a false weight to sell goods", "Returning a lost purse",
   "Admitting a mistake", "Paying the correct fare"],
  ["The other three are honest acts.",
   "<b>Using a false weight to sell goods</b> cheats the buyer, and is condemned in all three religions."],
  ok=True)
O("A candidate who takes prepared notes into the examination hall is guilty of",
  ["examination malpractice", "hard work", "good preparation", "self-discipline"],
  ["It is cheating, however much effort went into preparing the notes.",
   "It is <b>examination malpractice</b>, and the penalty is cancellation of the result."],
  ok=True)
O("The greatest reward of honesty is",
  ["trust and peace of mind", "instant wealth",
   "popularity among wrongdoers", "escape from all hardship"],
  ["Honesty does not promise riches or an easy life.",
   "Its reward is <b>trust and peace of mind</b> — and the responsibility that trust brings."],
  ok=True)
O("A pupil finds GH¢200 in the school compound. The honest thing to do is to",
  ["report it to a teacher at once", "share it with his friends",
   "keep it because he found it", "hide it until the term ends"],
  ["Finding is not owning.", "He should <b>report it to a teacher at once</b> so that the owner can be found."],
  ok=True)
T("(a) What is honesty? (b) State four forms of dishonesty common among pupils. "
  "(c) Give four benefits of honesty and two consequences of dishonesty.",
  ["(a) <b>Honesty is the habit of speaking the truth and acting uprightly — not stealing, cheating or deceiving — "
   "even when there is advantage in doing otherwise.</b>",
   "(b) Any four: <b>cheating in tests and examinations</b>; <b>lying to parents and teachers</b> about where one has "
   "been or whether work is done; <b>stealing</b> pens, money, food or school property; <b>copying another's work and "
   "presenting it as one's own</b>; <b>breaking promises</b>; forging a parent's signature or a sick note.",
   "(c) Benefits: <b>trust</b> — people believe you and give you responsibility; <b>peace of mind</b>, since the "
   "honest person has nothing to hide; <b>good reputation</b>, which opens doors to work and help; and <b>real "
   "learning and lasting success</b>, because the honest pupil's results reflect what he actually knows. "
   "Consequences: <b>loss of trust and disgrace</b> — including cancellation of examination results — and <b>punishment "
   "under the law</b>, up to imprisonment, besides the harm done to others and to the nation."],
  marks=12)
extras("honesty",
  plain="Honesty is tested in small amounts long before it is tested in large ones. The pupil who returns the extra "
        "change is practising for the day he handles a public budget — which is exactly how the syllabus links this topic to corruption in Social Studies.",
  examples=[
    E("A friend asks a pupil to sign the attendance register for him while he goes to town. Analyse.",
      "Step 1. Signing for an absent person is forgery, a form of lying in writing.",
      "Step 2. It also helps the friend deceive the school, so the pupil becomes a partner in the wrong.",
      "Step 3. The honest reply is <b>no, with the reason given plainly</b> — and a real friend would not ask twice."),
    E("Why is examination malpractice harmful to the whole country, not only to the candidate?",
      "Step 1. Certificates stop meaning what they claim, so employers cannot trust them.",
      "Step 2. Unqualified people are placed in positions they cannot handle — including clinics and construction.",
      "Step 3. Honest candidates are <b>cheated of places they earned</b>, and public confidence in the whole system falls.")])

topic("chastity", "Chastity, courtship & marriage", D, [
  "Chastity is purity in sexual matters: abstaining from sexual activity before marriage and faithfulness within it.",
  "All three religions teach chastity. Christianity and Islam forbid adultery and fornication; "
  "traditional puberty rites taught girls and boys to keep themselves until marriage, "
  "and pregnancy before the rites was treated as a serious offence.",
  "<b>Courtship</b> is the period of getting to know each other before marriage. It should be open, "
  "known to both families, and free of sexual activity.",
  "Ghanaian law recognises <b>three</b> forms of marriage: <b>customary (traditional)</b>, <b>Islamic</b> and <b>Ordinance</b> \u2014 and a marriage under the Ordinance may be celebrated either in a licensed church or before a registrar. The legal minimum age of marriage is <b>18 years</b>.",
  "Advantages of chastity: it prevents teenage pregnancy, sexually transmitted infections including HIV, "
  "and abortion; it protects education and self-respect; and it builds the self-control on which a faithful "
  "marriage later depends.",
])
O("Chastity in R.M.E. means",
  ["abstaining from sexual activity before marriage", "refusing to marry at all",
   "marrying very early", "living alone"],
  ["It is about purity, not about avoiding marriage.",
   "Chastity means <b>abstaining from sexual activity before marriage</b>, and faithfulness within it."],
  ok=True)
O("The legal minimum age of marriage in Ghana is",
  ["18 years", "16 years", "21 years", "15 years"],
  ["It is set by the <b>Children's Act, 1998 (Act 560)</b>, which also forbids the betrothal of a child.",
   "The minimum age of marriage is <b>18 years</b>."],
  ok=True)
O("The main purpose of courtship is to",
  ["allow the couple and their families to know each other well", "allow the couple to live together",
   "show off to friends", "avoid paying the bride price"],
  ["It is a period of acquaintance before commitment.",
   "Its purpose is to <b>allow the couple and their families to know each other well</b>."],
  ok=True)
O("Which of these is NOT a benefit of chastity to a J.H.S. pupil?",
  ["Popularity among peers who are sexually active", "Protection from teenage pregnancy",
   "Protection from sexually transmitted infections", "Freedom to concentrate on education"],
  ["Chastity may indeed cost some popularity; that is not a benefit of it.",
   "<b>Popularity among peers who are sexually active</b> is not a benefit — the other three are."],
  ok=True)
O("Traditional puberty rites such as bragoro and dipo helped to promote chastity because they",
  ["taught girls to keep themselves until marriage", "arranged marriages for all girls",
   "forbade girls from going to school", "allowed early sexual activity"],
  ["The instruction given was moral and practical.",
   "They <b>taught girls to keep themselves until marriage</b>, and the community honoured those who did."],
  ok=True)
T("(a) What is chastity? (b) State four advantages of chastity to a young person. "
  "(c) Name the forms of marriage in Ghana and state three qualities a person should look for in a marriage partner.",
  ["(a) <b>Chastity is sexual purity — abstaining from sexual intercourse before marriage, and remaining faithful to "
   "one's partner within marriage.</b>",
   "(b) It <b>prevents teenage pregnancy</b>, with its danger to health and its interruption of schooling; it "
   "<b>protects against sexually transmitted infections, including HIV</b>; it <b>preserves self-respect and the "
   "respect of family and community</b>; it <b>leaves a young person free to concentrate on education and training</b>; "
   "and it <b>builds the self-control that makes a faithful marriage possible later</b>.",
   "(c) Forms of marriage: <b>customary (traditional) marriage; Islamic marriage; and marriage under the Ordinance, celebrated either in a licensed church or before a registrar; "
   "and civil marriage at a registrar's office.</b> "
   "Qualities to look for: <b>good character — honesty, kindness and faithfulness</b>; <b>responsibility and "
   "industry</b>, shown in work and in care for family; <b>respect and compatibility</b>, including shared values and "
   "the acceptance of both families; and good health and maturity."],
  marks=12)
extras("chastity",
  plain="This topic is practical rather than theoretical: the syllabus asks you to know what chastity is, why it is "
        "taught by all three religions, and what it protects. The strongest answers name the protections concretely — pregnancy, infection, interrupted education, self-respect.",
  examples=[
    E("A pupil is told that 'everybody is doing it'. How should she reason?",
      "Step 1. The claim is usually untrue, and in any case numbers do not decide right and wrong.",
      "Step 2. The consequences — pregnancy, infection, a stopped education — fall on her, not on those urging her.",
      "Step 3. So the sensible reply is <b>no, firmly and without debate</b>, and the sensible step is to keep different company."),
    E("Why do both religious teaching and Ghanaian law set marriage at 18 and above?",
      "Step 1. Below that age a girl's body and mind are still developing, so pregnancy is dangerous.",
      "Step 2. A child cannot give free and informed consent to a lifelong commitment.",
      "Step 3. Early marriage also <b>ends schooling and locks a family into poverty</b> — which is why both the law and the religions oppose it.")])

topic("familyduties", "The family: roles & responsibilities", D, [
  "The family is the basic unit of society and the first school of character.",
  "<b>Parents' duties</b>: provide food, clothing, shelter, health care and education; love and protect the children; "
  "teach moral and religious values; discipline fairly; and be good examples.",
  "<b>Children's duties</b>: obey and respect parents; help with household work; study hard; "
  "care for younger brothers and sisters; protect the family's name; and support parents in old age.",
  "<b>Duties to the extended family</b>: respect for elders, help at funerals and festivals, "
  "support for needy relatives and care of family property.",
  "Causes of broken homes: infidelity, irresponsibility, poverty, alcohol and drug abuse, "
  "interference from relatives, and lack of communication. Effects fall hardest on children — "
  "dropping out of school, street life and emotional harm.",
  "A good home is built on love, communication, faithfulness, responsible parenthood, "
  "family prayer and shared work.",
])
O("Which of the following is a duty of children in the home?",
  ["Helping with household work", "Paying the rent",
   "Choosing the family's house", "Paying their own school fees"],
  ["The others are the responsibility of parents.",
   "Children should <b>help with household work</b>, obey their parents and study hard."],
  ok=True)
O("The first and most important school of character for a child is the",
  ["family", "church or mosque", "junior high school", "peer group"],
  ["Formation begins long before a child reaches any other institution.",
   "The first school of character is the <b>family</b>."],
  ok=True)
O("A major cause of broken homes in Ghana is",
  ["infidelity and irresponsibility of partners", "regular family prayer",
   "good communication", "shared household duties"],
  ["The last three strengthen a home.",
   "<b>Infidelity and irresponsibility of partners</b> is a major cause of broken homes."],
  ok=True)
O("The group most affected when a home breaks down is the",
  ["children", "grandparents", "neighbours", "landlord"],
  ["All may be affected, but one group has no choice and no resources.",
   "The <b>children</b> suffer most — in schooling, in security and emotionally."],
  ok=True)
O("Responsible parenthood means",
  ["having only the number of children one can properly care for", "having as many children as possible",
   "leaving the children with relatives", "having no children at all"],
  ["The emphasis is on the care given, not the number alone.",
   "It means <b>having only the number of children one can properly care for</b>, and caring for them well."],
  ok=True)
T("(a) State four duties of parents towards their children and four duties of children towards their parents. "
  "(b) Give three causes and three effects of broken homes. "
  "(c) Suggest three ways of building a happy home.",
  ["(a) <b>Parents</b>: provide food, clothing, shelter and health care; pay for and support education; teach moral "
   "and religious values and discipline fairly; love, protect and set a good example. "
   "<b>Children</b>: obey and respect their parents; help with household chores; study hard and behave well; "
   "care for younger siblings and for parents in old age, and protect the family's good name.",
   "(b) Causes: <b>infidelity</b>; <b>irresponsibility and neglect</b>, often with alcohol or drug abuse; "
   "<b>poverty and quarrels over money</b>; interference by relatives; poor communication. "
   "Effects: <b>children drop out of school</b> or perform poorly; <b>children may take to the streets, crime or early "
   "sexual activity</b>; <b>emotional damage</b> — insecurity, bitterness and loss of trust — besides poverty for the "
   "parent left with the children.",
   "(c) <b>Faithfulness and good communication between the parents</b>, settling differences by discussion rather than "
   "quarrelling before the children. <b>Shared responsibility</b> — both parents providing, and all members doing "
   "household work. <b>Family prayer, shared meals and recreation</b>, with fair and loving discipline, so that "
   "children feel secure and valued."],
  marks=12)
extras("familyduties",
  plain="Nearly every social problem in the R.M.E. and Social Studies syllabus — street children, drug abuse, teenage "
        "pregnancy, indiscipline — is traced in part to the home. That is why this topic asks for duties on both sides: a home works when parents and children each do theirs.",
  examples=[
    E("A pupil is the eldest of five and is often kept from school to mind the younger ones. Discuss.",
      "Step 1. Caring for siblings is a genuine family duty.",
      "Step 2. But education is both her right and the family's long-term escape from poverty.",
      "Step 3. The balance is <b>chores outside school hours, and help sought from relatives or social welfare</b> — no duty is served by keeping her out of school."),
    E("Suggest three practical habits that would improve communication in a home.",
      "Step 1. One shared meal a day with no phones, where each person speaks.",
      "Step 2. A weekly family meeting to settle plans, money and complaints before they grow.",
      "Step 3. <b>Parents who listen without immediately punishing</b>, so that children bring problems home instead of hiding them.")])

topic("work", "Work, vocation & attitudes to work", D, [
  "Work is any useful activity, physical or mental, done to earn a living or serve others. "
  "All three religions teach the dignity of honest work.",
  "<b>Christianity</b>: 'if anyone will not work, let him not eat'; Jesus himself worked as a carpenter. "
  "<b>Islam</b>: the Prophet traded and taught that the best earnings are those of one's own hands. "
  "<b>Traditional religion</b>: laziness is despised; communal labour (<i>nnoboa</i>) is honoured.",
  "Good attitudes: punctuality, diligence, honesty, co-operation, neatness, obedience to instructions, "
  "care of tools and property, and pride in a job well done.",
  "Bad attitudes: lateness, laziness, absenteeism, lateness to return from break, stealing from one's employer, "
  "dishonest sick notes, and contempt for manual work.",
  "Benefits of work: income and self-reliance, self-respect, development of talent, service to the community "
  "and national development. The dignity of labour means every honest job deserves respect.",
])
O("The expression 'dignity of labour' means that",
  ["every honest work deserves respect", "only office work is respectable",
   "manual work is for the uneducated", "work should be avoided when possible"],
  ["It is a direct rejection of contempt for manual work.",
   "It means <b>every honest work deserves respect</b>."],
  ok=True)
O("Which of the following is a good attitude to work?",
  ["Punctuality and diligence", "Reporting late and leaving early",
   "Using the employer's materials for private jobs", "Pretending to be sick"],
  ["The others are forms of dishonesty at work.",
   "<b>Punctuality and diligence</b> is the good attitude."],
  ok=True)
O("Prophet Muhammad is reported to have taught that the best earnings are those",
  ["of a person's own hands", "received as gifts",
   "won by gambling", "inherited from relatives"],
  ["Islam places a high value on productive labour.",
   "The best earnings are those <b>of a person's own hands</b>."],
  ok=True)
O("A worker who steals his employer's materials is guilty of",
  ["dishonesty at work", "hard work", "co-operation", "resourcefulness"],
  ["Theft from an employer is theft.", "He is guilty of <b>dishonesty at work</b>."],
  ok=True)
O("The main reason why pupils should respect vocational and technical work is that it",
  ["provides useful skills and honest income", "is easier than other work",
   "requires no training", "is only for school drop-outs"],
  ["Such work requires real training and is in high demand.",
   "It deserves respect because it <b>provides useful skills and honest income</b>."],
  ok=True)
T("(a) What is work? (b) State four good attitudes and four bad attitudes to work. "
  "(c) Give four benefits of work to the individual and the nation.",
  ["(a) <b>Work is any useful physical or mental activity undertaken to earn a living, to produce goods or services, "
   "or to serve others.</b>",
   "(b) Good: <b>punctuality and regular attendance</b>; <b>diligence and thoroughness</b>; <b>honesty</b> with money, "
   "materials and time; <b>co-operation with others and obedience to lawful instructions</b>; care of tools and neatness. "
   "Bad: <b>lateness and absenteeism</b>; <b>laziness and idling during working hours</b>; <b>stealing the employer's "
   "money, materials or time</b>; <b>contempt for manual work</b>; carelessness with tools and quarrelling with colleagues.",
   "(c) To the individual: <b>income for food, shelter and school fees</b>, and so self-reliance; <b>self-respect and "
   "the respect of others</b>; <b>development of talents and skills</b>. "
   "To the nation: <b>production of goods and services</b>, which raises national wealth, taxes and employment, and "
   "reduces poverty, crime and dependence on imports."],
  marks=12)
extras("work",
  plain="The syllabus insists on the dignity of labour because Ghana loses too much to the idea that only desk work is "
        "respectable. The mason, the seamstress and the farmer carry the economy — and the religions studied here all put honest manual work above idle dependence.",
  examples=[
    E("A J.H.S. graduate is offered an apprenticeship with a welder but wants only an office job. Advise him.",
      "Step 1. Office jobs are few and usually require further qualifications he does not yet have.",
      "Step 2. A trade gives him income, skills and the possibility of his own workshop within a few years.",
      "Step 3. He can <b>learn the trade and continue his education part-time</b> — the two are not opposites."),
    E("Name three ways a pupil can practise good work attitudes before leaving school.",
      "Step 1. Be punctual and present every day, and submit assignments on time.",
      "Step 2. Do assigned duties — cleaning, farming, fetching — thoroughly rather than carelessly.",
      "Step 3. <b>Look after school tools and property as if they were his own</b>, which is exactly what an employer will later expect.")])

topic("substance", "Substance abuse", D, [
  "Substance abuse is the wrong or excessive use of drugs and other substances — "
  "alcohol, tobacco, marijuana (<i>wee</i>), cocaine, heroin, tramadol and other medicines taken without "
  "prescription, and inhalants such as glue and petrol fumes.",
  "Causes: peer pressure, curiosity, idleness, desire to escape problems, imitation of musicians and films, "
  "easy availability, broken homes and poverty.",
  "Effects on health: damage to the brain, liver, lungs and heart; mental illness; addiction; accidents; "
  "and death from overdose.",
  "Effects on life: poor school performance and drop-out, loss of money, theft and crime, violence and broken "
  "relationships, unemployment, and disgrace to the family.",
  "All three religions forbid intoxication and the destruction of the body, which is regarded as God's gift.",
  "Prevention: refuse firmly, choose good friends, keep busy with sport, clubs and study, "
  "take no medicine without prescription, seek counselling, and report pushers. "
  "Help is available at clinics, from the Mental Health Authority and from counsellors.",
])
O("Substance abuse means",
  ["the wrong or excessive use of drugs and similar substances", "taking medicine prescribed by a doctor",
   "selling medicine in a pharmacy", "refusing to take any medicine"],
  ["Prescribed use is not abuse.",
   "Substance abuse is <b>the wrong or excessive use of drugs and similar substances</b>."],
  ok=True)
O("The commonest reason why young people begin to abuse drugs is",
  ["peer pressure", "the advice of doctors", "school assignments", "religious teaching"],
  ["Doctors and religious teaching warn against it.",
   "The commonest reason is <b>peer pressure</b>, together with curiosity and idleness."],
  ok=True)
O("Which of these is a health effect of long-term alcohol abuse?",
  ["Damage to the liver", "Improved eyesight", "Stronger bones", "Better memory"],
  ["Alcohol harms rather than helps the body.",
   "Long-term abuse causes <b>damage to the liver</b>, as well as to the brain, heart and stomach."],
  ok=True)
O("Taking tramadol or other medicines without a doctor's prescription is dangerous because it",
  ["can cause addiction and organ damage", "is always cheaper",
   "cures every illness", "improves sporting ability permanently"],
  ["Self-medication with such drugs is one of Ghana's growing problems.",
   "It <b>can cause addiction and organ damage</b>, and overdose can kill."],
  ok=True)
O("The best thing a pupil can do when offered a drug by a friend is to",
  ["refuse firmly and tell a trusted adult", "take a little to be polite",
   "keep it for another day", "sell it to someone else"],
  ["Any of the other actions draws him into the trade or the habit.",
   "He should <b>refuse firmly and tell a trusted adult</b>."],
  ok=True)
T("(a) What is substance abuse? Name four substances commonly abused in Ghana. "
  "(b) Give three causes of substance abuse among the youth. "
  "(c) State four effects of substance abuse and three ways of preventing it.",
  ["(a) <b>Substance abuse is the use of drugs or other substances in the wrong way, in the wrong quantity, or without "
   "medical prescription, so that they harm the user.</b> Commonly abused: <b>alcohol, tobacco, marijuana (wee), "
   "tramadol and other unprescribed medicines, cocaine, heroin, and inhalants such as glue or petrol fumes.</b>",
   "(b) <b>Peer pressure</b> — the desire to be accepted by friends who use them; <b>curiosity and imitation</b> of "
   "musicians, films and older youths; <b>idleness and lack of guidance</b>, often in broken homes; and the wish to "
   "escape poverty, examination stress or family problems.",
   "(c) Effects: <b>damage to health</b> — brain, liver, lungs, mental illness and addiction; <b>poor school work and "
   "drop-out</b>; <b>crime and violence</b>, as the addict steals to buy more; <b>loss of money, employment and "
   "reputation</b>, and disgrace to the family; accidents and premature death. "
   "Prevention: <b>learn to refuse firmly and choose good friends</b>; <b>keep busy with study, sport, clubs and "
   "religious activity</b>; <b>take no medicine without prescription and report pushers</b>; and <b>seek counselling "
   "early</b> at a clinic or from a counsellor if already involved."],
  marks=12)
extras("substance",
  plain="This is a topic where the exam answer and real life coincide exactly. Learn the chain — peer pressure, "
        "curiosity, idleness → use → addiction → health, school and family collapse — and note that the whole chain is broken most easily at the first link, by refusing.",
  examples=[
    E("A pupil's older brother smokes wee and tells him it is harmless because he is still healthy.",
      "Step 1. Damage from such drugs builds up over years and is often hidden at first.",
      "Step 2. Marijuana use in adolescence is linked to poor concentration, school failure and mental illness.",
      "Step 3. A healthy-looking user proves nothing — <b>the risk is to the pupil's own brain, at the very age when it is developing</b>."),
    E("Write three sentences a pupil can actually use to refuse an offer of alcohol.",
      "Step 1. 'No thanks, I don't drink.' — short, final, no argument.",
      "Step 2. 'I'm in training / I have an exam tomorrow.' — a reason that ends the discussion.",
      "Step 3. <b>'I'm going now — see you tomorrow.'</b> Leaving is always available, and it works.")])

topic("manners", "Courtesy, decency & good manners", D, [
  "Courtesy is polite and considerate behaviour towards others; it costs nothing and earns much.",
  "Marks of good manners: greeting elders and visitors, saying please, thank you and sorry, "
  "giving up a seat, not interrupting, table manners, respect for other people's property and privacy, "
  "and courtesy on the road and in public transport.",
  "Traditional courtesy in Ghana: greeting with the right hand, removing a hat and lowering the voice before "
  "an elder, not receiving things with the left hand, and announcing oneself before entering a room.",
  "<b>Decency in dressing</b> means dressing neatly and modestly, suitably for the occasion \u2014 "
  "school, worship, funeral, work or play. Dressing suitably shows self-respect and respect for the occasion. "
  "Note carefully: harassment is always the fault of the person who harasses, never of what anyone is wearing.",
  "Hygiene is part of decency: bathing daily, clean clothes, trimmed nails and hair, brushing the teeth, "
  "and clean surroundings.",
  "Good manners bring friendship, respect, goodwill and opportunities; bad manners close doors that ability alone "
  "cannot open.",
])
O("Courtesy may best be described as",
  ["polite and considerate behaviour towards others", "speaking only when spoken to",
   "expensive dressing", "keeping to oneself"],
  ["It is about consideration, not silence or expense.",
   "Courtesy is <b>polite and considerate behaviour towards others</b>."],
  ok=True)
O("Which of the following shows good manners in a crowded bus?",
  ["Offering your seat to a pregnant woman", "Playing loud music on your phone",
   "Putting your bag on an empty seat", "Pushing to the front to get off"],
  ["The others inconvenience everybody else.",
   "<b>Offering your seat to a pregnant woman</b> shows consideration."],
  ok=True)
O("Decency in dressing means dressing",
  ["neatly and modestly, suitably for the occasion", "in the most expensive clothes available",
   "exactly like one's favourite musician", "in the same clothes every day"],
  ["It is about suitability and modesty, not cost or imitation.",
   "It means dressing <b>neatly and modestly, suitably for the occasion</b>."],
  ok=True)
O("In many Ghanaian cultures, it is regarded as discourteous to",
  ["give or receive things with the left hand", "greet an elder first",
   "remove your hat before an elder", "lower your voice before an elder"],
  ["The other three are marks of respect.",
   "It is discourteous <b>to give or receive things with the left hand</b>."],
  ok=True)
O("Good manners are important to a pupil chiefly because they",
  ["earn him respect, friendship and opportunities", "make him feared",
   "replace the need to study", "allow him to break rules politely"],
  ["Manners complement ability; they do not replace it.",
   "They <b>earn him respect, friendship and opportunities</b> throughout life."],
  ok=True)
T("(a) State six marks of good manners in a J.H.S. pupil. (b) Explain what is meant by decency in dressing and give "
  "three reasons why it matters. (c) Give three benefits of courtesy in later life.",
  ["(a) Any six: <b>greeting elders, teachers and visitors</b>; <b>saying please, thank you and sorry</b>; "
   "<b>not interrupting when others are speaking</b>; <b>giving up a seat to an elder, a pregnant woman or a "
   "physically challenged person</b>; <b>good table manners</b> — washing hands, eating quietly, not talking with a "
   "full mouth; <b>respect for other people's property and privacy</b>, including knocking before entering; "
   "punctuality and apologising for lateness; keeping quiet in class, church, mosque and hospital.",
   "(b) <b>Decency in dressing means wearing clean, neat and modest clothing that is appropriate to the occasion and "
   "does not expose the body.</b> It matters because: it <b>shows self-respect and earns the respect of others</b>; it "
   "<b>shows respect for the occasion and for the people present</b>; and it <b>creates the right impression</b> "
   "at school, at worship, at a funeral and especially at an interview, where a first impression may decide the outcome.",
   "(c) Courtesy <b>wins goodwill and friendship</b>, so people are willing to help you; it <b>opens opportunities</b> "
   "— employers, customers and colleagues prefer to deal with pleasant, respectful people; and it <b>reduces conflict</b>, "
   "since a courteous person settles disagreements without quarrelling, and so keeps peace at home and at work."],
  marks=12)
extras("manners",
  plain="Manners are the small change of moral life: hundreds of tiny transactions a day that decide how people treat "
        "you. Ability gets you the interview, but courtesy often decides what happens in the room — which is why the syllabus takes it seriously.",
  examples=[
    E("A pupil is going for an interview for an apprenticeship. List four courtesies that will help him.",
      "Step 1. Arrive early, neatly and modestly dressed, hair trimmed and shoes clean.",
      "Step 2. Greet everyone he meets, including the watchman and the receptionist.",
      "Step 3. <b>Listen without interrupting, answer respectfully, and thank them before leaving</b> — all free, and all noticed."),
    E("How would you correct a friend who keeps shouting across the room at a teacher?",
      "Step 1. Not by shouting back or embarrassing him in front of others.",
      "Step 2. Speak to him privately, pointing out how it looks and what it costs him.",
      "Step 3. Suggest the alternative: <b>go up, greet, and speak at a normal volume</b> — and model it yourself.")])

topic("rules", "Rules, regulations & their importance", D, [
  "Rules and regulations are agreed statements of what may and may not be done in a given place.",
  "Sources: the family, the school, the religious body, the community and traditional authority, "
  "and the laws of the state.",
  "Importance: they bring order and peace, protect life and property, ensure fairness, protect the weak, "
  "make work possible, and train self-discipline.",
  "Consequences of breaking rules: punishment, loss of privileges, suspension or dismissal, "
  "arrest and prosecution, injury and loss of life, and disorder in the community.",
  "Rules must be known, reasonable, fairly applied and consistently enforced. Where a rule is unjust, "
  "the right course is to complain through the proper channel, not to break it violently.",
])
O("Rules and regulations are made chiefly to",
  ["bring order and protect everybody", "punish pupils",
   "make life difficult", "favour the leaders"],
  ["Punishment is a consequence, not the purpose.",
   "Rules exist to <b>bring order and protect everybody</b>."],
  ok=True)
O("Which of the following is an effect of lawlessness in a community?",
  ["Insecurity and destruction of property", "Peace and development",
   "Increase in investment", "Respect for the weak"],
  ["The others follow from order, not from its absence.",
   "Lawlessness brings <b>insecurity and destruction of property</b>."],
  ok=True)
O("A pupil who believes a school rule is unfair should",
  ["raise it through the prefects or a teacher", "break it to show his disagreement",
   "organise a strike at once", "ignore it quietly"],
  ["Breaking rules to protest usually costs the pupil, not the rule.",
   "He should <b>raise it through the prefects or a teacher</b> — the proper channel."],
  ok=True)
O("Traffic regulations are important mainly because they",
  ["save lives and prevent accidents", "increase government revenue",
   "slow down every journey", "give work to the police"],
  ["Revenue and police work are side effects.",
   "They <b>save lives and prevent accidents</b>."],
  ok=True)
O("For a rule to be effective it must be",
  ["known, reasonable and fairly enforced", "secret", "changed every week", "applied only to juniors"],
  ["A rule nobody knows, or that is applied selectively, soon collapses.",
   "It must be <b>known, reasonable and fairly enforced</b>."],
  ok=True)
T("(a) State four sources of rules and regulations in the life of a pupil. "
  "(b) Give four reasons why rules and regulations are necessary. "
  "(c) State four consequences of breaking rules, and explain what a pupil should do about a rule he considers unjust.",
  ["(a) <b>The family</b> (house rules); <b>the school</b> (school rules and regulations); <b>the religious body</b> "
   "(its code of conduct); <b>the community and traditional authority</b> (customs, taboos and by-laws); and "
   "<b>the state</b> (the laws of Ghana).",
   "(b) They <b>bring order and peace</b>, so that people can live and work together; they <b>protect life and "
   "property</b> — traffic rules, safety rules, laws against theft; they <b>ensure fairness</b>, so that the strong do "
   "not simply take what they want; and they <b>train self-discipline</b>, which the pupil carries into adult life. "
   "(They also make planning and development possible.)",
   "(c) Consequences: <b>punishment and loss of privileges</b>; <b>suspension or dismissal</b> from school or work; "
   "<b>arrest, prosecution and imprisonment</b> where a law is broken; <b>injury or loss of life</b>, as in a traffic "
   "offence; and <b>disorder and loss of trust</b> in the community. "
   "On an unjust rule: he should <b>use the proper channels</b> — speak to the prefects, the class teacher, the "
   "guidance counsellor or the student representative, and let a case be made for review — rather than breaking it, "
   "which merely transfers attention from the rule to his own conduct."],
  marks=12)
extras("rules",
  plain="Rules are easiest to respect when you can see what they are protecting. A rule about running in the corridor is "
        "about broken teeth; a rule about lateness is about the lesson everybody else is losing. Examiners want that kind of reason, not just 'to prevent disorder'.",
  examples=[
    E("Give the protective purpose behind three common school rules.",
      "Step 1. 'No fighting' — protects bodies, and keeps small disputes from becoming injuries.",
      "Step 2. 'Be in class by 7:30' — protects everybody's lesson time, including the latecomer's own.",
      "Step 3. 'No phones in class' — <b>protects attention, which is the one thing a lesson needs</b>."),
    E("Pupils are unhappy that a new rule bans all food in the dormitory. Outline the proper response.",
      "Step 1. Find out the reason for the rule — probably pests, ants or stolen food.",
      "Step 2. Through the prefects, propose an alternative that meets that concern: a locked food store with set opening times.",
      "Step 3. <b>Present it respectfully in writing to the housemaster</b>. A reasoned proposal is far more likely to change a rule than a boycott.")])

topic("service", "Commitment, perseverance & service", D, [
  "<b>Commitment</b> is giving oneself fully to a duty, a person or a cause. "
  "<b>Perseverance</b> is continuing in it despite difficulty.",
  "Religious examples: the prophets who continued to preach under persecution; "
  "Jesus who went to the cross; traditional leaders who served their people for life.",
  "Service to God: worship, obedience, teaching, giving, caring for the needy. "
  "Service to the nation: honest work, paying taxes, voting, national service, keeping the environment clean, "
  "defending the country, and refusing to give or take bribes.",
  "Marks of commitment in a pupil: regular attendance, completing assignments, keeping to the training schedule, "
  "staying with a club or choir to the end of the year, and keeping promises.",
  "Rewards: achievement and skill, trust and promotion, self-respect, the gratitude of others, "
  "and the knowledge of having done one's duty.",
])
O("Perseverance means",
  ["continuing in a task despite difficulty", "starting many tasks at once",
   "finishing a task quickly", "leaving a task to others"],
  ["It is about staying with it.", "Perseverance is <b>continuing in a task despite difficulty</b>."],
  ok=True)
O("Which of the following shows commitment in a pupil?",
  ["Attending class and completing assignments regularly", "Joining a club and never returning",
   "Promising to help and then forgetting", "Studying only before examinations"],
  ["The other three show the lack of it.",
   "<b>Attending class and completing assignments regularly</b> shows commitment."],
  ok=True)
O("National service to one's country is best shown by",
  ["working honestly and paying one's taxes", "shouting at political rallies",
   "criticising every leader", "avoiding all public duty"],
  ["Service is practical.",
   "It is shown by <b>working honestly and paying one's taxes</b> — and by voting, keeping the law and caring for the environment."],
  ok=True)
O("The lives of the prophets teach us that service to God often requires",
  ["patience and willingness to suffer", "wealth and comfort",
   "political power", "the support of everybody"],
  ["Few of them were rich, powerful or popular.",
   "Their lives teach <b>patience and willingness to suffer</b> for what is right."],
  ok=True)
O("A pupil who abandons every activity he starts is likely to",
  ["achieve little and lose the trust of others", "be admired for trying many things",
   "become an expert quickly", "be given more responsibility"],
  ["Achievement comes from finishing, not from starting.",
   "He will <b>achieve little and lose the trust of others</b>."],
  ok=True)
T("(a) Explain the terms commitment and perseverance. (b) Give three examples of commitment from the lives of "
  "religious leaders. (c) State four ways in which a pupil can serve God and his country, "
  "and three rewards of perseverance.",
  ["(a) <b>Commitment</b> is the act of binding oneself to a duty, person or cause and giving it one's full effort "
   "and loyalty. <b>Perseverance</b> is the steady continuation of that effort in spite of difficulty, delay, "
   "discouragement or opposition.",
   "(b) <b>Prophet Muhammad</b> continued to preach in Mecca through years of insult, boycott and threat, and finally "
   "migrated rather than abandon his message. <b>Jesus Christ</b> kept to his mission knowing it would cost his life, "
   "and prayed for his enemies from the cross. <b>Okomfo Anokye and other traditional leaders</b> gave their whole "
   "lives to the service of their states. (Moses leading his people out of slavery through forty years of wandering is "
   "equally acceptable.)",
   "(c) Service: <b>worship God sincerely and obey His commands</b>; <b>study hard and develop his talents</b>, since "
   "what he becomes is what he will have to give; <b>serve in school and community</b> — as a prefect, in the choir, "
   "in clean-up campaigns, helping the aged and the sick; and <b>live honestly, respect the law and care for the "
   "environment and public property</b>. "
   "Rewards: <b>achievement and mastery of a skill</b>; <b>trust, respect and responsibility</b> given by others; "
   "and <b>self-respect and peace of mind</b>, besides the lasting good done to others."],
  marks=12)
extras("service",
  plain="This last topic draws the whole syllabus together: belief in God, respect for creation, honesty, work and "
        "service all meet in the question 'what will you actually do?'. The examiner is looking for concrete answers — a duty you keep, a club you stay in, a promise you honour.",
  examples=[
    E("A pupil joins the school's sanitation club in September. Describe what commitment would look like by July.",
      "Step 1. He attends the weekly clean-up all year, not only when teachers are watching.",
      "Step 2. He takes a specific responsibility — the bins, or the notice board — and keeps it.",
      "Step 3. By July <b>the club's work is visible and other pupils have joined because of his example</b>. That is service, and it will appear on no certificate."),
    E("How does perseverance apply to a pupil who has failed a mock examination badly?",
      "Step 1. Treat the result as information, not a verdict: identify exactly which topics failed.",
      "Step 2. Make a revision plan for those topics and get help from the teacher or a classmate.",
      "Step 3. <b>Keep to the plan for the weeks remaining</b> — most candidates who improve sharply do so this way, not by luck.")])
