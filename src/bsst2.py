"""BECE Social Studies - Section B: Governance, politics and stability."""
from core import *
import draw

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}
B = "B. Governance, politics & stability"

topic("constitution", "The Constitution & citizenship", B, [
  "A constitution is the set of rules by which a country is governed. Ghana's present constitution is the "
  "<b>1992 Constitution</b>, which began the <b>Fourth Republic</b> on 7 January 1993.",
  "It is a <b>written and rigid</b> constitution — it can be changed only by a special procedure, and some "
  "entrenched clauses need a referendum.",
  "The constitution is the <b>supreme law</b>: any other law or act that conflicts with it is void.",
  "A citizen is a full member of a state. Citizenship may be acquired by <b>birth</b>, by <b>descent</b> "
  "(parent or grandparent a citizen), by <b>marriage</b>, by <b>registration</b> or by <b>naturalisation</b>.",
  "Duties of a citizen: obey the law, pay taxes, defend the country, protect public property, vote, "
  "report crime and respect the rights of others.",
])
O("The constitution under which Ghana is governed today is the",
  ["1992 Constitution", "1957 Constitution", "1969 Constitution", "1979 Constitution"],
  ["Earlier constitutions governed earlier republics.",
   "The Fourth Republic operates under the <b>1992 Constitution</b>, which came into force on 7 January 1993."],
  ok=True)
O("The statement that the constitution is the supreme law of the land means that",
  ["any law that conflicts with it is void", "only the President may read it",
   "it can never be changed", "it is written in English"],
  ["Supremacy is about rank among laws.",
   "It means <b>any law that conflicts with it is void</b> — Parliament, the President and the courts are all bound by it."],
  ok=True)
O("A child born in Ghana to parents who are both Ghanaians is a citizen by",
  ["birth", "registration", "naturalisation", "marriage"],
  ["Registration and naturalisation are for people who were not citizens before.",
   "Such a child is a citizen by <b>birth</b>."],
  ok=True)
O("Which of the following is a duty of a citizen?",
  ["Paying taxes honestly", "Criticising every government decision",
   "Refusing to serve on a jury", "Avoiding the census"],
  ["Rights come with responsibilities.",
   "<b>Paying taxes honestly</b> is a constitutional duty, since taxes pay for schools, roads and clinics."],
  ok=True)
O("The Fourth Republic of Ghana began on",
  ["7 January 1993", "6 March 1957", "1 July 1960", "4 June 1979"],
  ["6 March 1957 is Independence Day and 1 July 1960 the start of the First Republic.",
   "The Fourth Republic began on <b>7 January 1993</b>, which is why the President is sworn in on 7 January."],
  ok=True)
T("(a) What is a constitution? (b) State four ways by which a person may become a citizen of Ghana. "
  "(c) Give four duties of a good citizen and explain why each is important.",
  ["(a) <b>A constitution is the body of fundamental rules and principles according to which a country is governed, "
   "setting out the powers of the organs of government and the rights and duties of citizens.</b>",
   "(b) By <b>birth</b>; by <b>descent</b> (having a Ghanaian parent or grandparent); by <b>marriage</b> to a Ghanaian; "
   "by <b>registration</b>; and by <b>naturalisation</b> after satisfying the conditions set by law.",
   "(c) <b>Obeying the law</b> — without it there is no order and no safety. "
   "<b>Paying taxes</b> — taxes are the money with which roads, schools, clinics and the security services are provided. "
   "<b>Voting in elections</b> — it is how citizens choose and change their leaders peacefully. "
   "<b>Protecting public property and the environment</b> — street lights, school buildings and forests belong to all of "
   "us, and replacing what is destroyed takes money that could build something new."],
  marks=12)
extras("constitution",
  plain="A constitution is the country's rule book, and like the rules of a football match it binds the players and the "
        "referee alike. Ghana's is written, rigid and supreme — which is exactly why a court can declare even an Act of Parliament invalid.",
  examples=[
    E("Parliament passes a law banning all newspapers from criticising a minister. What can a citizen do?",
      "Step 1. The 1992 Constitution guarantees freedom of speech and of the media.",
      "Step 2. The constitution is supreme, so a law that conflicts with it is void.",
      "Step 3. A citizen can <b>go to the Supreme Court to have the law declared unconstitutional</b>."),
    E("Why does Ghana celebrate two separate national days in January and March?",
      "Step 1. 6 March 1957 is the day Ghana gained independence from British rule.",
      "Step 2. 7 January 1993 is the day the 1992 Constitution came into force, beginning the Fourth Republic.",
      "Step 3. So one marks <b>the birth of the nation</b> and the other <b>the return to constitutional rule</b>.")])

topic("govt", "Government: the three arms", B, [
  "Government has three arms. The <b>Executive</b> (President, Vice-President, Ministers, Council of State and the "
  "civil service) carries out policy. The <b>Legislature</b> (Parliament) makes laws. "
  "The <b>Judiciary</b> (the courts) interprets the law and settles disputes.",
  "The separation of powers and the system of <b>checks and balances</b> prevent any one arm from becoming too powerful.",
  "Parliament has <b>276 members</b>, each elected from a constituency for four years. A bill becomes law when it is "
  "passed by Parliament and <b>assented to by the President</b>.",
  "The President is both Head of State and Head of Government, elected for a term of four years and eligible for "
  "<b>no more than two terms</b>. The Chief Justice heads the Judiciary, whose highest court is the <b>Supreme Court</b>.",
  "Examples of checks: Parliament approves ministerial appointments and the budget; the courts can declare an act "
  "unconstitutional; the President assents to bills.",
])
O("The arm of government that makes laws is the",
  ["Legislature", "Executive", "Judiciary", "Civil service"],
  ["The Executive carries out laws and the Judiciary interprets them.",
   "Laws are made by the <b>Legislature</b> — Parliament."],
  ok=True)
O("The number of members of Ghana's Parliament is",
  ["276", "230", "200", "300"],
  ["The number has grown with the creation of new constituencies.",
   "Parliament currently has <b>276</b> members, one for each constituency."],
  ok=True)
O("The head of the Judiciary in Ghana is the",
  ["Chief Justice", "Attorney-General", "Speaker of Parliament", "Inspector-General of Police"],
  ["The Attorney-General is a minister and the Speaker presides over Parliament.",
   "The Judiciary is headed by the <b>Chief Justice</b>."],
  ok=True)
O("A President of Ghana may serve a maximum of",
  ["two terms of four years each", "one term of five years",
   "three terms of four years each", "any number of terms"],
  ["The 1992 Constitution limits the term of office.",
   "A President may serve <b>two terms of four years each</b>, and no more."],
  ok=True)
O("Which of the following is an example of checks and balances?",
  ["Parliament approving the President's ministerial nominees", "The President dissolving the Supreme Court",
   "A minister writing a law by himself", "A judge contesting an election while on the bench"],
  ["The other options would break the separation of powers.",
   "<b>Parliament approving the President's ministerial nominees</b> is the Legislature checking the Executive."],
  ok=True)
T("(a) Name the three arms of government and state one function of each. "
  "(b) Explain what is meant by 'separation of powers'. "
  "(c) Give three examples of how one arm of government checks another in Ghana.",
  ["(a) <b>Executive</b> — implements policies and runs the day-to-day administration of the country. "
   "<b>Legislature (Parliament)</b> — makes laws and approves the national budget. "
   "<b>Judiciary</b> — interprets the law, settles disputes and punishes offenders.",
   "(b) <b>Separation of powers means that the three arms of government are kept distinct, with different persons and "
   "different functions, so that no single arm or person controls everything.</b> It prevents dictatorship and protects "
   "the liberty of citizens.",
   "(c) <b>Parliament vets and approves ministerial nominees</b> and can reject them. "
   "<b>The Supreme Court can declare a law passed by Parliament, or an act of the Executive, unconstitutional.</b> "
   "<b>The President assents to bills</b> before they become law, and may refer a bill back to Parliament. "
   "(Parliament also approves the budget and can impeach the President, and the President appoints judges subject to "
   "approval.)"],
  marks=12, fig=draw.tree("GOVERNMENT", ["Executive: President, Ministers — carries out",
                                         "Legislature: Parliament — makes laws",
                                         "Judiciary: the Courts — interprets"],
                          label="The three arms of government"))
extras("govt",
  plain="Three arms, three jobs: make the law, carry out the law, interpret the law. Keeping them in different hands is "
        "what stops one person deciding everything — and every time you hear of Parliament vetting a nominee or a court striking down a law, you are watching that system work.",
  examples=[
    E("A minister orders the police to arrest a journalist without charge. Which arm can correct this, and how?",
      "Step 1. The order comes from the Executive.",
      "Step 2. Arrest without charge breaches the constitutional right to personal liberty.",
      "Step 3. The <b>Judiciary</b> can correct it: the journalist applies to court, which can order his release and declare the act unlawful."),
    E("Trace the steps by which a bill becomes law in Ghana.",
      "Step 1. The bill is published, then introduced in Parliament and read a first time.",
      "Step 2. It is debated at second reading, examined by a committee, amended and read a third time.",
      "Step 3. Once passed, it goes to the President; <b>on his assent it becomes an Act of Parliament</b>.")])

topic("democracy", "Democracy, elections & voting", B, [
  "Democracy is government of the people, by the people and for the people. In a <b>representative</b> democracy, "
  "citizens elect people to govern on their behalf.",
  "Features: regular free and fair elections, universal adult suffrage, rule of law, respect for human rights, "
  "freedom of speech and of the press, and more than one political party.",
  "Every Ghanaian of <b>18 years or above</b> and of sound mind is entitled to be registered and to vote.",
  "Elections are conducted by the <b>Electoral Commission</b>, an independent body. Voting is by <b>secret ballot</b>, "
  "so that no one can be punished for his choice.",
  "Presidential and parliamentary elections are held every four years, on <b>7 December</b>. "
  "A presidential candidate must obtain more than 50% of the valid votes cast.",
])
O("The minimum age at which a Ghanaian may vote is",
  ["18 years", "16 years", "21 years", "25 years"],
  ["The constitution sets universal adult suffrage at adulthood.", "The voting age is <b>18 years</b>."],
  ok=True)
O("Elections in Ghana are conducted by the",
  ["Electoral Commission", "Ghana Police Service",
   "National Commission for Civic Education", "Supreme Court"],
  ["The NCCE educates citizens and the courts settle disputes.",
   "Elections are organised by the <b>Electoral Commission</b>, which is independent."],
  ok=True)
O("Voting by secret ballot is important because it",
  ["allows a voter to choose freely without fear", "makes counting faster",
   "reduces the cost of elections", "keeps the result secret for ever"],
  ["Only the voter's choice is secret, not the result.",
   "The secret ballot <b>allows a voter to choose freely without fear</b> of intimidation or reprisal."],
  ok=True)
O("Which of the following is NOT a feature of democracy?",
  ["Rule by one party only", "Free and fair elections",
   "Respect for human rights", "Freedom of the press"],
  ["Democracy requires choice and competition.",
   "<b>Rule by one party only</b> removes that choice, so it is not a feature of democracy."],
  ok=True)
O("To be declared the winner of a presidential election in Ghana, a candidate must obtain",
  ["more than 50% of the valid votes cast", "the highest number of votes, however small",
   "two-thirds of all registered voters", "a majority in every region"],
  ["Ghana's constitution requires an absolute majority, which is why a run-off is possible.",
   "A candidate must obtain <b>more than 50% of the valid votes cast</b>."],
  ok=True)
T("(a) What is democracy? (b) State four features of a democratic government. "
  "(c) Give three reasons why every eligible citizen should vote, and two problems that can spoil an election.",
  ["(a) <b>Democracy is a system of government in which the people rule, either directly or through representatives "
   "whom they freely elect, and in which the government is accountable to them.</b>",
   "(b) Any four: <b>regular free and fair elections</b>; <b>universal adult suffrage</b>; <b>rule of law and an "
   "independent judiciary</b>; <b>respect for fundamental human rights</b>; <b>freedom of speech and of the press</b>; "
   "<b>existence of more than one political party</b>; separation of powers.",
   "(c) Reasons: voting is <b>how citizens choose leaders and policies</b>; it is <b>how a government is changed "
   "peacefully</b>; and it <b>makes leaders accountable</b>, since they know they must face the voters again. "
   "Problems: <b>violence, intimidation and vote-buying</b>; <b>rigging, multiple voting or impersonation</b>; and "
   "inflammatory language that divides the country."],
  marks=12)
extras("democracy",
  plain="Democracy is more than voting once every four years: it also means the law applies to everyone, the press may "
        "criticise, and the loser accepts the result. Ghana's reputation rests on that last point — power changing hands peacefully after a count.",
  examples=[
    E("Why is the Electoral Commission made independent of the government?",
      "Step 1. The government of the day is itself a contestant in the election.",
      "Step 2. If it controlled the referee, it could tilt the result in its own favour.",
      "Step 3. Independence means the commission <b>can be trusted by all parties</b>, which is what makes the result acceptable."),
    E("A candidate loses narrowly and believes the count was wrong. What should he do in a democracy?",
      "Step 1. Not call his supporters onto the streets — that destroys life and property.",
      "Step 2. Collect his evidence from the polling-station results sheets.",
      "Step 3. <b>Petition the court</b>, which has the power to order a recount or a fresh election — the lawful remedy.")])

topic("localgov", "Local government & decentralisation", B, [
  "<b>Decentralisation</b> is the transfer of power, functions and resources from the central government to local "
  "bodies, so that people take part in decisions that affect them.",
  "Ghana has <b>16 regions</b>, each with a Regional Co-ordinating Council, and Metropolitan, Municipal and "
  "District Assemblies (MMDAs) as the highest political authority in each district.",
  "The assembly is made up of elected members (chosen on a <b>non-partisan</b> basis), members appointed by the "
  "President, the Member of Parliament, and the Chief Executive. Below it are urban, town, zonal and area councils "
  "and unit committees.",
  "Functions of an assembly: planning and development of the district, by-laws, markets and lorry parks, sanitation, "
  "basic schools and clinics, feeder roads, and collection of local revenue (rates, tolls, licences).",
  "Sources of funds: the <b>District Assemblies Common Fund</b>, basic rates, property rates, market tolls, "
  "business licences, grants and donor support.",
])
O("The highest political authority in a district in Ghana is the",
  ["District Assembly", "unit committee", "Regional Minister", "chief of the area"],
  ["The unit committee is the lowest tier and the Regional Minister represents central government.",
   "By law the <b>District Assembly</b> is the highest political authority in the district."],
  ok=True)
O("Elections to the District Assembly are held on a",
  ["non-partisan basis", "party basis", "regional basis", "religious basis"],
  ["Local elections are deliberately kept free of party symbols.",
   "They are held on a <b>non-partisan basis</b>, so candidates stand on their own merit."],
  ok=True)
O("The transfer of power and resources from the central government to local bodies is called",
  ["decentralisation", "centralisation", "privatisation", "nationalisation"],
  ["Centralisation is the opposite.", "The transfer downwards is <b>decentralisation</b>."],
  ok=True)
O("Which of the following is a source of revenue for a District Assembly?",
  ["Market tolls and property rates", "Import duties at the ports",
   "Salaries of teachers", "Fines imposed by the Supreme Court"],
  ["Import duties and court fines go to central government.",
   "Assemblies raise money locally from <b>market tolls and property rates</b>, besides the Common Fund."],
  ok=True)
O("The number of administrative regions in Ghana is",
  ["16", "10", "12", "20"],
  ["Six new regions were created in 2019, raising the number from ten.", "Ghana now has <b>16</b> regions."],
  ok=True)
T("(a) What is decentralisation? (b) State four functions of a District Assembly. "
  "(c) Give three benefits of decentralisation to the ordinary citizen, and two problems facing District Assemblies.",
  ["(a) <b>Decentralisation is the transfer of power, functions, responsibilities and resources from the central "
   "government to local government units, so that people can take part in making the decisions that affect their lives.</b>",
   "(b) Any four: <b>preparing and carrying out development plans</b> for the district; <b>making and enforcing "
   "by-laws</b>; <b>providing and maintaining basic services</b> — schools, clinics, markets, lorry parks, boreholes, "
   "feeder roads; <b>sanitation and waste management</b>; <b>collecting local revenue</b>; maintaining security and "
   "settling local disputes with the police and the chiefs.",
   "(c) Benefits: <b>decisions are taken closer to the people</b>, so projects match local needs; <b>citizens can "
   "take part and hold their assembly members to account</b>; and <b>development reaches rural areas</b> rather than "
   "being concentrated in Accra. "
   "Problems: <b>inadequate and delayed funds</b> and a weak local revenue base; <b>shortage of qualified staff</b>; "
   "and <b>political interference and apathy</b>, shown by the low turnout at district assembly elections."],
  marks=12)
extras("localgov",
  plain="Decentralisation is the idea that the people who live with a problem are best placed to solve it. The test of "
        "whether it is working is simple: does the gutter in your town get cleared because somebody in the town decided it, or because somebody in Accra remembered?",
  examples=[
    E("A community needs a borehole. Describe the proper steps to get it through the assembly.",
      "Step 1. Raise it at the unit committee or at a community meeting with the assembly member.",
      "Step 2. The assembly member presents it to the District Assembly, where it is considered for the district development plan.",
      "Step 3. If approved, it is <b>funded from the Common Fund or internally generated revenue</b> and built — and the community helps maintain it."),
    E("Why are district assembly elections held on a non-partisan basis?",
      "Step 1. District work — gutters, markets, school blocks — is practical rather than ideological.",
      "Step 2. Party contests at that level would divide small communities and make co-operation harder.",
      "Step 3. So candidates stand as individuals, and are <b>judged on their own record and ideas</b>.")])

topic("rights", "Human rights & responsibilities", B, [
  "Human rights are the basic entitlements every person has simply by being human. "
  "Chapter 5 of the 1992 Constitution guarantees them in Ghana.",
  "Examples: the right to life; personal liberty; dignity (freedom from torture and slavery); equality before the law; "
  "freedom of speech, assembly, association, movement and religion; the right to own property; the right to education; "
  "and the right to a fair trial.",
  "<b>Children's rights</b>: a name and nationality, parental care, education, health care, "
  "protection from abuse, child labour and child marriage, and the right to be heard.",
  "Every right carries a <b>responsibility</b>: free speech must not become insult or incitement, "
  "and the right to property does not allow you to build on a waterway.",
  "Bodies that protect rights: the courts, the <b>Commission on Human Rights and Administrative Justice (CHRAJ)</b>, "
  "the <b>National Commission for Civic Education (NCCE)</b>, the Legal Aid Commission, "
  "the Domestic Violence and Victim Support Unit (DOVVSU) of the police, and the media.",
])
O("Human rights are the rights a person enjoys because",
  ["he is a human being", "he has paid his taxes",
   "he belongs to a political party", "he is educated"],
  ["They are not earned or bought.",
   "They belong to a person simply <b>because he is a human being</b>."],
  ok=True)
O("The body set up to investigate complaints of human rights abuse and administrative injustice in Ghana is",
  ["CHRAJ", "the Electoral Commission", "the Ghana Revenue Authority", "the Ghana Standards Authority"],
  ["Each body has its own mandate.",
   "Complaints of abuse and injustice go to the <b>Commission on Human Rights and Administrative Justice (CHRAJ)</b>."],
  ok=True)
O("Which of the following is a right of the child?",
  ["The right to education", "The right to vote",
   "The right to drive a vehicle", "The right to marry at fifteen"],
  ["Voting and driving have minimum ages, and marriage below 18 is unlawful.",
   "<b>The right to education</b> is a right of every child."],
  ok=True)
O("The responsibility that goes with the right to freedom of speech is to",
  ["avoid insults and false statements that harm others", "speak only in English",
   "speak only when asked", "praise the government"],
  ["A right is limited by the rights of others.",
   "With free speech goes the duty to <b>avoid insults and false statements that harm others</b>."],
  ok=True)
O("A pupil who is beaten and injured at home should report the matter to",
  ["DOVVSU or a trusted teacher", "no one, because it is a family matter",
   "the chief alone", "his classmates"],
  ["Child abuse is a crime, not a private matter.",
   "The pupil should report to <b>DOVVSU or a trusted teacher</b>, who can involve social welfare and the police."],
  ok=True)
T("(a) State five fundamental human rights guaranteed by the 1992 Constitution. "
  "(b) For any three of them, state the responsibility that goes with it. "
  "(c) Name three institutions that protect human rights in Ghana and give one function of each.",
  ["(a) Any five: <b>the right to life</b>; <b>personal liberty</b>; <b>human dignity</b> (freedom from torture and "
   "slavery); <b>equality before the law</b>; <b>freedom of speech and of the press</b>; <b>freedom of worship</b>; "
   "<b>freedom of movement</b>; <b>the right to own property</b>; <b>the right to education</b>; the right to a fair trial.",
   "(b) <b>Freedom of speech</b> → do not insult, defame or incite others to violence. "
   "<b>The right to own property</b> → do not build on waterways or acquire property by fraud, and pay your property rate. "
   "<b>Freedom of movement</b> → obey traffic laws and respect other people's premises and privacy.",
   "(c) <b>The courts</b> — hear cases and enforce rights, and can order release or compensation. "
   "<b>CHRAJ</b> — investigates complaints of human rights abuse and administrative injustice free of charge. "
   "<b>NCCE</b> — educates citizens on the constitution, their rights and their civic responsibilities. "
   "(DOVVSU, the Legal Aid Commission and the media are equally acceptable.)"],
  marks=12)
extras("rights",
  plain="Rights and responsibilities are two sides of one coin. Your right to play music is real; so is your neighbour's "
        "right to sleep. Where they meet, the rule is that your freedom stops where another person's begins — and the courts, CHRAJ and the NCCE exist to keep that line clear.",
  examples=[
    E("A landlord locks a tenant's room and seizes her belongings over unpaid rent. Which rights are involved and what should she do?",
      "Step 1. She has a right to own property and a right not to be deprived of it except by law.",
      "Step 2. The landlord must go to court; he may not take the law into his own hands.",
      "Step 3. She should <b>report to the police and seek help from the Rent Control Department, Legal Aid or CHRAJ</b>."),
    E("A pupil is withdrawn from school to hawk goods. Explain which of her rights are breached.",
      "Step 1. The right to education is denied, which damages her whole future.",
      "Step 2. Hawking exposes her to road accidents and abuse — a breach of the right to protection from child labour and harm.",
      "Step 3. Her parents' poverty may be real, but the law is clear: <b>she must be in school, and social welfare can help the family</b>.")])

topic("leadership", "Leadership & followership", B, [
  "A leader is a person who guides, directs and influences others towards a goal. "
  "Leadership exists in the home, school, church, mosque, community and nation.",
  "Qualities of a good leader: honesty and integrity, selflessness, courage, tolerance, discipline, hard work, "
  "fairness, humility, good communication and the ability to take advice.",
  "Types: <b>democratic</b> (consults and involves others), <b>autocratic</b> (decides alone), "
  "<b>laissez-faire</b> (leaves others to do as they wish).",
  "Good followership matters just as much: obedience to lawful authority, loyalty, hard work, honest advice, "
  "constructive criticism and co-operation.",
  "Leaders are accountable: they must explain their actions and answer for the use of public funds.",
])
O("A good leader is best described as one who",
  ["guides and serves the people honestly", "gives orders and is never questioned",
   "makes himself rich from the office", "does whatever the loudest people want"],
  ["Leadership in a democracy is service, not privilege.",
   "A good leader <b>guides and serves the people honestly</b>."],
  ok=True)
O("A leader who takes all decisions alone without consulting others practises",
  ["autocratic leadership", "democratic leadership",
   "laissez-faire leadership", "collective leadership"],
  ["A democratic leader consults; a laissez-faire leader leaves others alone.",
   "Deciding everything alone is <b>autocratic leadership</b>."],
  ok=True)
O("Which of the following is a quality of a good follower?",
  ["Offering honest advice to the leader", "Agreeing with everything the leader says",
   "Refusing to do any assigned work", "Spreading rumours about the leader"],
  ["Flattery and sabotage both weaken a group.",
   "A good follower <b>offers honest advice to the leader</b>, and then co-operates in carrying out the decision."],
  ok=True)
O("Accountability in leadership means that a leader",
  ["must explain and answer for his actions", "may do as he pleases",
   "is above the law", "cannot be removed from office"],
  ["Holding office carries a duty to report.",
   "Accountability means a leader <b>must explain and answer for his actions</b>, especially the use of public money."],
  ok=True)
O("A school prefect who reports a wrong done by his own friend shows",
  ["fairness and integrity", "disloyalty to friends", "weakness", "fear of the teachers"],
  ["Leadership is service to the whole school, not to a few friends.",
   "Reporting the wrong shows <b>fairness and integrity</b>."],
  ok=True)
T("(a) Give five qualities of a good leader. (b) State three qualities of a good follower. "
  "(c) Explain, with examples, three ways in which bad leadership can harm a community.",
  ["(a) Any five: <b>honesty and integrity</b>; <b>selflessness</b> (putting the group before himself); "
   "<b>courage</b> to take hard decisions; <b>tolerance</b> of criticism and of other views; <b>fairness</b> and "
   "impartiality; <b>discipline and hard work</b>; <b>humility and willingness to listen</b>; good communication; "
   "vision and the ability to plan.",
   "(b) Any three: <b>obedience to lawful authority and the rules</b>; <b>loyalty and co-operation</b>; "
   "<b>honest advice and constructive criticism</b>; <b>hard work and punctuality</b>; <b>respect for the leader and "
   "for other members</b>.",
   "(c) <b>Misuse of funds</b> — money meant for a school block or a borehole is diverted, so children continue to "
   "study under trees. <b>Division and conflict</b> — a leader who favours his own family or tribe breaks the unity of "
   "the community and can trigger violence. <b>Loss of trust and development</b> — when leaders are known to be "
   "dishonest, citizens refuse to pay rates and donors withdraw support, so projects stop altogether."],
  marks=12)
extras("leadership",
  plain="Leadership is not a title; it is a job of service that can be done well or badly. And every leader is also a "
        "follower of someone — which is why the exam asks about both. The qualities on both lists overlap: honesty, hard work and respect for others.",
  examples=[
    E("A class captain is told by the teacher to collect money for a trip. How should he show accountability?",
      "Step 1. Record every payment in a list with each pupil's name and the amount.",
      "Step 2. Hand the money over promptly and get a receipt.",
      "Step 3. <b>Report back to the class on what was collected and what was spent</b> — that is accountability in practice."),
    E("Which style of leadership suits a school environment club, and why?",
      "Step 1. The members are volunteers who need to feel ownership of the project.",
      "Step 2. An autocratic leader would silence their ideas; a laissez-faire one would let the club drift.",
      "Step 3. <b>Democratic leadership</b> works best — consult the members, agree a plan together, then insist that the agreed plan is carried out.")])

topic("conflict", "Conflict, peace & national security", B, [
  "Conflict is a disagreement or clash between individuals or groups. Causes include land and boundary disputes, "
  "chieftaincy succession, religious and ethnic intolerance, politics, unequal distribution of resources, "
  "and poverty and unemployment.",
  "Effects: loss of life and property, displacement of people, closure of schools and markets, "
  "loss of investment, hunger, and lasting hatred.",
  "Peaceful resolution: dialogue and negotiation, mediation by elders or a neutral party, arbitration, "
  "the courts, the National Peace Council and the House of Chiefs.",
  "Peace is more than the absence of fighting: it is a state in which people live together with justice, tolerance "
  "and respect for one another's rights.",
  "The security services — the Police, the Armed Forces, Immigration, Prisons, Fire Service and National Security — "
  "protect life, property and the borders.",
])
O("Which of the following is a common cause of conflict in Ghanaian communities?",
  ["Disputes over land and chieftaincy", "Celebration of festivals",
   "Payment of school fees", "Building of boreholes"],
  ["Festivals and boreholes usually unite people.",
   "<b>Disputes over land and chieftaincy</b> are among the commonest causes of local conflict."],
  ok=True)
O("The best first step in resolving a conflict between two communities is",
  ["dialogue between the parties", "a fight to decide who is stronger",
   "both sides arming themselves", "ignoring the problem"],
  ["Force deepens the quarrel and the courts take time.",
   "The best first step is <b>dialogue between the parties</b>, often with elders as mediators."],
  ok=True)
O("A major effect of conflict on children is that",
  ["their schooling is interrupted", "they learn new skills",
   "they get more food", "they travel abroad"],
  ["When a town is unsettled, schools close and families flee.",
   "So <b>their schooling is interrupted</b>, and many never return to class."],
  ok=True)
O("The body established to help resolve conflicts and promote peace in Ghana is the",
  ["National Peace Council", "National Lottery Authority",
   "Ghana Tourism Authority", "Public Utilities Regulatory Commission"],
  ["Each of these bodies has a different purpose.",
   "Peace-building is the work of the <b>National Peace Council</b>, together with the houses of chiefs and religious bodies."],
  ok=True)
O("Peace in a country is best described as a situation in which",
  ["people live together with justice and respect for rights", "there are many soldiers on the streets",
   "nobody disagrees with anybody", "all political parties are banned"],
  ["Silence enforced by force is not peace, and disagreement is normal in a democracy.",
   "Peace is a situation in which <b>people live together with justice and respect for rights</b>, settling differences without violence."],
  ok=True)
T("(a) State four causes of conflict in Ghana. (b) Describe four effects of conflict on national development. "
  "(c) Suggest four ways of maintaining peace in a community.",
  ["(a) Any four: <b>land and boundary disputes</b>; <b>chieftaincy succession disputes</b>; <b>ethnic or religious "
   "intolerance</b>; <b>political rivalry and inflammatory language</b>; <b>unequal sharing of resources and "
   "development projects</b>; <b>poverty and unemployment</b>, especially among the youth.",
   "(b) <b>Loss of lives and destruction of property</b>, including schools and clinics. "
   "<b>Displacement of people</b>, who become refugees and lose their farms and jobs. "
   "<b>Economic loss</b> — markets close, investors stay away, and government money goes to security instead of "
   "development. <b>Interruption of education and health services</b>, whose effects last a generation.",
   "(c) <b>Dialogue and tolerance</b> — settle differences by talking, and respect other tribes and religions. "
   "<b>Use of the proper institutions</b> — the courts, the House of Chiefs, the National Peace Council — instead of "
   "taking the law into one's own hands. <b>Fair distribution of development projects and jobs</b>, so no group feels "
   "cheated. <b>Civic education and responsible media</b>, avoiding rumour, insult and hate speech."],
  marks=12)
extras("conflict",
  plain="Conflict itself is normal — people want different things. What matters is how it is handled: talk and the "
        "community grows, fight and everybody loses. Notice that almost every cause on the list is a question of fairness, which is why justice and peace are always discussed together.",
  examples=[
    E("Two families claim the same plot of land. Outline the peaceful route to a settlement.",
      "Step 1. Each side states its claim before the family heads or the chief's court, with witnesses and documents.",
      "Step 2. Elders mediate and try to find a settlement both can accept.",
      "Step 3. If that fails, the dispute goes to the <b>law courts, whose decision binds both sides</b> — never to machetes."),
    E("Why is hate speech during an election campaign dangerous?",
      "Step 1. It turns a contest of ideas into a quarrel between groups of people.",
      "Step 2. Supporters who believe their group is under attack may answer with violence.",
      "Step 3. The result can be <b>loss of life, destruction of property and years of mistrust</b> — which is why the law punishes it.")])

topic("corruption", "Corruption & accountability", B, [
  "Corruption is the dishonest use of public office or trust for private gain. Forms: bribery, embezzlement, "
  "misappropriation of funds, nepotism and favouritism, extortion, examination malpractice, "
  "padded payrolls and inflated contracts.",
  "Causes: greed, poverty and low pay, weak supervision, delays in the justice system, "
  "and a public that accepts and even admires sudden wealth.",
  "Effects: projects are not completed or are poorly done; money meant for schools, clinics and roads disappears; "
  "prices rise; investors stay away; and citizens lose faith in the state.",
  "Bodies that fight it: the <b>Office of the Special Prosecutor</b>, <b>CHRAJ</b>, the <b>Auditor-General</b>, "
  "the Economic and Organised Crime Office (EOCO), the Police, the courts, Parliament's Public Accounts Committee, "
  "and the media.",
  "<b>Accountability</b> and <b>transparency</b> are the cure: public accounts audited and published, "
  "open procurement, assets declared, whistle-blowers protected, and citizens who refuse to pay or take a bribe.",
])
O("Corruption may best be defined as",
  ["the dishonest use of public office for private gain", "working overtime for extra pay",
   "borrowing money from a bank", "paying taxes late"],
  ["The essential element is abusing a position of trust for oneself.",
   "Corruption is <b>the dishonest use of public office for private gain</b>."],
  ok=True)
O("Which of the following is an example of corruption?",
  ["A contractor paying an official to win a contract", "A trader giving a customer a discount",
   "A teacher giving extra classes free of charge", "A farmer selling maize at the market price"],
  ["Only one of these involves abusing an official position.",
   "<b>A contractor paying an official to win a contract</b> is bribery, a form of corruption."],
  ok=True)
O("The office created specifically to investigate and prosecute corruption in Ghana is the",
  ["Office of the Special Prosecutor", "Ghana Revenue Authority",
   "Electoral Commission", "Ghana National Service Authority"],
  ["The others have different mandates.",
   "Corruption cases are investigated and prosecuted by the <b>Office of the Special Prosecutor</b>, alongside EOCO and CHRAJ."],
  ok=True)
O("A direct effect of corruption on education in a district is that",
  ["funds meant for classrooms are diverted", "more teachers are trained",
   "textbooks become cheaper", "school fees are abolished"],
  ["Money stolen cannot build anything.",
   "<b>Funds meant for classrooms are diverted</b>, so pupils continue to learn under trees or in unsafe buildings."],
  ok=True)
O("The officer whose duty is to audit the accounts of all public institutions in Ghana is the",
  ["Auditor-General", "Attorney-General", "Accountant of the district", "Chief Justice"],
  ["The Attorney-General advises on law, and the Chief Justice heads the Judiciary.",
   "Public accounts are examined by the <b>Auditor-General</b>, whose report goes to Parliament."],
  ok=True)
T("(a) State four forms of corruption. (b) Give four effects of corruption on national development. "
  "(c) Suggest four measures for controlling corruption in Ghana.",
  ["(a) Any four: <b>bribery</b>; <b>embezzlement or misappropriation of public funds</b>; <b>nepotism and "
   "favouritism</b> in appointments and contracts; <b>extortion</b> (demanding money for a service that is free); "
   "<b>inflated contracts and padded payrolls</b>; <b>examination malpractice</b>; smuggling and tax evasion.",
   "(b) <b>Development projects are abandoned or badly built</b>, because the money has gone. "
   "<b>Poor public services</b> — understocked clinics, overcrowded classrooms, bad roads. "
   "<b>Loss of government revenue</b> through tax evasion and smuggling, so there is less to spend on everyone. "
   "<b>Loss of investor and donor confidence</b>, which means fewer jobs; and a general <b>loss of trust in the "
   "state</b>, which makes people unwilling to pay taxes themselves.",
   "(c) <b>Strengthen and resource the anti-corruption bodies</b> — the Special Prosecutor, CHRAJ, EOCO, the "
   "Auditor-General — and let them act without interference. <b>Punish offenders promptly, whoever they are</b>, and "
   "recover the stolen money, so that corruption stops being profitable. <b>Make government business transparent</b> — "
   "open procurement, published accounts, declaration of assets, and digital payment of fees to remove cash from the "
   "counter. <b>Civic education and protection for whistle-blowers</b>, so that citizens refuse to give or take bribes "
   "and can report safely."],
  marks=12)
extras("corruption",
  plain="Corruption is not a victimless offence: every cedi diverted is a desk not bought, a drug not stocked, a culvert "
        "not built. Notice too that it takes two — the one who demands and the one who pays — which is why a citizen who refuses to offer a bribe is part of the cure.",
  examples=[
    E("A driver is stopped for a traffic offence and offers the officer money to let him go. Who is guilty?",
      "Step 1. The officer who accepts money to overlook an offence commits bribery.",
      "Step 2. The driver who offers it commits bribery too — giving is as much an offence as taking.",
      "Step 3. <b>Both are guilty</b>, and the proper course is for the driver to accept the lawful penalty."),
    E("Explain how the Auditor-General's report helps fight corruption.",
      "Step 1. Every public institution's accounts are examined independently.",
      "Step 2. Missing or wrongly spent money is named publicly in a report laid before Parliament.",
      "Step 3. Parliament's Public Accounts Committee then <b>questions the officers concerned in public</b>, and cases can be sent for prosecution and recovery.")])
