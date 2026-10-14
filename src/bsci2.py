"""BECE Integrated Science - Systems (plants, human body, ecosystems, space, machines, farming)."""
from core import *
import draw

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}
C = "C. Systems"

# ------------------------------------------------------------------ plants
topic("plants", "Plants: parts, photosynthesis & reproduction", C, [
  "Roots anchor the plant and absorb water and mineral salts; the stem supports the plant and carries water and food; "
  "leaves make food; flowers produce seeds.",
  "<b>Photosynthesis</b>: carbon dioxide + water, in the presence of sunlight and chlorophyll → glucose + oxygen. "
  "It takes place mainly in the leaves.",
  "Gases enter and leave the leaf through tiny openings called <b>stomata</b>, usually on the lower surface.",
  "Parts of a flower: sepals (protect the bud), petals (attract insects), stamens (anther + filament, make pollen) "
  "and the pistil/carpel (stigma, style, ovary — contains the ovules).",
  "<b>Pollination</b> is the transfer of pollen from anther to stigma; <b>fertilisation</b> is the fusion of the "
  "<b>male nucleus from the pollen grain with the egg cell inside the ovule</b>. The ovary then becomes the fruit "
  "and each fertilised ovule becomes a seed.",
])
O("The raw materials for photosynthesis are",
  ["carbon dioxide and water", "oxygen and water",
   "glucose and oxygen", "carbon dioxide and glucose"],
  ["Glucose and oxygen are the <i>products</i>, not the raw materials.",
   "The raw materials are <b>carbon dioxide and water</b>, with sunlight as the energy source."],
  ok=True)
O("The green substance in leaves that traps sunlight is",
  ["chlorophyll", "chloroform", "cytoplasm", "starch"],
  ["It is housed in the chloroplasts of leaf cells.", "The green pigment is <b>chlorophyll</b>."],
  ok=True)
O("The tiny openings in a leaf through which gases pass are called",
  ["stomata", "veins", "cuticles", "petioles"],
  ["Each opening is guarded by two guard cells that can open and close it.",
   "They are the <b>stomata</b> (singular: stoma)."],
  ok=True)
O("The part of the flower that produces pollen grains is the",
  ["anther", "stigma", "ovary", "sepal"],
  ["The stigma receives pollen and the ovary holds the ovules.",
   "Pollen is produced by the <b>anther</b>, at the top of the stamen."],
  ok=True)
O("After fertilisation, the ovary of a flower develops into the",
  ["fruit", "seed", "flower bud", "root"],
  ["The ovules inside become the seeds.", "The ovary itself becomes the <b>fruit</b>, which encloses them."],
  ok=True)
T("(a) Write the word equation for photosynthesis. (b) Describe an experiment to show that light is necessary for "
  "photosynthesis. (c) State two differences between pollination and fertilisation.",
  ["(a) <b>Carbon dioxide + water → glucose + oxygen</b> (in the presence of sunlight and chlorophyll).",
   "(b) Destarch a potted plant by keeping it in the dark for two days. Then cover part of one leaf on both sides with "
   "black paper and place the plant in sunlight for several hours. Remove the leaf and boil it in water to kill it. "
   "<b>Put out the flame</b>, then decolourise the leaf in alcohol stood in a <b>hot water bath</b> \u2014 alcohol catches fire easily, so it must never be heated directly over a flame. Rinse the leaf in warm water to soften it, then add iodine solution. "
   "<b>The uncovered part turns blue-black (starch present) while the covered part stays brown (no starch)</b>, "
   "showing that light is necessary.",
   "(c) Pollination is the <b>transfer of pollen</b> from anther to stigma and happens <b>outside</b> the ovule, often "
   "with the help of insects or wind. Fertilisation is the <b>fusion of the male and female nuclei</b> and happens "
   "<b>inside the ovule</b>, after the pollen has grown a tube down the style."],
  marks=12, fig=draw.flow(["CO₂ (through stomata) + water (from roots)",
                           "Sunlight trapped by chlorophyll", "Glucose (food) + oxygen"],
                          label="Photosynthesis in a leaf"))
extras("plants",
  plain="Green plants are the only members of an ecosystem that make their own food, which is why every food chain begins "
        "with them. Photosynthesis is the single most important reaction on earth: it stores the sun's energy as food and releases the oxygen we breathe.",
  examples=[
    E("Why are most stomata found on the lower surface of a leaf?",
      "Step 1. Open stomata lose water vapour as well as exchanging gases.",
      "Step 2. The upper surface faces the sun and is much hotter.",
      "Step 3. Keeping the stomata underneath <b>reduces water loss</b> while still allowing gases in and out."),
    E("A plant is kept in a well-lit room but is never watered. Why does photosynthesis stop?",
      "Step 1. Photosynthesis needs two raw materials: carbon dioxide and water.",
      "Step 2. Light and carbon dioxide are available, but water is not.",
      "Step 3. A missing raw material <b>stops the process</b>, however much light there is.")])

# ------------------------------------------------------------------ digestion
topic("digest", "Food, nutrition & digestion", C, [
  "A balanced diet contains carbohydrates (energy), proteins (growth and repair), fats and oils (energy and warmth), "
  "vitamins, mineral salts, water and roughage (fibre).",
  "Deficiency diseases: kwashiorkor and marasmus (protein-energy), scurvy (vitamin C), rickets (vitamin D), "
  "night blindness (vitamin A), anaemia (iron), goitre (iodine).",
  "Digestion begins in the mouth, where <b>amylase</b> in saliva acts on starch; the stomach makes hydrochloric acid "
  "and <b>pepsin</b> for protein; the small intestine completes digestion and absorbs the food.",
  "<b>Bile</b> from the liver (stored in the gall bladder) emulsifies fats — it is not an enzyme.",
  "Food tests: iodine → blue-black for starch; Benedict's solution → brick-red for reducing sugar; "
  "a greasy translucent mark on paper for fat.",
])
O("Which class of food is needed mainly for growth and repair of the body?",
  ["Proteins", "Carbohydrates", "Fats and oils", "Vitamins"],
  ["Carbohydrates and fats supply energy, and vitamins protect the body.",
   "<b>Proteins</b> build and repair tissue, so growing children need plenty of them."],
  ok=True)
O("The disease caused by a shortage of vitamin C is",
  ["scurvy", "rickets", "goitre", "night blindness"],
  ["Rickets comes from a lack of vitamin D, goitre from a lack of iodine and night blindness from a lack of vitamin A.",
   "A shortage of vitamin C causes <b>scurvy</b> — bleeding gums and slow healing."],
  ok=True)
O("The enzyme in saliva acts on",
  ["starch", "protein", "fat", "vitamins"],
  ["Salivary amylase breaks starch down to maltose.", "So the enzyme in saliva acts on <b>starch</b>."],
  ok=True)
O("Iodine solution is added to a food sample and turns blue-black. The food contains",
  ["starch", "protein", "fat", "sugar"],
  ["Blue-black with iodine is the standard test result for one food class.",
   "The food contains <b>starch</b>."],
  ok=True)
O("Most of the absorption of digested food takes place in the",
  ["small intestine", "stomach", "mouth", "large intestine"],
  ["The small intestine is long and lined with villi, giving a huge surface area.",
   "So most absorption happens in the <b>small intestine</b>. (The large intestine absorbs mainly water.)"],
  ok=True)
T("(a) Name the seven components of a balanced diet. (b) State the cause and two symptoms of kwashiorkor. "
  "(c) Describe how you would test a sample of food for starch and for fat.",
  ["(a) <b>Carbohydrates, proteins, fats and oils, vitamins, mineral salts, water and roughage (fibre).</b>",
   "(b) Kwashiorkor is caused by a <b>shortage of protein in the diet</b>, usually in young children after weaning. "
   "Symptoms: <b>swollen belly, legs and feet (oedema)</b>, <b>thin reddish hair that falls out easily</b>, "
   "a thin wasted body with a moon face, and loss of appetite.",
   "(c) <b>Starch</b>: put a little of the food in a dish and add two or three drops of iodine solution. "
   "A blue-black colour shows starch. "
   "<b>Fat</b>: rub the food on a piece of plain paper and hold it up to the light. A permanent translucent (greasy) "
   "spot shows fat. (Alternatively, shake the food with ethanol and add water: a milky emulsion shows fat.)"],
  marks=12, fig=draw.flow(["Mouth: amylase on starch", "Stomach: acid + pepsin on protein",
                           "Small intestine: digestion completed, food absorbed",
                           "Large intestine: water absorbed", "Rectum: waste removed"],
                          label="The path of food through the alimentary canal"))
extras("digest",
  plain="Digestion is the business of turning food you cannot use into food your blood can carry. Big molecules (starch, "
        "protein, fat) are chopped into small ones (sugar, amino acids, fatty acids) by enzymes, then absorbed through the wall of the small intestine.",
  examples=[
    E("Why is roughage important even though it is not digested?",
      "Step 1. Roughage is plant fibre that passes through the gut unchanged.",
      "Step 2. It adds bulk, which the muscles of the gut can push against.",
      "Step 3. So it <b>keeps food moving and prevents constipation</b>."),
    E("A child eats only cassava and gari. Which deficiency disease is likely, and why?",
      "Step 1. Cassava and gari are almost pure carbohydrate.",
      "Step 2. The diet therefore lacks protein.",
      "Step 3. The likely disease is <b>kwashiorkor</b>; adding beans, groundnuts, fish or eggs would prevent it.")])

# ------------------------------------------------------------------ respiration & circulation
topic("circ", "Respiration & circulation", C, [
  "<b>Respiration</b> releases energy from food: glucose + oxygen → carbon dioxide + water + energy. "
  "It happens in every living cell, in the mitochondria.",
  "<b>Breathing</b> is only the taking in and giving out of air; respiration is the chemical release of energy. "
  "They are not the same thing.",
  "Air passes: nose → trachea → bronchi → bronchioles → alveoli (air sacs), where gases exchange with the blood.",
  "The heart has four chambers: right atrium, right ventricle, left atrium, left ventricle. "
  "<b>Arteries</b> carry blood away from the heart, <b>veins</b> carry it back, and <b>capillaries</b> link them.",
  "Blood carries oxygen (in red cells, using haemoglobin), food, carbon dioxide and wastes; "
  "white cells fight disease and platelets help clotting.",
])
O("The word equation for respiration is",
  ["glucose + oxygen → carbon dioxide + water + energy",
   "carbon dioxide + water → glucose + oxygen",
   "glucose → carbon dioxide + energy",
   "oxygen + water → glucose + carbon dioxide"],
  ["Respiration is the reverse of photosynthesis in its materials, and it releases energy.",
   "So: <b>glucose + oxygen → carbon dioxide + water + energy</b>."],
  ok=True)
O("Gaseous exchange in the lungs takes place in the",
  ["alveoli", "trachea", "bronchi", "diaphragm"],
  ["The alveoli are thin-walled air sacs surrounded by capillaries, giving a large moist surface.",
   "So exchange happens in the <b>alveoli</b>."],
  ok=True)
O("Blood vessels that carry blood away from the heart are called",
  ["arteries", "veins", "capillaries", "ventricles"],
  ["Veins return blood to the heart; capillaries join the two.",
   "<b>Arteries</b> carry blood away from the heart, under high pressure."],
  ok=True)
O("The substance in red blood cells that carries oxygen is",
  ["haemoglobin", "plasma", "platelets", "insulin"],
  ["It is an iron-containing pigment that joins loosely with oxygen.", "It is <b>haemoglobin</b>."],
  ok=True)
O("Which of the following shows the difference between breathing and respiration?",
  ["Breathing takes in air; respiration releases energy from food",
   "Breathing happens in plants; respiration happens in animals",
   "Breathing uses carbon dioxide; respiration uses oxygen",
   "They mean exactly the same thing"],
  ["Breathing is a physical process of the chest; respiration is a chemical process in the cells.",
   "So: <b>breathing takes in air; respiration releases energy from food</b>."],
  ok=True)
T("(a) State three ways in which the alveoli are suited to gaseous exchange. (b) Name the four chambers of the heart. "
  "(c) State two differences between an artery and a vein.",
  ["(a) They are <b>very numerous and thin-walled (one cell thick)</b>, giving a short distance for gases to cross; "
   "they provide a <b>very large surface area</b>; and they are <b>moist and richly supplied with capillaries</b>, so "
   "gases dissolve and are carried away at once.",
   "(b) <b>Right atrium, right ventricle, left atrium and left ventricle.</b>",
   "(c) An artery has <b>thick, muscular, elastic walls</b> and carries blood <b>away from the heart under high "
   "pressure</b>, with no valves along its length. A vein has <b>thinner walls and a wider lumen</b>, carries blood "
   "<b>towards the heart under low pressure</b>, and has <b>valves</b> to stop back-flow."],
  marks=11)
extras("circ",
  plain="Two systems work as one: the lungs load oxygen into the blood and the heart pushes that blood to every cell. "
        "Keep the two words straight — breathing is the air going in and out, respiration is the energy being released inside the cells.",
  examples=[
    E("Why do you breathe faster when you run?",
      "Step 1. Running makes the muscles work harder, so they need more energy.",
      "Step 2. More energy means more respiration, which needs more oxygen and produces more carbon dioxide.",
      "Step 3. Breathing speeds up to <b>supply the extra oxygen and remove the extra carbon dioxide</b>."),
    E("A person with too little iron in the diet feels tired all the time. Explain.",
      "Step 1. Iron is needed to make haemoglobin.",
      "Step 2. With little haemoglobin the blood carries less oxygen — this is anaemia.",
      "Step 3. Cells get less oxygen, so <b>less energy is released and the person feels weak and tired</b>.")])

# ------------------------------------------------------------------ reproduction & adolescence
topic("repro", "Reproduction & adolescent health", C, [
  "Reproduction is the production of new individuals. Humans reproduce sexually: a sperm cell fuses with an egg cell "
  "(fertilisation) to form a zygote, which develops in the uterus.",
  "The male reproductive system includes the testes (which make sperm), while the female system includes the ovaries "
  "(which make egg cells), the oviducts, the uterus and the vagina.",
  "<b>Adolescence</b> is the stage between childhood and adulthood, brought about by hormones. "
  "Changes include rapid growth, growth of body hair, change of voice and the development of the reproductive organs.",
  "Adolescents need good personal hygiene (daily bathing, clean clothing), a balanced diet, enough sleep and exercise.",
  "Responsible behaviour — abstinence, avoiding peer pressure, saying no firmly, concentrating on school work and "
  "talking to a trusted adult — protects an adolescent from teenage pregnancy and sexually transmitted infections, "
  "which interrupt education and endanger health.",
])
O("The fusion of a sperm cell and an egg cell is called",
  ["fertilisation", "pollination", "ovulation", "menstruation"],
  ["Ovulation is the release of the egg; fusion is a different event.",
   "The fusion of the two sex cells is <b>fertilisation</b>."],
  ok=True)
O("In the human female, the egg cells are produced in the",
  ["ovaries", "uterus", "oviduct", "vagina"],
  ["The uterus is where the baby develops and the oviduct carries the egg.",
   "Egg cells are produced in the <b>ovaries</b>."],
  ok=True)
O("Which of the following is a change that occurs during adolescence?",
  ["Growth of hair in the armpits", "Loss of the milk teeth",
   "Learning to walk", "Shortening of the bones"],
  ["Losing milk teeth and learning to walk happen in childhood.",
   "<b>Growth of hair in the armpits</b> is one of the changes of adolescence, caused by hormones."],
  ok=True)
O("The fertilised egg (zygote) develops into a baby in the",
  ["uterus", "ovary", "oviduct", "cervix"],
  ["The zygote travels down the oviduct and attaches to the wall of the womb.",
   "It develops in the <b>uterus</b> (womb)."],
  ok=True)
O("The surest way for a school pupil to avoid teenage pregnancy and sexually transmitted infections is",
  ["abstinence", "keeping it a secret", "taking herbal medicine", "changing schools"],
  ["Only one choice removes the risk completely.",
   "<b>Abstinence</b> — choosing not to engage in sexual activity — is the surest protection, and it also protects a "
   "pupil's education."],
  ok=True)
T("(a) State four physical changes that take place in adolescents. (b) Give three reasons why personal hygiene is "
  "especially important during adolescence. (c) State three effects of teenage pregnancy on a pupil's life.",
  ["(a) Any four of: <b>rapid increase in height and weight</b>; <b>growth of hair under the arms and on the body</b>; "
   "<b>change (deepening) of the voice, especially in boys</b>; <b>broadening of the shoulders in boys and of the hips in "
   "girls</b>; <b>development of the reproductive organs</b>; <b>increased activity of the sweat and oil glands</b>.",
   "(b) The sweat and oil glands become more active, so the body develops an odour and the skin becomes oily — "
   "<b>daily bathing and clean clothes prevent body odour and skin infections</b>. "
   "Good hygiene also <b>builds confidence and self-respect</b>, and it <b>prevents the spread of germs</b> to others.",
   "(c) Any three of: the pupil's <b>education is interrupted or ended</b>; there are <b>health risks to a young mother "
   "and her baby</b>; <b>loss of income and dependence on others</b>; <b>stigma and loss of friendships</b>; "
   "<b>the baby may be poorly cared for</b> because the mother is herself a child."],
  marks=10)
extras("repro",
  plain="Adolescence is the body preparing for adulthood, and the changes are normal — they happen to everybody, though at "
        "different times. The science matters practically: understanding how reproduction works is what makes it possible to make informed, responsible decisions about your own body and your future.",
  examples=[
    E("Why do adolescents sweat more and need to bathe more often?",
      "Step 1. Hormones make the sweat and oil glands in the skin much more active.",
      "Step 2. Sweat itself has little smell, but bacteria on the skin break it down and produce the odour.",
      "Step 3. <b>Bathing daily with soap and wearing clean clothes removes the sweat and the bacteria</b>, so there is no odour."),
    E("A classmate is pressing a pupil to do something she knows is wrong. What should she do?",
      "Step 1. Recognise that this is peer pressure, and that the decision is hers alone.",
      "Step 2. Say no clearly and firmly, without arguing or explaining at length, and leave the situation.",
      "Step 3. <b>Talk to a parent, teacher, counsellor or another trusted adult</b> — getting support early is what makes it easier to keep saying no.")])

# ------------------------------------------------------------------ health
topic("health", "Diseases, hygiene & first aid", C, [
  "Communicable (infectious) diseases are caused by germs that can be passed on \u2014 directly from person to person "
  "(tuberculosis, measles, COVID-19, HIV and AIDS), through contaminated food and water (cholera, typhoid), or "
  "through a <b>vector</b> such as a mosquito (malaria). Malaria is <i>not</i> caught from another person.",
  "Non-communicable diseases do not spread: diabetes, high blood pressure, sickle-cell disease, cancer, asthma.",
  "Malaria is caused by a <b>parasite (Plasmodium)</b> carried by the female <i>Anopheles</i> mosquito. "
  "Cholera and typhoid come from water and food contaminated with faeces; they spread where sanitation is poor.",
  "Prevention: clean water, washing hands with soap, proper toilets, covering food, immunisation, treated nets, "
  "clearing stagnant water and refuse.",
  "First aid is the immediate help given before the patient reaches a health worker: "
  "wash a wound with clean water and cover it; cool a burn under clean running water for <b>at least 20 minutes</b>; immobilise a suspected fracture; "
  "lay a faint patient down with the legs raised. Then send for help.",
])
O("Malaria is caused by",
  ["a parasite carried by the female Anopheles mosquito", "a bacterium in dirty water",
   "a virus spread by coughing", "a shortage of iron in the diet"],
  ["The mosquito is only the carrier (vector), not the cause.",
   "Malaria is caused by <b>a parasite (Plasmodium) carried by the female Anopheles mosquito</b>."],
  ok=True)
O("Which of these diseases is NOT communicable?",
  ["Diabetes", "Cholera", "Tuberculosis", "Measles"],
  ["Cholera, tuberculosis and measles all pass from one person to another.",
   "<b>Diabetes</b> cannot be caught from another person, so it is non-communicable."],
  ok=True)
O("Cholera spreads mainly through",
  ["contaminated food and water", "mosquito bites", "shaking hands", "breathing dusty air"],
  ["The bacterium is passed out in faeces and reaches others through what they swallow.",
   "So cholera spreads through <b>contaminated food and water</b>."],
  ok=True)
O("The first thing to do for a person with a minor burn is to",
  ["cool it under clean running water", "rub oil or butter on it",
   "cover it with cotton wool", "burst the blister"],
  ["Oil traps the heat and cotton wool sticks to the wound; bursting a blister invites infection.",
   "You should <b>cool it under clean running water for at least 20 minutes</b>, then cover it loosely with a clean cloth or cling film. Never use ice, oil, butter or toothpaste."],
  ok=True)
O("The best way to prevent the spread of diarrhoeal diseases in a school is to",
  ["wash hands with soap after using the toilet", "take medicine every morning",
   "drink only cold water", "close the school"],
  ["The germs travel from faeces to mouth, usually on hands.",
   "<b>Washing hands with soap after using the toilet</b> breaks that route."],
  ok=True)
T("(a) State three differences between communicable and non-communicable diseases, giving one example of each. "
  "(b) Describe four ways of preventing malaria in your community. "
  "(c) State the first aid you would give to a classmate who has a deep cut on the arm.",
  ["(a) Communicable diseases are <b>caused by germs</b>, <b>spread from person to person</b> (through air, water, food, "
   "contact or a vector) and can cause outbreaks — for example <b>cholera</b>. Non-communicable diseases are "
   "<b>not caused by germs passing between people</b>, often arise from the way we live or from heredity, and "
   "<b>cannot be caught</b> — for example <b>diabetes</b>.",
   "(b) <b>Sleep under an insecticide-treated net.</b> <b>Clear stagnant water</b> and weeds around the house so "
   "mosquitoes cannot breed. <b>Screen windows and doors</b> and use repellents. "
   "<b>Report fever early for testing and complete the treatment</b>, so the parasite is not passed on.",
   "(c) <b>Protect yourself first</b> \u2014 wash your hands and, if you can, wear gloves or put a clean plastic bag over your hand, because blood can carry infection. <b>Press a clean cloth firmly on the wound</b> to stop the bleeding and "
   "<b>raise the arm above the level of the heart</b>. When bleeding slows, <b>clean around the wound with clean water "
   "and cover it with a sterile dressing</b>. Do not apply herbs or dust. "
   "<b>Take the classmate to the clinic at once</b>, as a deep cut may need stitches and an anti-tetanus injection."],
  marks=12)
extras("health",
  plain="Almost every common disease in Ghana is preventable, and the methods are cheap: clean water, soap, a covered "
        "toilet, a treated net and immunisation. Knowing how a disease travels tells you exactly where to break its journey.",
  examples=[
    E("A village uses the same stream for drinking and for washing. Which diseases are likely, and what single change would help most?",
      "Step 1. Faecal matter reaching the stream carries cholera and typhoid bacteria, and the water also hosts bilharzia.",
      "Step 2. Those are water-borne or water-related diseases.",
      "Step 3. The greatest single improvement is <b>a protected water source (borehole) plus proper latrines away from the stream</b>."),
    E("Why is it important to finish a course of prescribed medicine even after you feel better?",
      "Step 1. Feeling better means most of the germs have been killed, not all.",
      "Step 2. The survivors can multiply again, and they are the ones best able to resist the drug.",
      "Step 3. Stopping early can cause <b>a relapse and drug-resistant germs</b> — which is how resistant tuberculosis and malaria arise.")])

# ------------------------------------------------------------------ ecosystems
topic("ecosystem", "Ecosystems & food chains", C, [
  "An <b>ecosystem</b> is a community of living things together with their non-living surroundings.",
  "<b>Producers</b> (green plants) make their own food. <b>Consumers</b> eat other organisms: "
  "herbivores eat plants, carnivores eat flesh, omnivores eat both. "
  "<b>Decomposers</b> (bacteria and fungi) break down dead matter.",
  "A <b>food chain</b> shows the flow of energy: grass → grasshopper → lizard → hawk. The arrow means 'is eaten by'.",
  "Several interlinked food chains make a <b>food web</b>. Energy is lost at each step, so a chain is usually short.",
  "Relationships: competition (for food, light, space), predation, parasitism and symbiosis.",
])
O("In the food chain maize → grasshopper → lizard → hawk, the producer is",
  ["maize", "grasshopper", "lizard", "hawk"],
  ["Only green plants make their own food by photosynthesis.", "So the producer is <b>maize</b>."],
  ok=True)
O("Organisms that break down dead plants and animals are called",
  ["decomposers", "producers", "herbivores", "predators"],
  ["Bacteria and fungi return nutrients to the soil.", "They are the <b>decomposers</b>."],
  ok=True)
O("In a food chain, the arrow (→) means",
  ["is eaten by", "eats", "lives with", "changes into"],
  ["The arrow follows the direction in which energy flows.",
   "'Grass → goat' therefore reads 'grass <b>is eaten by</b> goat'."],
  ok=True)
O("An animal that eats both plants and flesh is called",
  ["an omnivore", "a herbivore", "a carnivore", "a decomposer"],
  ["A herbivore eats plants only and a carnivore flesh only.",
   "An animal that eats both — like the domestic fowl or a human being — is <b>an omnivore</b>."],
  ok=True)
O("Why are food chains usually short?",
  ["Energy is lost at each stage", "Animals cannot find enough water",
   "There are too few decomposers", "Plants grow slowly"],
  ["Each organism uses most of the energy it takes in for its own life processes, and much is lost as heat.",
   "Because <b>energy is lost at each stage</b>, there is not enough left to support many more levels."],
  ok=True)
T("The following organisms live in a grassland: grass, grasshoppers, lizards, hawks and mushrooms. "
  "(a) Construct a food chain using four of them. (b) Name the producer and the top consumer in your chain. "
  "(c) What is the role of the mushroom? (d) Explain what would happen to the lizards if all the grasshoppers died.",
  ["(a) <b>Grass → grasshopper → lizard → hawk.</b>",
   "(b) Producer: <b>grass</b>. Top consumer: <b>hawk</b>.",
   "(c) The mushroom is a fungus and therefore a <b>decomposer</b>: it feeds on dead organic matter and returns "
   "nutrients to the soil, where the grass can use them again.",
   "(d) The lizards would lose their food supply. Their numbers would <b>fall sharply</b> as they starved or migrated; "
   "the hawks that depend on them would then also decline, while the grass, no longer eaten by grasshoppers, "
   "would increase at first. This shows how every member of a food chain depends on the others."],
  marks=10, fig=draw.flow(["Grass (producer)", "Grasshopper (herbivore)", "Lizard (carnivore)", "Hawk (top consumer)"],
                          label="A grassland food chain", note="Mushrooms and bacteria decompose all of them"))
extras("ecosystem",
  plain="An ecosystem is a working whole: remove one part and the others feel it. Follow the arrows in a food chain and "
        "you are following the sun's energy — captured by a green plant, passed on at each bite, and finally returned to the soil by decomposers.",
  examples=[
    E("Farmers kill all the hawks in an area to protect their chickens. What may happen to the rats?",
      "Step 1. Hawks are predators of rats as well as of chickens.",
      "Step 2. With the predator gone, fewer rats are eaten.",
      "Step 3. The rat population <b>increases</b>, and the farmers may lose more grain to rats than they ever lost chickens to hawks."),
    E("Why is a mushroom not a producer, even though it is not an animal?",
      "Step 1. A producer makes its own food by photosynthesis.",
      "Step 2. Mushrooms have no chlorophyll, so they cannot photosynthesise.",
      "Step 3. They feed on dead organic matter, so they are <b>decomposers</b> (saprophytes).")])

# ------------------------------------------------------------------ space
topic("solar", "The solar system & space science", C, [
  "The solar system is the sun together with the eight planets and other bodies that orbit it.",
  "In order from the sun: <b>Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune</b>.",
  "The earth <b>rotates</b> on its axis once in 24 hours, which gives day and night. "
  "It <b>revolves</b> round the sun once in about 365¼ days, which gives the year and the seasons.",
  "The moon is the earth's natural satellite. It shines by reflected sunlight and its phases depend on how much of "
  "the lit half we can see.",
  "An <b>eclipse of the sun</b> occurs when the moon comes between the sun and the earth; "
  "an <b>eclipse of the moon</b> occurs when the earth comes between the sun and the moon.",
])
O("Which planet is nearest to the sun?",
  ["Mercury", "Venus", "Earth", "Mars"],
  ["The order outwards begins Mercury, Venus, Earth, Mars.", "The nearest is <b>Mercury</b>."],
  ok=True)
O("Day and night are caused by the",
  ["rotation of the earth on its axis", "revolution of the earth round the sun",
   "movement of the moon round the earth", "tilting of the earth's axis"],
  ["Rotation turns one half of the earth towards the sun and the other away from it.",
   "So day and night are caused by the <b>rotation of the earth on its axis</b> once every 24 hours."],
  ok=True)
O("An eclipse of the sun occurs when",
  ["the moon comes between the sun and the earth", "the earth comes between the sun and the moon",
   "the sun comes between the earth and the moon", "the moon enters the earth's shadow"],
  ["The body in the middle casts the shadow, and in a solar eclipse the shadow falls on the earth.",
   "So it happens when <b>the moon comes between the sun and the earth</b>."],
  ok=True)
O("The moon is seen at night because it",
  ["reflects light from the sun", "produces its own light",
   "burns gases like the sun", "reflects light from the earth"],
  ["The moon has no light of its own.", "We see it because it <b>reflects light from the sun</b>."],
  ok=True)
O("The earth takes about 365¼ days to",
  ["revolve once round the sun", "rotate once on its axis",
   "complete one phase of the moon", "change from one season to the next"],
  ["One rotation takes 24 hours.", "It takes about 365¼ days to <b>revolve once round the sun</b> — one year."],
  ok=True)
T("(a) List the eight planets in order of their distance from the sun. (b) State two differences between rotation and "
  "revolution of the earth. (c) With the aid of a simple diagram, explain how an eclipse of the moon occurs.",
  ["(a) <b>Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune.</b>",
   "(b) Rotation is the spinning of the earth <b>on its own axis</b> and takes <b>24 hours</b>, causing day and night. "
   "Revolution is the movement of the earth <b>round the sun</b> and takes <b>about 365¼ days</b>, causing the year and "
   "the seasons.",
   "(c) In a lunar eclipse the <b>earth lies between the sun and the moon</b>, in a straight line. "
   "The earth blocks the sunlight and casts its shadow on the moon, so the moon darkens. "
   "The diagram should show the sun on one side, then the earth, then the moon inside the earth's shadow."],
  marks=10, fig=draw.flow(["SUN", "EARTH (casts a shadow)", "MOON in the shadow → lunar eclipse"],
                          label="Eclipse of the moon"))
extras("solar",
  plain="Two different movements explain almost every question about the earth in space: spinning (rotation) gives day and "
        "night, and travelling round the sun (revolution) gives the year. Keep the two words apart and the topic becomes easy.",
  examples=[
    E("Why is it daytime in Ghana while it is night in Japan?",
      "Step 1. The earth is a sphere, so the sun can light only one half of it at a time.",
      "Step 2. As the earth rotates, different places turn into and out of that lit half.",
      "Step 3. Ghana and Japan are far apart in longitude, so <b>when Ghana faces the sun, Japan has turned away from it</b>."),
    E("Why can an eclipse of the sun be seen only from a small part of the earth?",
      "Step 1. The moon is much smaller than the earth.",
      "Step 2. Its full shadow (umbra) therefore covers only a narrow strip of the earth's surface.",
      "Step 3. <b>Only people inside that strip see a total eclipse</b>; others nearby see a partial one, and the rest see none.")])

# ------------------------------------------------------------------ machines
topic("machines", "Simple machines", C, [
  "A machine makes work easier by changing the size or direction of a force. "
  "Examples: lever, inclined plane, pulley, wheel and axle, screw, wedge.",
  "<b>Levers</b> have three classes according to the position of the fulcrum, the effort and the load: "
  "class 1 — fulcrum in the middle (see-saw, scissors, claw hammer); "
  "class 2 — load in the middle (wheelbarrow, nut-cracker); "
  "class 3 — effort in the middle (tongs, broom, fishing rod).",
  "Mechanical advantage = load ÷ effort. Velocity ratio = distance moved by effort ÷ distance moved by load.",
  "Efficiency = (work output ÷ work input) × 100%. No machine is 100% efficient because of friction and the "
  "weight of the moving parts.",
  "Work = force × distance, measured in joules (J).",
])
O("A wheelbarrow is an example of a lever of the",
  ["second class", "first class", "third class", "fourth class"],
  ["In a wheelbarrow the wheel is the fulcrum, the hands apply the effort at the handles and the load sits between them.",
   "Load in the middle means a lever of the <b>second class</b>."],
  ok=True)
O("A machine lifts a load of 600 N when an effort of 200 N is applied. Find the mechanical advantage.",
  ["3", "0.33", "800", "120 000"],
  ["Mechanical advantage = load ÷ effort = 600 ÷ 200.", "= <b>3</b> (it has no unit)."],
  v=600 / 200, nv=[3, 0.33, 800, 120000])
O("A force of 50 N moves a box through 4 m in the direction of the force. Calculate the work done.",
  ["200 J", "12.5 J", "54 J", "2 000 J"],
  ["Work = force × distance = 50 × 4.", "= <b>200 J</b>."],
  v=50 * 4, nv=[200, 12.5, 54, 2000])
O("No machine is 100% efficient because",
  ["some energy is used to overcome friction", "machines are made of metal",
   "the load is always too heavy", "effort is always greater than the load"],
  ["Part of the work put in never reaches the load.",
   "<b>Some energy is used to overcome friction</b> (and to move the parts of the machine itself), so output is always less than input."],
  ok=True)
O("Which of these is an example of an inclined plane?",
  ["A ramp used to push goods into a lorry", "A see-saw",
   "A pair of scissors", "A pulley on a flagpole"],
  ["An inclined plane is a sloping surface that lets you raise a load with a smaller force over a longer distance.",
   "<b>A ramp used to push goods into a lorry</b> is an inclined plane."],
  ok=True)
T("A labourer uses a pulley system to raise a load of 400 N by applying an effort of 250 N. The effort moves 4 m while "
  "the load rises 2 m. Calculate (a) the mechanical advantage, (b) the velocity ratio, (c) the efficiency of the system. "
  "(d) Suggest one way of improving the efficiency.",
  ["(a) M.A. = load ÷ effort = 400 ÷ 250 = <b>1.6</b>.",
   "(b) V.R. = distance moved by effort ÷ distance moved by load = 4 ÷ 2 = <b>2</b>.",
   "(c) Efficiency = (M.A. ÷ V.R.) × 100 = (1.6 ÷ 2) × 100 = <b>80%</b>.",
   "(Check by work: input = 250 × 4 = 1 000 J; output = 400 × 2 = 800 J; 800/1 000 × 100 = 80%. ✓)",
   "(d) <b>Oil or grease the pulley wheels to reduce friction</b> (or use lighter pulley blocks and rope)."],
  marks=10, fig=draw.leverfig(2, label="A wheelbarrow: lever of the second class"),
  ok=(close(400 / 250 / 2 * 100, 80) and close(400 * 2 / (250 * 4) * 100, 80)))
extras("machines",
  plain="A machine never creates energy — it only makes a job more convenient, usually by letting you use a smaller force "
        "over a longer distance. That is why the work you put in is always a little more than the work you get out: friction takes its share.",
  examples=[
    E("Why is it easier to push a drum up a ramp than to lift it straight into a lorry?",
      "Step 1. Lifting it straight up means applying a force equal to its whole weight.",
      "Step 2. The ramp is an inclined plane: it spreads the same work over a longer distance.",
      "Step 3. So <b>a smaller force is needed, though it must act for longer</b> — the work done is about the same."),
    E("A machine has a velocity ratio of 5 and an efficiency of 60%. Find its mechanical advantage.",
      "Step 1. Efficiency = (M.A. ÷ V.R.) × 100.",
      "Step 2. So 60 = (M.A. ÷ 5) × 100, which gives M.A. ÷ 5 = 0.6.",
      "Step 3. M.A. = 0.6 × 5 = <b>3</b>.")])

# ------------------------------------------------------------------ farming
topic("farming", "Crop & animal production", C, [
  "Crop production stages: land clearing and preparation, nursery, planting (correct spacing), weeding, "
  "fertiliser application, pest and disease control, harvesting, and storage.",
  "<b>Crop rotation</b> means growing different crops on the same land in turn. It keeps the soil fertile, "
  "reduces pests and diseases, and controls weeds.",
  "Legumes (cowpea, groundnut, soya bean) have nodules containing bacteria that fix nitrogen, enriching the soil.",
  "Farm animals: ruminants (cattle, sheep, goats) chew the cud; non-ruminants (pigs, poultry) do not. "
  "Good animal husbandry means proper housing, clean water, balanced feed, and vaccination against disease.",
  "Farm tools: hoe, cutlass, mattock, rake, watering can, shovel, wheelbarrow, pruning shears. "
  "Tools are cleaned, oiled and stored dry so that they do not rust.",
])
O("Growing different crops on the same piece of land in successive seasons is called",
  ["crop rotation", "mixed cropping", "mono-cropping", "shifting cultivation"],
  ["Mixed cropping means growing them together at the same time.",
   "Growing them one after another in turn is <b>crop rotation</b>."],
  ok=True)
O("Legumes such as cowpea improve soil fertility because they",
  ["fix nitrogen in their root nodules", "have deep tap roots",
   "produce much shade", "need very little water"],
  ["Bacteria living in the nodules convert nitrogen from the air into compounds the plant and soil can use.",
   "So legumes <b>fix nitrogen in their root nodules</b>."],
  ok=True)
O("Which of the following animals is a ruminant?",
  ["Cattle", "Pig", "Fowl", "Rabbit"],
  ["Ruminants have a stomach with several compartments and chew the cud.",
   "Of those listed, <b>cattle</b> are ruminants."],
  ok=True)
O("Why should farm tools be cleaned and oiled after use?",
  ["To prevent rusting and make them last longer", "To make them heavier",
   "To make them look new for sale", "To sharpen the blades"],
  ["Moisture and soil left on metal cause rust, which weakens and spoils the tool.",
   "So tools are cleaned and oiled <b>to prevent rusting and make them last longer</b>."],
  ok=True)
O("Correct spacing of crops on the farm is important because it",
  ["reduces competition for water, nutrients and light", "makes the farm look beautiful",
   "increases the number of weeds", "makes harvesting slower"],
  ["Plants crowded together fight one another for the same resources and all grow poorly.",
   "Correct spacing <b>reduces competition for water, nutrients and light</b>, so yields are higher."],
  ok=True)
T("(a) Outline five stages in the production of a maize crop. (b) State three advantages of crop rotation. "
  "(c) Give two reasons why a poultry house should be kept clean and dry.",
  ["(a) <b>Land preparation</b> (clearing, ploughing or hoeing); <b>planting</b> at the correct spacing and depth; "
   "<b>weeding</b> and <b>fertiliser application</b>; <b>pest and disease control</b>; "
   "<b>harvesting, drying and proper storage</b>.",
   "(b) It <b>maintains soil fertility</b> (especially when a legume is included in the rotation); it "
   "<b>reduces pests and diseases</b>, because each pest loses its host crop for a season; and it "
   "<b>controls weeds</b> and makes better use of nutrients at different soil depths.",
   "(c) A dirty, damp house allows <b>disease organisms and parasites to multiply</b>, so birds fall sick and may die; "
   "and <b>damp litter releases ammonia</b>, which irritates the birds' lungs and reduces growth and egg production."],
  marks=12)
extras("farming",
  plain="Farming is applied science: every practice has a reason behind it. Spacing reduces competition, rotation breaks "
        "pest cycles, legumes add nitrogen, and clean tools last. In the exam, always give the reason as well as the practice.",
  examples=[
    E("A farmer plants maize on the same plot for five years running and his yields fall each year. Explain and advise him.",
      "Step 1. Maize takes the same nutrients from the same depth every season, so those nutrients run short.",
      "Step 2. Pests and diseases of maize also build up in the soil year after year.",
      "Step 3. Advise him to <b>rotate his crops — for example maize, then cowpea, then cassava</b> — and to add manure or compost."),
    E("Why are seedlings raised in a nursery before being transplanted?",
      "Step 1. Young seedlings are delicate and need close attention — shade, regular water, protection from pests.",
      "Step 2. A small nursery bed makes that care possible.",
      "Step 3. Only the <b>strongest, healthiest seedlings are then transplanted</b>, which gives a more even and productive field.")])
