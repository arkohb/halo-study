"""BECE Computing - Introduction to computing, and productivity software."""
from core import *
import draw

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}
A, B = "A. Introduction to computing", "B. Productivity software"

topic("compbasics", "Introduction to computing", A, [
  "A computer is an electronic device that accepts data (<b>input</b>), works on it (<b>processing</b>), "
  "gives results (<b>output</b>) and can keep them (<b>storage</b>).",
  "<b>Data</b> are raw, unprocessed facts; <b>information</b> is processed data that has meaning. "
  "Marks of 30, 45 and 60 are data; 'the class average is 45' is information.",
  "Characteristics of a computer: speed, accuracy, diligence (it does not get tired), versatility, "
  "large storage and automation. Its limits: it has no intelligence of its own — "
  "<b>GIGO</b>, garbage in, garbage out.",
  "Generations: 1st — vacuum tubes; 2nd — transistors; 3rd — integrated circuits; "
  "4th — microprocessors (the PCs we use); 5th — artificial intelligence.",
  "Types by size: supercomputer, mainframe, mini computer, micro computer "
  "(desktop, laptop, tablet, smartphone).",
  "Uses: schools, banking, hospitals, business, transport, communication, entertainment and government.",
])
O("The four basic operations of a computer, in order, are",
  ["input, processing, output, storage", "storage, output, input, processing",
   "processing, input, storage, output", "output, input, processing, storage"],
  ["Data must first get in, then be worked on, then come out, and may then be kept.",
   "The order is <b>input, processing, output, storage</b>."],
  ok=True)
O("Which of the following is an example of information rather than data?",
  ["The average score of the class is 45", "30, 45, 60",
   "Kofi, Ama, Yaw", "A list of unmarked scripts"],
  ["The others are raw facts that have not been worked on.",
   "<b>The average score of the class is 45</b> is the result of processing, so it is information."],
  ok=True)
O("The main electronic component used in first-generation computers was the",
  ["vacuum tube", "transistor", "integrated circuit", "microprocessor"],
  ["Transistors came in the second generation and integrated circuits in the third.",
   "First-generation computers used the <b>vacuum tube</b>."],
  ok=True)
O("GIGO in computing means",
  ["garbage in, garbage out", "good input, good output",
   "general input, general output", "get in, get out"],
  ["It warns that a computer cannot correct wrong data.",
   "GIGO means <b>garbage in, garbage out</b> — wrong data gives wrong results."],
  ok=True)
O("Which characteristic of the computer means that it can work for long hours without getting tired?",
  ["Diligence", "Speed", "Accuracy", "Versatility"],
  ["Speed is how fast it works and versatility is how many kinds of work it can do.",
   "Working without tiring is <b>diligence</b>."],
  ok=True)
T("(a) Define a computer. (b) State the difference between data and information, with one example of each. "
  "(c) State four characteristics of a computer and two of its limitations.",
  ["(a) <b>A computer is an electronic device that accepts data as input, processes it according to a set of "
   "instructions, produces information as output and can store both data and results for later use.</b>",
   "(b) <b>Data</b> are raw, unprocessed facts and figures — for example the marks 30, 45 and 60. "
   "<b>Information</b> is data that has been processed and given meaning — for example 'the average mark is 45' or "
   "'Ama had the highest score'.",
   "(c) Characteristics: <b>speed</b> — it performs millions of operations a second; <b>accuracy</b> — it does not "
   "make arithmetic mistakes if the data and instructions are correct; <b>diligence</b> — it does not tire or lose "
   "concentration; <b>versatility</b> — the same machine can type, calculate, play music and browse; "
   "<b>large storage</b> and <b>automation</b>. "
   "Limitations: it has <b>no intelligence or common sense of its own</b> and simply obeys instructions (GIGO); and it "
   "<b>cannot work without power and correct instructions</b>, nor make moral judgements or decisions on its own."],
  marks=12, fig=draw.flow(["INPUT: keyboard, mouse, scanner", "PROCESSING: the CPU",
                           "OUTPUT: monitor, printer", "STORAGE: hard disk, flash drive"],
                          label="How a computer works"))
extras("compbasics",
  plain="Everything in Computing hangs on one cycle: input → processing → output, with storage alongside. Once you can "
        "place any device or action in that cycle, the rest of the syllabus — hardware, software, files, networks — falls into place.",
  examples=[
    E("A pupil types marks into a computer, which then prints each pupil's total and position. Identify the input, processing, output and storage.",
      "Step 1. Input — the marks typed on the keyboard.",
      "Step 2. Processing — the adding and ranking done by the CPU.",
      "Step 3. Output — the printed report sheet; Storage — <b>the file saved on the hard disk for next term</b>."),
    E("Why is a computer said to be accurate yet still able to give a wrong answer?",
      "Step 1. The machine itself does not make arithmetic errors.",
      "Step 2. But it works only on the data and instructions it is given.",
      "Step 3. So if a mark is typed as 95 instead of 59, the answer is <b>wrongly calculated from wrong data — GIGO</b>.")])

topic("hardware", "Hardware: input, output & the system unit", A, [
  "<b>Hardware</b> is the physical, touchable part of the computer.",
  "<b>Input devices</b> send data in: keyboard, mouse, scanner, microphone, webcam, joystick, "
  "light pen, barcode reader, touch screen, biometric (fingerprint) reader.",
  "<b>Output devices</b> give results out: monitor (VDU), printer, speaker, plotter, projector, headphones.",
  "The <b>system unit</b> houses the motherboard, the <b>CPU</b>, memory, power supply and drives. "
  "The CPU has the <b>control unit</b> (directs operations), the <b>ALU</b> (arithmetic and logic unit, "
  "which calculates and compares) and registers.",
  "The CPU is often called the <b>brain of the computer</b>. Its speed is measured in hertz (MHz, GHz).",
  "Peripherals are devices attached to the system unit; ports (USB, HDMI, VGA, audio) are the sockets "
  "through which they connect.",
])
O("Which of the following is an input device?",
  ["Scanner", "Printer", "Monitor", "Speaker"],
  ["The other three present results to the user.",
   "A <b>scanner</b> takes a picture of a document and sends it into the computer, so it is an input device."],
  ok=True)
O("The part of the CPU that performs calculations and comparisons is the",
  ["arithmetic and logic unit", "control unit", "register", "motherboard"],
  ["The control unit directs operations and registers hold data briefly.",
   "Calculation and comparison are done by the <b>arithmetic and logic unit (ALU)</b>."],
  ok=True)
O("The CPU is often described as the brain of the computer because it",
  ["controls and processes all the work", "stores all the files permanently",
   "displays the results", "supplies electricity to the computer"],
  ["Storage, display and power are the work of other parts.",
   "The CPU <b>controls and processes all the work</b>, which is why it is called the brain."],
  ok=True)
O("Which of these is BOTH an input and an output device?",
  ["A touch screen", "A keyboard", "A printer", "A microphone"],
  ["A touch screen displays information and also accepts your touch as input.",
   "So <b>a touch screen</b> does both."],
  ok=True)
O("Hardware may best be described as",
  ["the physical parts of the computer", "the programs that run on the computer",
   "the data stored in the computer", "the user of the computer"],
  ["Programs are software and data are what programs work on.",
   "Hardware is <b>the physical parts of the computer</b> — the parts you can touch."],
  ok=True)
T("(a) What is hardware? (b) Name four input and four output devices. "
  "(c) Name the three main parts of the CPU and state the function of each.",
  ["(a) <b>Hardware refers to all the physical, tangible components of a computer system — the parts you can see and "
   "touch.</b>",
   "(b) Input: <b>keyboard, mouse, scanner, microphone</b> (also webcam, joystick, barcode reader, fingerprint reader). "
   "Output: <b>monitor, printer, speaker, projector</b> (also plotter, headphones).",
   "(c) <b>Control unit</b> — directs and co-ordinates all the operations of the computer, fetching and interpreting "
   "instructions. <b>Arithmetic and logic unit (ALU)</b> — performs all calculations (addition, subtraction, "
   "multiplication, division) and all comparisons (greater than, equal to). <b>Registers</b> — very fast, very small "
   "storage areas inside the CPU that hold the data and instructions currently being worked on."],
  marks=12, fig=draw.tree("COMPUTER SYSTEM", ["Input: keyboard, mouse, scanner",
                                              "System unit: CPU (control unit, ALU, registers), memory",
                                              "Output: monitor, printer, speaker",
                                              "Storage: hard disk, flash drive, cloud"],
                          label="Parts of a computer system"))
extras("hardware",
  plain="Sort every device by the question 'is it bringing data in, or sending results out?'. A few do both — a touch "
        "screen, a modem, a multifunction printer with a scanner — and those make favourite exam questions.",
  examples=[
    E("A supermarket cashier passes goods over a glass panel and the price appears on a screen. Name the devices and their type.",
      "Step 1. The glass panel reads the barcode — a <b>barcode reader, an input device</b>.",
      "Step 2. The screen shows the price — a <b>monitor, an output device</b>.",
      "Step 3. The receipt comes from a <b>printer, also output</b>; the CPU in between does the look-up."),
    E("Why is a projector classed with monitors rather than with scanners?",
      "Step 1. Ask which way the data is flowing.",
      "Step 2. A projector takes information from the computer and displays it for an audience.",
      "Step 3. Data flows <b>out</b> of the computer, so it is an output device.")])

topic("storage", "Memory & storage devices", A, [
  "<b>Primary memory</b> is inside the computer and works directly with the CPU. "
  "<b>RAM</b> (random access memory) holds what you are working on now and is <b>volatile</b> — "
  "its contents are lost when power goes off. <b>ROM</b> (read-only memory) holds the start-up "
  "instructions permanently and is non-volatile.",
  "<b>Secondary storage</b> keeps data permanently: hard disk drive (HDD), solid state drive (SSD), "
  "flash (pen) drive, memory card, CD, DVD, external hard drive and <b>cloud storage</b>.",
  "Units: 8 bits = 1 <b>byte</b>; 1 024 bytes = 1 kilobyte (KB); 1 024 KB = 1 megabyte (MB); "
  "1 024 MB = 1 gigabyte (GB); 1 024 GB = 1 terabyte (TB).",
  "Always <b>save</b> your work (Ctrl + S) as you go, and <b>back up</b> important files in a second place.",
  "Care of storage media: keep them away from heat, water, dust and magnets; "
  "remove a flash drive safely; scan it for viruses.",
])
O("Which type of memory loses its contents when the computer is switched off?",
  ["RAM", "ROM", "The hard disk", "A flash drive"],
  ["ROM, hard disks and flash drives all keep their contents without power.",
   "<b>RAM</b> is volatile — that is why unsaved work is lost in a power cut."],
  ok=True)
O("How many bits make one byte?",
  ["8", "4", "16", "1 024"],
  ["1 024 is the number of bytes in a kilobyte.", "One byte is made up of <b>8 bits</b>."],
  v=8)
O("Which of the following is a secondary storage device?",
  ["Flash drive", "RAM", "ROM", "Register"],
  ["RAM, ROM and registers are all primary memory inside the machine.",
   "A <b>flash drive</b> is secondary storage — removable and permanent."],
  ok=True)
O("1 gigabyte is approximately equal to",
  ["1 024 megabytes", "1 024 kilobytes", "1 024 bytes", "1 024 terabytes"],
  ["Each step up the scale multiplies by 1 024.", "1 GB = <b>1 024 megabytes</b>."],
  ok=True)
O("The best way to protect important school files against loss is to",
  ["keep a backup copy in another place", "print them only",
   "rename them often", "store them on the desktop"],
  ["A file in one place only is one accident away from being gone.",
   "You should <b>keep a backup copy in another place</b> — another drive or the cloud."],
  ok=True)
T("(a) State three differences between RAM and ROM. (b) Name four secondary storage devices. "
  "(c) Convert: (i) 3 KB to bytes (ii) 2 MB to KB. (d) State two ways of caring for a flash drive.",
  ["(a) <b>RAM</b> is volatile (contents lost when power goes off), can be <b>read from and written to</b>, and holds "
   "the work in progress. <b>ROM</b> is non-volatile (keeps its contents), is normally <b>read only</b>, and holds the "
   "permanent start-up instructions. RAM is also much larger in capacity than ROM in a modern computer.",
   "(b) <b>Hard disk drive, solid state drive, flash (pen) drive, memory card</b> (also CD, DVD, external hard drive, "
   "cloud storage).",
   "(c) (i) 3 KB = 3 × 1 024 = <b>3 072 bytes</b>. (ii) 2 MB = 2 × 1 024 = <b>2 048 KB</b>.",
   "(d) Any two: <b>remove it safely</b> using 'eject' rather than pulling it out while in use; <b>keep it away from "
   "heat, water, dust and magnets</b>; <b>scan it for viruses</b> before opening files; keep the cap on and do not "
   "bend or drop it."],
  marks=12, ok=(3 * 1024 == 3072 and 2 * 1024 == 2048))
extras("storage",
  plain="Think of RAM as your desk and the hard disk as the cupboard. The desk is fast but it is cleared every time the "
        "lights go out; the cupboard is slower but keeps things. That is exactly why Ctrl + S matters.",
  examples=[
    E("A pupil types an essay for two hours and the power goes off before she saves. Explain what happened.",
      "Step 1. While she typed, the essay existed only in RAM.",
      "Step 2. RAM is volatile, so its contents vanish the moment power is lost.",
      "Step 3. Nothing was written to the hard disk, so <b>the work is gone</b> — the lesson is to save every few minutes."),
    E("How many 4 MB photographs can be stored on a 2 GB memory card?",
      "Step 1. Convert to the same unit: 2 GB = 2 × 1 024 = 2 048 MB.",
      "Step 2. Divide: 2 048 ÷ 4.",
      "Step 3. = <b>512 photographs</b> (a little fewer in practice, since the card itself uses some space).")])

topic("software", "Software & its types", A, [
  "<b>Software</b> is the set of programs and instructions that tell the hardware what to do. "
  "Hardware without software is useless, and the reverse.",
  "<b>System software</b> runs the computer itself: the operating system (Windows, macOS, Linux, Android, iOS), "
  "utility programs (antivirus, disk clean-up, backup) and language translators.",
  "<b>Application software</b> does work for the user: word processors (MS Word), spreadsheets (MS Excel), "
  "presentation software (PowerPoint), browsers, media players, games, accounting packages.",
  "Software may be bought (<b>proprietary</b>, licensed, e.g. Microsoft Office), <b>free and open source</b> "
  "(LibreOffice, Linux), <b>shareware</b> (try then pay) or <b>freeware</b>.",
  "Using software without a licence (piracy) is illegal and risks viruses; "
  "always install from genuine sources and keep an antivirus updated.",
])
O("Software may best be described as",
  ["the programs and instructions that run a computer", "the physical parts of the computer",
   "the data typed by the user", "the person who operates the computer"],
  ["Physical parts are hardware and the operator is the user.",
   "Software is <b>the programs and instructions that run a computer</b>."],
  ok=True)
O("Which of the following is system software?",
  ["Operating system", "Word processor", "Spreadsheet", "Web browser"],
  ["The last three are applications used to do work.",
   "An <b>operating system</b> runs the computer itself, so it is system software."],
  ok=True)
O("A program used to type, edit and print documents is called a",
  ["word processor", "spreadsheet", "database", "web browser"],
  ["Spreadsheets handle numbers and databases handle records.",
   "Typing documents is the work of a <b>word processor</b>."],
  ok=True)
O("An antivirus program is an example of",
  ["utility software", "application software for entertainment",
   "a programming language", "hardware"],
  ["It maintains and protects the system rather than doing the user's work.",
   "It is <b>utility software</b>, a kind of system software."],
  ok=True)
O("Installing software without paying for its licence is",
  ["illegal and risky", "legal if the computer is personal",
   "encouraged in schools", "the only way to get software"],
  ["Free and open-source alternatives exist legally.",
   "Unlicensed installation is <b>illegal and risky</b> — it is piracy, and pirated copies often carry viruses."],
  ok=True)
T("(a) State the difference between hardware and software. (b) Name the two main types of software and give three "
  "examples of each. (c) Give three disadvantages of using pirated software.",
  ["(a) <b>Hardware</b> is the physical, touchable part of the computer — keyboard, monitor, CPU. "
   "<b>Software</b> is the set of programs and instructions that tell the hardware what to do; it cannot be touched. "
   "Neither is of any use without the other.",
   "(b) <b>System software</b>: operating systems (Windows, Linux, Android), utility programs (antivirus, disk "
   "clean-up), language translators (compilers). "
   "<b>Application software</b>: word processor (MS Word), spreadsheet (MS Excel), presentation software (PowerPoint) — "
   "also browsers, media players and games.",
   "(c) It is <b>illegal</b> and the user or school can be prosecuted; it often carries <b>viruses and malware</b> "
   "that damage files and steal information; it receives <b>no updates or technical support</b>, so faults cannot be "
   "fixed and security holes remain; and it denies the developers the income that pays for improvements."],
  marks=12)
extras("software",
  plain="The test for system versus application software is simple: does the program serve the <b>computer</b> or the "
        "<b>user</b>? Windows and an antivirus serve the computer; Word and a browser serve you.",
  examples=[
    E("A school has old computers and no money for Microsoft Office. Suggest a legal solution.",
      "Step 1. Pirating Office is illegal and risky.",
      "Step 2. Free and open-source alternatives do the same work: LibreOffice Writer, Calc and Impress.",
      "Step 3. They are <b>free to install on every machine, open the same file types, and are lighter on old hardware</b>."),
    E("Classify each as system or application software: Android, Chrome, Microsoft Defender, Excel.",
      "Step 1. Android \u2014 an operating system \u2192 <b>system</b>.",
      "Step 2. Chrome \u2014 used by the person to browse \u2192 <b>application</b>; Microsoft Defender (Windows Security) \u2014 protects the machine \u2192 <b>system (utility)</b>.",
      "Step 3. Excel — used to do the user's calculations → <b>application</b>.")])

topic("os", "The operating system, files & folders", A, [
  "The <b>operating system (OS)</b> is the master program that starts the computer and manages everything: "
  "memory, files, devices, security and the user interface.",
  "Functions: booting the computer, memory management, file management, device (driver) management, "
  "process management, providing the user interface, and security through user accounts and passwords.",
  "The desktop shows <b>icons</b>, the <b>taskbar</b>, the <b>start menu</b> and <b>windows</b>. "
  "A window has a title bar, minimise, maximise and close buttons, and scroll bars.",
  "A <b>file</b> holds data under a name and an extension that shows its type: "
  ".docx (Word), .xlsx (Excel), .pptx (PowerPoint), .pdf, .txt, .jpg or .png (pictures), .mp3 (sound), .mp4 (video), "
  ".exe (program). A <b>folder</b> holds files and other folders.",
  "File operations: create, open, save, save as, rename, copy, move, delete (goes to the Recycle Bin), restore, "
  "and search.",
  "Shortcuts: Ctrl + S save, Ctrl + C copy, Ctrl + X cut, Ctrl + V paste, Ctrl + Z undo, Ctrl + P print, "
  "Ctrl + A select all.",
])
O("The master program that manages all the activities of a computer is the",
  ["operating system", "word processor", "antivirus", "web browser"],
  ["The others each do one job under its control.",
   "The <b>operating system</b> manages memory, files, devices and security."],
  ok=True)
O("Which of the following is an operating system?",
  ["Android", "Excel", "PowerPoint", "Google Chrome"],
  ["The other three are applications that run on top of an operating system.",
   "<b>Android</b> is an operating system, used on most phones and tablets."],
  ok=True)
O("A file with the extension .xlsx was most likely created with",
  ["a spreadsheet program", "a word processor", "a presentation program", "a web browser"],
  [".docx is Word and .pptx is PowerPoint.", "<b>.xlsx</b> is the file type of a spreadsheet, such as MS Excel."],
  ok=True)
O("The keyboard shortcut for saving a document is",
  ["Ctrl + S", "Ctrl + P", "Ctrl + V", "Ctrl + Z"],
  ["Ctrl + P prints, Ctrl + V pastes and Ctrl + Z undoes.", "Save is <b>Ctrl + S</b>."],
  ok=True)
O("When a file is deleted from a Windows computer, it is first sent to the",
  ["Recycle Bin", "Control Panel", "Taskbar", "Clipboard"],
  ["The Clipboard holds copied items and the Taskbar shows running programs.",
   "A deleted file goes to the <b>Recycle Bin</b>, from which it can be restored."],
  ok=True)
T("(a) State four functions of an operating system. (b) Give four file extensions and state the type of file each "
  "represents. (c) Describe the steps for creating a folder named 'BECE 2027' on the desktop and moving a document "
  "into it.",
  ["(a) <b>Booting (starting up) the computer</b>; <b>memory management</b> — allocating RAM to each program; "
   "<b>file management</b> — organising, saving, renaming and deleting files; <b>device management</b> — controlling "
   "the printer, keyboard and other peripherals through drivers; <b>providing the user interface</b>; and "
   "<b>security</b> through user accounts and passwords.",
   "(b) <b>.docx</b> — a word-processing document; <b>.xlsx</b> — a spreadsheet workbook; <b>.pptx</b> — a "
   "presentation; <b>.jpg or .png</b> — a picture; (also <b>.pdf</b> — a portable document, <b>.mp3</b> — sound, "
   "<b>.mp4</b> — video, <b>.exe</b> — a program).",
   "(c) Right-click on an empty part of the desktop, point to <b>New</b> and choose <b>Folder</b>. Type the name "
   "<b>BECE 2027</b> and press Enter. Then locate the document, click it once and press <b>Ctrl + X</b> to cut it "
   "(or right-click → Cut). Open the new folder and press <b>Ctrl + V</b> to paste. "
   "(Dragging the file onto the folder icon does the same thing.)"],
  marks=12)
extras("os",
  plain="The operating system is the manager you never see: it decides which program gets memory, where your file is "
        "written and whether your password is correct. Learn the shortcut keys — they are free marks and they make you faster for life.",
  examples=[
    E("A pupil cannot find a document she saved yesterday. Give an orderly way to find it.",
      "Step 1. Open File Explorer and check 'Recent files' — the OS keeps a list.",
      "Step 2. Use the search box with part of the name, or with the extension (*.docx).",
      "Step 3. If it was deleted, <b>check the Recycle Bin and restore it</b>; next time, save into a named folder, not just the desktop."),
    E("Why does a computer with little free RAM become slow when many programs are open?",
      "Step 1. The OS must fit all the running programs into memory.",
      "Step 2. When RAM runs short it swaps parts out to the much slower hard disk.",
      "Step 3. The constant swapping is what you feel as <b>slowness</b> — closing unused programs fixes it.")])

topic("safety", "Health, safety & care of the computer", A, [
  "Sit upright with the screen at eye level, feet flat, and wrists straight. "
  "Take a short break and look into the distance every 20–30 minutes to rest the eyes.",
  "Health risks of long computer use: eye strain, back and neck pain, repetitive strain injury in the wrists, "
  "headaches, and tiredness. Noise and poor light make them worse.",
  "Electrical safety: do not overload a socket; use a surge protector or UPS; keep liquids away from the computer; "
  "do not touch sockets or cables with wet hands; report frayed cables.",
  "Care of the computer: keep it dust-free and well ventilated; shut it down properly; do not force a disk or cable; "
  "keep food and drink away; cover it when not in use.",
  "Protect data: use a strong password, scan removable media for viruses, update the antivirus, "
  "and back up important files.",
  "In the computer laboratory: no running, no eating, no unplugging equipment, and report any fault at once.",
])
O("Which of the following is a health risk of using a computer for long hours?",
  ["Eye strain and back pain", "Loss of hearing",
   "Tooth decay", "Shortness of breath"],
  ["All four are real health problems, but only one comes from sitting at a screen for too long.",
   "The common computer risks are <b>eye strain and back pain</b>, together with wrist injury (RSI) and headaches \u2014 which is why you should sit upright, keep the screen at eye level and look away every 20 minutes."],
  ok=True)
O("The best way to protect a computer against damage from a sudden power surge is to use",
  ["a surge protector or UPS", "a longer cable",
   "a dust cover", "a faster processor"],
  ["Covers keep out dust and processors affect speed, not safety.",
   "A <b>surge protector or UPS</b> protects against voltage spikes and sudden power loss."],
  ok=True)
O("Eating and drinking in a computer laboratory should be avoided because",
  ["spills and crumbs can damage the equipment", "it makes pupils sleepy",
   "the food becomes cold", "it is against the timetable"],
  ["The danger is to the equipment.",
   "<b>Spills and crumbs can damage the equipment</b> — liquid in a keyboard usually destroys it."],
  ok=True)
O("To reduce eye strain while working on a computer, a user should",
  ["look away into the distance at intervals", "sit as close to the screen as possible",
   "work in a completely dark room", "increase the brightness to maximum"],
  ["The other three make eye strain worse.",
   "You should <b>look away into the distance at intervals</b> — about every twenty minutes — and blink often."],
  ok=True)
O("The correct way to switch off a computer is to",
  ["use the shut-down command in the operating system", "pull out the power cable",
   "press and hold the power button", "switch off at the wall while it is running"],
  ["The other methods can corrupt files and damage the disk.",
   "Always <b>use the shut-down command in the operating system</b>."],
  ok=True)
T("(a) State four rules to be observed in a computer laboratory. (b) Give three health problems associated with the "
  "long use of computers and one way of preventing each. (c) State three ways of caring for a computer.",
  ["(a) Any four: <b>do not eat or drink in the laboratory</b>; <b>do not run or play</b> among the equipment; "
   "<b>do not unplug or interfere with cables and sockets</b>; <b>keep hands clean and dry</b>; <b>shut down properly "
   "before leaving</b>; <b>report any fault or damage to the teacher at once</b>; do not install or download software "
   "without permission.",
   "(b) <b>Eye strain</b> — look away into the distance every 20–30 minutes, blink often, and set the screen "
   "brightness to match the room. <b>Back and neck pain</b> — sit upright on a chair of the right height with the "
   "screen at eye level, and stand up and stretch regularly. <b>Repetitive strain injury in the wrists</b> — keep the "
   "wrists straight and level with the keyboard, use a wrist rest, and take breaks.",
   "(c) Any three: <b>keep it in a cool, dust-free, well-ventilated place</b> and cover it when not in use; "
   "<b>shut it down properly and use a UPS or surge protector</b>; <b>keep food, drink and magnets away</b>; "
   "<b>run and update an antivirus and scan flash drives</b>; handle cables and disks gently."],
  marks=12)
extras("safety",
  plain="This topic is examined almost entirely as 'state four rules' and 'give three health risks'. Learn them as a "
        "list you could recite in the lab, because that is where they actually matter — a single spilled drink can cost a school a computer.",
  examples=[
    E("A pupil complains of headaches and sore eyes after two hours at a screen. Give three practical changes.",
      "Step 1. Raise the screen to eye level and sit about an arm's length away.",
      "Step 2. Reduce glare: move the screen away from the window and lower the brightness to match the room.",
      "Step 3. <b>Apply the 20-20-20 habit — every 20 minutes, look 20 feet away for 20 seconds</b>, and blink deliberately."),
    E("Lightning struck nearby and three school computers stopped working. What should have been done beforehand?",
      "Step 1. Lightning causes a surge far above normal voltage.",
      "Step 2. Equipment should be connected through surge protectors, and unplugged during a storm.",
      "Step 3. Important files should also have been <b>backed up off the machines</b>, so that the data survives even when hardware does not.")])

# ------------------------------------------------------------------ productivity
topic("typing", "Keyboarding skills", B, [
  "The keyboard has alphanumeric keys, function keys (F1–F12), the numeric keypad, "
  "cursor (arrow) keys and special keys.",
  "Special keys: <b>Enter</b> (new line / confirm), <b>Shift</b> (capitals and upper symbols), "
  "<b>Caps Lock</b> (continuous capitals), <b>Backspace</b> (deletes to the left), "
  "<b>Delete</b> (deletes to the right), <b>Tab</b> (moves in set steps), <b>Space bar</b>, "
  "<b>Esc</b>, <b>Ctrl</b> and <b>Alt</b> (used in combinations).",
  "In <b>touch typing</b> the fingers rest on the <b>home keys</b> — ASDF for the left hand and "
  "JKL; for the right — and each finger has its own keys. The thumbs work the space bar.",
  "Good posture: sit upright, elbows at about a right angle, wrists straight, eyes on the screen and not on the keys.",
  "Speed is measured in <b>words per minute (wpm)</b>, but <b>accuracy comes first</b> — "
  "a fast typist who must correct every line is slower than a careful one.",
])
O("The home keys for the left hand in touch typing are",
  ["A S D F", "Q W E R", "Z X C V", "J K L ;"],
  ["J K L ; are the home keys for the right hand.", "The left hand rests on <b>A S D F</b>."],
  ok=True)
O("Which key deletes the character to the LEFT of the cursor?",
  ["Backspace", "Delete", "Esc", "Tab"],
  ["Delete removes the character to the right.", "<b>Backspace</b> deletes to the left."],
  ok=True)
O("To type a single capital letter, you hold down",
  ["Shift", "Caps Lock", "Ctrl", "Alt"],
  ["Caps Lock gives continuous capitals until it is pressed again.",
   "For one capital letter, hold <b>Shift</b> and press the letter."],
  ok=True)
O("Typing speed is measured in",
  ["words per minute", "characters per hour", "bytes per second", "pages per day"],
  ["The standard measure is per minute.", "Typing speed is measured in <b>words per minute (wpm)</b>."],
  ok=True)
O("In touch typing, the space bar is operated with the",
  ["thumbs", "little fingers", "index fingers", "wrists"],
  ["Each other finger has its own column of keys.", "The space bar is pressed with the <b>thumbs</b>."],
  ok=True)
T("(a) Name four special keys on the keyboard and state the function of each. "
  "(b) Explain what is meant by touch typing and give two of its advantages. "
  "(c) State three correct postures to adopt while typing.",
  ["(a) <b>Enter</b> — starts a new line or confirms a command. <b>Shift</b> — produces capital letters and the upper "
   "symbols on the number keys. <b>Backspace</b> — deletes the character to the left of the cursor. "
   "<b>Tab</b> — moves the cursor forward in fixed steps, used for indenting and moving between cells or fields. "
   "(Caps Lock, Delete, Esc, Ctrl and Alt are equally acceptable.)",
   "(b) <b>Touch typing is typing without looking at the keyboard, with the fingers resting on the home keys and each "
   "finger responsible for its own keys.</b> Advantages: it is <b>much faster</b>, since the eyes stay on the copy or "
   "the screen; it is <b>more accurate and less tiring</b>; and it allows the typist to concentrate on the content "
   "rather than on finding the keys.",
   "(c) <b>Sit upright with the back supported</b> and feet flat on the floor; keep the <b>wrists straight and level "
   "with the keyboard</b>, elbows at about a right angle; and keep the <b>screen at eye level, about an arm's length "
   "away</b>, with the eyes on the screen rather than on the keys."],
  marks=12)
extras("typing",
  plain="Keyboarding is the one Computing skill you will use every single day, and the only way to gain it is a few "
        "careful minutes daily with the eyes off the keys. Accuracy first — speed follows on its own.",
  examples=[
    E("A pupil types 300 words in 6 minutes with 10 errors. Find his gross speed and comment.",
      "Step 1. Gross speed = 300 ÷ 6 = <b>50 wpm</b>.",
      "Step 2. Many tests subtract one word per error: 300 − 10 = 290, giving about 48 wpm net.",
      "Step 3. Comment: a good speed, but <b>10 errors in 300 words is high</b> — slowing slightly would raise his useful output."),
    E("Explain the difference between Shift and Caps Lock with an example.",
      "Step 1. Shift works only while it is held down.",
      "Step 2. Caps Lock stays on until pressed again.",
      "Step 3. To type 'Ghana' use <b>Shift + g</b>; to type 'GHANA' turn <b>Caps Lock</b> on, type, then turn it off.")])

topic("word", "Word processing", B, [
  "A word processor is used to create, edit, format, save and print text documents. "
  "Examples: Microsoft Word, LibreOffice Writer, Google Docs, WPS Office.",
  "<b>Editing</b> changes the content: insert, delete, cut, copy, paste, undo, redo, find and replace, spell check.",
  "<b>Formatting</b> changes the appearance: font type, size and colour; <b>bold</b>, <i>italic</i>, underline; "
  "alignment (left, centre, right, justify); line spacing; bullets and numbering; margins; "
  "headers and footers; page numbers.",
  "Other features: tables, insert picture, word count, columns, page break, mail merge, and print preview.",
  "Useful shortcuts: Ctrl + B bold, Ctrl + I italic, Ctrl + U underline, Ctrl + E centre, "
  "Ctrl + S save, Ctrl + P print, Ctrl + F find.",
  "<b>Save</b> keeps changes to the existing file; <b>Save As</b> makes a new copy under a new name or place.",
])
O("Which of the following is a word processing program?",
  ["Microsoft Word", "Microsoft Excel", "Microsoft PowerPoint", "Microsoft Access"],
  ["Excel is a spreadsheet, PowerPoint a presentation program and Access a database.",
   "<b>Microsoft Word</b> is a word processor."],
  ok=True)
O("The feature used to place text in the middle of a line is",
  ["centre alignment", "justify", "indent", "line spacing"],
  ["Justify spreads text evenly to both margins.", "Putting text in the middle is <b>centre alignment</b> (Ctrl + E)."],
  ok=True)
O("The shortcut Ctrl + B is used to",
  ["make the selected text bold", "open a new file", "print the document", "insert a border"],
  ["Ctrl + P prints and Ctrl + N opens a new document.", "Ctrl + B makes the selected text <b>bold</b>."],
  ok=True)
O("To change every occurrence of the word 'teacher' to 'tutor' in a long document quickly, use",
  ["Find and Replace", "Spell check", "Word count", "Print preview"],
  ["The others check, count or display rather than change text.",
   "Use <b>Find and Replace</b>, which can change all occurrences at once."],
  ok=True)
O("The difference between Save and Save As is that Save As",
  ["creates a new copy under a different name or location", "deletes the original file",
   "prints the document", "closes the program"],
  ["Save simply updates the file you are working on.",
   "<b>Save As creates a new copy under a different name or location</b>, leaving the original as it was."],
  ok=True)
T("(a) State four editing and four formatting features of a word processor. "
  "(b) Describe the steps for typing a letter, centring its heading in bold, and saving it as "
  "'Application' in a folder called 'Letters'. (c) Give three advantages of a word processor over a typewriter.",
  ["(a) Editing: <b>insert and delete text; cut, copy and paste; undo and redo; find and replace</b> (also spell check). "
   "Formatting: <b>change font type, size and colour; bold, italic and underline; alignment and line spacing; "
   "bullets and numbering</b> (also margins, headers and footers, page numbers).",
   "(b) Open the word processor and type the letter. Select the heading, then click <b>Centre</b> (or press Ctrl + E) "
   "and click <b>Bold</b> (or Ctrl + B). Now press <b>Ctrl + S</b> (or File → Save As). In the dialogue box, navigate "
   "to the <b>Letters</b> folder, type the file name <b>Application</b> in the File name box, and click <b>Save</b>.",
   "(c) <b>Mistakes can be corrected before printing</b>, without starting the page again; <b>the document can be "
   "saved, re-used and edited later</b>, and many copies printed from one file; and it offers <b>formatting, spell "
   "check, tables and pictures</b> that a typewriter cannot produce. (It is also easy to send the file by email.)"],
  marks=12)
extras("word",
  plain="Word processing questions divide neatly into editing (changing what the words are) and formatting (changing how "
        "they look). Sort the features into those two baskets and the objective questions answer themselves.",
  examples=[
    E("A pupil's heading is typed in capitals using Caps Lock but she wants it bold and centred. What exactly does she do?",
      "Step 1. Select the heading by dragging across it.",
      "Step 2. Press <b>Ctrl + B</b> for bold.",
      "Step 3. Press <b>Ctrl + E</b> to centre it. Both affect only the selected text."),
    E("Classify as editing or formatting: deleting a paragraph, underlining a word, pasting a sentence, double line spacing.",
      "Step 1. Deleting a paragraph changes the content → <b>editing</b>.",
      "Step 2. Underlining changes appearance → <b>formatting</b>; pasting changes content → <b>editing</b>.",
      "Step 3. Double line spacing changes appearance → <b>formatting</b>.")])

topic("present", "Presentation software", B, [
  "Presentation software is used to make a series of <b>slides</b> for showing information to an audience. "
  "Examples: Microsoft PowerPoint, LibreOffice Impress, Google Slides, Canva.",
  "Each slide may hold a title, text, bullet points, pictures, charts, tables, sound and video. "
  "A <b>layout</b> arranges the placeholders; a <b>theme</b> sets the colours and fonts for the whole deck.",
  "<b>Transition</b> is the effect between one slide and the next; <b>animation</b> is the effect on an item "
  "within a slide.",
  "Views: Normal, Slide Sorter, Notes Page and <b>Slide Show</b> (F5 starts the show; Esc ends it).",
  "Good practice: one idea per slide; few words in large type; high-contrast colours; "
  "pictures that explain rather than decorate; and never read the slides aloud word for word.",
])
O("A single page in a presentation is called a",
  ["slide", "sheet", "record", "document"],
  ["A sheet belongs to a spreadsheet and a record to a database.",
   "In presentation software each page is a <b>slide</b>."],
  ok=True)
O("The effect that appears when moving from one slide to the next is called a",
  ["transition", "animation", "layout", "theme"],
  ["An animation affects an object within a slide.", "The effect between slides is a <b>transition</b>."],
  ok=True)
O("Which key is pressed to start a slide show in PowerPoint?",
  ["F5", "F1", "Esc", "Ctrl + P"],
  ["F1 opens help, Esc ends the show and Ctrl + P prints.", "A slide show is started with <b>F5</b>."],
  ok=True)
O("Which of the following makes a presentation EASIER for an audience to follow?",
  ["Few words in large, high-contrast type", "Long paragraphs on every slide",
   "Many different fonts and colours", "Reading every word on the slide aloud"],
  ["Crowded slides and clashing styles make an audience stop reading.",
   "<b>Few words in large, high-contrast type</b> is the rule — one idea per slide."],
  ok=True)
O("The view that shows all the slides as small pictures, so they can be rearranged, is",
  ["Slide Sorter view", "Normal view", "Notes Page view", "Reading view"],
  ["Normal view shows one slide for editing.",
   "<b>Slide Sorter view</b> shows thumbnails of every slide for reordering."],
  ok=True)
T("(a) Name three presentation programs. (b) State the difference between a transition and an animation. "
  "(c) Describe the steps for creating a three-slide presentation on 'Keeping our school clean', "
  "adding a picture and a transition, and running it.",
  ["(a) <b>Microsoft PowerPoint, LibreOffice Impress, Google Slides</b> (Canva and WPS Presentation are also acceptable).",
   "(b) A <b>transition</b> is the visual effect that occurs as one slide gives way to the next — it applies to the "
   "whole slide. An <b>animation</b> is the effect applied to an object <i>within</i> a slide, such as a heading "
   "flying in or bullet points appearing one by one.",
   "(c) Open PowerPoint and choose a <b>blank presentation</b>. On slide 1 type the title 'Keeping our school clean' "
   "and your name. Click <b>New Slide</b> and type the second slide's heading and three bullet points (for example "
   "'Use the bins', 'Sweep daily', 'Clear the gutters'). Add a third slide for the conclusion. "
   "To add the picture: on a chosen slide click <b>Insert → Pictures</b>, select the image and resize it. "
   "To add the transition: click the <b>Transitions</b> tab, choose an effect such as Fade, and click "
   "<b>Apply to All</b>. Save with Ctrl + S, then press <b>F5</b> to run the show, clicking or pressing the space bar "
   "to advance, and <b>Esc</b> to end."],
  marks=12)
extras("present",
  plain="Slides are for the audience, not the speaker. The commonest fault — and the one the syllabus warns against — is "
        "putting whole paragraphs on the screen and then reading them out. Few words, large type, one idea per slide.",
  examples=[
    E("A pupil's slide has 120 words in size 14 font. How should he fix it?",
      "Step 1. Cut it to the three or four points that actually matter.",
      "Step 2. Write each as a short bullet of a few words, in size 28 or larger.",
      "Step 3. <b>Keep the detail in his own notes or in the Notes pane</b> and say it aloud instead."),
    E("Why should a presenter test the slide show before the audience arrives?",
      "Step 1. Projector resolution and room light change how colours and font sizes appear.",
      "Step 2. Videos, sounds and fonts may not play or display on another computer.",
      "Step 3. Testing lets him <b>fix contrast, size and missing media before it matters</b>.")])

topic("sheets", "Spreadsheets", B, [
  "A spreadsheet arranges data in <b>rows</b> (numbered 1, 2, 3 …) and <b>columns</b> (lettered A, B, C …). "
  "The box where a row and a column meet is a <b>cell</b>, and its name — the cell address — is the column letter "
  "followed by the row number, such as <b>B5</b>.",
  "A <b>range</b> is a block of cells written with a colon: A1:A10.",
  "Every formula begins with <b>=</b>. Operators: + − * / ^ and ( ).",
  "Common functions: <b>=SUM(A1:A10)</b>, <b>=AVERAGE(B2:B9)</b>, <b>=MAX</b>, <b>=MIN</b>, <b>=COUNT</b>, "
  "and <b>=IF(C2>=50,\"PASS\",\"FAIL\")</b>.",
  "Other features: sorting, filtering, formatting cells, borders, freeze panes, and charts "
  "(column, bar, line, pie).",
  "Uses: class mark sheets, household budgets, shop records, stock lists, "
  "and any table where numbers must be totalled or compared.",
])
O("In a spreadsheet, the intersection of a row and a column is called a",
  ["cell", "range", "sheet", "field"],
  ["A range is a group of cells and a sheet is the whole page.",
   "The intersection of a row and a column is a <b>cell</b>."],
  ok=True)
O("Every formula in a spreadsheet must begin with",
  ["=", "+", "@", "#"],
  ["Without it, the entry is treated as plain text.", "A formula begins with the <b>equals sign (=)</b>."],
  ok=True)
O("Which formula adds the values in cells A1 to A10?",
  ["=SUM(A1:A10)", "=TOTAL(A1:A10)", "=ADD(A1+A10)", "=A1:A10"],
  ["TOTAL and ADD are not spreadsheet functions.", "The correct formula is <b>=SUM(A1:A10)</b>."],
  ok=True)
O("The cell at the meeting of column D and row 7 is addressed as",
  ["D7", "7D", "D:7", "4-7"],
  ["The column letter always comes first.", "The address is <b>D7</b>."],
  ok=True)
O("To find the average of the marks in cells B2 to B9 you would type",
  ["=AVERAGE(B2:B9)", "=MEAN(B2:B9)", "=SUM(B2:B9)/B9", "=AVG(B2-B9)"],
  ["MEAN and AVG are not valid function names in Excel.",
   "The correct entry is <b>=AVERAGE(B2:B9)</b>."],
  ok=True)
T("A teacher keeps the marks of five pupils in a spreadsheet. The names are in A2:A6 and the marks in B2:B6. "
  "(a) Write the formula to find the total of the marks, placing it in B7. "
  "(b) Write the formula to find the average mark. (c) Write a formula in C2 that displays PASS if the mark in B2 is "
  "50 or more and FAIL if it is not. (d) State three advantages of using a spreadsheet for this work.",
  ["(a) In B7: <b>=SUM(B2:B6)</b>.",
   "(b) <b>=AVERAGE(B2:B6)</b>. (Equivalently =SUM(B2:B6)/5, though the function is safer.)",
   "(c) In C2: <b>=IF(B2>=50,\"PASS\",\"FAIL\")</b>, then copy the formula down to C6.",
   "(d) <b>Calculations are automatic and accurate</b>, and they update by themselves when a mark is corrected; "
   "<b>results can be sorted and ranked instantly</b>, so positions are found without re-working; and "
   "<b>charts can be produced from the same data</b>, besides saving the file for re-use next term."],
  marks=12)
extras("sheets",
  plain="A spreadsheet is a calculator that remembers. The real power is that a formula refers to <b>cells</b>, not to "
        "numbers: correct one mark and every total, average and position updates on its own. That is why examiners insist on =SUM(B2:B6) rather than =30+45+60.",
  examples=[
    E("Why is '=B2+B3+B4+B5+B6' worse than '=SUM(B2:B6)' even though both give the same answer?",
      "Step 1. If a row is inserted, the long version misses the new cell while SUM adjusts.",
      "Step 2. The long version is slow to type and easy to mistype for many rows.",
      "Step 3. So SUM is <b>shorter, safer and self-adjusting</b>."),
    E("A trader records daily sales in B2:B31. Write formulas for the total, the best day and the daily average.",
      "Step 1. Total: <b>=SUM(B2:B31)</b>.",
      "Step 2. Best day's figure: <b>=MAX(B2:B31)</b>.",
      "Step 3. Average: <b>=AVERAGE(B2:B31)</b> — and a column chart of B2:B31 shows the pattern at a glance.")])

topic("database", "Data, information & databases", B, [
  "A <b>database</b> is an organised collection of related data, kept so that it can be searched, "
  "sorted and updated easily. Examples of software: Microsoft Access, MySQL.",
  "Structure: a <b>field</b> is one item of data (Name, Age, Class); a <b>record</b> is all the fields about one "
  "person or thing; a <b>table</b> (file) is a collection of records; a <b>database</b> is a set of related tables.",
  "A <b>primary key</b> is a field whose value is different for every record — an index number, "
  "for instance — and it identifies each record uniquely.",
  "Operations: enter data, edit, delete, <b>sort</b> (arrange in order), <b>search or query</b> "
  "(find records that meet a condition), and produce <b>reports</b>.",
  "Advantages over paper files: fast searching, no duplication, easy updating, less storage space, "
  "better security, and reports produced automatically.",
  "Uses in Ghana: school records, hospital records, the voters' register, "
  "the National Identification database, bank accounts and payrolls.",
])
O("All the data about one pupil in a school database is called a",
  ["record", "field", "file", "key"],
  ["A field is one item, such as the date of birth alone.",
   "All the fields about one pupil form a <b>record</b>."],
  ok=True)
O("A field whose value is unique for every record is called the",
  ["primary key", "data type", "query", "report"],
  ["A query searches and a report presents results.",
   "A uniquely identifying field is the <b>primary key</b>."],
  ok=True)
O("Which of the following is a database management program?",
  ["Microsoft Access", "Microsoft Word", "Microsoft PowerPoint", "Notepad"],
  ["The others are for text and presentations.",
   "<b>Microsoft Access</b> is a database management program."],
  ok=True)
O("The operation used to find all pupils in a database who scored above 70 is a",
  ["query", "sort", "format", "backup"],
  ["Sorting only arranges records in order.",
   "Finding records that meet a condition is a <b>query</b> (search)."],
  ok=True)
O("A major advantage of a computerised database over a paper filing system is that it",
  ["can be searched in seconds", "needs no electricity",
   "cannot be damaged", "requires no training"],
  ["It does need power, care and training.",
   "Its great advantage is that it <b>can be searched in seconds</b>, and updated without rewriting."],
  ok=True)
T("(a) Define a database. (b) Explain the terms field, record and table, using a school database as an example. "
  "(c) State four advantages of a computerised database over a manual filing system.",
  ["(a) <b>A database is an organised collection of related data stored in such a way that it can be easily accessed, "
   "searched, sorted, updated and reported on.</b>",
   "(b) A <b>field</b> is a single item of data about an entity — in a school database, 'Surname', 'Class' or "
   "'Date of birth'. A <b>record</b> is the complete set of fields about one entity — all the details of the pupil "
   "Ama Mensah. A <b>table</b> is a collection of records of the same type — the details of all the pupils in the school.",
   "(c) <b>Fast searching and sorting</b> — a record is found in seconds instead of hours; <b>easy updating</b>, since "
   "a change is made in one place and appears everywhere; <b>less storage space and no torn or lost papers</b>; "
   "<b>better security</b>, through passwords, access levels and backups; and <b>automatic reports and summaries</b>, "
   "such as class lists, totals and statistics."],
  marks=12, fig=draw.tree("DATABASE", ["Table: all pupils", "Record: one pupil's details",
                                       "Field: Surname, Class, D.O.B.", "Primary key: index number"],
                          label="Database structure"))
extras("database",
  plain="The hierarchy is the whole topic: field → record → table → database. Fix it with a school example and you can "
        "answer almost any question here, including why the voters' register and the national ID are databases rather than lists.",
  examples=[
    E("A clinic keeps patient cards in a cabinet. Give two problems a database would solve.",
      "Step 1. Finding a card takes long and cards get misfiled or lost — a database search is instant and cannot misfile.",
      "Step 2. A patient's address written on several cards gets out of date in some of them — in a database it is stored once.",
      "Step 3. The database also gives <b>automatic reports</b>: how many patients this month, which illnesses are commonest."),
    E("Why should the index number, not the pupil's name, be the primary key?",
      "Step 1. Two pupils may share exactly the same name.",
      "Step 2. A primary key must be unique for every record, or records cannot be told apart.",
      "Step 3. An index number is <b>issued once and never repeated</b>, so it is the proper key.")])
