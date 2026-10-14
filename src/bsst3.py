"""BECE Social Studies - Section C: Social and economic development."""
from core import *
import draw

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}
C = "C. Social & economic development"

topic("nationalism", "Nationalism & national identity", C, [
  "Nationalism is the love of and loyalty to one's country, and the desire to see it free, united and developed.",
  "Ghana (then the Gold Coast) gained independence on <b>6 March 1957</b>, the first country in sub-Saharan Africa "
  "to do so, and became a <b>Republic on 1 July 1960</b>. Dr Kwame Nkrumah led the independence struggle.",
  "National symbols: the <b>flag</b> — red for the blood of those who fought, gold for the mineral wealth, "
  "green for the forests and farms, and the <b>black star</b> for African freedom; "
  "the <b>coat of arms</b>; the <b>national anthem</b>; the national pledge; and the motto "
  "<b>Freedom and Justice</b>.",
  "Ways of showing patriotism: obeying the law, paying taxes, protecting public property, working hard, "
  "buying made-in-Ghana goods, respecting the symbols, and keeping the country clean and peaceful.",
  "National unity is built by the use of English as the official language, national service, boarding and "
  "co-educational schools, inter-regional sports and festivals, and fair development across all regions.",
])
O("Ghana attained independence on",
  ["6 March 1957", "1 July 1960", "7 January 1993", "4 June 1979"],
  ["1 July 1960 is Republic Day and 7 January 1993 the start of the Fourth Republic.",
   "Independence Day is <b>6 March 1957</b>."],
  ok=True)
O("In the national flag of Ghana, the gold (yellow) colour stands for",
  ["the mineral wealth of the country", "the blood of those who died",
   "the forests and farmland", "the freedom of Africa"],
  ["Red stands for the blood shed, green for the forests and the black star for African freedom.",
   "Gold stands for <b>the mineral wealth of the country</b>."],
  ok=True)
O("The black star in the middle of the national flag represents",
  ["the freedom of Africa", "the gold mines", "the Volta Lake", "the forests of Ghana"],
  ["Ghana took the lead in the struggle against colonial rule.",
   "The black star represents <b>the freedom of Africa</b> — which is why the national team is called the Black Stars."],
  ok=True)
O("Which of the following best shows patriotism in a pupil?",
  ["Taking care of school property", "Refusing to sing the anthem",
   "Writing on the walls of the classroom", "Buying only imported goods"],
  ["Patriotism shows in everyday behaviour, not in words.",
   "<b>Taking care of school property</b> protects what the whole nation paid for."],
  ok=True)
O("Ghana became a Republic on",
  ["1 July 1960", "6 March 1957", "24 February 1966", "31 December 1981"],
  ["Independence came in 1957, but the country still had the British monarch as head of state.",
   "Ghana became a Republic, with its own head of state, on <b>1 July 1960</b>."],
  ok=True)
T("(a) What is nationalism? (b) Name four national symbols of Ghana and state what each stands for. "
  "(c) Give four ways in which the youth of Ghana can show patriotism.",
  ["(a) <b>Nationalism is the deep love of and loyalty to one's own country, shown in the desire to see it free, "
   "united, respected and developed.</b>",
   "(b) <b>The national flag</b> — red for the blood of those who died in the struggle, gold for the mineral wealth, "
   "green for the forests and farms, and the black star for African freedom. "
   "<b>The coat of arms</b> — the authority of the state, carrying the motto Freedom and Justice. "
   "<b>The national anthem</b> — a prayer and pledge for the nation. "
   "<b>The national pledge</b> — a personal promise of loyal and dedicated service to Ghana. "
   "(The mace, the presidential seal and the Independence Arch are also acceptable.)",
   "(c) Any four, explained: <b>obeying the laws of the land</b>; <b>protecting public property</b> such as school "
   "buildings, street lights and water pipes; <b>working and studying hard</b> so as to contribute skills to the "
   "country; <b>buying and using made-in-Ghana goods</b>, which creates jobs at home; <b>keeping the environment "
   "clean</b>; <b>respecting the national symbols</b> and living peacefully with people of every tribe and religion."],
  marks=12)
extras("nationalism",
  plain="Patriotism is not shouting at a football match; it is the quiet habit of looking after what belongs to everybody. "
        "Learn the four flag colours with their meanings and the two dates — 6 March 1957 and 1 July 1960 — and a good share of this topic's marks are secured.",
  examples=[
    E("Why is Ghana's independence of 1957 described as important for the whole of Africa?",
      "Step 1. Ghana was the first country in sub-Saharan Africa to break free from colonial rule.",
      "Step 2. Its success showed other colonies that independence was achievable, and Ghana actively supported their movements.",
      "Step 3. That is why the <b>black star</b> on the flag stands for African freedom, not only Ghana's."),
    E("A trader says buying imported rice instead of local rice is just a personal choice. Comment.",
      "Step 1. It is a personal choice, but it has a national effect.",
      "Step 2. Money spent on imports pays foreign farmers; money spent on local rice pays Ghanaian farmers, millers and transporters.",
      "Step 3. So buying local <b>creates jobs at home and keeps foreign exchange in the country</b> — one reason patriotism is practical, not sentimental.")])

topic("education", "Education & national development", C, [
  "Education is the process of acquiring knowledge, skills, attitudes and values. It may be <b>formal</b> (school), "
  "<b>informal</b> (home and community) or <b>non-formal</b> (adult literacy, apprenticeship, mass education).",
  "Ghana's system: kindergarten (2 years), primary (6), junior high (3) — together free and compulsory basic "
  "education — then senior high or technical/vocational (3), and tertiary.",
  "Benefits to the individual: knowledge and skills, employment and higher income, self-confidence, "
  "better health decisions, and the ability to take part in public life.",
  "Benefits to the nation: skilled workforce, higher productivity, lower birth rate, better health, "
  "informed citizens and a stable democracy.",
  "Problems: inadequate classrooms and teaching materials, shortage of trained teachers in rural areas, "
  "child labour and teenage pregnancy, poverty, and the cost of transport and feeding.",
])
O("Education received through the family, peers and community without a classroom is described as",
  ["informal education", "formal education", "non-formal education", "technical education"],
  ["Formal education happens in school with a syllabus; non-formal is organised outside school for adults.",
   "Learning through the family and community is <b>informal education</b>."],
  ok=True)
O("Basic education in Ghana consists of",
  ["kindergarten, primary and junior high school", "primary school only",
   "junior high and senior high school", "senior high and university"],
  ["Basic education is the free and compulsory part of the system.",
   "It is <b>kindergarten, primary and junior high school</b> — eleven years in all."],
  ok=True)
O("Which of the following is a benefit of education to the nation?",
  ["A skilled and productive workforce", "More festivals in the year",
   "A larger population", "Higher prices for goods"],
  ["Education changes what citizens can do.",
   "The main benefit is <b>a skilled and productive workforce</b>, which raises output and incomes."],
  ok=True)
O("A major cause of school drop-out among girls in some communities is",
  ["teenage pregnancy", "too many teachers", "free textbooks", "short school hours"],
  ["The others would keep girls in school rather than remove them.",
   "<b>Teenage pregnancy</b> — with early marriage and poverty — is a major cause of drop-out."],
  ok=True)
O("Technical and vocational education is important because it",
  ["gives learners practical skills for work and self-employment", "is easier than other courses",
   "requires no examination", "takes only one year"],
  ["It is neither easier nor shorter.",
   "Its value is that it <b>gives learners practical skills for work and self-employment</b> — building, tailoring, electrical work, catering, ICT."],
  ok=True)
T("(a) State the three types of education and give an example of each. "
  "(b) Give four benefits of education to the individual. "
  "(c) State four problems facing basic education in Ghana and suggest a solution to each.",
  ["(a) <b>Formal</b> — learning in school following a syllabus, leading to the BECE. "
   "<b>Informal</b> — learning good manners, language and work habits from the family and community. "
   "<b>Non-formal</b> — adult literacy classes, apprenticeship with a mason or seamstress, radio and mass education programmes.",
   "(b) Any four: <b>knowledge and skills</b> for work; <b>better jobs and higher income</b>; "
   "<b>self-confidence and the ability to express oneself</b>; <b>better health and family decisions</b>; "
   "<b>awareness of one's rights and duties</b>, so one cannot easily be cheated; opportunity for further study.",
   "(c) <b>Inadequate classrooms and furniture</b> → government, assemblies and old pupils' associations build and "
   "furnish classrooms. <b>Shortage of trained teachers in rural areas</b> → incentives such as accommodation and rural "
   "allowances, and teacher training with posting agreements. <b>Poverty, hunger and the cost of transport</b> → "
   "school feeding, free uniforms and exercise books, and capitation grants. <b>Teenage pregnancy and child labour</b> → "
   "counselling and reproductive-health education, enforcement of the law on child labour, and re-entry policies so "
   "that young mothers can return to school."],
  marks=12)
extras("education",
  plain="Education is the one investment that pays the individual and the nation at the same time: the pupil earns more, "
        "and the country gets a worker who can do more. Nearly every problem on the list above comes back to cost — which is why Ghana's policies focus on removing the cost barriers.",
  examples=[
    E("Explain how educating girls reduces the rate of population growth.",
      "Step 1. A girl in school marries later and starts a family later.",
      "Step 2. An educated woman is better informed about family planning and more able to decide for herself.",
      "Step 3. She therefore tends to have <b>fewer children, spaced further apart, who are healthier</b> — slowing population growth and improving family welfare."),
    E("A pupil says only white-collar jobs matter, so technical education is for the weak. Reply.",
      "Step 1. Every building, road, vehicle and electrical installation in the country is the work of technical hands.",
      "Step 2. Ghana imports skills and pays well for artisans precisely because they are in short supply.",
      "Step 3. So technical education <b>leads to employment and self-employment</b>, often sooner and more surely than a general certificate.")])

topic("adolescent", "Adolescence & responsible living", C, [
  "Adolescence is the stage between childhood and adulthood, marked by rapid physical, emotional and social changes.",
  "Challenges: peer pressure, emotional ups and downs, curiosity about sex, substance abuse, "
  "indiscipline, and the desire to be accepted.",
  "<b>Chastity</b> — abstaining from sexual activity — protects an adolescent from teenage pregnancy, "
  "sexually transmitted infections including HIV, and the loss of education.",
  "Teenage pregnancy interrupts schooling, endangers the health of a young mother and her baby, "
  "and often brings poverty and stigma to both.",
  "Responsible living: choose friends wisely, set goals and keep to them, say no firmly, avoid alcohol and drugs, "
  "spend free time on sport, clubs and study, and talk to a parent, teacher or counsellor when under pressure.",
])
O("The strongest influence on the behaviour of most adolescents, after the family, is",
  ["the peer group", "the weather", "the radio", "the district assembly"],
  ["Adolescents badly want to be accepted by people of their own age.",
   "So <b>the peer group</b> has the strongest influence, for good or ill."],
  ok=True)
O("Chastity in adolescence means",
  ["abstaining from sexual activity", "being rude to elders",
   "refusing to attend school", "eating only local food"],
  ["The word refers to sexual self-control.",
   "Chastity means <b>abstaining from sexual activity</b> \u2014 the surest way for a young person to avoid pregnancy and sexually transmitted infection."],
  ok=True)
O("A major effect of teenage pregnancy on a pupil is",
  ["interruption of her education", "improvement in her health",
   "better performance in class", "more pocket money"],
  ["The consequences fall heaviest on her schooling.",
   "The main effect is <b>interruption of her education</b>, which limits her opportunities for life."],
  ok=True)
O("Which of these is the best way to resist negative peer pressure?",
  ["Say no firmly and choose better friends", "Join in so as not to be laughed at",
   "Keep quiet and hope it stops", "Leave school"],
  ["Silence and conformity give in to the pressure.",
   "The best course is to <b>say no firmly and choose better friends</b>, and to tell a trusted adult if the pressure continues."],
  ok=True)
O("Substance abuse among the youth is harmful because it",
  ["damages health and destroys the future", "makes a person popular",
   "improves school performance", "increases family income"],
  ["Any short-term popularity is paid for dearly.",
   "Substance abuse <b>damages health and destroys the future</b> — the brain, the body, school work, money and reputation."],
  ok=True)
T("(a) State four changes that take place during adolescence. (b) Give four problems adolescents face in Ghana today. "
  "(c) Explain four ways in which an adolescent can live responsibly.",
  ["(a) <b>Rapid growth in height and weight</b>; <b>development of the reproductive organs and growth of body "
   "hair</b>; <b>change of voice, especially in boys</b>; <b>emotional changes</b> — moodiness, strong feelings, "
   "desire for independence; and <b>new social interests</b>, including attraction to the opposite sex.",
   "(b) Any four: <b>negative peer pressure</b>; <b>temptation of premarital sex, leading to pregnancy and STIs</b>; "
   "<b>drug and alcohol abuse</b>; <b>poverty, which pushes some into hawking or transactional relationships</b>; "
   "<b>misuse of the internet and social media</b>; <b>lack of guidance at home</b> and conflict with parents.",
   "(c) <b>Set clear goals and plan your time</b>, so that study comes before pleasure. "
   "<b>Choose friends who share those goals</b>, and learn to say no firmly without arguing. "
   "<b>Abstain from sex, alcohol and drugs</b>, which is the surest protection against pregnancy, infection and addiction. "
   "<b>Use your free time well</b> — sport, clubs, skills, religious activity — and <b>talk to a parent, teacher or "
   "counsellor</b> whenever you are confused or under pressure."],
  marks=12)
extras("adolescent",
  plain="Adolescence is a few short years in which decisions can shape a whole life. The pressures are real, but so is "
        "the simple arithmetic: a pupil who finishes school has choices, and the choices narrow sharply for one who does not.",
  examples=[
    E("A classmate offers a pupil a drink at a party, saying everyone is doing it. Suggest exactly what she should say and do.",
      "Step 1. Answer briefly and firmly — 'No, thanks, I don't drink' — without a long explanation or argument.",
      "Step 2. Change the activity or move to another group; staying in the situation invites more pressure.",
      "Step 3. If it continues, <b>leave the party and tell a parent or trusted adult</b>. A friend who cannot accept no is not much of a friend."),
    E("Explain why a 15-year-old pregnancy is a health risk as well as an educational one.",
      "Step 1. A girl of that age is still growing, and her pelvis and body are not fully developed.",
      "Step 2. That raises the risk of complications in labour, anaemia and low birth weight.",
      "Step 3. Added to the loss of schooling, the result is <b>danger to both mother and baby, and a lasting loss of opportunity</b>.")])

topic("economy", "Production & the sectors of the economy", C, [
  "Production is the creation of goods and services to satisfy human wants. "
  "The factors of production are <b>land, labour, capital</b> and <b>entrepreneurship</b>.",
  "The <b>primary</b> sector takes resources from nature: farming, fishing, forestry, mining. "
  "The <b>secondary</b> sector processes them: manufacturing, building, food processing. "
  "The <b>tertiary</b> sector provides services: trade, transport, banking, teaching, health.",
  "Ghana's main exports are <b>gold, cocoa, crude oil and timber</b>; the economy also depends on services.",
  "<b>Value addition</b> means processing raw materials before export — turning cocoa beans into chocolate — "
  "which earns far more money and creates jobs at home.",
  "Problems: dependence on a few raw exports whose prices change, inadequate capital and electricity, "
  "poor roads and storage, low technology, and smuggling.",
])
O("The four factors of production are",
  ["land, labour, capital and entrepreneurship", "land, water, air and sunlight",
   "money, machines, markets and management", "farming, mining, trading and teaching"],
  ["The question asks for the classic factors used by economists.",
   "They are <b>land, labour, capital and entrepreneurship</b>."],
  ok=True)
O("Fishing, farming and mining belong to the",
  ["primary sector", "secondary sector", "tertiary sector", "informal sector"],
  ["These activities take materials straight from nature.", "They belong to the <b>primary sector</b>."],
  ok=True)
O("A factory that turns cocoa beans into chocolate is engaged in",
  ["secondary production", "primary production", "tertiary production", "distribution only"],
  ["Processing a raw material into a finished good is manufacturing.",
   "That is <b>secondary production</b>."],
  ok=True)
O("Which of the following is Ghana's leading mineral export?",
  ["Gold", "Diamond", "Bauxite", "Manganese"],
  ["Ghana produces all four, but in very different values.", "<b>Gold</b> is by far the leading mineral export."],
  ok=True)
O("The main advantage of processing cocoa in Ghana rather than exporting raw beans is that it",
  ["earns more money and creates jobs", "makes the beans heavier",
   "reduces the quality of the cocoa", "removes the need for farmers"],
  ["Processed goods sell at many times the price of the raw material.",
   "So processing <b>earns more money and creates jobs</b> in Ghana — this is value addition."],
  ok=True)
T("(a) Name and explain the four factors of production. (b) Name the three sectors of the economy and give two "
  "examples of activities in each. (c) State four problems facing production in Ghana.",
  ["(a) <b>Land</b> — all natural resources: soil, minerals, water, forests. "
   "<b>Labour</b> — human effort, physical and mental, used in production. "
   "<b>Capital</b> — man-made assets used to produce more goods: tools, machines, buildings, money for investment. "
   "<b>Entrepreneurship</b> — the person who brings the other three together, organises production and bears the risk.",
   "(b) <b>Primary</b>: cocoa farming, fishing (also mining, lumbering). "
   "<b>Secondary</b>: cocoa processing, cement manufacture (also building, textiles). "
   "<b>Tertiary</b>: teaching, banking (also transport, trading, health care, tourism).",
   "(c) Any four: <b>inadequate capital and costly credit</b>; <b>unreliable and expensive electricity</b>; "
   "<b>poor roads, storage and marketing</b>, so produce spoils or sells cheaply; <b>low level of technology and "
   "skills</b>; <b>dependence on a few raw exports</b> whose world prices fluctuate; competition from cheap imports "
   "and smuggling."],
  marks=12, fig=draw.flow(["PRIMARY: cocoa farming, mining, fishing",
                           "SECONDARY: processing into chocolate, cement, cloth",
                           "TERTIARY: transport, banking, trade, teaching"],
                          label="The three sectors of the economy"))
extras("economy",
  plain="Every job in Ghana sits in one of three sectors, and the country gets richer as activity moves up the chain. A "
        "bag of cocoa beans earns a little; the same cocoa as chocolate earns many times more — which is why 'value addition' appears in almost every economic discussion.",
  examples=[
    E("A farmer sells fresh tomatoes but half rot before they reach the market. Suggest two solutions and the sector each belongs to.",
      "Step 1. Better roads and refrigerated transport reduce the losses — these are <b>tertiary</b> (services and infrastructure).",
      "Step 2. A small factory turning surplus tomatoes into paste adds value and stops the waste — that is <b>secondary</b>.",
      "Step 3. Both raise the farmer's income from the same crop, without planting a single extra seedling."),
    E("Why is it risky for a country to depend on one or two export crops?",
      "Step 1. World prices for raw materials rise and fall sharply, and the country does not control them.",
      "Step 2. A bad harvest or a price fall cuts national income suddenly.",
      "Step 3. So governments aim to <b>diversify</b> — more crops, more processing, more services — to spread the risk.")])

topic("money", "Money, saving & banking", C, [
  "Money is anything generally accepted as a means of payment. Ghana's currency is the <b>Ghana cedi (GH¢)</b>.",
  "Functions of money: a medium of exchange, a measure of value, a store of value, "
  "a standard for deferred payment (credit).",
  "Before money there was <b>trade by barter</b> — goods exchanged for goods — which failed because of the "
  "difficulty of finding a double coincidence of wants, of dividing goods and of storing value.",
  "<b>Saving</b> means setting aside part of one's income for future use. It is done through banks, "
  "credit unions, susu schemes, treasury bills, insurance and the purchase of property.",
  "The <b>Bank of Ghana</b> is the central bank: it issues the currency, keeps the nation's accounts, "
  "supervises the other banks and manages inflation. Commercial banks accept deposits, give loans, "
  "transfer money and keep valuables.",
])
O("The central bank of Ghana, which issues the country's currency, is the",
  ["Bank of Ghana", "GCB Bank", "Agricultural Development Bank", "Ghana Revenue Authority"],
  ["The others are commercial or revenue institutions.",
   "Only the <b>Bank of Ghana</b> issues currency and supervises the banks."],
  ok=True)
O("Trade by barter means the exchange of",
  ["goods for goods", "goods for money", "money for services", "cheques for cash"],
  ["Barter existed before money was invented.", "It is the exchange of <b>goods for goods</b>."],
  ok=True)
O("Which of the following is NOT a function of money?",
  ["Producing goods and services", "Acting as a medium of exchange",
   "Serving as a measure of value", "Serving as a store of value"],
  ["Money makes exchange easy, but it does not itself produce anything.",
   "<b>Producing goods and services</b> is not a function of money."],
  ok=True)
O("The main advantage of saving money in a bank rather than at home is that it",
  ["is safe and earns interest", "can be spent more easily",
   "cannot be withdrawn", "increases the price of goods"],
  ["Money at home can be lost, stolen or spent on impulse, and it earns nothing.",
   "In a bank it <b>is safe and earns interest</b>, and it builds a record for obtaining credit."],
  ok=True)
O("A susu collector helps petty traders mainly by",
  ["encouraging them to save small amounts regularly", "lending them money at no cost",
   "selling their goods for them", "paying their taxes"],
  ["The service is a savings service, not a sales or tax service.",
   "It <b>encourages them to save small amounts regularly</b>, which they could not easily do alone."],
  ok=True)
T("(a) State four functions of money. (b) Give three problems of trade by barter. "
  "(c) State four reasons why an individual should save, and name three places where savings can be kept.",
  ["(a) <b>Medium of exchange</b> — it is accepted in payment for goods and services. "
   "<b>Measure (unit) of value</b> — prices of all goods can be compared in cedis. "
   "<b>Store of value</b> — wealth can be kept in money form for later use. "
   "<b>Standard of deferred payment</b> — debts and credit can be expressed and settled in money.",
   "(b) <b>Double coincidence of wants</b> — each party had to want exactly what the other offered. "
   "<b>Indivisibility</b> — you cannot cut a cow in half to pay for a basket of maize. "
   "<b>No store of value</b> — goods such as fish and yam spoil, so wealth could not be kept; and there was no common "
   "measure of value, which made bargaining slow and unfair.",
   "(c) Reasons: <b>to meet future needs</b> such as school fees, rent or a funeral; <b>to guard against emergencies</b> "
   "— illness, loss of work; <b>to acquire capital</b> for a business, land or a house; <b>to earn interest</b> and to "
   "build a record that qualifies one for a loan. "
   "Places: <b>a commercial bank or rural bank</b>, <b>a credit union or co-operative</b>, <b>a susu scheme or mobile "
   "money wallet</b> (treasury bills, insurance policies and property are also acceptable)."],
  marks=12)
extras("money",
  plain="Money solved a practical problem: barter only works when two people happen to want each other's goods. Everything "
        "else — banks, saving, interest, credit — grew out of that one invention. Saving is simply the habit of letting today's income serve tomorrow's need.",
  examples=[
    E("A trader earns GH¢1 200 a month and saves 15% of it. How much does she save in a year?",
      "Step 1. Monthly saving = 15% of 1 200 = 0.15 × 1 200 = GH¢180.",
      "Step 2. Yearly saving = 180 × 12.",
      "Step 3. = <b>GH¢2 160</b> — before any interest, which is why saving in a bank beats saving in a box."),
    E("Why does the Bank of Ghana, rather than a commercial bank, print the cedi?",
      "Step 1. If every bank could print money, the amount in circulation would be uncontrolled.",
      "Step 2. Too much money chasing the same goods raises prices — inflation.",
      "Step 3. So one central bank controls the supply, in order to <b>keep the value of the cedi stable</b>.")])

topic("entrepreneur", "Entrepreneurship & self-reliance", C, [
  "An entrepreneur is a person who sees an opportunity, organises the factors of production and bears the risk "
  "of running a business.",
  "Qualities: creativity, hard work, honesty, risk-taking, good record-keeping, discipline with money, "
  "customer care, perseverance and the ability to plan.",
  "Benefits to the nation: creates jobs, raises incomes, adds value to raw materials, "
  "widens the tax base and reduces dependence on government employment.",
  "Problems faced by small businesses in Ghana: shortage of capital, high interest rates, unreliable electricity, "
  "poor record-keeping, competition from imports, high rents and multiple taxes.",
  "Support: micro-finance and rural banks, co-operatives and susu, government and NGO schemes, "
  "business advisory centres, and training in technical and vocational skills.",
])
O("An entrepreneur is a person who",
  ["organises a business and bears its risk", "works for the government",
   "lends money to banks", "collects taxes"],
  ["The distinguishing feature is bearing the risk.",
   "An entrepreneur <b>organises a business and bears its risk</b>."],
  ok=True)
O("Which of the following is the most important quality of a successful entrepreneur?",
  ["Hard work and honesty", "Having many friends",
   "Living in a city", "Speaking many languages"],
  ["The others may help, but they are not decisive.",
   "<b>Hard work and honesty</b> — with creativity and good records — decide whether a business survives."],
  ok=True)
O("The greatest problem facing small-scale businesses in Ghana is",
  ["inadequate capital", "too many customers", "low taxes", "cheap electricity"],
  ["Electricity is costly, not cheap, and taxes are felt as high.",
   "The most commonly cited problem is <b>inadequate capital</b> and the high cost of borrowing."],
  ok=True)
O("Keeping proper records in a small business helps the owner to",
  ["know whether he is making a profit or a loss", "avoid paying workers",
   "increase his prices every week", "escape all taxes"],
  ["Records are a management tool, not a way of avoiding obligations.",
   "They let the owner <b>know whether he is making a profit or a loss</b>, and they help in obtaining a loan."],
  ok=True)
O("Entrepreneurship contributes to national development mainly by",
  ["creating employment and incomes", "increasing the population",
   "reducing the number of schools", "raising import duties"],
  ["Jobs are the central contribution.",
   "Entrepreneurship <b>creates employment and incomes</b>, adds value to local materials and widens the tax base."],
  ok=True)
T("(a) Who is an entrepreneur? (b) State five qualities of a successful entrepreneur. "
  "(c) Give three problems facing small-scale businesses in Ghana and suggest how each can be solved.",
  ["(a) <b>An entrepreneur is a person who identifies a business opportunity, brings together land, labour and capital "
   "to produce goods or services, manages the business and bears the risk of profit or loss.</b>",
   "(b) Any five: <b>creativity and initiative</b>; <b>hard work and perseverance</b>; <b>honesty and good "
   "customer relations</b>; <b>willingness to take calculated risks</b>; <b>good record-keeping and financial "
   "discipline</b>; <b>ability to plan and organise</b>; <b>willingness to learn new skills</b>.",
   "(c) <b>Shortage of capital</b> → save through susu and credit unions, start small, and use micro-finance and "
   "government youth business schemes rather than expensive moneylenders. "
   "<b>Poor record-keeping</b> → learn simple book-keeping, separate business money from personal money, and attend "
   "training at a business advisory centre. "
   "<b>Unreliable or costly electricity and poor premises</b> → share facilities through co-operatives, use energy-"
   "efficient equipment or solar, and seek space in an industrial or market enclave provided by the assembly."],
  marks=12)
extras("entrepreneur",
  plain="Self-reliance is the practical answer to the shortage of formal jobs: the tailor, the welder, the hairdresser and "
        "the agro-processor all employ themselves and often others. The difference between a business that grows and one that folds is rarely luck — it is records, discipline and customer care.",
  examples=[
    E("A pupil wants to start a small business selling iced water after school. Outline four things she must decide first.",
      "Step 1. What exactly she will sell, to whom, and at what price — her market and margin.",
      "Step 2. How much capital she needs, and where it will come from (savings, family loan).",
      "Step 3. Where she will sell and how she will keep records of money in and money out; and <b>how she will protect her study time</b>, since the business must not cost her the BECE."),
    E("Why do many small businesses fail even when sales are good?",
      "Step 1. The owner mixes business money with household money, so capital is eaten away.",
      "Step 2. Without records, he cannot tell whether a line of goods is profitable.",
      "Step 3. The remedy is simple and dull: <b>separate accounts, written records, and paying oneself a fixed wage</b>.")])

topic("tourism", "Tourism in Ghana", C, [
  "Tourism is travel away from home for leisure, learning, business or culture. "
  "Tourists may be <b>domestic</b> (Ghanaians travelling within Ghana) or <b>international</b>.",
  "Attractions: historical — Cape Coast and Elmina castles (UNESCO World Heritage sites), Larabanga Mosque, "
  "Manhyia Palace, W. E. B. Du Bois Centre; natural — Kakum National Park, Mole National Park, Wli Waterfalls, "
  "Lake Volta, Lake Bosomtwe, Boti Falls, Paga crocodile ponds, Nzulezu stilt village; "
  "cultural — festivals, drumming and dancing, kente and adinkra, traditional food.",
  "Benefits: foreign exchange, employment (hotels, guides, transport, crafts), markets for local goods, "
  "better infrastructure, preservation of culture and heritage, and international friendship.",
  "Problems: poor roads to some sites, inadequate accommodation and publicity, poor maintenance of monuments, "
  "harassment of visitors, and damage to the environment and to culture.",
  "Development of tourism: the Ghana Tourism Authority, better roads and signage, training of guides, "
  "advertising abroad, and community involvement so that local people benefit.",
])
O("Which of these is a historical tourist attraction in Ghana?",
  ["Elmina Castle", "Kakum National Park", "Wli Waterfalls", "Lake Bosomtwe"],
  ["The other three are natural attractions.",
   "<b>Elmina Castle</b> is a historical site, and a UNESCO World Heritage site."],
  ok=True)
O("The canopy walkway, a major attraction for visitors to the Central Region, is found at",
  ["Kakum National Park", "Mole National Park", "Shai Hills", "Bui National Park"],
  ["Mole is in the Savannah Region and is known for elephants.",
   "The canopy walkway is at <b>Kakum National Park</b>."],
  ok=True)
O("The greatest economic benefit of tourism to Ghana is that it",
  ["earns foreign exchange and creates jobs", "reduces the population",
   "increases the price of food", "replaces farming"],
  ["Tourism supplements, not replaces, other activities.",
   "Its greatest benefit is that it <b>earns foreign exchange and creates jobs</b>."],
  ok=True)
O("Which of the following discourages tourists from visiting a site?",
  ["Bad roads and harassment by touts", "Trained and friendly guides",
   "Clean and well-kept surroundings", "Good hotels nearby"],
  ["The last three attract visitors.",
   "<b>Bad roads and harassment by touts</b> drive tourists away and spoil a destination's reputation."],
  ok=True)
O("Nzulezu, a village built on stilts over water, is found in the",
  ["Western Region", "Volta Region", "Northern Region", "Ashanti Region"],
  ["It stands on Lake Tadane, near Beyin.", "Nzulezu is in the <b>Western Region</b>."],
  ok=True)
T("(a) What is tourism? (b) Name four tourist attractions in Ghana, stating where each is found. "
  "(c) Give four benefits of tourism to Ghana and three problems facing the industry.",
  ["(a) <b>Tourism is the business of travelling away from one's usual place of residence for pleasure, education, "
   "culture or business, and the services provided for such travellers.</b>",
   "(b) Any four, with location: <b>Cape Coast and Elmina castles</b> — Central Region; <b>Kakum National Park "
   "(canopy walkway)</b> — Central Region; <b>Mole National Park</b> — Savannah Region; <b>Wli Waterfalls</b> — Volta "
   "Region; <b>Manhyia Palace</b> — Ashanti Region; <b>Paga crocodile pond</b> — Upper East Region; <b>Nzulezu stilt "
   "village</b> — Western Region; <b>Larabanga Mosque</b> — Savannah Region.",
   "(c) Benefits: <b>foreign exchange</b> for the country; <b>employment</b> for guides, drivers, hotel staff and "
   "craftsmen; <b>a market for local goods</b> — food, kente, carvings, beads; <b>improved infrastructure</b> such as "
   "roads, water and electricity at tourist centres; and <b>preservation of culture and heritage</b>. "
   "Problems: <b>poor roads and transport to many sites</b>; <b>inadequate accommodation, publicity and trained "
   "guides</b>; <b>poor maintenance of monuments and harassment of visitors</b>; environmental damage at popular sites."],
  marks=12)
extras("tourism",
  plain="Tourism turns things Ghana already has — castles, forests, waterfalls, festivals — into income, without digging "
        "anything out of the ground. That is why it is called a sustainable industry: look after the attraction and it pays for ever.",
  examples=[
    E("A community wants to develop a waterfall near their village. Suggest four things they should do.",
      "Step 1. Protect the site: stop farming and felling near the falls, and keep it clean.",
      "Step 2. Make it accessible and safe: a path, steps, railings, toilets and a place to park.",
      "Step 3. <b>Train local guides, set a fair entrance fee, and agree how the money is shared</b> — community benefit is what keeps the project alive."),
    E("Explain how a single tourist visiting Cape Coast benefits several different Ghanaians.",
      "Step 1. She pays a driver or bus company to get there, and a hotel or guesthouse to stay.",
      "Step 2. She pays an entrance fee that maintains the castle, and a guide who is paid from it.",
      "Step 3. She buys food from a chop bar and a carving or kente from a craftsman — so <b>one visitor's money spreads through many households</b>.")])

topic("intl", "International cooperation", C, [
  "Countries cooperate because no country can meet all its needs alone, and because peace, trade and development "
  "cross borders.",
  "The <b>United Nations (UN)</b>, formed in 1945, keeps international peace, promotes human rights and development. "
  "Ghana joined in 1957 and contributes troops to UN peacekeeping. Agencies: UNESCO, UNICEF, WHO, FAO, ILO.",
  "The <b>African Union (AU)</b>, formed in 2002 to replace the Organisation of African Unity (OAU, 1963), "
  "promotes African unity, peace and development.",
  "<b>ECOWAS</b> — the Economic Community of West African States — was formed in <b>1975</b> by the Treaty of Lagos "
  "to promote trade, free movement and economic integration in West Africa. Its headquarters is in Abuja, Nigeria.",
  "The <b>Commonwealth</b> links Britain and its former colonies for cooperation in education, sport and development.",
  "Benefits to Ghana: markets and trade, aid and loans, technical assistance, scholarships, peacekeeping experience, "
  "and a voice in world affairs.",
])
O("ECOWAS was established in",
  ["1975", "1957", "1963", "2002"],
  ["1963 is the OAU and 2002 the AU; 1957 is Ghana's independence.",
   "ECOWAS was established in <b>1975</b> by the Treaty of Lagos."],
  ok=True)
O("The headquarters of ECOWAS is in",
  ["Abuja", "Accra", "Addis Ababa", "Lomé"],
  ["Addis Ababa hosts the African Union.", "The ECOWAS Commission has its headquarters in <b>Abuja</b>, Nigeria."],
  ok=True)
O("The United Nations agency responsible for the welfare of children is",
  ["UNICEF", "UNESCO", "WHO", "FAO"],
  ["UNESCO deals with education and culture, WHO with health and FAO with food and agriculture.",
   "Children's welfare is the work of <b>UNICEF</b>."],
  ok=True)
O("The African Union replaced the",
  ["Organisation of African Unity", "Commonwealth of Nations",
   "United Nations", "Economic Community of West African States"],
  ["The OAU was founded in 1963 and gave way to the AU in 2002.",
   "The AU replaced the <b>Organisation of African Unity</b>."],
  ok=True)
O("A major benefit Ghana derives from membership of ECOWAS is",
  ["free movement of people and goods within the sub-region", "free electricity",
   "payment of civil servants' salaries", "control of Ghana's elections"],
  ["Member states keep their sovereignty and pay their own bills.",
   "The main benefit is <b>free movement of people and goods within the sub-region</b>, which widens the market for Ghanaian traders."],
  ok=True)
T("(a) Give three reasons why countries cooperate with one another. "
  "(b) Name four international organisations to which Ghana belongs and state one aim of each. "
  "(c) State four benefits Ghana derives from international cooperation.",
  ["(a) <b>No country produces everything it needs</b>, so trade is necessary; <b>problems cross borders</b> — "
   "disease, climate change, crime, conflict — and can be solved only together; and cooperation brings "
   "<b>aid, technology, skills and a voice in world decisions</b>.",
   "(b) <b>United Nations (UN)</b> — to maintain international peace and security and promote human rights and "
   "development. <b>African Union (AU)</b> — to promote the unity, peace and development of Africa. "
   "<b>ECOWAS</b> — to promote trade, free movement and economic integration in West Africa. "
   "<b>The Commonwealth</b> — cooperation in education, culture, sport and development among Britain and its former "
   "colonies. (The AfCFTA, WHO and World Bank are also acceptable.)",
   "(c) Any four: <b>wider markets for Ghanaian exports</b>; <b>aid, loans and grants</b> for roads, schools and "
   "health; <b>technical assistance and scholarships</b> that train Ghanaians; <b>help in emergencies</b> such as "
   "floods and epidemics; <b>peace and security</b>, including peacekeeping; and <b>a voice in world affairs</b> out "
   "of proportion to Ghana's size."],
  marks=12)
extras("intl",
  plain="Ghana is a small economy in a big world, and cooperation is how a small country gets heard and gets trade. Keep "
        "the four big names and their dates straight — UN 1945, OAU 1963, ECOWAS 1975, AU 2002 — and this topic is mostly secured.",
  examples=[
    E("A Ghanaian trader wants to sell shoes in Lomé and Abidjan. How does ECOWAS membership help her?",
      "Step 1. ECOWAS citizens may enter member states without a visa for up to 90 days.",
      "Step 2. Trade protocols reduce or remove duties on goods originating in the community.",
      "Step 3. So she can <b>travel freely and sell in a market of hundreds of millions</b> rather than Ghana's alone."),
    E("Why does Ghana send soldiers on United Nations peacekeeping missions?",
      "Step 1. As a UN member, Ghana shares the duty of maintaining international peace.",
      "Step 2. Peace in other countries, especially in West Africa, protects Ghana from refugee flows and spillover conflict.",
      "Step 3. Ghana also gains <b>international respect, training and allowances</b> for its armed forces.")])

topic("scitech", "Science, technology & development", C, [
  "Science and technology raise output, reduce drudgery, improve health and shorten distances. "
  "Development means a lasting improvement in people's living conditions.",
  "In agriculture: tractors, irrigation, improved seeds, fertilisers, storage silos and agro-processing.",
  "In health: vaccines, laboratory tests, scans, ambulances and telemedicine.",
  "In communication and business: mobile phones, mobile money, the internet, computers in schools and offices.",
  "Challenges: cost of equipment, shortage of trained people, unreliable power, poor maintenance culture, "
  "and e-waste and pollution. Ghana addresses these through STEM education, technical universities, "
  "research institutions and partnership with industry.",
])
O("Development may best be described as",
  ["a lasting improvement in people's living conditions", "the building of tall offices only",
   "an increase in the population", "the importation of machines"],
  ["Buildings and machines are means, not the end.",
   "Development is <b>a lasting improvement in people's living conditions</b> — income, health, education and opportunity."],
  ok=True)
O("Which technology has most transformed the way Ghanaians send and receive money?",
  ["Mobile money", "The radio", "The bicycle", "The typewriter"],
  ["It reaches people far from any bank branch.",
   "<b>Mobile money</b> has transformed payments and savings across the country."],
  ok=True)
O("The use of improved seeds and irrigation in farming leads to",
  ["higher yields and all-year production", "lower yields",
   "more bush burning", "smaller markets"],
  ["Better inputs and water supply raise output and remove the dependence on rain.",
   "The result is <b>higher yields and all-year production</b>."],
  ok=True)
O("A major challenge to the use of technology in Ghanaian schools is",
  ["inadequate equipment and unreliable electricity", "too many trained teachers",
   "pupils' lack of interest in phones", "the low cost of computers"],
  ["Interest is high and costs are not low.",
   "The real obstacle is <b>inadequate equipment and unreliable electricity</b>, along with too few trained ICT teachers."],
  ok=True)
O("STEM education refers to the study of",
  ["Science, Technology, Engineering and Mathematics", "Sports, Theatre, English and Music",
   "Social studies, Trade, Economics and Marketing", "Skills, Training, Employment and Money"],
  ["The acronym is used worldwide for one group of subjects.",
   "STEM means <b>Science, Technology, Engineering and Mathematics</b>."],
  ok=True)
T("(a) State four ways in which science and technology have improved life in Ghana. "
  "(b) Give three problems that limit the use of technology in Ghana. "
  "(c) Suggest three things the government and pupils can do to make Ghana more technologically advanced.",
  ["(a) <b>Agriculture</b> — tractors, irrigation, improved seeds and storage have raised food production. "
   "<b>Health</b> — vaccines, laboratory tests, scans and ambulances save lives, and diseases such as polio and "
   "measles are controlled. <b>Communication and business</b> — mobile phones, mobile money and the internet let "
   "people trade, pay and learn across distances. <b>Energy, water and transport</b> — dams, solar systems, "
   "treated water supply and better vehicles have improved daily living.",
   "(b) Any three: <b>high cost of equipment and of maintenance</b>; <b>shortage of trained technicians, engineers and "
   "ICT teachers</b>; <b>unreliable and expensive electricity</b>; <b>weak maintenance culture</b>, so equipment breaks "
   "down and is abandoned; and <b>poor disposal of electronic waste</b>.",
   "(c) Government: <b>invest in STEM and technical education</b>, equip laboratories and workshops, and fund research "
   "that industry can use; <b>provide reliable power and internet</b>, especially in schools; and <b>support local "
   "innovation and manufacturing</b> with credit and protection from dumping. "
   "Pupils: <b>take science and mathematics seriously, join science and ICT clubs, and use phones and computers for "
   "learning rather than only for entertainment</b>."],
  marks=12)
extras("scitech",
  plain="Technology is only useful when it is maintained and understood, which is why education, not equipment, is the "
        "real bottleneck. A country with trained hands can repair, adapt and eventually build; one without them replaces imported machines every few years.",
  examples=[
    E("Mobile money has reached villages that have no bank. Explain two effects on a farmer there.",
      "Step 1. He can be paid for his produce without carrying cash on a long journey — safer and quicker.",
      "Step 2. He can save small amounts, and build a record that may qualify him for credit.",
      "Step 3. So one technology brings <b>security, convenience and access to finance</b> at once."),
    E("A school receives twenty computers but they are unused after a year. Diagnose the likely problems.",
      "Step 1. No trained teacher or technician to run and maintain them.",
      "Step 2. Unreliable power or no protection against power surges, and no internet.",
      "Step 3. The lesson: <b>equipment without training, power and maintenance is wasted money</b> — plan for all three together.")])
