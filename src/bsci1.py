"""BECE Integrated Science - Diversity of matter, and Cycles."""
from core import *
import draw

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}
A, B = "A. Diversity of matter", "B. Cycles"

# ------------------------------------------------------------------ 1
topic("sciskills", "Science skills, measurement & apparatus", A, [
  "Science starts with <b>observing</b>, then asking a question, then making a prediction (hypothesis), "
  "then testing it by experiment, then drawing a conclusion.",
  "In a fair test you change only <b>one</b> thing at a time and keep everything else the same.",
  "Length is measured with a metre rule or tape (m, cm), mass with a balance (kg, g), "
  "volume of liquid with a measuring cylinder (cm³, ml), temperature with a thermometer (°C) and time with a stop-clock (s).",
  "Volume of an irregular solid is found by displacement: put it in water and measure how much the water rises.",
  "Density = mass ÷ volume, measured in g/cm³.",
])
O("Which instrument is used to measure the volume of a liquid accurately?",
  ["A measuring cylinder", "A beaker", "A test tube", "A funnel"],
  ["Beakers and test tubes hold liquids but are not marked for accurate measurement.",
   "A <b>measuring cylinder</b> has a fine scale, so it gives an accurate volume."],
  ok=True)
O("A stone of mass 60 g displaces 20 cm³ of water. Find its density.",
  ["3 g/cm^{3}", "1 200 g/cm^{3}", "0.33 g/cm^{3}", "80 g/cm^{3}"],
  ["Density = mass ÷ volume = 60 ÷ 20.", "= <b>3 g/cm³</b>."],
  v=60 / 20, nv=[3, 1200, 0.33, 80])
O("In an experiment to find out whether light affects plant growth, which factor must be CHANGED?",
  ["The amount of light", "The type of soil", "The amount of water", "The size of the pot"],
  ["A fair test changes only the factor being investigated and keeps all others the same.",
   "So only <b>the amount of light</b> is changed; soil, water and pot size must be kept the same."],
  ok=True)
O("The volume of an irregularly shaped stone is best found by",
  ["the displacement of water", "measuring with a ruler",
   "weighing it on a balance", "multiplying length by breadth by height"],
  ["An irregular solid has no length and breadth to measure.",
   "Lowering it into water and measuring the rise — <b>the displacement of water</b> — gives its volume."],
  ok=True)
O("Which of the following is a statement of a hypothesis?",
  ["Plants grown in the dark will have pale leaves.", "I measured the height of each plant.",
   "The leaves were pale and the stems were long.", "Why do plants need light?"],
  ["A hypothesis is a <b>prediction</b>, stated before the experiment, that the experiment can test.",
   "<b>Plants grown in the dark will have pale leaves</b> predicts a result, so it can be tested. The others are a question, a record of what was done, and an observation."],
  ok=True)
T("A pupil wants to find the density of a piece of metal. (a) Name the two quantities she must measure and the "
  "instrument for each. (b) Describe how she would find the volume. (c) If the mass is 135 g and the volume is 50 cm³, "
  "calculate the density.",
  ["(a) <b>Mass</b>, measured with a <b>beam balance (or electronic balance)</b>, and <b>volume</b>, measured using a "
   "<b>measuring cylinder</b>.",
   "(b) Half-fill the measuring cylinder with water and read the level, say 40 cm³. Lower the metal in gently and read the "
   "new level, say 90 cm³. The volume of the metal is the difference: 90 − 40 = 50 cm³.",
   "(c) Density = mass ÷ volume = 135 ÷ 50 = <b>2.7 g/cm³</b>."],
  marks=8, ok=(close(135 / 50, 2.7)))
extras("sciskills",
  plain="Science is a way of finding out, not a list of facts to swallow. Every experiment you meet in the BECE has the "
        "same shape: one thing changed, everything else kept the same, and careful measurement in the correct units.",
  examples=[
    E("A block measures 4 cm by 3 cm by 2 cm and has a mass of 96 g. Find its density.",
      "Step 1. Volume of a regular block = l × b × h = 4 × 3 × 2 = 24 cm³.",
      "Step 2. Density = mass ÷ volume = 96 ÷ 24.",
      "Step 3. = <b>4 g/cm³</b>. (Because this is more than 1 g/cm³, the block would sink in water.)"),
    E("Why must a thermometer be left in the liquid while you read it?",
      "Step 1. The liquid in the thermometer must reach the same temperature as the substance.",
      "Step 2. If you take it out, it starts to cool or warm towards room temperature at once.",
      "Step 3. So reading it in place gives <b>the true temperature of the substance</b>.")],
  fig=draw.flow(["Observe", "Ask a question", "Make a hypothesis", "Test by experiment",
                 "Record and analyse", "Draw a conclusion"], label="The scientific method"))

# ------------------------------------------------------------------ 2
topic("matter", "Matter: states, properties & changes", A, [
  "Matter is anything that has mass and occupies space. It exists as <b>solid</b>, <b>liquid</b> or <b>gas</b>.",
  "Solid: fixed shape and volume, particles closely packed and vibrating. Liquid: fixed volume but takes the shape of "
  "the container. Gas: no fixed shape or volume, particles far apart and moving fast.",
  "Changes of state: melting (solid → liquid), freezing (liquid → solid), evaporation and boiling (liquid → gas), "
  "condensation (gas → liquid), sublimation (solid → gas directly).",
  "A <b>physical change</b> can be reversed and makes no new substance (ice melting). "
  "A <b>chemical change</b> makes a new substance and is hard to reverse (wood burning, iron rusting).",
])
O("Which state of matter has a fixed volume but no fixed shape?",
  ["Liquid", "Solid", "Gas", "Vapour"],
  ["A liquid keeps the same volume but flows to take the shape of its container.",
   "A solid has both fixed; a gas (and a vapour, which is a gas) has neither. So the answer is <b>liquid</b>."],
  ok=True)
O("The change of a solid directly into a gas without becoming a liquid is called",
  ["sublimation", "evaporation", "condensation", "melting"],
  ["Camphor and dry ice behave this way.", "The process is called <b>sublimation</b>."],
  ok=True)
O("Which of the following is a chemical change?",
  ["Burning of charcoal", "Melting of candle wax", "Dissolving sugar in water", "Breaking a glass"],
  ["A chemical change makes new substances that cannot easily be changed back.",
   "<b>Burning of charcoal</b> produces ash and gases — the charcoal cannot be got back."],
  ok=True)
O("In which state of matter are the particles farthest apart and moving fastest?",
  ["Gas", "Solid", "Liquid", "They are the same in all three"],
  ["The faster the particles move, the farther apart they spread.",
   "Particles in a <b>gas</b> are farthest apart and move fastest, which is why a gas fills its container."],
  ok=True)
O("Water changing into water vapour at 100 °C is called",
  ["boiling", "condensation", "freezing", "sublimation"],
  ["A liquid becoming a gas throughout, at a fixed temperature, is boiling.",
   "So the change is <b>boiling</b>. (Evaporation happens below the boiling point, at the surface only.)"],
  ok=True)
T("(a) State three differences between a solid and a gas. (b) Give two examples each of a physical change and a "
  "chemical change. (c) Explain why a bicycle tyre becomes hard when it is pumped.",
  ["(a) Solid: fixed shape; fixed volume; particles closely packed and only vibrating. "
   "Gas: no fixed shape; no fixed volume (it fills the container); particles far apart and moving rapidly.",
   "(b) Physical: <b>melting of ice</b>, <b>dissolving salt in water</b> (both reversible, no new substance). "
   "Chemical: <b>rusting of iron</b>, <b>burning of paper</b> (new substances formed).",
   "(c) Pumping forces more air particles into the same space. The particles hit the inside walls of the tyre more often, "
   "so the pressure rises and the tyre feels hard."],
  marks=9, fig=draw.flow(["SOLID", "melting → LIQUID", "boiling → GAS", "condensing → LIQUID", "freezing → SOLID"],
                         label="Changes of state"))
extras("matter",
  plain="Everything around you is matter, and the difference between the three states is simply how closely the particles "
        "are packed and how fast they move. Heat gives particles energy, so heating pushes matter from solid towards gas and cooling pulls it back.",
  examples=[
    E("Why does a puddle of water disappear on a sunny day even though it never boils?",
      "Step 1. The sun gives the surface particles extra energy.",
      "Step 2. The fastest particles escape from the surface into the air — this is evaporation.",
      "Step 3. Evaporation happens at <b>any temperature</b>, so the puddle dries without boiling."),
    E("A pupil says that melting candle wax is a chemical change. Is she right?",
      "Step 1. Ask: is a new substance formed?",
      "Step 2. The melted wax is still wax, and it hardens again on cooling.",
      "Step 3. She is <b>wrong</b> — it is a physical change. (But wax <i>burning</i> is a chemical change.)")])

# ------------------------------------------------------------------ 3
topic("mixtures", "Mixtures & separation", A, [
  "A <b>mixture</b> contains two or more substances that are not chemically joined, so each keeps its own properties "
  "and the mixture can be separated by physical means.",
  "Choose the method by the difference between the parts: "
  "<b>filtration</b> (insoluble solid from liquid), <b>evaporation</b> (dissolved solid from liquid), "
  "<b>distillation</b> (pure liquid from a solution), <b>decantation</b> (pouring off a liquid from settled solid).",
  "Other methods: <b>magnetic separation</b> (iron from sand), <b>winnowing</b> (chaff from grain), "
  "<b>sieving</b> (different grain sizes), <b>chromatography</b> (coloured dyes in ink).",
  "A <b>solution</b> is a solute dissolved in a solvent. A <b>saturated</b> solution can dissolve no more solute at that temperature.",
])
O("Which method is used to separate sand from water?",
  ["Filtration", "Evaporation", "Distillation", "Magnetic separation"],
  ["Sand does not dissolve in water, so it can be trapped by filter paper.",
   "The method is <b>filtration</b>."],
  ok=True)
O("To obtain salt from salt solution, the best method is",
  ["evaporation", "filtration", "decantation", "sieving"],
  ["The salt is dissolved, so filter paper will not stop it.",
   "Heating the solution drives off the water and leaves the salt: <b>evaporation</b>."],
  ok=True)
O("A mixture of iron filings and sulphur powder can be separated using",
  ["a magnet", "a filter funnel", "a sieve", "warm water"],
  ["Iron is magnetic and sulphur is not.", "So <b>a magnet</b> will pick out the iron filings."],
  ok=True)
O("Which method would you use to obtain pure water from sea water?",
  ["Distillation", "Filtration", "Decantation", "Chromatography"],
  ["Filtration would not remove dissolved salts.",
   "<b>Distillation</b> boils the water off and condenses the steam, leaving the salts behind."],
  ok=True)
O("In a solution of sugar in water, the sugar is the",
  ["solute", "solvent", "residue", "filtrate"],
  ["The substance that dissolves is the solute; the liquid that dissolves it is the solvent.",
   "So the sugar is the <b>solute</b> and the water is the solvent."],
  ok=True)
T("A pupil is given a mixture of sand, common salt and iron filings. Describe, step by step, how she can obtain each "
  "of the three substances separately.",
  ["Step 1. <b>Remove the iron filings with a magnet.</b> Pass the magnet over the mixture; the iron sticks to it and "
   "the sand and salt are left.",
   "Step 2. <b>Add water and stir.</b> The salt dissolves; the sand does not.",
   "Step 3. <b>Filter the mixture.</b> The sand stays on the filter paper as the residue; dry it to recover the sand.",
   "Step 4. <b>Evaporate the filtrate.</b> Heat the salt solution gently until the water has gone, leaving the salt behind.",
   "Each step uses one physical difference: magnetism, solubility and then boiling point."],
  marks=10, fig=draw.flow(["Mixture: sand + salt + iron", "Magnet → iron filings",
                           "Add water, filter → sand (residue)", "Evaporate filtrate → salt"],
                          label="Separating a three-part mixture"))
extras("mixtures",
  plain="Every separation question is answered the same way: find a property in which the parts differ — magnetism, "
        "solubility, particle size, boiling point — and use the method that exploits it. Name the property in your answer and the marks follow.",
  examples=[
    E("How would you separate a mixture of groundnut oil and water?",
      "Step 1. Oil does not dissolve in water, and it is less dense, so it floats in a separate layer.",
      "Step 2. Pour the mixture into a separating funnel and let it settle.",
      "Step 3. Run off the lower layer (water) first, leaving the oil — or simply <b>decant</b> the oil off the top."),
    E("Why is filtration useless for separating sugar from sugar solution?",
      "Step 1. Dissolved sugar exists as tiny particles spread among the water particles.",
      "Step 2. These are far smaller than the pores in filter paper, so they pass straight through.",
      "Step 3. You must use <b>evaporation or crystallisation</b> instead.")])

# ------------------------------------------------------------------ 4
topic("elements", "Elements, compounds, atoms & molecules", A, [
  "An <b>element</b> is a pure substance made of only one kind of atom: oxygen, iron, carbon, gold.",
  "A <b>compound</b> is formed when elements join chemically in fixed proportions: water (H₂O), "
  "carbon dioxide (CO₂), sodium chloride (NaCl).",
  "An <b>atom</b> is the smallest particle of an element. A <b>molecule</b> is two or more atoms joined together.",
  "An atom has a nucleus containing <b>protons</b> (positive) and <b>neutrons</b> (no charge), "
  "with <b>electrons</b> (negative) moving around it.",
  "Metals (iron, copper, aluminium) conduct heat and electricity and are malleable; "
  "non-metals (sulphur, carbon, oxygen) generally do not conduct and are brittle.",
])
O("Which of the following is a compound?",
  ["Water", "Oxygen", "Iron", "Carbon"],
  ["Oxygen, iron and carbon are each made of one kind of atom, so they are elements.",
   "<b>Water</b> is made of hydrogen and oxygen chemically joined, so it is a compound."],
  ok=True)
O("The particle in the atom that carries a negative charge is the",
  ["electron", "proton", "neutron", "nucleus"],
  ["Protons are positive and neutrons carry no charge.", "The <b>electron</b> is negatively charged."],
  ok=True)
O("The chemical formula of carbon dioxide is",
  ["CO_{2}", "CO", "C_{2}O", "CaO"],
  ["One carbon atom joins two oxygen atoms.", "So the formula is <b>CO₂</b>. (CO is carbon monoxide.)"],
  ok=True)
O("Which of these is a property of most metals?",
  ["They conduct electricity", "They are brittle", "They are poor conductors of heat", "They are gases at room temperature"],
  ["Metals have free electrons, which carry an electric current.",
   "So most metals <b>conduct electricity</b> — that is why wires are made of copper or aluminium."],
  ok=True)
O("A molecule of oxygen gas contains",
  ["two oxygen atoms", "one oxygen atom", "two oxygen atoms and one hydrogen atom", "eight electrons only"],
  ["Oxygen gas exists as O₂.", "So a molecule of oxygen contains <b>two oxygen atoms</b>."],
  ok=True)
T("(a) State two differences between an element and a compound. (b) Name the three particles found in an atom and "
  "state the charge on each. (c) Give two uses of metals in the home, explaining the property that makes each use possible.",
  ["(a) An element contains only one kind of atom and cannot be broken down by chemical means; a compound contains two or "
   "more elements chemically combined in a fixed ratio and can be broken down into its elements.",
   "(b) <b>Proton</b> — positive; <b>neutron</b> — no charge (neutral); <b>electron</b> — negative.",
   "(c) Cooking pots are made of aluminium because metals are <b>good conductors of heat</b>. "
   "Electrical wiring is made of copper because metals are <b>good conductors of electricity</b>. "
   "(Roofing sheets also work: metals are malleable and can be rolled into sheets.)"],
  marks=9, fig=draw.tree("ATOM", ["Nucleus: protons (+)", "Nucleus: neutrons (0)", "Shells: electrons (−)"],
                         label="Structure of an atom"))
extras("elements",
  plain="Think of elements as the letters of the alphabet and compounds as the words you build with them. There are only "
        "about a hundred elements, but millions of compounds — and in a compound the elements lose their own properties completely.",
  examples=[
    E("Hydrogen burns and oxygen supports burning, yet water puts out fire. Explain.",
      "Step 1. Water is a compound, not a mixture of the two gases.",
      "Step 2. When elements combine chemically, the new substance has entirely new properties.",
      "Step 3. So <b>water behaves like water, not like hydrogen or oxygen</b>."),
    E("Classify each as element, compound or mixture: air, common salt, copper, soft drink.",
      "Step 1. Air is several gases not chemically joined → <b>mixture</b>.",
      "Step 2. Common salt is sodium joined to chlorine → <b>compound</b>; copper is one kind of atom → <b>element</b>.",
      "Step 3. A soft drink contains water, sugar and gas mixed together → <b>mixture</b>.")])

# ------------------------------------------------------------------ 5
topic("acids", "Acids, bases & salts", A, [
  "<b>Acids</b> taste sour, turn blue litmus red and have a pH below 7: lemon juice, vinegar, "
  "hydrochloric acid in the stomach.",
  "<b>Bases (alkalis)</b> feel slippery, turn red litmus blue and have a pH above 7: "
  "caustic soda, lime water, wood ash, soap.",
  "Neutral substances have pH 7: pure water, common salt solution.",
  "Acid + base → <b>salt + water</b>. This reaction is called neutralisation.",
  "Everyday uses: lime or wood ash neutralises acidic soil; antacid tablets neutralise excess stomach acid; "
  "soap (a base) removes acidic dirt.",
])
O("An acid turns blue litmus paper",
  ["red", "blue", "green", "colourless"],
  ["Litmus is the standard indicator: acids turn blue litmus red; bases turn red litmus blue.",
   "So an acid turns blue litmus <b>red</b>."],
  ok=True)
O("A solution with a pH of 10 is",
  ["basic", "acidic", "neutral", "a salt only"],
  ["pH 7 is neutral, below 7 is acidic and above 7 is basic.", "pH 10 is above 7, so the solution is <b>basic</b>."],
  ok=True)
O("When an acid reacts with a base, the products are",
  ["a salt and water", "a salt and hydrogen", "water only", "carbon dioxide and water"],
  ["This reaction is neutralisation.", "Acid + base → <b>salt and water</b>."],
  ok=True)
O("A farmer whose soil is too acidic should add",
  ["lime", "vinegar", "common salt", "sugar"],
  ["Acidic soil must be neutralised by something basic.",
   "<b>Lime</b> (or wood ash) is basic, so it raises the pH of the soil."],
  ok=True)
O("Which of the following is an acid found in the stomach?",
  ["Hydrochloric acid", "Citric acid", "Ethanoic acid", "Sulphuric acid"],
  ["Citric acid is in citrus fruits and ethanoic acid is in vinegar.",
   "The stomach produces <b>hydrochloric acid</b>, which helps digestion and kills germs."],
  ok=True)
T("(a) State three properties of acids. (b) Name one indicator and state the colour it gives in an acid and in a base. "
  "(c) Explain, with an example, how neutralisation is used in everyday life.",
  ["(a) Acids <b>taste sour</b>, <b>turn blue litmus red</b> and <b>react with bases to form salts and water</b>. "
   "(They also react with reactive metals to give off hydrogen, and have a pH below 7.)",
   "(b) <b>Litmus</b>: red in an acid, blue in a base. "
   "(Methyl orange is another acceptable answer: red in acid, yellow in base.)",
   "(c) A person with heartburn takes an <b>antacid tablet</b>, which contains a base. The base neutralises the excess "
   "hydrochloric acid in the stomach, forming a harmless salt and water, and the pain stops. "
   "(Adding lime to acidic farmland is an equally good example.)"],
  marks=9)
extras("acids",
  plain="Acids and bases are opposites, and when they meet they cancel each other out — that is all neutralisation means. "
        "You meet it every day: toothpaste (a base) neutralising acid on your teeth, ash spread on sour soil, an antacid tablet after a heavy meal.",
  examples=[
    E("A pupil tests four liquids with litmus paper. Lime water turns red litmus blue. What does this tell her?",
      "Step 1. Red litmus turning blue is the test for a base.",
      "Step 2. So lime water is basic (alkaline).",
      "Step 3. Its pH must be <b>above 7</b>, and it would neutralise an acid."),
    E("Why does toothpaste contain a mild base?",
      "Step 1. Bacteria in the mouth turn sugar into acid.",
      "Step 2. Acid attacks the enamel of the teeth and causes decay.",
      "Step 3. The mild base in toothpaste <b>neutralises that acid</b>, protecting the enamel.")])

# ------------------------------------------------------------------ 6
topic("living", "Living & non-living things; cells", A, [
  "Living things show the seven characteristics: <b>M</b>ovement, <b>R</b>espiration, <b>S</b>ensitivity, "
  "<b>G</b>rowth, <b>R</b>eproduction, <b>E</b>xcretion and <b>N</b>utrition (MRS GREN).",
  "The <b>cell</b> is the smallest unit of life. Cells form tissues, tissues form organs, organs form systems, "
  "and systems form the organism.",
  "Parts common to plant and animal cells: cell membrane, cytoplasm, nucleus, mitochondria.",
  "Found only in plant cells: a <b>cell wall</b> (made of cellulose), <b>chloroplasts</b> (for photosynthesis) "
  "and a large permanent <b>vacuole</b>.",
  "The nucleus controls the cell's activities; the cell membrane controls what enters and leaves.",
])
O("Which part is found in a plant cell but NOT in an animal cell?",
  ["Chloroplast", "Nucleus", "Cell membrane", "Cytoplasm"],
  ["Nucleus, cell membrane and cytoplasm are found in both kinds of cell.",
   "The <b>chloroplast</b>, which traps sunlight for photosynthesis, is found only in plant cells."],
  ok=True)
O("The part of the cell that controls all its activities is the",
  ["nucleus", "cytoplasm", "cell wall", "vacuole"],
  ["The nucleus contains the genetic material that directs the cell.", "So the answer is the <b>nucleus</b>."],
  ok=True)
O("Which of the following is NOT a characteristic of living things?",
  ["Having a fixed shape", "Reproduction", "Excretion", "Sensitivity"],
  ["Reproduction, excretion and sensitivity are all in MRS GREN.",
   "<b>Having a fixed shape</b> is not a characteristic of life — many non-living things have fixed shapes."],
  ok=True)
O("Arrange in order from the smallest to the largest: organ, cell, tissue, system.",
  ["cell, tissue, organ, system", "cell, organ, tissue, system",
   "tissue, cell, organ, system", "system, organ, tissue, cell"],
  ["Cells of one kind form a tissue; tissues form an organ; organs working together form a system.",
   "So the order is <b>cell, tissue, organ, system</b>."],
  ok=True)
O("The structure that controls the movement of substances into and out of a cell is the",
  ["cell membrane", "nucleus", "cytoplasm", "chloroplast"],
  ["The membrane is the boundary of the cell and is partially permeable.",
   "So it is the <b>cell membrane</b> that controls what goes in and out."],
  ok=True)
T("(a) State the seven characteristics of living things. (b) Draw and label a plant cell, showing three parts not found "
  "in an animal cell. (c) State one function each of the nucleus and the chloroplast.",
  ["(a) <b>Movement, respiration, sensitivity, growth, reproduction, excretion and nutrition</b> (MRS GREN).",
   "(b) The labelled drawing should show the cell wall, cell membrane, cytoplasm, nucleus, a large vacuole and "
   "chloroplasts. The three found only in plant cells are the <b>cell wall</b>, the <b>chloroplasts</b> and the "
   "<b>large permanent vacuole</b>.",
   "(c) The <b>nucleus</b> controls the activities of the cell and carries the hereditary material. "
   "The <b>chloroplast</b> traps sunlight so that the cell can carry out photosynthesis."],
  marks=10, fig=draw.cellfig("plant", label="Plant cell"))
extras("living",
  plain="MRS GREN is the quickest way to decide whether something is alive: a car moves and uses fuel, but it does not "
        "grow, reproduce or respond, so it is not alive. And every living thing, from a maize plant to you, is built from cells.",
  examples=[
    E("A seed looks lifeless. How would you show that it is alive?",
      "Step 1. Living things respire, and respiration releases heat and carbon dioxide.",
      "Step 2. Put soaked seeds in a flask with a thermometer, and boiled (dead) seeds in another.",
      "Step 3. The temperature rises only in the flask of living seeds, showing <b>respiration — so the seed is alive</b>."),
    E("Why do plant cells need a cell wall but animal cells do not?",
      "Step 1. Plants have no bones to hold them up.",
      "Step 2. The rigid cellulose wall keeps each cell firm, and many firm cells together hold the plant upright.",
      "Step 3. Animals have <b>skeletons for support</b>, so their cells need only a flexible membrane.")])

# ------------------------------------------------------------------ 7
topic("classify", "Classification of living things", A, [
  "Living things are grouped to make study easier. The main groups (kingdoms) are plants, animals, fungi, "
  "bacteria and protists.",
  "<b>Vertebrates</b> have a backbone: fish, amphibians, reptiles, birds and mammals. "
  "<b>Invertebrates</b> have none: insects, worms, molluscs, crustaceans, arachnids.",
  "Mammals have hair, give birth to young alive and feed them with milk. Birds have feathers and lay eggs. "
  "Reptiles have dry scaly skin and lay eggs on land. Amphibians live in water and on land. Fish have gills and scales.",
  "Insects have three body parts (head, thorax, abdomen), six legs and usually two pairs of wings.",
  "Flowering plants are divided into <b>monocots</b> (one seed leaf, parallel veins, e.g. maize) and "
  "<b>dicots</b> (two seed leaves, net veins, e.g. beans).",
])
O("Which group of animals has a backbone, hair and feeds its young with milk?",
  ["Mammals", "Birds", "Reptiles", "Amphibians"],
  ["Hair and milk are the two features unique to one group.", "They are the marks of <b>mammals</b>."],
  ok=True)
O("A grasshopper is classified as an insect because it has",
  ["three body parts and six legs", "a backbone and scales",
   "eight legs and two body parts", "feathers and a beak"],
  ["Eight legs would make it an arachnid (like a spider).",
   "An insect has <b>three body parts and six legs</b>."],
  ok=True)
O("Which of the following is an invertebrate?",
  ["Earthworm", "Tilapia", "Toad", "Lizard"],
  ["Tilapia, toad and lizard all have backbones.", "The <b>earthworm</b> has no backbone, so it is an invertebrate."],
  ok=True)
O("Maize is classified as a monocotyledon because its seed has",
  ["one seed leaf", "two seed leaves", "no seed leaf", "a hard shell"],
  ["'Mono' means one.", "A monocotyledon has <b>one seed leaf</b>, and its leaves have parallel veins."],
  ok=True)
O("Animals whose young breathe through gills in water and which later breathe through lungs and a moist skin on land belong to the group called",
  ["amphibians", "reptiles", "fish", "mammals"],
  ["Frogs and toads breathe through gills as tadpoles and through lungs and a moist skin as adults.",
   "Such animals are <b>amphibians</b>. A crocodile also uses water and land, but it is a reptile that breathes with lungs all its life."],
  ok=True)
T("(a) Give two reasons why scientists classify living things. (b) Name the five groups of vertebrates and give one "
  "example of each. (c) State two differences between a monocotyledon and a dicotyledon.",
  ["(a) To make the study of the great variety of living things <b>easier and more orderly</b>, and to show the "
   "<b>relationships</b> between organisms so that information about one member can guide our understanding of others.",
   "(b) <b>Fish</b> — tilapia;  <b>Amphibians</b> — toad;  <b>Reptiles</b> — lizard;  <b>Birds</b> — fowl;  "
   "<b>Mammals</b> — goat.",
   "(c) Monocot: one seed leaf; leaves with parallel veins; fibrous roots (e.g. maize). "
   "Dicot: two seed leaves; leaves with net veins; tap root (e.g. cowpea)."],
  marks=10, fig=draw.tree("ANIMALS", ["Vertebrates: fish, amphibians, reptiles, birds, mammals",
                                      "Invertebrates: insects, worms, molluscs, crustaceans, arachnids"],
                          label="Classification of animals"))
extras("classify",
  plain="Classification is just careful sorting, and the examiner wants the <b>reason</b> for the sorting. Never answer "
        "'it is a mammal' alone — say 'it is a mammal <i>because</i> it has hair and feeds its young with milk'.",
  examples=[
    E("A spider has eight legs and two body parts. Is it an insect? Explain.",
      "Step 1. Recall the insect features: three body parts, six legs, usually wings and antennae.",
      "Step 2. The spider has eight legs and two body parts, and no antennae or wings.",
      "Step 3. So it is <b>not an insect</b> — it belongs to the arachnids."),
    E("Why is a whale classified as a mammal and not as a fish?",
      "Step 1. It lives in water, which makes people guess 'fish'.",
      "Step 2. But it breathes with lungs, has hair, is warm-blooded, and feeds its young with milk.",
      "Step 3. Those are <b>mammalian features</b>, so the whale is a mammal.")])

# ------------------------------------------------------------------ 8  (Cycles)
topic("water", "Water & the water cycle", B, [
  "The water cycle: <b>evaporation</b> from seas and lakes → <b>transpiration</b> from plants → "
  "<b>condensation</b> into clouds → <b>precipitation</b> as rain → run-off and infiltration back to the sea.",
  "Sources of water: rain, rivers, streams, lakes, springs, wells, boreholes and the sea.",
  "Water is called the universal solvent because so many substances dissolve in it.",
  "<b>Hard water</b> contains dissolved calcium and magnesium salts; it wastes soap and forms scale. "
  "<b>Soft water</b> lathers easily with soap.",
  "Water is made safe by filtering, boiling, adding chlorine (or alum to settle the dirt), "
  "and by storing it in clean, covered containers.",
])
O("The change of water from liquid to vapour in the water cycle is called",
  ["evaporation", "condensation", "precipitation", "infiltration"],
  ["Heat from the sun turns surface water into vapour.", "That change is <b>evaporation</b>."],
  ok=True)
O("The loss of water vapour from the leaves of plants is called",
  ["transpiration", "respiration", "condensation", "germination"],
  ["Water escapes through the stomata of the leaves.", "This process is <b>transpiration</b>."],
  ok=True)
O("Clouds are formed when water vapour",
  ["condenses on tiny dust particles high in the air", "evaporates from the sea",
   "freezes in the soil", "dissolves in rain"],
  ["As vapour rises it cools, and cool air cannot hold as much vapour.",
   "So it <b>condenses on tiny dust particles high in the air</b>, forming the droplets we see as cloud."],
  ok=True)
O("Which of these makes water hard?",
  ["Dissolved calcium and magnesium salts", "Dissolved oxygen", "Suspended mud", "Chlorine"],
  ["Hardness is caused by particular dissolved salts, not by dirt.",
   "<b>Dissolved calcium and magnesium salts</b> make water hard, so it wastes soap."],
  ok=True)
O("The best household method of killing germs in drinking water is to",
  ["boil it", "filter it through cloth", "let it settle", "pour it into a clean bottle"],
  ["Filtering and settling remove solid dirt but not germs.",
   "<b>Boiling</b> kills bacteria and other disease organisms."],
  ok=True)
T("(a) Draw a labelled diagram of the water cycle. (b) Name three sources of water in your community. "
  "(c) Describe two ways of making water from a stream safe for drinking. "
  "(d) State two effects of hard water in the home.",
  ["(a) The diagram should show the sun, evaporation from a water body, transpiration from trees, condensation into "
   "cloud, precipitation as rain, and run-off returning to the water body.",
   "(b) Any three of: <b>rain, river or stream, well, borehole, spring, pipe-borne supply</b>.",
   "(c) <b>Boiling</b>: heat the water to boiling point for a few minutes to kill germs. "
   "<b>Filtration followed by chlorination</b>: filter out the mud with clean cloth or a filter, then add the "
   "recommended amount of chlorine (or use alum first to make the dirt settle).",
   "(d) Hard water <b>wastes soap</b> (it forms scum instead of lather) and <b>forms scale in kettles and boilers</b>, "
   "which wastes fuel and can block pipes."],
  marks=12, fig=draw.cyclefig(["Evaporation", "Condensation", "Precipitation", "Run-off"],
                              centre="WATER CYCLE", label="The water cycle"))
extras("water",
  plain="The water you drink today has been round the cycle countless times. Nothing is added and nothing lost — the sun "
        "lifts it, the cold air drops it, and the land returns it. That is why protecting rivers matters: the same water comes back to us.",
  examples=[
    E("Why do drops of water form on the outside of a cold bottle of soft drink?",
      "Step 1. The air around the bottle contains invisible water vapour.",
      "Step 2. The cold surface cools that air below its dew point.",
      "Step 3. The vapour <b>condenses</b> into visible droplets on the bottle — the same process that makes clouds."),
    E("A pupil adds alum to muddy water. What is its purpose?",
      "Step 1. The mud is suspended, not dissolved, and settles very slowly.",
      "Step 2. Alum makes the fine particles clump together into larger, heavier lumps.",
      "Step 3. These sink quickly, so the clear water can be poured off — but it <b>still needs boiling or chlorine</b> to be safe.")])

# ------------------------------------------------------------------ 9
topic("air", "Air, weather & climate", B, [
  "Air is a mixture: about <b>78% nitrogen</b>, <b>21% oxygen</b>, about <b>0.9% noble gases</b> (mostly argon) "
  "and about <b>0.04% carbon dioxide</b>, plus water vapour and dust.",
  "Oxygen supports burning and respiration; carbon dioxide is used by plants in photosynthesis and puts out fire; "
  "nitrogen dilutes oxygen and is used by plants (through bacteria) to make protein.",
  "<b>Weather</b> is the day-to-day condition of the atmosphere; <b>climate</b> is the average weather of a place "
  "over many years.",
  "Weather instruments: rain gauge (rainfall), thermometer (temperature), wind vane (wind direction), "
  "anemometer (wind speed), barometer (air pressure), hygrometer (humidity).",
  "Air has mass, occupies space and exerts pressure — that is why a drinking straw and a syringe work.",
])
O("The percentage of oxygen in air is about",
  ["21%", "78%", "0.04%", "50%"],
  ["Nitrogen makes up about 78% and carbon dioxide only about 0.04%.", "Oxygen is about <b>21%</b> of air."],
  ok=True)
O("Which instrument measures the amount of rainfall?",
  ["Rain gauge", "Barometer", "Anemometer", "Hygrometer"],
  ["A barometer measures pressure, an anemometer wind speed and a hygrometer humidity.",
   "A <b>rain gauge</b> collects and measures rainfall."],
  ok=True)
O("The gas in air used by plants to make food is",
  ["carbon dioxide", "oxygen", "nitrogen", "water vapour"],
  ["Photosynthesis uses carbon dioxide and water in the presence of sunlight.",
   "So the gas is <b>carbon dioxide</b>."],
  ok=True)
O("The average weather condition of a place over a long period is called its",
  ["climate", "weather", "temperature", "season"],
  ["Weather changes from day to day; the long-term pattern is different.",
   "The average over many years is the <b>climate</b>."],
  ok=True)
O("A candle burning in a closed jar goes out after a short time because",
  ["the oxygen in the jar has been used up", "the candle has melted",
   "carbon dioxide has escaped", "the jar has become too hot"],
  ["Burning needs oxygen, and the jar holds only a limited amount.",
   "The flame dies because <b>the oxygen in the jar has been used up</b>."],
  ok=True)
T("(a) Name the two main gases in air and give the approximate percentage of each. "
  "(b) Describe an experiment to show that air has mass. (c) State two differences between weather and climate.",
  ["(a) <b>Nitrogen, about 78%</b>, and <b>oxygen, about 21%</b>.",
   "(b) Balance two identical deflated balloons on a metre rule so that it is level. Now blow air into one balloon and "
   "replace it. <b>The side with the inflated balloon goes down</b>, showing that the air in it has mass. "
   "(Weighing a football before and after pumping works equally well.)",
   "(c) Weather is the condition of the atmosphere <b>at a particular time</b> and it <b>changes from day to day</b>; "
   "climate is the <b>average</b> condition <b>over many years</b> and changes only very slowly."],
  marks=9)
extras("air",
  plain="Air is invisible, which makes it easy to forget that it is matter: it has mass, takes up space and pushes on "
        "everything. Most of it is nitrogen; the fifth of it that is oxygen is what keeps fires burning and keeps us alive.",
  examples=[
    E("Why does a lighted splint go out when lowered into a gas jar of carbon dioxide?",
      "Step 1. Burning needs oxygen.",
      "Step 2. Carbon dioxide does not support burning and is denser than air, so it stays in the jar.",
      "Step 3. The flame has no oxygen and <b>goes out</b> — which is why CO₂ is used in fire extinguishers."),
    E("A pupil records the rainfall for seven days and calls it the climate of the town. Correct her.",
      "Step 1. Seven days of readings describe the <b>weather</b>.",
      "Step 2. Climate needs readings averaged over many years — usually thirty or more.",
      "Step 3. So she has recorded <b>the weather, not the climate</b>.")])

# ------------------------------------------------------------------ 10
topic("soil", "Soil & its properties", B, [
  "Soil is formed by the <b>weathering</b> of rocks together with decayed plant and animal matter (humus).",
  "Soil contains mineral particles, humus, water, air and living organisms.",
  "<b>Sandy soil</b>: large particles, drains quickly, poor at holding water and nutrients. "
  "<b>Clay soil</b>: tiny particles, holds too much water, becomes sticky and waterlogged. "
  "<b>Loamy soil</b>: a balance of sand, silt and clay plus humus — the best for farming.",
  "<b>Humus</b> is decayed organic matter. It supplies nutrients, improves water retention and makes soil crumbly.",
  "Soil is conserved by mulching, cover cropping, crop rotation, adding manure, contour ploughing and terracing, "
  "and by planting trees to break the wind.",
])
O("Which soil type is best for farming?",
  ["Loamy soil", "Sandy soil", "Clay soil", "Gravel"],
  ["Sandy soil loses water and nutrients; clay soil becomes waterlogged.",
   "<b>Loamy soil</b> holds enough water while still draining, and it is rich in humus."],
  ok=True)
O("The decayed remains of plants and animals in the soil is called",
  ["humus", "clay", "silt", "loam"],
  ["This dark organic matter supplies nutrients and improves soil structure.", "It is called <b>humus</b>."],
  ok=True)
O("Sandy soil drains quickly because it has",
  ["large particles with large air spaces", "very small particles",
   "much humus", "a lot of clay"],
  ["Water passes easily through wide gaps between particles.",
   "Sandy soil has <b>large particles with large air spaces</b>, so it drains fast and dries out."],
  ok=True)
O("The breaking down of rocks to form soil is called",
  ["weathering", "erosion", "leaching", "evaporation"],
  ["Erosion is the carrying away of soil; leaching is the washing down of nutrients.",
   "The breaking down of rock itself is <b>weathering</b>."],
  ok=True)
O("Which farming practice best prevents soil erosion on a slope?",
  ["Terracing", "Burning the grass", "Ploughing up and down the slope", "Removing all the trees"],
  ["Ploughing up and down a slope makes channels for water to rush down.",
   "<b>Terracing</b> cuts the slope into steps so that water slows down and soaks in."],
  ok=True)
T("(a) Name the five constituents of soil. (b) Describe a simple experiment to compare the drainage of sandy soil and "
  "clay soil. (c) State three ways in which a farmer can maintain soil fertility.",
  ["(a) <b>Mineral particles (sand, silt, clay), humus, water, air and living organisms.</b>",
   "(b) Set up two funnels with filter paper, each over a measuring cylinder. Put equal masses of dry sandy soil and dry "
   "clay soil in the funnels, and pour the same volume of water (say 100 cm³) into each. After five minutes, measure the "
   "water collected. <b>More water passes through the sandy soil</b>, showing that it drains faster.",
   "(c) Any three of: <b>adding organic manure or compost</b>; <b>crop rotation</b>; <b>planting legumes</b> (which fix "
   "nitrogen); <b>mulching</b>; <b>applying fertiliser in the right amount</b>; <b>leaving land fallow</b>."],
  marks=11, fig=draw.flow(["Rock", "Weathering → small particles",
                           "+ decayed plants and animals (humus)", "SOIL"], label="How soil is formed"))
extras("soil",
  plain="Soil is not just dirt — it is a living mixture of rock particles, humus, water, air and organisms, and it takes "
        "hundreds of years to form a few centimetres of it. That is why farmers protect it: once it washes off a slope, it is gone for a lifetime.",
  examples=[
    E("Why do farmers add manure instead of only chemical fertiliser?",
      "Step 1. Fertiliser supplies nutrients, but nothing else.",
      "Step 2. Manure supplies nutrients <i>and</i> adds humus.",
      "Step 3. Humus <b>holds water, improves the crumb structure and feeds soil organisms</b>, so the soil stays fertile longer."),
    E("A pupil pours water into a pot of clay soil and it stands on the surface. Explain.",
      "Step 1. Clay particles are extremely small and pack tightly together.",
      "Step 2. The air spaces between them are tiny, so water moves through very slowly.",
      "Step 3. The water therefore <b>collects on top — the soil becomes waterlogged</b>, which drowns plant roots.")])

# ------------------------------------------------------------------ 11
topic("lifecycles", "Life cycles of organisms", B, [
  "<b>Complete metamorphosis</b> (four stages): egg → larva → pupa → adult. Examples: mosquito, butterfly, housefly.",
  "<b>Incomplete metamorphosis</b> (three stages): egg → nymph → adult. Examples: grasshopper, cockroach.",
  "The mosquito lays eggs in <b>stagnant water</b>; its larva and pupa live in water and breathe at the surface.",
  "Breaking the cycle controls disease: clear stagnant water, fill pots and tyres, add oil to still water, "
  "use treated nets and screens.",
  "Frog: egg → tadpole (gills, tail, lives in water) → young frog → adult frog (lungs, legs, land and water).",
])
O("The stages in the life cycle of a butterfly are",
  ["egg, larva, pupa, adult", "egg, nymph, adult", "larva, egg, adult", "egg, pupa, larva, adult"],
  ["A butterfly undergoes complete metamorphosis with four stages, in order.",
   "They are <b>egg, larva (caterpillar), pupa and adult</b>."],
  ok=True)
O("The mosquito lays its eggs in",
  ["stagnant water", "dry sand", "fast-flowing rivers", "the leaves of plants"],
  ["The larvae need still water in which to hang at the surface.",
   "So eggs are laid in <b>stagnant water</b> — in pots, tins, old tyres and gutters."],
  ok=True)
O("The best way to control mosquitoes in a community is to",
  ["clear all stagnant water around the houses", "kill adult mosquitoes with the hand",
   "close the windows at night", "boil all drinking water"],
  ["Killing adults one by one hardly dents the population, and boiling water deals with a different problem.",
   "Removing the breeding places — <b>clearing all stagnant water</b> — destroys thousands of larvae at once."],
  ok=True)
O("Which insect undergoes incomplete metamorphosis?",
  ["Cockroach", "Butterfly", "Mosquito", "Housefly"],
  ["A cockroach hatches as a nymph that looks like a small adult and has no pupa stage.",
   "So the <b>cockroach</b> shows incomplete metamorphosis."],
  ok=True)
O("A tadpole breathes by means of",
  ["gills", "lungs", "the skin only", "spiracles"],
  ["A tadpole lives in water and has not yet developed lungs.", "It breathes through <b>gills</b>."],
  ok=True)
T("(a) Draw and label the life cycle of the mosquito. (b) State which two stages live in water. "
  "(c) Give three ways of breaking the life cycle of the mosquito in your community, and explain how each works.",
  ["(a) The cycle is <b>egg → larva → pupa → adult</b>, drawn as a circle with arrows, and labelled.",
   "(b) The <b>larva and the pupa</b> both live in water (and the eggs are laid on water).",
   "(c) <b>Clear stagnant water</b> — pots, tins and tyres — so that there is nowhere to lay eggs. "
   "<b>Pour a thin layer of oil on standing water</b> — the larvae and pupae cannot reach the air to breathe and they die. "
   "<b>Sleep under a treated net and screen the windows</b> — the adult cannot bite, so the malaria parasite is not passed on."],
  marks=11, fig=draw.cyclefig(["Egg (on water)", "Larva (in water)", "Pupa (in water)", "Adult (flies)"],
                              centre="MOSQUITO", label="Life cycle of the mosquito"))
extras("lifecycles",
  plain="Knowing a life cycle is not just book work — it tells you where to strike. The mosquito spends three of its four "
        "stages in still water, so a community that empties its containers every week does more against malaria than any amount of swatting.",
  examples=[
    E("Why is a caterpillar more damaging to crops than an adult butterfly?",
      "Step 1. The caterpillar is the larval stage, whose job is to grow.",
      "Step 2. To grow it eats leaves almost continuously.",
      "Step 3. The adult butterfly feeds only on nectar, so <b>the larva does the damage</b>."),
    E("A pond is full of tadpoles. What will they become, and what changes must happen first?",
      "Step 1. Tadpoles are the larval stage of a frog or toad.",
      "Step 2. They must grow legs, lose the tail, and replace gills with lungs.",
      "Step 3. Then they become <b>young frogs that can live on land as well as in water</b>.")])
