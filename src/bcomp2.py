"""BECE Computing - Networks and the internet; programming and digital citizenship."""
from core import *
import draw

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}
C, D = "C. Networks & the internet", "D. Programming & digital life"

topic("network", "Communication networks", C, [
  "A <b>network</b> is two or more computers linked together so that they can share data, "
  "programs and devices such as printers.",
  "Types by size: <b>LAN</b> (local area network — one building or school), "
  "<b>MAN</b> (metropolitan — a town or city), <b>WAN</b> (wide area network — across countries; "
  "the internet is the largest WAN). A <b>PAN</b> links a person's own devices, for example by Bluetooth.",
  "Network devices: <b>modem</b> (converts signals for transmission), <b>router</b> (directs data between networks), "
  "switch and hub (join computers within a LAN), network interface card, access point, cables and connectors.",
  "Transmission media: <b>wired</b> — twisted pair, coaxial cable, fibre optic (fastest); "
  "<b>wireless</b> — radio, Wi-Fi, Bluetooth, microwave, satellite.",
  "Topologies: <b>star</b> (all nodes to a central device), <b>ring</b>, <b>bus</b>, and <b>mesh</b>.",
  "Advantages of networking: sharing of files, printers and internet access; central backup; communication. "
  "Disadvantages: cost of setting up, spread of viruses, risk of unauthorised access, "
  "and total disruption if the server fails.",
])
O("A network that covers a single school building is a",
  ["LAN", "WAN", "MAN", "PAN"],
  ["A WAN spans countries and a MAN a city.", "A single building is served by a <b>LAN</b> (local area network)."],
  ok=True)
O("The largest wide area network in the world is the",
  ["internet", "intranet", "extranet", "ethernet"],
  ["An intranet is private to one organisation and ethernet is a cabling standard.",
   "The largest WAN is the <b>internet</b>."],
  ok=True)
O("The device that directs data between two different networks is the",
  ["router", "monitor", "scanner", "printer"],
  ["The other three are input or output devices.", "Data is directed between networks by a <b>router</b>."],
  ok=True)
O("Which transmission medium carries data fastest over long distances?",
  ["Fibre optic cable", "Twisted pair cable", "Coaxial cable", "Infrared link"],
  ["Copper cables lose signal strength over distance, and an infrared link works only over a few metres, in line of sight.",
   "<b>Fibre optic cable</b> carries data fastest and furthest, using light."],
  ok=True)
O("One disadvantage of networking computers is that",
  ["viruses can spread quickly from one computer to others", "files cannot be shared",
   "printers must be bought for each computer", "communication becomes slower"],
  ["The other three are what networking prevents.",
   "<b>Viruses can spread quickly from one computer to others</b>, and unauthorised access becomes a risk."],
  ok=True)
T("(a) What is a computer network? (b) State three types of network by size and where each is used. "
  "(c) Give three advantages and two disadvantages of networking.",
  ["(a) <b>A computer network is a group of two or more computers and other devices connected together, by cable or "
   "wirelessly, so that they can communicate and share data, programs and resources such as printers and internet "
   "access.</b>",
   "(b) <b>LAN (local area network)</b> — within one building or compound, such as a school computer laboratory or an "
   "office. <b>MAN (metropolitan area network)</b> — across a town or city, such as the branches of a bank in Kumasi. "
   "<b>WAN (wide area network)</b> — across regions and countries; the internet is the largest example.",
   "(c) Advantages: <b>sharing of hardware</b> — one printer serves many computers, which saves money; "
   "<b>sharing of files and programs</b>, so that everyone works from the same up-to-date data; and "
   "<b>communication and central backup</b> — email, messaging and one secure copy of important files. "
   "Disadvantages: <b>cost of setting up and maintaining</b> the cables, devices and expertise; and "
   "<b>security risks</b> — viruses spread quickly, data can be intercepted, and if the server fails the whole "
   "network stops working."],
  marks=12, fig=draw.flow(["PAN: one person's devices (Bluetooth)", "LAN: one building (school lab)",
                           "MAN: one city (bank branches)", "WAN: countries (the internet)"],
                          label="Networks by size"))
extras("network",
  plain="A network exists to share — files, printers, internet, messages. Sort the questions by scale (PAN, LAN, MAN, "
        "WAN) and by device (modem converts, router directs, switch joins), and this topic is straightforward.",
  examples=[
    E("A school has 20 computers and one printer. Explain how a LAN helps, and name the devices needed.",
      "Step 1. All 20 computers can print to the one printer, instead of buying twenty.",
      "Step 2. Pupils' files can be stored centrally and backed up once, and the internet line shared.",
      "Step 3. Devices needed: <b>a switch, network cables (or a wireless access point), network cards, and a router plus modem for internet</b>."),
    E("Why does a village with no telephone lines sometimes get internet by satellite?",
      "Step 1. Wired media need cable to be laid all the way to the user.",
      "Step 2. Where that is too costly or the terrain too difficult, no cable arrives.",
      "Step 3. <b>Satellite is wireless and needs only a dish and power</b>, so it reaches places cable has not.")])

topic("internet", "The internet & the World Wide Web", C, [
  "The <b>internet</b> is a global network of networks. The <b>World Wide Web</b> is the collection of "
  "linked pages and documents carried on it — the two are not the same thing.",
  "To get online you need a computer or phone, a modem or router, and an account with an "
  "<b>Internet Service Provider (ISP)</b>.",
  "A <b>browser</b> (Chrome, Firefox, Edge, Opera, Safari) displays web pages. "
  "A <b>search engine</b> (Google, Bing, DuckDuckGo) finds them.",
  "A <b>URL</b> is a web address, for example https://www.waecgh.org — <i>https</i> is the protocol, "
  "<i>www.waecgh.org</i> is the domain. Domain endings: .com (commercial), .org (organisation), "
  ".edu (education), .gov (government), .gh (Ghana).",
  "Searching well: use specific words, put a phrase in quotation marks, and check <b>who</b> published the page "
  "and <b>when</b>. Compare at least two sources before believing a claim.",
  "Uses: research and learning, email, news, banking, mobile money, buying and selling, "
  "job hunting, and keeping in touch.",
])
O("The World Wide Web is",
  ["the collection of linked pages carried on the internet", "the same thing as the internet",
   "a type of computer", "a search engine"],
  ["The internet is the network; the Web is one service running on it.",
   "The Web is <b>the collection of linked pages carried on the internet</b>."],
  ok=True)
O("A program used to view web pages is called a",
  ["browser", "search engine", "server", "modem"],
  ["A search engine is a website that finds pages; a browser displays them.",
   "A <b>browser</b> such as Chrome or Firefox views web pages."],
  ok=True)
O("In the address https://www.waecgh.org, the part 'www.waecgh.org' is the",
  ["domain name", "protocol", "search term", "password"],
  ["'https' is the protocol.", "'www.waecgh.org' is the <b>domain name</b>."],
  ok=True)
O("A company that provides internet access to homes and schools is called a/an",
  ["Internet Service Provider", "Internet Security Programme",
   "Information System Provider", "International Server Provider"],
  ["The standard term is abbreviated ISP.", "It is an <b>Internet Service Provider</b>."],
  ok=True)
O("Before using information found on a website for a school project, a pupil should first",
  ["check who published it and when", "copy it word for word",
   "print the whole page", "share it on social media"],
  ["Not everything online is true or current.",
   "He should <b>check who published it and when</b>, and compare it with another source."],
  ok=True)
T("(a) State the difference between the internet and the World Wide Web. "
  "(b) Name three browsers and two search engines. (c) Give four uses of the internet to a J.H.S. pupil and "
  "two precautions he should take when using information from a website.",
  ["(a) The <b>internet</b> is the worldwide system of interconnected computer networks — the infrastructure. "
   "The <b>World Wide Web</b> is one of the services that run on it: the vast collection of linked web pages and "
   "documents viewed with a browser. Email, file transfer and online games also use the internet but are not part of "
   "the Web.",
   "(b) Browsers: <b>Google Chrome, Mozilla Firefox, Microsoft Edge</b> (also Opera, Safari). "
   "Search engines: <b>Google, Bing</b> (also DuckDuckGo, Yahoo).",
   "(c) Uses: <b>research for assignments and past-question practice</b>; <b>online lessons, videos and e-books</b>; "
   "<b>email and messaging</b> to teachers, family and study groups; <b>news and examination information</b> — for "
   "example checking the WAEC timetable; and learning new skills such as coding or typing. "
   "Precautions: <b>check the source and date</b> of the information, preferring official sites such as waecgh.org; "
   "<b>compare at least two sources</b> before accepting a claim; and <b>never copy word for word</b> — rewrite in your "
   "own words and acknowledge the source."],
  marks=12)
extras("internet",
  plain="Two distinctions carry most of the marks here: internet versus Web, and browser versus search engine. Beyond "
        "that, the syllabus wants judgement — the skill is not finding information, which is easy, but deciding whether to trust it.",
  examples=[
    E("A pupil finds two different answers to the same question online. How should he decide?",
      "Step 1. Look at who published each page — an official body, a school, a newspaper, or an anonymous blog?",
      "Step 2. Look at the date; facts such as prices, officeholders and syllabuses change.",
      "Step 3. <b>Prefer the official and more recent source, and look for a third page to confirm it</b>."),
    E("Explain the parts of the URL https://moe.gov.gh/curriculum",
      "Step 1. <b>https</b> — the protocol, and the 's' means the connection is encrypted.",
      "Step 2. <b>moe.gov.gh</b> — the domain: a government (gov) body in Ghana (gh).",
      "Step 3. <b>/curriculum</b> — the particular page or folder on that site.")])

topic("email", "Email & online communication", C, [
  "<b>Email</b> (electronic mail) is the sending of messages between users over a network. "
  "Services: Gmail, Yahoo Mail, Outlook.",
  "An email address has two parts separated by @: the <b>user name</b> and the <b>domain</b> — "
  "for example <i>amamensah@gmail.com</i>. It contains no spaces.",
  "Parts of a message: <b>To</b>, <b>Cc</b> (copy, visible to all), <b>Bcc</b> (blind copy, hidden), "
  "<b>Subject</b>, the body, the signature and <b>attachments</b>.",
  "Folders: Inbox, Sent, Drafts, Spam (junk), Trash. Actions: compose, reply, reply all, forward, delete.",
  "Advantages over a letter: speed, low cost, attachments, copies to many people at once, and a record kept. "
  "Disadvantages: needs internet and power, spam and scams, viruses in attachments, and no personal touch.",
  "<b>Netiquette</b>: use a clear subject line, write in proper sentences, do not TYPE IN CAPITALS "
  "(it reads as shouting), be polite, do not forward chain messages, and never open an attachment "
  "from a stranger.",
])
O("Which of the following is a correctly formed email address?",
  ["amamensah@gmail.com", "ama mensah@gmail.com", "amamensah.gmail.com", "amamensah@gmail@com"],
  ["An email address has exactly one @ and no spaces.",
   "<b>amamensah@gmail.com</b> is correctly formed."],
  ok=True)
O("The part of an email used to send a hidden copy to another person is",
  ["Bcc", "Cc", "To", "Subject"],
  ["Cc copies are visible to all recipients.",
   "<b>Bcc</b> (blind carbon copy) sends a copy that other recipients cannot see."],
  ok=True)
O("A file sent along with an email message is called an",
  ["attachment", "inbox", "archive", "extension"],
  ["The inbox is where mail arrives.", "A file sent with a message is an <b>attachment</b>."],
  ok=True)
O("Unwanted and unsolicited email is called",
  ["spam", "draft", "signature", "forward"],
  ["A draft is a message you have not yet sent.", "Unwanted bulk email is <b>spam</b> (junk mail)."],
  ok=True)
O("Typing an email entirely in capital letters is poor netiquette because it",
  ["reads as if you are shouting", "takes longer to type",
   "cannot be delivered", "uses more data"],
  ["It delivers perfectly well — the problem is tone.",
   "Capitals <b>read as if you are shouting</b> at the recipient."],
  ok=True)
T("(a) Name the two parts of an email address and explain each, using an example. "
  "(b) State four advantages and two disadvantages of email compared with an ordinary letter. "
  "(c) Give four rules of netiquette.",
  ["(a) In <b>amamensah@gmail.com</b>: the part before the @ is the <b>user name</b>, which identifies the particular "
   "account holder; the part after the @ is the <b>domain name</b>, which identifies the mail service or organisation "
   "hosting the account. The @ separates the two, and the address contains no spaces.",
   "(b) Advantages: <b>speed</b> — it arrives in seconds anywhere in the world; <b>low cost</b>, with no stamp or "
   "transport; <b>attachments</b> — documents, photographs and spreadsheets can be sent with the message; "
   "<b>one message can be sent to many people at once</b>, and <b>a copy is kept automatically</b> in Sent items. "
   "Disadvantages: it <b>requires electricity, a device and internet access</b>; and it carries risks — "
   "<b>spam, scams and viruses in attachments</b>, besides lacking the personal touch of a handwritten letter.",
   "(c) Any four: <b>use a clear, specific subject line</b>; <b>write in proper sentences and check the spelling</b>; "
   "<b>do not type in capital letters</b>, which reads as shouting; <b>be polite and avoid insults or sarcasm</b>; "
   "<b>do not forward chain letters or spam</b>; <b>do not open attachments from strangers</b>; and reply within a "
   "reasonable time."],
  marks=12)
extras("email",
  plain="Email is the first piece of professional communication most pupils will own. The mechanics are easy; what the "
        "syllabus is really teaching is tone — a clear subject, complete sentences, no capitals, and no attachment from a stranger.",
  examples=[
    E("Write a suitable subject line and opening for an email to a headmaster requesting a transcript.",
      "Step 1. Subject: <b>Request for BECE transcript — Ama Mensah, 2026 candidate</b>. Specific, so it is not mistaken for spam.",
      "Step 2. Opening: 'Dear Sir, I am writing to request a copy of my academic transcript for use in my application to…'",
      "Step 3. End with a thank-you, your full name and index number — <b>never 'Hi' and never in capitals</b>."),
    E("An email says a pupil has won a phone and must click a link to claim it. What should she do and why?",
      "Step 1. She entered no competition, so the claim is almost certainly false.",
      "Step 2. Such links lead to pages that steal passwords, or to downloads that install malware.",
      "Step 3. She should <b>delete it, mark it as spam, and click nothing</b>.")])

topic("netsafety", "Online safety, cybercrime & digital citizenship", C, [
  "Cybercrime is crime committed with computers or over networks: <b>hacking</b>, "
  "<b>phishing</b> (fake messages that trick you into giving passwords or money), identity theft, "
  "online fraud (<i>sakawa</i>), cyberbullying, spreading of viruses, and software piracy.",
  "<b>Malware</b> includes viruses, worms, trojans, spyware and ransomware. Signs of infection: "
  "the computer slows down, files disappear or will not open, strange messages appear, "
  "and programs start by themselves.",
  "Protection: a <b>strong password</b> (long, mixed letters, numbers and symbols, not a name or birthday), "
  "a different password for each account, two-step verification, an updated antivirus, "
  "a firewall, software updates, and regular backups.",
  "Personal safety: never share your password, home address, school or a photograph with a stranger online; "
  "never agree to meet someone you met online without telling a parent; "
  "and tell a trusted adult at once about any threatening or indecent message.",
  "Digital footprint: anything you post can be copied, saved and found years later — "
  "by a school, an employer or a stranger. Post nothing you would not want a parent to see.",
  "Good digital citizenship: respect others online, do not bully or insult, do not share false news, "
  "acknowledge the work of others instead of copying, and use devices at reasonable hours.",
])
O("Sending a fake message that tricks a person into revealing a password is called",
  ["phishing", "hacking", "piracy", "spamming"],
  ["Hacking is breaking in directly; piracy is illegal copying.",
   "Tricking someone into revealing details is <b>phishing</b>."],
  ok=True)
O("Which of the following is the strongest password?",
  ["Gh#2026Kw!bz", "password", "12345678", "kofi2010"],
  ["Names, birth years and simple sequences are guessed in seconds.",
   "<b>Gh#2026Kw!bz</b> is long and mixes capitals, small letters, numbers and symbols."],
  ok=True)
O("A program that can copy itself and damage files on a computer is a",
  ["virus", "browser", "driver", "spreadsheet"],
  ["The others are ordinary software.", "A self-copying, damaging program is a <b>virus</b>."],
  ok=True)
O("A pupil receives threatening messages on social media from a classmate. The best action is to",
  ["save the evidence and tell a trusted adult", "reply with worse insults",
   "ignore it and delete the messages", "post the messages publicly"],
  ["Retaliating makes him a party to it, and deleting destroys the evidence.",
   "He should <b>save the evidence and tell a trusted adult</b> — a parent, teacher or counsellor — and block the sender."],
  ok=True)
O("The record of everything a person has posted or done online is called a",
  ["digital footprint", "download history", "hard copy", "database query"],
  ["It persists even after a post is deleted, because others may have copied it.",
   "It is a person's <b>digital footprint</b>."],
  ok=True)
T("(a) Name four forms of cybercrime. (b) State four ways of protecting a computer and its data. "
  "(c) Give three rules a J.H.S. pupil should follow to stay safe online, and explain the term digital footprint.",
  ["(a) Any four: <b>hacking</b> — gaining unauthorised access to a system; <b>phishing</b> — fake messages that trick "
   "people into revealing passwords or sending money; <b>identity theft</b>; <b>online fraud (sakawa)</b>; "
   "<b>cyberbullying</b>; <b>spreading viruses and other malware</b>; <b>software piracy</b>.",
   "(b) <b>Use strong, different passwords</b> and never share them; <b>install and update an antivirus and a "
   "firewall</b>, and scan every flash drive; <b>keep the operating system and programs updated</b>, since updates "
   "close security holes; and <b>back up important files</b> regularly to another drive or the cloud. "
   "(Switching on two-step verification and locking the screen are also valid.)",
   "(c) Rules: <b>never share personal details — password, address, school, phone number — or photographs with "
   "strangers online</b>; <b>never agree to meet someone met online without telling a parent, and never go alone</b>; "
   "<b>report any threatening, indecent or bullying message to a trusted adult at once, keeping the evidence</b>; "
   "and think before posting, because posts can be copied and spread. "
   "<b>A digital footprint is the lasting trail of everything a person posts, searches, likes and shares online, "
   "which can be found and used by others — including schools and employers — years later, even after it has been "
   "deleted.</b>"],
  marks=12)
extras("netsafety",
  plain="Online safety is one place where exam knowledge protects you directly. Two habits do most of the work: a long "
        "password that is not a name or a birthday, and a flat refusal to click links or open attachments you did not expect.",
  examples=[
    E("A message claims to be from a bank and asks a pupil's mother to confirm her PIN by clicking a link. Explain the three warning signs.",
      "Step 1. No genuine bank asks for a PIN or password by message or link — that alone settles it.",
      "Step 2. Such messages create urgency ('your account will be closed today') to stop you thinking.",
      "Step 3. The link's address is not the bank's real domain. <b>Do not click; contact the bank on its published number</b>."),
    E("Why can a post deleted after five minutes still cause harm two years later?",
      "Step 1. Anyone who saw it could screenshot, download or forward it within those minutes.",
      "Step 2. Copies on other people's devices and servers are beyond your control.",
      "Step 3. So the rule is <b>think before posting, not after</b> — that is what a digital footprint means.")])

# ------------------------------------------------------------------ programming
topic("binary", "Number systems in computing", D, [
  "Computers work with two states — on and off — so they use the <b>binary</b> system, "
  "which has only the digits <b>0 and 1</b>. Each digit is a <b>bit</b>.",
  "Place values in binary double from the right: 1, 2, 4, 8, 16, 32, 64, 128.",
  "<b>Binary to decimal</b>: multiply each digit by its place value and add. "
  "1101 = (1×8) + (1×4) + (0×2) + (1×1) = 13.",
  "<b>Decimal to binary</b>: divide by 2 again and again, writing the remainders, then read them upwards. "
  "13 ÷ 2 = 6 r 1; 6 ÷ 2 = 3 r 0; 3 ÷ 2 = 1 r 1; 1 ÷ 2 = 0 r 1 → 1101.",
  "Characters are stored as codes — <b>ASCII</b> gives each letter and symbol a number, "
  "so 'A' is 65 and 'a' is 97.",
  "Other systems used in computing are octal (base 8) and hexadecimal (base 16).",
])
O("The number system used internally by computers is",
  ["binary", "decimal", "octal", "roman"],
  ["It matches the two electrical states of a circuit.", "Computers use the <b>binary</b> system, with digits 0 and 1."],
  ok=True)
O("Convert the binary number 1011 to decimal.",
  ["11", "13", "9", "15"],
  ["Place values from the right are 1, 2, 4, 8.",
   "(1×8) + (0×4) + (1×2) + (1×1) = 8 + 0 + 2 + 1 = <b>11</b>."],
  v=int("1011", 2))
O("Convert the decimal number 10 to binary.",
  ["1010", "1001", "1100", "0110"],
  ["Divide by 2 repeatedly: 10 ÷ 2 = 5 r 0; 5 ÷ 2 = 2 r 1; 2 ÷ 2 = 1 r 0; 1 ÷ 2 = 0 r 1.",
   "Reading the remainders upwards gives <b>1010</b>."],
  ok=(bin(10)[2:] == "1010"))
O("A single binary digit is called a",
  ["bit", "byte", "word", "nibble"],
  ["Eight bits make a byte.", "One binary digit is a <b>bit</b>."],
  ok=True)
O("The code that gives each letter and symbol a number so that it can be stored is",
  ["ASCII", "BIOS", "HTML", "URL"],
  ["BIOS starts the computer, HTML builds web pages and a URL is an address.",
   "Characters are stored using <b>ASCII</b> codes."],
  ok=True)
T("(a) Explain why computers use the binary system. (b) Convert 1 1 0 1 1 (binary) to decimal, showing your working. "
  "(c) Convert 25 (decimal) to binary, showing your working. (d) State how many bits make a byte.",
  ["(a) The electronic circuits of a computer have only <b>two reliable states — on and off</b> (high voltage and low "
   "voltage). These two states match the two binary digits 1 and 0 exactly, so data can be represented and processed "
   "without ambiguity. A ten-state circuit would be far harder to build reliably.",
   "(b) Place values from the right: 1, 2, 4, 8, 16. "
   "(1×16) + (1×8) + (0×4) + (1×2) + (1×1) = 16 + 8 + 0 + 2 + 1 = <b>27</b>.",
   "(c) 25 ÷ 2 = 12 r <b>1</b>;  12 ÷ 2 = 6 r <b>0</b>;  6 ÷ 2 = 3 r <b>0</b>;  3 ÷ 2 = 1 r <b>1</b>;  "
   "1 ÷ 2 = 0 r <b>1</b>. Reading the remainders upwards: <b>11001</b>. "
   "(Check: 16 + 8 + 0 + 0 + 1 = 25. ✓)",
   "(d) <b>8 bits</b> make one byte."],
  marks=12, ok=(int("11011", 2) == 27 and bin(25)[2:] == "11001"))
extras("binary",
  plain="Binary looks strange only until you notice it is ordinary place value with 2 instead of 10. Write the place "
        "values 1, 2, 4, 8, 16, 32 above the digits and every conversion becomes addition.",
  examples=[
    E("Convert 100101 to decimal.",
      "Step 1. Write the place values above, from the right: 32, 16, 8, 4, 2, 1.",
      "Step 2. The 1s sit under 32, 4 and 1.",
      "Step 3. 32 + 4 + 1 = <b>37</b>."),
    E("Convert 40 to binary.",
      "Step 1. Find the largest place value not exceeding 40: that is 32, so there is a 1 there and 8 remains.",
      "Step 2. 8 is itself a place value, so put 1 under 8 and 0 under 16.",
      "Step 3. Fill zeros elsewhere: 32 + 8 = 40 gives <b>101000</b>. (Check by repeated division if unsure.)")])

topic("algorithm", "Algorithms, flowcharts & programming", D, [
  "An <b>algorithm</b> is a finite, ordered set of clear steps for solving a problem. "
  "It must have a beginning and an end, and each step must be unambiguous.",
  "<b>Pseudocode</b> writes the algorithm in plain structured words; a <b>flowchart</b> draws it.",
  "Flowchart symbols: <b>oval</b> — start/stop (terminal); <b>parallelogram</b> — input/output; "
  "<b>rectangle</b> — process; <b>diamond</b> — decision; <b>arrows</b> — flow of control.",
  "Control structures: <b>sequence</b> (one step after another), <b>selection</b> (if … then … else), "
  "<b>repetition / loop</b> (repeat while a condition holds).",
  "A <b>program</b> is an algorithm written in a programming language. "
  "Block-based: Scratch. Text-based: Python, Java, C, Visual Basic. "
  "A <b>bug</b> is an error, and <b>debugging</b> is finding and removing it.",
  "Webpages are built with <b>HTML</b> for structure, <b>CSS</b> for appearance and "
  "<b>JavaScript</b> for behaviour.",
])
O("An algorithm may best be described as",
  ["a set of ordered steps for solving a problem", "a programming language",
   "a type of computer", "an error in a program"],
  ["A language is how you write it; an error is a bug.",
   "An algorithm is <b>a set of ordered steps for solving a problem</b>."],
  ok=True)
O("In a flowchart, a decision is represented by a",
  ["diamond", "rectangle", "oval", "parallelogram"],
  ["Rectangles are processes, ovals are start and stop, parallelograms are input and output.",
   "A decision is shown by a <b>diamond</b>."],
  ok=True)
O("The symbol used to show the beginning or end of a flowchart is the",
  ["oval", "diamond", "rectangle", "arrow"],
  ["Arrows show the direction of flow.", "Start and stop are shown with an <b>oval</b> (terminal symbol)."],
  ok=True)
O("Which of these is a block-based programming language designed for beginners?",
  ["Scratch", "Python", "Java", "C"],
  ["The others are text-based languages.",
   "<b>Scratch</b> is block-based: you drag blocks together instead of typing code."],
  ok=True)
O("Finding and correcting errors in a program is called",
  ["debugging", "compiling", "formatting", "booting"],
  ["Compiling translates the program and booting starts the computer.",
   "Removing errors is <b>debugging</b>."],
  ok=True)
T("(a) State four features of a good algorithm. (b) Write an algorithm, in steps, to find the average of three "
  "numbers. (c) Draw a flowchart for the same problem, naming the symbol used at each stage. "
  "(d) Explain the terms bug and debugging.",
  ["(a) It must have a <b>clear beginning and a definite end</b>; each step must be <b>precise and unambiguous</b>; "
   "it must have a <b>finite number of steps</b> (it cannot run for ever); and it must be <b>effective — it actually "
   "solves the problem</b> for all valid inputs. (Being independent of any particular programming language is also "
   "acceptable.)",
   "(b) <b>Step 1</b> Start. <b>Step 2</b> Input the three numbers A, B and C. "
   "<b>Step 3</b> Compute SUM = A + B + C. <b>Step 4</b> Compute AVERAGE = SUM ÷ 3. "
   "<b>Step 5</b> Output AVERAGE. <b>Step 6</b> Stop.",
   "(c) <b>Oval</b> (Start) → <b>parallelogram</b> (Input A, B, C) → <b>rectangle</b> (SUM = A + B + C) → "
   "<b>rectangle</b> (AVERAGE = SUM/3) → <b>parallelogram</b> (Output AVERAGE) → <b>oval</b> (Stop), "
   "with arrows joining them in that order.",
   "(d) A <b>bug</b> is an error or fault in a program that makes it fail or give a wrong result. "
   "<b>Debugging</b> is the process of finding, locating and correcting such errors, usually by testing the program "
   "with known data and checking the output step by step."],
  marks=12, fig=draw.flow(["Start (oval)", "Input A, B, C (parallelogram)", "SUM = A + B + C (rectangle)",
                           "AVERAGE = SUM / 3 (rectangle)", "Output AVERAGE (parallelogram)", "Stop (oval)"],
                          label="Flowchart: average of three numbers"))
extras("algorithm",
  plain="An algorithm is just a recipe written carefully enough that somebody who knows nothing could follow it. Practise "
        "by writing out an everyday task — making tea, or deciding whether a pupil has passed — in numbered steps with no gaps.",
  examples=[
    E("Write an algorithm that prints PASS if a mark is 50 or more and FAIL otherwise.",
      "Step 1. Start; input MARK.",
      "Step 2. If MARK ≥ 50 then output 'PASS' else output 'FAIL'. (This is <b>selection</b> — a diamond in the flowchart.)",
      "Step 3. Stop. <b>Notice the decision has exactly two exits</b>, labelled Yes and No."),
    E("Why must an algorithm have a finite number of steps?",
      "Step 1. If there is no end, the computer repeats for ever — an infinite loop.",
      "Step 2. The program would never give an answer and would waste memory and processing time.",
      "Step 3. So every loop must have a <b>condition that will eventually become false</b>.")])

topic("emerging", "Technology in society & emerging trends", D, [
  "ICT has changed every sector in Ghana: mobile money and online banking; e-learning and "
  "online registration; telemedicine and electronic health records; e-commerce; "
  "digital addressing and the national ID; e-government services.",
  "Emerging technologies: <b>artificial intelligence (AI)</b>, machine learning, robotics, "
  "the <b>Internet of Things</b> (ordinary objects connected to the internet), cloud computing, "
  "3D printing, drones, virtual reality and blockchain.",
  "Benefits: speed and convenience, wider access to services and learning, new jobs and businesses, "
  "better records and planning, and inclusion of remote communities.",
  "Problems: job displacement for some workers, over-dependence on devices, cybercrime, "
  "misinformation, <b>e-waste</b>, loss of privacy, and the <b>digital divide</b> — "
  "the gap between those with access to technology and those without.",
  "Responsible use: learn the skills, protect personal data, check information before believing or sharing it, "
  "dispose of old devices properly, and keep screen time in balance with study, sleep and exercise.",
])
O("The use of ordinary objects such as fridges and street lights connected to the internet is called",
  ["the Internet of Things", "artificial intelligence", "cloud computing", "virtual reality"],
  ["AI is about machines that learn, and the cloud is about remote storage.",
   "Connecting everyday objects is <b>the Internet of Things</b>."],
  ok=True)
O("The gap between people who have access to computers and the internet and those who do not is called the",
  ["digital divide", "digital footprint", "digital signature", "digital literacy"],
  ["A footprint is your online trail and literacy is your skill.",
   "The gap in access is the <b>digital divide</b>."],
  ok=True)
O("Discarded computers, phones and batteries are known as",
  ["e-waste", "hardware", "freeware", "spam"],
  ["They are a serious environmental problem in Ghana.",
   "Discarded electronic equipment is <b>e-waste</b>."],
  ok=True)
O("Which technology has most expanded financial services to Ghanaians without bank accounts?",
  ["Mobile money", "Virtual reality", "3D printing", "Drones"],
  ["It reaches anyone with a basic phone.",
   "<b>Mobile money</b> has brought payments, transfers and savings to millions without bank branches."],
  ok=True)
O("A responsible response to a shocking news item forwarded on social media is to",
  ["check a reliable source before sharing it", "forward it to everyone at once",
   "add your own details to it", "post it as your own"],
  ["Forwarding unchecked claims is how false news spreads.",
   "You should <b>check a reliable source before sharing it</b> — and not share it if you cannot."],
  ok=True)
T("(a) State four ways in which ICT has improved life in Ghana. (b) Name four emerging technologies and give one "
  "use of each. (c) State three problems created by the spread of technology and suggest how each can be reduced.",
  ["(a) <b>Mobile money and online banking</b> let people send, receive and save money without a bank branch; "
   "<b>e-learning and online registration</b> give pupils access to lessons, past questions and examination "
   "registration; <b>health care</b> has improved through electronic records, telemedicine and faster laboratory "
   "results; and <b>business and government services</b> — e-commerce, the national ID, digital addressing and online "
   "tax and passport applications — are faster and more transparent.",
   "(b) <b>Artificial intelligence</b> — translating languages, diagnosing diseases from scans, helping pupils "
   "practise. <b>Internet of Things</b> — smart meters and sensors that report water levels or soil moisture to "
   "farmers. <b>Drones</b> — delivering blood and medicines to remote clinics, and surveying farms. "
   "<b>3D printing</b> — producing spare parts and medical models locally. (Cloud computing, robotics, virtual "
   "reality and blockchain are equally acceptable.)",
   "(c) <b>Cybercrime and loss of privacy</b> → strong passwords, two-step verification, public education and "
   "enforcement of the cybersecurity laws. <b>E-waste</b> → formal collection and recycling centres, repair rather "
   "than replacement, and a ban on open burning of cables. <b>Job displacement and over-dependence on devices</b> → "
   "retraining workers in digital and technical skills, and agreed limits on screen time so that study, sleep and "
   "exercise are protected. (The digital divide, reduced by providing internet and devices to rural schools, is also "
   "a valid answer.)"],
  marks=12)
extras("emerging",
  plain="This last topic asks you to judge technology rather than just name it. Every item has two columns: what it makes "
        "possible, and what it costs. The best answers in the exam name both, and then say what should be done about the cost.",
  examples=[
    E("A clinic in a remote district receives blood by drone. Give two benefits and one risk.",
      "Step 1. Benefits: blood arrives in minutes rather than hours, and no road or vehicle is needed in the rainy season.",
      "Step 2. Risk: the service depends on power, trained operators and spare parts — if any fails, the clinic is back where it started.",
      "Step 3. So the technology must come with <b>training, maintenance and a fallback plan</b>."),
    E("Explain the digital divide using two Ghanaian schools as an example.",
      "Step 1. A city school with a computer laboratory, electricity and internet can teach ICT practically.",
      "Step 2. A rural school without power or devices teaches the same syllabus from a textbook only.",
      "Step 3. The second school's pupils sit the same examination and later compete for the same jobs — <b>that unequal access is the digital divide</b>, and closing it needs power, devices, connectivity and trained teachers together.")])
