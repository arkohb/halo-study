"""Illustrations (animated where it helps) and a plain "use it in real life" note for every topic.

Imported last by the build for whichever subject is being dumped; entries for topics that are
not loaded are skipped, so one file can carry both levels.
"""
import sys
import core, draw
from core import extras, plot

PACK = {}
FIGS = {}


def apply_pack(subject):
    n_fig = n_app = 0
    have = {t["id"]: t for t in core.TOPICS}
    for tid, v in PACK.get(subject, {}).items():
        t = have.get(tid)
        if not t:
            continue
        ap = v[0] if isinstance(v, tuple) else v
        fig = v[1] if isinstance(v, tuple) and len(v) > 1 else None
        cap = v[2] if isinstance(v, tuple) and len(v) > 2 else None
        if ap:
            t["apply"] = core.fmt(ap)
            n_app += 1
        if fig and not t.get("fig"):
            t["fig"] = fig
            n_fig += 1
            if cap:
                t["figcap"] = cap
    for tid, v in FIGS.get(subject, {}).items():
        t = have.get(tid)
        if not t or t.get("fig"):
            continue
        t["fig"] = v[0]
        if len(v) > 1 and v[1]:
            t["figcap"] = v[1]
        n_fig += 1
    return n_app, n_fig


# shorthands
F = draw.animflow
C = draw.animcycle
T = draw.tree
PT = draw.particles

# ===================================================================== BECE MATHS
PACK["bmaths"] = {
 "whole": ("Prices, populations and bank balances are all read by their columns — "
           "GH¢4 783 is read, written and rounded by place value every time you shop or fill a form.",),
 "bodmas": ("Any calculator, spreadsheet or phone bill works in this order. "
            "When you work out 2 bags at GH¢35 plus 3 tins at GH¢8, you are doing BODMAS without noticing.",
            F(["Brackets", "Of (powers)", "Divide", "Multiply", "Add", "Subtract"],
              label="BODMAS order", note="always in this order, left to right"),
            "Work from left to right within each pair"),
 "facmul": ("Sharing items into equal bundles with nothing left over uses the H.C.F.; "
            "working out when two buses, two bells or two market days next fall together uses the L.C.M.",),
 "frac": ("Half a bag of cement, three quarters of a tank of fuel, a third of your pocket money saved — "
          "every recipe and every sharing problem is fractions.",
          F(["Same denominator?", "If not, use the L.C.M.", "Add or subtract the numerators", "Simplify"],
            label="Adding fractions", note="the pieces must be the same size first"),
          "Multiplying and dividing need no common denominator"),
 "decper": ("Discounts, VAT, mobile-money charges, mark-ups and school percentages are all this one skill: "
            "change the percentage to a fraction or decimal, then multiply.",
            F(["Fraction 3/8", "× 100", "37.5%", "÷ 100 again", "decimal 0.375"],
              label="Fraction, percentage and decimal", note="three ways of writing the same amount"),
            "Learn to move between the three forms quickly"),
 "integers": ("Temperatures below zero, profit and loss, overdrafts, and heights above and below sea level "
              "are all directed numbers.",),
 "ratio": ("Mixing concrete 1 : 2 : 4, sharing profit between partners, scaling a recipe up for a crowd, "
           "and reading a map scale all use ratio.",
           plot(lambda x: 8 * x, 0, 10, 0, 80, step=2,
                pts=[(1, 8, "1 book"), (5, 40, ""), (8, 64, "8 books")],
                label="Cost rises in direct proportion"),
           "Direct proportion is always a straight line through the origin"),
 "indices": ("Computer storage, the mass of a dust grain and the distance to the sun are all written in "
             "standard form, because the plain numbers would be unreadable.",),
 "sets": ("Any survey question — how many pupils take both Maths and Science, how many take neither — "
          "is a Venn diagram waiting to be drawn.",),
 "patterns": ("Rows of blocks, instalment payments, interest added each month and tiles along a wall all follow "
              "patterns; the nth-term rule lets you jump straight to the 50th without counting.",
              plot(None, 0, 7, 0, 24, step=1,
                   pts=[(1, 5, ""), (2, 8, ""), (3, 11, ""), (4, 14, ""), (5, 17, ""), (6, 20, "")],
                   lines=[(0, 2, 7, 23)], label="Sequence 5, 8, 11, 14 …"),
              "A constant difference makes the points lie on a straight line"),
 "money": ("Buying to sell, paying by instalments, saving at a bank and checking an electricity bill — "
           "this is the maths you will use every week for the rest of your life.",
           F(["Cost price", "+ profit or − loss", "Selling price", "% is always on the COST"],
             label="Profit and loss", note="percentage profit = profit ÷ cost price × 100"),
           "Hire purchase always costs more than the cash price"),
 "approx": ("Estimating the cost of a basket of shopping before you reach the counter, "
            "and checking that a calculator answer is sensible, both depend on rounding well.",),
 "algexp": ("A letter simply stands for a number you do not know yet — the fare per person, "
            "the number of blocks per row — and algebra is how you work with it.",
            F(["Replace the letters", "Brackets round negatives", "Powers first", "Then × ÷ + −"],
              label="Substituting into an expression"),
            "Always put a negative value in brackets"),
 "factorise": ("Factorising is how formulas are tidied before they are used, and it is the step that turns a "
               "hard quadratic into two easy brackets at senior high school.",),
 "equations": ("'I think of a number' problems are really everyday ones: how many bags can I buy with GH¢500, "
               "what width gives a 26 m fence, how many days until the money runs out.",
               F(["Clear brackets", "Clear fractions", "Letters one side", "Numbers the other", "Divide", "Check"],
                 label="Solving a linear equation"),
               "The check at the end costs ten seconds and saves the mark"),
 "inequal": ("'At least', 'at most', 'not more than' — budgets, load limits, pass marks and age limits are "
             "all inequalities.",
             draw.numline(-4, 6, seg=(None, 2, False, False), label="x < 2"),
             "Open circle: 2 itself is not included"),
 "relmap": ("A function is a machine: put in the number of units of power used, get out the amount to pay. "
            "Tariffs, fares and conversion tables are all functions.",
            F(["Input x", "The rule: × 2 then + 3", "Output f(x)"], label="A function machine"),
            "f(4) just means 'what comes out when 4 goes in?'"),
 "graphs": ("Phone tariffs, taxi fares and savings plans are all drawn as straight-line graphs; "
            "the gradient is the rate and the intercept is the fixed charge.",
            plot(lambda x: 2 * x - 1, -3, 4, -6, 6,
                 pts=[(-2, -5, ""), (0, -1, "(0, −1)"), (2, 3, ""), (3, 5, "")],
                 label="y = 2x − 1"),
            "Gradient 2 (up 2 for each 1 across), cutting the y-axis at −1"),
 "angles": ("Carpenters, masons, tilers and tailors all set out their work with angles; "
            "a roof, a staircase and a window frame depend on them being right.",),
 "shapes": ("Floor tiles, zinc roofing sheets, paving stones and the honeycomb pattern on a football "
            "all come from the angle rules of polygons.",),
 "pythag": ("Builders square a foundation with a 3-4-5 triangle, a ladder's safe reach is a right-angled "
            "triangle, and the shortest way across a field is the hypotenuse.",),
 "perim": ("Fencing a plot, buying roofing sheets, painting a wall and laying tiles are perimeter and area "
           "problems with prices attached.",),
 "circles": ("Wheels, tanks, culverts, plates and the distance a bicycle travels in one turn are all "
             "circumference and area.",
             draw.circlefig("centre", angles=["r", ""], label="Parts of a circle"),
             "C = 2πr goes round the edge; A = πr² fills the inside"),
 "volume": ("Water tanks, cement bags, tins of paint, lorry loads of sand and the capacity of a poly tank "
            "are all volume.",
            draw.solidfig("cylinder", labels=["r", "h"], label="A cylinder"),
            "V = πr²h; 1 000 cm³ = 1 litre"),
 "construct": ("Setting out a building, dividing land fairly and drawing a plan to scale all use the same "
               "ruler-and-compasses constructions.",),
 "transform": ("Patterns on kente and adinkra cloth, tiling a floor, and the way a photocopier enlarges a "
               "drawing are translation, reflection, rotation and enlargement.",),
 "bearing": ("Fishermen, pilots, surveyors and anyone using a compass app give direction as a three-figure "
             "bearing from north.",
             draw.compass([(90, "east 090°", 0.9), (180, "south 180°", 0.75)],
                          label="Bearings are measured clockwise from north"),
             "Always three figures: 045°, not 45°"),
 "measure": ("Journey planning, fuel use, cooking times and the speed limit on a road are distance, "
             "speed and time.",
             plot(lambda x: 60 * x, 0, 4, 0, 240, step=1,
                  pts=[(1, 60, ""), (2, 120, ""), (3, 180, "180 km in 3 h")],
                  label="Distance-time graph at 60 km/h"),
             "On a distance-time graph the gradient IS the speed"),
 "stats": ("School marks, market prices, rainfall figures and election results are all summarised with mean, "
           "median, mode and a chart.",
           draw.barfig([("2", 3), ("3", 5), ("4", 6), ("5", 4), ("6", 2)],
                       label="Marks of 20 pupils", ylab="pupils"),
           "The tallest bar shows the mode at a glance"),
 "prob": ("Weather forecasts, insurance, lottery odds and the chance of rain on your travel day are all "
          "probability between 0 and 1.",),
}

# ===================================================================== BECE SCIENCE
PACK["bscience"] = {
 "sciskills": ("Every trade measures: a tailor in centimetres, a trader in kilograms, a nurse in millilitres. "
               "Reading a scale correctly and changing only one thing at a time is science in daily use.",
               F(["Observe", "Ask a question", "Predict", "Test fairly", "Record", "Conclude"],
                 label="The scientific method", note="change ONE thing, keep the rest the same"),
               "A fair test is what makes the answer believable"),
 "matter": ("Ice melting in a cup, water boiling for banku, petrol evaporating from an open tin — "
            "the particles are the same, only their arrangement and speed change.",
            PT("liquid"), "Heat gives particles energy: solid → liquid → gas"),
 "mixtures": ("Panning for gold, sieving flour, filtering drinking water and winnowing grain are all "
              "separation methods chosen by one physical difference.",
              draw.labware("filter"), "Filtration: the residue stays, the filtrate passes through"),
 "elements": ("The gold in a ring, the oxygen in your blood and the salt in your soup are the same few "
              "elements rearranged — that is all chemistry is.",
              T("MATTER", ["Element: one kind of atom (gold, oxygen)",
                           "Compound: elements chemically joined (water, salt)",
                           "Mixture: not joined, easy to separate (air, soup)"],
                label="Elements, compounds and mixtures"),
              "In a compound the elements lose their own properties"),
 "acids": ("Lime on sour farmland, antacid for heartburn, toothpaste against mouth acid, "
           "and vinegar in the kitchen — neutralisation every day.",
           draw.phscale(3, "lemon juice"), "Below 7 acidic, 7 neutral, above 7 basic"),
 "living": ("Deciding whether something is alive, and knowing that every living thing is built from cells, "
            "is the base of farming, health and hygiene.",
            draw.cellfig("plant"), "A plant cell: wall, chloroplasts and a large vacuole as well"),
 "classify": ("Farmers, fishermen, hunters and health workers all sort living things into groups — "
              "which fish is edible, which insect is a pest, which snake is dangerous.",
              T("ANIMALS", ["Vertebrates: fish, amphibians, reptiles, birds, mammals",
                            "Invertebrates: insects, worms, molluscs, arachnids"],
                label="Classification of animals"),
              "Always give the REASON for the group"),
 "water": ("Why rain falls, why a cold bottle 'sweats', why wells dry up, and why water must be boiled or "
           "chlorinated — all one cycle and one habit of care.",
           C(["Evaporation", "Condensation", "Precipitation", "Run-off"], centre="WATER CYCLE",
             label="The water cycle"),
           "The sun lifts it, the cold air drops it, the land returns it"),
 "air": ("A candle that goes out under a jar, a tyre that hardens when pumped, and the weather report on "
         "the radio all come from the properties of air.",
         draw.piefig([("Nitrogen", 78), ("Oxygen", 21), ("Others", 1)], label="What air is made of"),
         "About 78% nitrogen, 21% oxygen, the rest a trace"),
 "soil": ("Which soil to plant in, why water stands on clay, and why manure is worth more than fertiliser "
          "alone — every farmer's decisions.",
          F(["Rock", "Weathering", "+ humus from dead plants", "SOIL"], label="How soil is formed"),
          "Loam: enough sand to drain, enough clay to hold water"),
 "lifecycles": ("Clearing a tin of standing water stops thousands of mosquitoes before they can bite — "
                "knowing the life cycle tells you exactly where to strike.",
                C(["Egg on water", "Larva", "Pupa", "Adult flies"], centre="MOSQUITO",
                  label="Life cycle of the mosquito"),
                "Three of the four stages need still water"),
 "plants": ("Why crops need sun and water, why weeding helps, and why forests cool the air — "
            "photosynthesis is the reason there is food and oxygen at all.",
            draw.plantfig(), "Light + water + carbon dioxide → food + oxygen"),
 "digest": ("Planning a balanced meal on a small budget, and knowing why a child who eats only gari gets "
            "kwashiorkor, is this topic in practice.",
            F(["Mouth: starch", "Stomach: protein", "Small intestine: absorbed", "Large intestine: water"],
              label="The path of food"),
            "Enzymes cut big molecules into small ones the blood can carry"),
 "circ": ("Why you pant after running, why a smoker coughs, and why anaemia makes you tired — "
          "breathing brings oxygen in, the blood carries it to every cell.",
          F(["Nose", "Trachea", "Bronchi", "Alveoli ↔ blood"], label="Air into the blood"),
          "Breathing is the air; respiration is the energy released inside cells"),
 "repro": ("Understanding the changes of adolescence, keeping clean, and making informed decisions about "
           "your own body and your education.",),
 "health": ("Hand-washing, a treated net, a covered latrine and finishing your medicine prevent more "
            "illness in Ghana than any hospital can cure.",
            F(["Germ leaves a person", "Travels: water, air, food, vector",
               "Enters another person", "Break ANY link"], label="How a disease spreads"),
            "Break one link and the chain stops"),
 "ecosystem": ("Why killing the hawks brings rats, why a polluted river empties the nets, and why bees "
               "matter to a cocoa farm.",
               F(["Grass", "Grasshopper", "Lizard", "Hawk"], label="A food chain",
                 note="the arrow means 'is eaten by'"),
               "Energy is lost at every step, so chains are short"),
 "solar": ("Day and night, the seasons, the phases of the moon and an eclipse — two movements explain "
           "them all: spinning and orbiting.",
           F(["SUN", "EARTH casts a shadow", "MOON darkens"], label="Eclipse of the moon"),
           "Rotation gives day and night; revolution gives the year"),
 "machines": ("A wheelbarrow, a claw hammer, a ramp onto a lorry and a pulley on a building site all let a "
              "small force move a big load.",
              draw.leverfig(2, label="A wheelbarrow is a second-class lever"),
              "Load in the middle, effort at the handles, wheel as fulcrum"),
 "farming": ("Spacing, rotation, legumes and clean tools are the difference between a farm that feeds a "
             "family and one that fails.",
             C(["Maize", "Cowpea (fixes nitrogen)", "Cassava", "Fallow"], centre="CROP ROTATION",
               label="Crop rotation"),
             "Rotation feeds the soil and starves the pests"),
 "energy": ("A torch, a solar lamp, a fan and your own body all change energy from one form to another; "
            "none of them creates it.",
            F(["Sunlight", "Solar panel → electrical", "Lamp → light + heat"],
              label="Energy changes in a solar lamp"),
            "Energy is never used up, only changed"),
 "heat": ("Why a cooking spoon is wooden, why the freezer is at the top, why white clothes are cooler, "
          "and why a flask keeps tea hot.",
          F(["Conduction: through solids", "Convection: moving liquids and gases",
             "Radiation: no material needed"], label="Three ways heat travels"),
          "Heat always moves from hot to cold"),
 "light": ("Mirrors, shadows, a bent spoon in a glass of water, a rainbow and the reason an ambulance's "
           "name is written backwards.",
           draw.reflectfig(40), "The angle of incidence equals the angle of reflection"),
 "sound": ("Why you see lightning before you hear thunder, why a loud speaker harms hearing, and how an "
           "echo tells a fisherman the depth.",
           F(["Something vibrates", "Particles pass it on", "Ear-drum vibrates", "You hear it"],
             label="How sound reaches you"),
           "No particles, no sound — space is silent"),
 "elec": ("House wiring, a torch that will not light, a blown fuse and an electric bell all follow one rule: "
          "the circuit must be complete.",
          draw.circuitfig(label="A simple series circuit"),
          "Break it anywhere in series and everything stops"),
 "force": ("Why a tractor has wide tyres, why a knife is sharpened, why brakes work, and the difference "
           "between your mass and your weight.",
           F(["Force ÷ area = pressure", "Small area → big pressure (a nail)",
              "Big area → small pressure (a tractor tyre)"], label="Pressure"),
           "Same force, different area, very different effect"),
 "envcare": ("Choked gutters that flood a town, galamsey that poisons a river, and tree-planting that brings "
             "a stream back — every one is a choice somebody makes.",
             C(["Reduce", "Reuse", "Recycle"], centre="WASTE", label="The three Rs"),
             "Refusing one plastic bag is where it starts"),
 "tech": ("Mobile money, a solar lamp, a vaccine and a borehole pump are science turned into things that "
          "change daily life — with costs to manage as well.",),
}

# ===================================================================== BECE SOCIAL STUDIES
PACK["bsocial"] = {
 "envtypes": ("Every decision about where to farm, build or dump waste is a decision about the environment "
              "you and your neighbours depend on.",
              T("ENVIRONMENT", ["Physical: land, water, air, plants",
                                "Human-made: roads, houses, dams",
                                "Social: people, customs, institutions"], label="The three components"),
              "Damage one part and the others feel it"),
 "mapping": ("Reading a map, giving directions, and understanding why Ghana is hot and has two rainy "
             "seasons in the south.",
             draw.compass([(0, "Burkina Faso", 0.95), (90, "Togo", 0.8), (180, "Gulf of Guinea", 0.9),
                           (270, "Côte d'Ivoire", 0.8)], label="Ghana and its neighbours"),
             "Title, key, scale and north arrow: every map needs all four"),
 "settle": ("Why towns grow where they do, and why so many young people leave the village — and what "
            "would make them stay.",
            F(["Village: farming, few services", "Town: work, schools, clinics",
               "Migration → crowding, slums", "Answer: services in the villages"],
              label="Rural-urban migration"),
            "People move towards work, schools and services"),
 "popn": ("A census is how government knows where to build the next school, clinic and borehole — "
          "including in your own district.",
          draw.pyramidfig(["0-14 years: very wide", "15-59: working age", "60+: narrow"],
                          label="A young population"),
          "Many children today means many classrooms needed now"),
 "envprob": ("Floods after a rain, a stream that has dried up, a farm that no longer yields — each has a "
             "cause somebody can stop.",
             F(["Trees cut", "Soil left bare", "Rain washes topsoil",
                "Streams silt up", "Crops fail"], label="How deforestation ends in hunger"),
             "A short-term gain for a few, a long-term loss for all"),
 "conserve": ("Using a resource without finishing it: selective logging, closed fishing seasons, "
              "replanting and recycling.",),
 "culture": ("Greeting an elder, a naming ceremony, a festival that funds a school — and the courage to "
             "drop practices that deny people their rights.",),
 "family": ("The home is where character is formed; knowing the duties on both sides keeps it working.",
            T("FAMILY", ["Nuclear: parents and children",
                         "Extended: + grandparents, uncles, aunts, cousins"], label="Types of family"),
            "The extended family is Ghana's oldest social security"),
 "constitution": ("Your rights at a police station, your duty to pay tax, and the rule that no law may "
                  "override the Constitution.",),
 "govt": ("Why a minister cannot jail you, why Parliament vets nominees, and why a court can strike down "
          "a law — three arms, three jobs.",
          T("GOVERNMENT", ["Executive: carries out the law",
                           "Legislature: makes the law",
                           "Judiciary: interprets the law"], label="The three arms"),
          "Separation of powers is what prevents dictatorship"),
 "democracy": ("Registering at 18, voting in secret, and accepting the result — or petitioning the court "
               "rather than the street.",
               F(["Register at 18", "Campaign and debate", "Vote in secret",
                  "Count in public", "Winner takes office"], label="An election, step by step"),
               "A presidential winner needs more than 50% of valid votes"),
 "localgov": ("The gutter in your town is cleared because somebody in your town decided it — that is "
              "decentralisation in one sentence.",),
 "rights": ("Your right to education and to be heard, and the duty that comes with each — plus who to "
            "report to when a right is broken.",),
 "leadership": ("Being a prefect, a club secretary or a class captain is practice for every office that "
                "follows. Service, not privilege.",),
 "conflict": ("Land and chieftaincy disputes close schools and markets. Dialogue, elders, the House of "
              "Chiefs and the courts are the way through.",),
 "corruption": ("Every cedi diverted is a desk not bought. It takes two — which is why refusing to pay a "
                "bribe is part of the cure.",
                F(["Bribe or diversion", "Project not built", "Services fail",
                   "Trust and investment fall"], label="What corruption actually costs"),
                "Report to CHRAJ, the Special Prosecutor or the Auditor-General"),
 "nationalism": ("Looking after public property, buying made-in-Ghana goods and keeping the peace are "
                 "patriotism you can practise today.",),
 "education": ("Education is the one investment that pays the pupil and the country at the same time — "
               "including technical and vocational training.",),
 "adolescent": ("Peer pressure, goals and self-control: the decisions of these few years shape the "
                "opportunities of the next forty.",),
 "economy": ("Why a bag of cocoa beans earns little and the same cocoa as chocolate earns much more — "
             "value addition is the whole argument.",
             F(["PRIMARY: farming, mining", "SECONDARY: processing, factories",
                "TERTIARY: trade, transport, services"], label="The three sectors"),
             "Moving up the chain is how a country gets richer"),
 "money": ("Saving through a bank, a credit union or susu; why the Bank of Ghana alone prints the cedi; "
           "and why money kept at home earns nothing.",),
 "entrepreneur": ("The tailor, the welder and the agro-processor employ themselves and others. Records, "
                  "discipline and customer care decide who survives.",),
 "tourism": ("Castles, waterfalls and festivals turn into income for drivers, guides, cooks and craftsmen "
             "— if the site is protected and the community shares.",),
 "intl": ("ECOWAS lets a Ghanaian trader sell in Lomé and Abidjan; the UN, AU and Commonwealth bring "
          "aid, scholarships and a voice.",),
 "scitech": ("Mobile money, telemedicine, irrigation and e-registration — technology is only useful when "
             "it is maintained and understood.",),
}

# ===================================================================== BECE R.M.E.
PACK["brme"] = {
 "creation": ("All three religions teach that creation belongs to God and we only look after it — "
              "which is why wasting or spoiling it is treated as a moral wrong.",),
 "attributes": ("If God is all-seeing, cheating in secret makes no sense; if God is merciful, there is a way "
                "back after a wrong. Attributes are ideas with consequences.",),
 "stewardship": ("Sacred groves, taboo days and closed seasons protected forests and fish long before the "
                 "word 'conservation' existed.",
                 C(["Sacred grove: no felling", "Taboo day: land rests",
                    "Closed season: fish breed", "Totem: species protected"],
                   centre="STEWARDSHIP", label="Traditional care of creation"),
                 "The language is religious; the effect is conservation"),
 "purpose": ("Purpose turns talent into duty: what you are good at is meant to be developed and used for "
             "others, not buried.",),
 "worship": ("Worship builds reverence, self-discipline and unity — the same three things every "
             "community needs to function.",
             T("WORSHIP", ["Christianity: church, prayer, Bible, communion",
                           "Islam: salat five times, Friday Jumu'ah, Qur'an",
                           "A.T.R.: libation, offerings, festivals, taboos"],
               label="Worship in the three religions"),
             "Different forms, the same moral training"),
 "prayer": ("Pray for the harvest, then weed the farm. Faith and effort belong together — that balance "
            "is itself an exam answer.",),
 "festivals": ("Festivals bring citizens home, settle quarrels, raise funds for schools and clinics, and "
               "bring tourists — culture becoming income.",),
 "obligations": ("Fasting trains self-control, zakat trains generosity. Each takes a virtue and gives it a "
                 "timetable, which is how character is actually built.",),
 "youth": ("A good youth group gives a young person company, responsibility and skills — the three "
           "things that keep idleness and bad company away.",),
 "rites": ("Naming, puberty, marriage and funeral rites teach identity and responsibility — and a "
           "dignified funeral within the family's means is itself a moral choice.",),
 "jesus": ("The parable of the Good Samaritan answers a question you will face this week: who counts as "
           "your neighbour when somebody different is in trouble?",),
 "muhammad": ("He was trusted with other people's goods long before he was believed as a prophet — "
              "honesty in small things is where authority comes from.",),
 "tradleaders": ("The Golden Stool shows religion used to build a nation: one shared symbol achieved what "
                 "politics alone could not.",),
 "leaderlessons": ("Every leader studied here is remembered for service and patience, not wealth — the "
                   "same test applies to a prefect, a chief or a president.",),
 "obedience": ("Obedience is to lawful authority. If a senior tells you to steal or lie, the right answer is "
               "to refuse and report it.",),
 "honesty": ("The pupil who returns the extra change is practising for the day he handles a budget. "
             "Examination malpractice is the same failure, earlier.",),
 "chastity": ("Chastity protects health, education and self-respect at once — and the law sets 18 as the "
              "minimum age of marriage for the same reasons.",),
 "familyduties": ("Street children, drug abuse and early pregnancy are all traced in part to the home. "
                  "Duties run both ways: parents provide, children obey and help.",),
 "work": ("The mason, the seamstress and the farmer carry the economy. The dignity of labour means no "
          "honest work is beneath you.",),
 "substance": ("Peer pressure, curiosity, idleness → use → addiction → health, school and family "
               "collapse. The chain is easiest to break at the first link.",
               F(["Peer pressure", "First use", "Habit", "Addiction",
                  "Health, school and family lost"], label="How substance abuse takes hold"),
               "Refusing once is far easier than stopping later"),
 "manners": ("Ability gets you the interview; courtesy often decides what happens in the room. "
             "Greeting, listening and dressing decently cost nothing.",),
 "rules": ("Every rule protects something: 'no running' protects teeth, 'be in class by 7:30' protects "
           "everybody's lesson. Unjust rules are changed through the proper channel.",),
 "service": ("Commitment is what turns a promise into a result — the club you stay in, the duty you keep, "
             "the revision plan you finish.",),
}

# ===================================================================== BECE COMPUTING
PACK["bcomputing"] = {
 "compbasics": ("Marks typed in, totals printed out, the file kept for next term — every computer you "
                "meet is doing the same four things.",
                F(["INPUT", "PROCESSING (CPU)", "OUTPUT", "STORAGE"], label="How a computer works",
                  note="data in, information out"),
                "Data is raw; information is data that has been worked on"),
 "hardware": ("Choosing a laptop, replacing a keyboard or explaining why the printer is 'output' — "
              "sort every device by which way the data flows.",
              T("COMPUTER", ["Input: keyboard, mouse, scanner",
                             "System unit: CPU, memory",
                             "Output: monitor, printer, speaker",
                             "Storage: hard disk, flash drive"], label="Parts of a computer system"),
              "A touch screen does both input and output"),
 "storage": ("Why unsaved work disappears in a power cut, and why one copy of a file is one accident away "
             "from gone.",
             F(["RAM: your desk, cleared at power-off", "Hard disk: the cupboard",
                "Flash / cloud: the backup"], label="Where your work lives"),
             "Ctrl + S often, and keep a second copy"),
 "software": ("Windows runs the computer, Word does your work, the antivirus guards it — and pirated "
              "copies bring viruses and no updates.",),
 "os": ("Finding a lost file, making a folder for your BECE notes, and using Ctrl + S, Ctrl + C and Ctrl + V "
        "without thinking.",),
 "safety": ("Screen at eye level, a break every twenty minutes, no drinks near the keyboard, and a surge "
            "protector — cheap habits that save eyes and equipment.",),
 "typing": ("Touch typing is the one computing skill you will use every working day; a few careful minutes "
            "daily beats an hour of hunting for keys.",),
 "word": ("A letter, a report, a CV or an application — typed once, corrected before printing, saved and "
          "reused.",),
 "present": ("Few words, large type, one idea per slide — and never read the slide aloud. That is most of "
             "the mark and most of the audience's patience.",),
 "sheets": ("A class mark sheet, a shop's daily takings or a household budget: change one figure and every "
            "total, average and chart updates itself.",
            F(["Type data in cells", "=SUM(B2:B6)", "Totals update by themselves", "Insert a chart"],
              label="A spreadsheet in four steps"),
            "Formulas refer to cells, not to numbers"),
 "database": ("A school's records, the voters' register and the national ID are databases — that is why a "
              "record can be found in seconds.",
              T("DATABASE", ["Table: all pupils", "Record: one pupil",
                             "Field: surname, class, D.O.B.", "Key: index number"],
                label="Field, record, table"),
              "The key must be unique — names are not"),
 "network": ("One printer shared by twenty computers, and the internet itself: a network exists to share.",
             F(["PAN: your own devices", "LAN: one building", "MAN: one city",
                "WAN: the internet"], label="Networks by size"),
             "Modem converts, router directs, switch joins"),
 "internet": ("Past questions, timetables, online lessons and mobile money — and the judgement to ask who "
              "published a page and when.",),
 "email": ("A clear subject line, complete sentences, no capitals and no attachment from a stranger: "
           "your first piece of professional communication.",),
 "netsafety": ("A long password that is not your name or birthday, and never clicking a link you did not "
               "expect — two habits that stop most trouble.",
               F(["Strong, different passwords", "Updated antivirus",
                  "Think before posting", "Report and keep the evidence"],
                 label="Staying safe online"),
               "A deleted post can already have been copied"),
 "binary": ("Every file, photo and message on your phone is stored as 0s and 1s — place value with 2 "
            "instead of 10.",
            F(["128", "64", "32", "16", "8", "4", "2", "1"], label="Binary place values",
              note="1 1 0 1 1 = 16+8+2+1 = 27"),
            "Each place is double the one to its right"),
 "algorithm": ("Writing clear steps anybody could follow is the skill behind every program — and behind "
               "a good set of instructions at work.",
               F(["Start", "Input A, B, C", "SUM = A+B+C", "AVERAGE = SUM/3", "Output", "Stop"],
                 label="An algorithm as a flowchart"),
               "Oval start/stop, parallelogram input/output, diamond decision"),
 "emerging": ("Mobile money, drones carrying blood, AI in a clinic — each one brings a benefit and a cost "
              "(e-waste, jobs, privacy) that has to be managed.",),
}

# ===================================================================== extra illustrations
FIGS["bsocial"] = {
 "conserve": (T("RESOURCES", ["Renewable: forests, water, fish, soil",
                              "Non-renewable: gold, bauxite, crude oil"],
                label="Two kinds of resource"), "Renewables last only if they are managed"),
 "culture": (T("CULTURE", ["Language, dress, food, music", "Festivals and rites",
                           "Beliefs, values and government"], label="What culture includes"),
             "Culture is learned, shared, and it changes"),
 "constitution": (F(["1992 Constitution", "7 January 1993", "Fourth Republic", "Supreme law"],
                    label="Ghana's constitutional order"),
                  "Any law that conflicts with it is void"),
 "localgov": (T("DECENTRALISATION", ["16 Regional Co-ordinating Councils",
                                     "Metropolitan / Municipal / District Assemblies",
                                     "Urban, town and area councils", "Unit committees"],
                label="Local government in Ghana"),
              "The Assembly is the highest <b>political</b> authority in the district"),
 "rights": (F(["A right", "carries a duty", "Free speech → no insult or lies",
               "Property → not on a waterway"], label="Rights and responsibilities"),
            "Your freedom stops where another person's begins"),
 "leadership": (T("A GOOD LEADER", ["Honest and selfless", "Fair and tolerant",
                                    "Hard-working and disciplined", "Accountable"],
                  label="Qualities of leadership"), "Leadership is service, not privilege"),
 "conflict": (F(["Dialogue", "Elders mediate", "House of Chiefs / Peace Council", "The courts"],
                label="Settling a dispute peacefully"), "Never machetes — every step is cheaper"),
 "nationalism": (T("NATIONAL SYMBOLS", ["Flag: red, gold, green and the black star",
                                        "Coat of arms and the motto",
                                        "Anthem and pledge"], label="Ghana's symbols"),
                 "6 March 1957 independence; 1 July 1960 republic"),
 "education": (F(["Kindergarten 2", "Primary 6", "Junior high 3", "Senior high / TVET 3", "Tertiary"],
                 label="The education ladder"), "Basic education is the first eleven years"),
 "adolescent": (F(["Physical changes", "New feelings", "Peer pressure",
                   "Goals and self-control"], label="Adolescence"),
                "Set the goal first; it makes saying no easier"),
 "money": (F(["Barter: find a double want", "Money: a common measure",
              "Save: bank, credit union, susu", "Interest and credit"], label="Why money was invented"),
           "Money's four jobs: exchange, measure, store, deferred payment"),
 "entrepreneur": (C(["See an opportunity", "Gather land, labour, capital", "Produce and sell",
                     "Keep records", "Reinvest"], centre="BUSINESS", label="How a business runs"),
                  "Records are what separate growth from guesswork"),
 "tourism": (T("ATTRACTIONS", ["Historical: castles, palaces, mosques",
                               "Natural: Kakum, Mole, Wli, Lake Volta",
                               "Cultural: festivals, kente, food"], label="Tourism in Ghana"),
             "One visitor's money spreads through many households"),
 "intl": (T("GHANA BELONGS TO", ["UN (1945) — peace and development",
                                 "AU (2002, from the OAU of 1963)",
                                 "ECOWAS (1975) — trade and free movement",
                                 "The Commonwealth"], label="International bodies"),
          "ECOWAS citizens may enter member states without a visa"),
 "scitech": (F(["Science asks why", "Technology builds with it",
                "Mobile money, irrigation, vaccines", "Maintain it or lose it"],
               label="From science to development"), "Training matters more than equipment"),
}

FIGS["brme"] = {
 "creation": (T("GOD THE CREATOR", ["Christianity: six days, rest on the seventh",
                                    "Islam: six periods, Adam from clay",
                                    "A.T.R.: the Supreme Being made the world"],
                label="Creation in the three religions"), "Different stories, one teaching"),
 "attributes": (C(["Omnipotent", "Omniscient", "Omnipresent", "Merciful", "Just"], centre="GOD",
                  label="Attributes of God"), "Each attribute asks something of our conduct"),
 "purpose": (F(["Worship and serve God", "Live together in community",
                "Work and be productive", "Care for creation"], label="Why we were created"),
             "Purpose turns a talent into a duty"),
 "prayer": (F(["Adoration", "Thanksgiving", "Confession", "Petition"],
              label="The four parts of prayer"), "Pray for the harvest, then weed the farm"),
 "festivals": (T("FESTIVALS", ["Christian: Christmas, Easter",
                               "Islamic: Eid-ul-Fitr, Eid-ul-Adha",
                               "Traditional: Homowo, Odwira, Aboakyer, Damba"],
                 label="Festivals of the three religions"), "Thanksgiving, history, unity and development"),
 "obligations": (F(["Shahadah", "Salat", "Zakat", "Sawm", "Hajj"], label="The five pillars of Islam"),
                 "Each one gives a virtue a timetable"),
 "youth": (T("YOUTH GROUPS", ["Christian: Scripture Union, Brigade",
                              "Islamic: Muslim Students' Association",
                              "Traditional: Asafo companies"], label="Religious youth organisations"),
           "Good company, service and leadership practice"),
 "rites": (F(["Birth and naming", "Puberty", "Marriage", "Death and funeral"],
             label="Rites of passage"), "Each stage brings new responsibilities"),
 "jesus": (F(["Born in Bethlehem", "Baptised by John", "Taught and healed",
              "Crucified and risen"], label="The life of Jesus Christ"),
           "Humility, love, forgiveness, service"),
 "muhammad": (F(["Born in Mecca, c. 570", "Al-Amin, the trustworthy",
                 "First revelation at Hira", "Hijra to Medina, 622"],
                label="The life of Prophet Muhammad"), "Honesty first, prophethood after"),
 "tradleaders": (T("TRADITIONAL LEADERS", ["Okomfo (priest): prayer, sacrifice, healing",
                                           "Chief: custodian of land and stools",
                                           "Queen mother and okyeame",
                                           "Head of family: libation"], label="Who leads worship"),
                 "Okomfo Anokye and the Golden Stool united Asante"),
 "leaderlessons": (C(["Obedience to God", "Honesty", "Humility", "Patience", "Service"],
                     centre="CHARACTER", label="Virtues of the religious leaders"),
                   "The same test applies to a prefect today"),
 "obedience": (F(["God", "Parents", "Teachers and prefects", "The laws of the land"],
                 label="Lawful authority"), "But never obedience to an order to do wrong"),
 "honesty": (F(["Truth in words", "Honesty with money", "No cheating in exams", "Trust earned"],
               label="Integrity"), "Integrity is who you are when nobody is watching"),
 "chastity": (F(["Chastity", "No teenage pregnancy or STI", "Education continues",
                 "Self-respect kept"], label="What chastity protects"),
              "The law sets 18 as the minimum age of marriage"),
 "familyduties": (T("THE FAMILY", ["Parents: provide, protect, teach",
                                   "Children: obey, help, study",
                                   "Extended: support in need"], label="Duties on both sides"),
                  "A broken home costs the children most"),
 "work": (F(["Punctual", "Diligent", "Honest with time and materials", "Proud of the job"],
            label="Good attitudes to work"), "The dignity of labour: no honest work is beneath you"),
 "manners": (F(["Greet", "Say please and thank you", "Listen without interrupting",
                "Dress decently"], label="Everyday courtesy"), "Free to give, and always noticed"),
 "rules": (T("WHERE RULES COME FROM", ["The family", "The school", "Religious bodies",
                                       "The community and the state"], label="Sources of rules"),
           "Every rule protects something — find out what"),
 "service": (F(["Commit", "Persevere", "Finish", "Serve others"], label="Commitment"),
             "Achievement comes from finishing, not starting"),
}

FIGS["bcomputing"] = {
 "software": (T("SOFTWARE", ["System: operating system, utilities",
                             "Application: Word, Excel, browser"], label="Two kinds of software"),
              "Does it serve the computer or the user?"),
 "os": (T("OPERATING SYSTEM", ["Starts the computer", "Manages memory and files",
                               "Controls devices", "Provides the interface and security"],
          label="What the OS does"), "Ctrl+S save, Ctrl+C copy, Ctrl+V paste, Ctrl+Z undo"),
 "safety": (F(["Screen at eye level", "Break every 20 minutes",
               "No food or drink", "Shut down properly"], label="Health and safety at the computer"),
            "A spilled drink usually ends a keyboard"),
 "typing": (F(["Home keys A S D F — J K L ;", "Eyes on the screen",
               "Thumbs on the space bar", "Accuracy before speed"], label="Touch typing"),
            "A few careful minutes a day is enough"),
 "word": (T("WORD PROCESSING", ["Editing: cut, copy, paste, find and replace",
                                "Formatting: font, bold, alignment, spacing",
                                "Insert: tables, pictures, page numbers"], label="What a word processor does"),
          "Editing changes the words; formatting changes the look"),
 "present": (F(["One idea per slide", "Few words, large type",
                "A picture that explains", "Never read it aloud"], label="Good slides"),
             "The slide supports you; it is not your script"),
 "internet": (F(["Internet: the network", "Web: the pages on it",
                 "Browser shows them", "Search engine finds them"], label="Internet and Web"),
              "Check who published a page, and when"),
 "email": (T("AN EMAIL", ["To, Cc, Bcc", "A clear subject line",
                          "Body in full sentences", "Attachment if needed"], label="Parts of an email"),
           "Never open an attachment from a stranger"),
 "emerging": (T("EMERGING TECHNOLOGY", ["Artificial intelligence", "Internet of Things",
                                        "Drones and 3D printing", "Cloud computing"],
                label="What is coming next"), "Every one brings a benefit and a cost"),
}

# ===================================================================== BECE ENGLISH
PACK["benglish"] = {
 "nouns": ("Filling a form, writing an address, labelling a list of goods — getting plurals and "
           "apostrophes right is what makes writing look educated.",),
 "pronouns": ("'Between you and me', 'my brother and I' — these two phrases appear in letters, "
              "interviews and speeches more than any rule in the book.",
              T("PRONOUNS", ["Subject: I, we, he, she, they",
                             "Object: me, us, him, her, them",
                             "After a preposition → object form"], label="Which form to use"),
              "Drop the other person and your ear will tell you"),
 "verbs": ("Telling what happened yesterday, what you have done since, and what you will do — "
           "tense is how a story stays clear.",
           F(["Stated past time → simple past", "No time stated → present perfect",
              "Earlier of two past actions → past perfect"], label="Choosing a past tense"),
           "'Yesterday' and 'have' never go together"),
 "adjectives": ("Describing goods for sale, a person for an ID form, or a place in a composition.",
                F(["Two things → comparative (-er / more)",
                   "Three or more → superlative (-est / most)",
                   "Never both at once"], label="Comparing"),
                "'More taller' is the commonest error of all"),
 "adverbs": ("Saying HOW something was done — carefully, quickly, well — is what turns a flat "
             "report into a clear one.",
             T("WHICH WORD?", ["Points at a noun → adjective (a careful driver)",
                               "Points at a verb → adverb (he drives carefully)"],
               label="Adjective or adverb"), "good → well, fast → fast, hard → hard"),
 "prepos": ("Good AT maths, afraid OF snakes, married TO, depend ON, prefer TO — these pairs must be "
            "learned, and they appear in every letter you write.",),
 "conj": ("Joining short sentences well is the difference between writing that flows and writing that "
          "reads like a list.",
          F(["Although … (no 'but' later)", "Neither … nor",
             "Either … or", "Not only … but also"], label="Pairs that must stay together"),
          "One contrast word per sentence is enough"),
 "concord": ("'The box of pencils IS on the table.' Hiding the subject behind extra words is the examiner's "
             "favourite trick — and a common mistake in official letters.",
             F(["Find the subject", "Cross out the words between",
                "Match the verb to the subject"], label="Getting concord right"),
             "Each, every, one of, neither — all singular"),
 "articles": ("A university, an hour, an honest man — a/an follows the SOUND, not the letter.",),
 "qtags": ("Tags appear in speech all day: 'You are coming, aren't you?' Four odd ones carry most of the "
           "marks: aren't I, shall we, will you, did they.",
           F(["Positive statement → negative tag", "Negative statement → positive tag",
              "Repeat the helper + a pronoun"], label="Making a question tag"),
           "No helper? Use do, does or did"),
 "reported": ("Reporting what somebody said — in a complaint, a witness statement or a letter home — "
              "follows three mechanical steps.",
              F(["Tense back one step", "Change the pronouns",
                 "Shift time and place words"], label="Direct → reported speech"),
              "is → was, I → he/she, now → then"),
 "voice": ("'The window was broken' is used when the doer is unknown or unimportant — common in reports, "
           "notices and news.",
           F(["Object becomes the subject", "Add the right form of BE",
              "Use the past participle", "Doer after 'by' (or dropped)"], label="Active → passive"),
           "Keep the tense exactly as it was"),
 "sentence": ("Varying simple, compound and complex sentences is what gives a composition its expression "
              "mark.",
              T("SENTENCES", ["Simple: one clause", "Compound: two main clauses joined",
                              "Complex: main + subordinate"], label="Sentence types"),
              "A phrase has no verb; a clause has one"),
 "punct": ("A comma in a list, an apostrophe for possession, and quotation marks for speech — the three "
           "places most marks are lost.",
           F(["Capital at the start", "Commas in a list", "Apostrophe: possession or missing letter",
              "Full stop, ? or !"], label="Punctuation checklist"),
           "The comma goes INSIDE the quotation marks"),
 "synant": ("A wider vocabulary makes every answer shorter and sharper — three new words a day is about "
            "a thousand a year.",),
 "idioms": ("Idioms appear in speeches, radio and newspapers; learning them inside a full sentence is what "
            "makes them stick.",),
 "vocab": ("One root word gives a family: care → careful, careless, carefully, carelessness. Learn the "
           "family and your vocabulary doubles.",
           T("WORD FAMILIES", ["Prefix: un-, dis-, im-, ir-, mis-",
                               "Suffix: -ness, -ment, -tion, -ful, -less",
                               "care → careful → carelessness"], label="Building words"),
           "Ask what part of speech the gap needs"),
 "confuse": ("their/there/they're, its/it's, advice/advise, lose/loose — these slip past when you write "
             "quickly, and they cost marks in every subject.",
             F(["it's = it is", "its = belonging to it",
                "you're = you are", "your = belonging to you"], label="The apostrophe test"),
             "Say the long form aloud and the choice is obvious"),
 "figspeech": ("One simile or metaphor well placed lifts a composition's expression mark; overused, it sinks "
               "it.",),
 "comp": ("Comprehension is not a memory test — the answers are in front of you. The skill is finding "
          "the line and rewriting it in your own words.",
          F(["Read once for the story", "Read the question",
             "Find the exact line", "Answer in your own words"], label="How to answer comprehension"),
          "Four marks usually means four separate points"),
 "summ": ("Reading a long notice and saying what it means in four sentences is a workplace skill as much as "
          "an exam one.",
          F(["Read the question FIRST", "Underline only what answers it",
             "One point, one short sentence", "No opinions, no repeats"], label="Summary method"),
          "Examiners mark the first points only — choose them"),
 "letter": ("A letter to the headmaster, the assembly or an employer — the layout is learned once and "
            "used for life.",
            draw.letterfig(label="Layout of a formal letter"),
            "'Dear Sir' goes with 'Yours faithfully'"),
 "narrative": ("A story or description with one problem, five paragraphs and a clear ending — simple "
               "beats complicated every time.",
               F(["Plan 5 minutes", "Beginning: set the scene", "Middle: the problem",
                  "End: how it was settled", "Check spelling"], label="Planning a composition"),
               "Show, do not tell: give the detail and let the reader conclude"),
 "article": ("An article for a magazine, a report of an event, a speech at a gathering — each has its own "
             "opening and its own audience.",
             T("WHO IS LISTENING?", ["Article: strangers → a strong title",
                                     "Report: someone absent → facts in order",
                                     "Speech: an audience → vocatives first"],
               label="Article, report or speech"), "'Mr Chairman, the Headmistress, fellow pupils …'"),
 "oral": ("Spelling and sound do not match in English: sugar starts with 'sh', eight rhymes with late. "
          "Say the words quietly and listen.",
          F(["Say it aloud", "Listen to the SOUND", "Match sounds, not letters",
             "Mark the stressed syllable"], label="Answering an oral English question"),
          "PRE-sent (a gift) but pre-SENT (to give)"),
}

FIGS["benglish"] = {
 "prepos": (T("FIXED PAIRS", ["good AT, afraid OF, married TO",
                              "depend ON, insist ON, congratulate ON",
                              "different FROM, prefer TO, listen TO"], label="Verb + preposition"),
            "Keep a page in your notebook and add to it weekly"),
 "articles": (F(["a + consonant SOUND (a university)", "an + vowel SOUND (an hour)",
                 "the = we both know which one", "no article: football, English, lunch"],
                label="a, an, the — or nothing"), "Judge by the sound, not the spelling"),
 "synant": (T("WORD PAIRS", ["Synonym: furious = very angry",
                             "Antonym: permanent ≠ temporary",
                             "Prefix opposites: un-, im-, il-, ir-, dis-"],
               label="Synonyms and antonyms"), "Learn each new word with one friend and one enemy"),
 "idioms": (F(["Words you cannot take literally", "'in hot water' = in trouble",
               "Never change the words", "Learn it inside a sentence"], label="Idioms"),
            "Proverbs teach the lesson in one line"),
 "figspeech": (T("FIGURES OF SPEECH", ["Simile: as soft as silk (like / as)",
                                       "Metaphor: my father is a rock",
                                       "Personification: the angry sea",
                                       "Hyperbole: told you a million times"],
                 label="The four tested most"), "Name it AND give the reason"),
}

FIGS["bmaths"] = {
 "indices": (F(["a^m × a^n = a^(m+n)", "a^m ÷ a^n = a^(m−n)",
                "(a^m)^n = a^(mn)", "a^0 = 1,  a^(−n) = 1/a^n"], label="The laws of indices"),
             "Standard form: A × 10^n with 1 ≤ A < 10"),
 "approx": (F(["Look at the next digit", "5 or more → round up",
               "4 or less → leave it", "Keep the place-holders"], label="Rounding"),
            "Estimate first: it tells you whether the answer is sensible"),
 "factorise": (F(["Take out the H.C.F.", "Two brackets (FOIL backwards)",
                  "a² − b² = (a−b)(a+b)", "Grouping in pairs"],
                 label="Ways to factorise"), "Expand your answer in your head to check it"),
 "angles": (draw.tri(A="x", B="2x", C="3x", label="Angles in a triangle add up to 180°"),
            "Straight line 180°, point 360°, triangle 180°"),
 "shapes": (F(["Interior sum = (n − 2) × 180°", "Exterior sum = 360°",
               "Regular: each exterior = 360° ÷ n",
               "Interior + exterior = 180°"], label="Polygon angle rules"),
            "Decide which of the two sums the question needs"),
 "pythag": (draw.tri(a="12", b="h", c="9", A="", B="", C="", right=True,
                     label="A right-angled triangle"),
            "h² = 9² + 12² → h = 15. Add for the hypotenuse, subtract for a shorter side"),
 "perim": (F(["Rectangle: l × w", "Triangle: ½ × b × h",
              "Parallelogram: b × h", "Trapezium: ½(a + b) × h"], label="Areas to know"),
           "Perimeter is in cm; area is in cm²"),
 "construct": (F(["Equilateral triangle → 60°", "Bisect it → 30°",
                  "Perpendicular → 90°", "Bisect that → 45°"],
                 label="Angles you can construct"), "Leave every arc showing — they carry marks"),
 "transform": (F(["Translation: slide (x+a, y+b)", "Reflection in x-axis: (x, −y)",
                  "Rotation 90° anticlockwise: (−y, x)", "Enlargement k: (kx, ky)"],
                 label="The four transformations"),
               "Only enlargement changes the size"),
 "prob": (draw.piefig([("Red 3", 3), ("Blue 5", 5)], label="A bag of 8 balls"),
          "P(red) = 3/8, and P(not red) = 1 − 3/8 = 5/8"),
}

# ===================================================================== WASSCE CORE MATHS
import math as _m

PACK["maths"] = {
 "bases": ("Computers work in base two and older machines in base eight; changing base is the same place-value "
           "idea you already use in base ten.",
           F(["89 ÷ 5 = 17 r 4", "17 ÷ 5 = 3 r 2", "3 ÷ 5 = 0 r 3", "Read up: 324 base five"],
             label="Decimal to another base"), "Divide repeatedly and read the remainders upwards"),
 "mod": ("Clocks, days of the week, shift rotas and check digits on an account number all run on modular "
         "arithmetic.",
         C(["0", "1", "2", "3", "4"], centre="mod 5", label="Arithmetic in a cycle"),
         "After the last value you come back to the start"),
 "approx": ("Pricing, estimating a bill and judging whether a calculator answer is sensible.",),
 "indices": ("Compound interest, population growth, computer storage and scientific measurement are all "
             "written with indices.",
             F(["a^m × a^n = a^(m+n)", "a^m ÷ a^n = a^(m−n)",
                "(a^m)^n = a^(mn)", "a^(1/n) = the nth root"], label="The laws of indices"),
             "Make the bases the same before you compare powers"),
 "logs": ("Sound in decibels, earthquakes on the Richter scale and pH are all logarithmic — "
          "a log turns multiplying into adding.",
          plot(lambda x: _m.log10(x), 0.4, 10, -1.2, 1.2, step=1, pts=[(1, 0, "log 1 = 0"), (10, 1, "log 10 = 1")],
               label="y = log x"),
          "The curve rises fast at first, then slowly — and never reaches the y-axis"),
 "surds": ("Exact lengths in construction and in trigonometry are left in surd form so that no accuracy is "
           "lost before the final step.",),
 "seq": ("Instalment payments, salary increments, depreciation and compound interest are APs and GPs with "
         "money attached.",
         plot(None, 0, 7, 0, 26, step=1,
              pts=[(1, 4, ""), (2, 7, ""), (3, 10, ""), (4, 13, ""), (5, 16, ""), (6, 19, "")],
              lines=[(0, 1, 7, 22)], label="An AP plotted: 4, 7, 10, 13 …"),
         "An AP gives points on a straight line; a GP curves away"),
 "sets": ("Any survey, voter analysis or stock count with overlapping categories is a Venn diagram.",
          draw.venn3(["Maths", "Science", "ICT"], [8, 5, 4, 3, 2, 6, 7, 5], label="Three overlapping sets"),
          "Always fill the centre of the diagram first"),
 "logic": ("Contracts, laws and arguments on the radio all turn on 'if … then': knowing the converse from "
           "the contrapositive stops you being misled.",
           F(["p → q", "Converse: q → p", "Inverse: ~p → ~q",
              "Contrapositive: ~q → ~p (always true if p → q is)"], label="Implication"),
           "Only the contrapositive always keeps the truth value"),
 "fin": ("Hire purchase, VAT, income tax, commission, depreciation and a bank loan — the maths of earning "
         "and spending.",
         F(["Cost price", "Mark-up or discount", "Selling price", "% always on the stated base"],
           label="Financial arithmetic"), "Read carefully whether the % is of cost, of selling price or of the total"),
 "var": ("Fuel used varies directly with distance; time taken varies inversely with speed; a worker's pay "
         "varies jointly with rate and hours.",
         plot(lambda x: 12.0 / x, 1, 10, 0, 14, step=1, pts=[(2, 6, "(2, 6)"), (6, 2, "(6, 2)")],
              label="Inverse variation: y = 12/x"),
         "Direct → a straight line through the origin; inverse → this curve"),
 "matrix": ("Matrices store tables of data — stock in several shops, marks in several subjects — and "
            "transform shapes in computer graphics.",
            F(["det = ad − bc", "If det = 0 there is no inverse",
               "Inverse = (1/det) × the adjoint"], label="2 × 2 matrices"),
            "Check the determinant before trying to invert"),
 "alg": ("Every formula you rearrange — making the subject, solving for an unknown rate or an unknown "
         "quantity — is this topic.",),
 "quad": ("The path of a thrown object, the profit curve of a business and the area of a field with a fixed "
          "fence are all quadratics.",
          plot(lambda x: x * x - 2 * x - 3, -3, 5, -5, 8, step=1,
               pts=[(-1, 0, "x = −1"), (3, 0, "x = 3"), (1, -4, "minimum")],
               label="y = x² − 2x − 3"),
          "The roots are where the curve crosses the x-axis"),
 "ineq": ("Linear programming decides how many of each product to make within limits of money, time and "
          "material — real planning, not just shading.",
          plot(lambda x: 6 - x, 0, 7, 0, 7, step=1, shade=[(0, 0), (6, 0), (0, 6)],
               label="The region x + y ≤ 6, x ≥ 0, y ≥ 0"),
          "Shade the region that satisfies every inequality at once"),
 "afunc": ("Rates, averages and formulas that involve division all become algebraic fractions — and the "
           "domain tells you which values are forbidden.",),
 "area": ("Quantity surveying: tiles for a floor, paint for a wall, roofing sheets, land area and the cost "
          "that follows from each.",
          F(["Split the shape", "Rectangle + triangle + sector",
             "Add the parts", "Watch the units"], label="Compound areas"),
          "Area in m², so a price per m² multiplies straight in"),
 "vol": ("Tanks, silos, drums, concrete volumes and the capacity of a reservoir.",
         draw.solidfig("cone", labels=["r", "h", "l"], label="A cone"),
         "Volume ⅓πr²h; curved surface πrl"),
 "geo": ("Setting out a building, a roof truss and a staircase all depend on the angle rules.",),
 "circle": ("Arches, culverts, gear wheels and any design based on a circle use the circle theorems.",
            draw.circlefig("centre", angles=["2x", "x"], label="Angle at the centre"),
            "The angle at the centre is twice the angle at the circumference"),
 "loci": ("Where to sink a borehole equidistant from three houses, or where a goat tied to a post can reach "
          "— that is a locus.",),
 "coord": ("Phone tariffs, taxi fares, depreciation and any 'fixed charge plus rate' agreement is y = mx + c.",
           plot(lambda x: 0.5 * x + 2, -4, 6, -2, 6, step=1, pts=[(0, 2, "(0, 2)"), (4, 4, "")],
                label="y = ½x + 2"),
           "m is the rate (gradient), c is the fixed charge (intercept)"),
 "trig": ("Surveyors find the height of a mast, and builders the pitch of a roof, with sine, cosine and "
          "tangent.",
          plot(lambda t: _m.sin(_m.radians(t)), 0, 360, -1.3, 1.3, step=90,
               pts=[(90, 1, "max"), (270, -1, "min")], label="y = sin x"),
          "The sine curve repeats every 360°"),
 "bear": ("Navigation at sea and in the air, and any survey of a plot with three sides and angles, "
          "use bearings with the sine and cosine rules.",
          draw.compass([(65, "B, 12 km", 0.9), (155, "C", 0.7)], label="A bearing journey"),
          "Draw a north line at EVERY point before you start"),
 "calc": ("Maximum profit, minimum cost, the speed of a moving body and the area under a curve all come "
          "from calculus.",
          plot(lambda x: x * x, -3, 3, -1, 9, step=1, lines=[(0, -4, 3, 8)],
               pts=[(2, 4, "gradient = 4")], label="y = x² and the tangent at x = 2"),
          "The derivative is the gradient of the tangent at that point"),
 "stat": ("Market research, examination analysis, rainfall and election results are all summarised and "
          "pictured with statistics.",
          draw.barfig([("0-9", 3), ("10-19", 7), ("20-29", 12), ("30-39", 9), ("40-49", 4)],
                      label="A frequency distribution", ylab="frequency"),
          "Mean from Σfx ÷ Σf; mode is the tallest bar"),
 "prob": ("Insurance premiums, quality control, weather forecasts and games of chance are probability "
          "in business.",),
 "vec": ("Forces on a structure, a boat crossing a current and movement in computer graphics are all "
         "vectors.",
         plot(None, -1, 6, -1, 6, step=1, lines=[(0, 0, 4, 3)], pts=[(4, 3, "(4, 3)")],
              label="The vector (4, 3)"),
         "Magnitude = √(4² + 3²) = 5"),
 "intfac": ("H.C.F. and L.C.M. decide packaging sizes, delivery schedules and when two cycles coincide.",),
 "simil": ("Scale drawings, maps, model buildings and photographs enlarging are all similarity.",
           F(["Equal angles", "Sides in the same ratio", "Area ratio = k²", "Volume ratio = k³"],
             label="Similar figures"), "Lengths × k, areas × k², volumes × k³"),
 "earth": ("Flight distances, time zones and GPS positions come from latitude and longitude on a sphere.",
           draw.solidfig("sphere", labels=["R = 6 400 km"], label="The earth as a sphere"),
           "Along a parallel of latitude α the radius shrinks to R cos α"),
 "cumfreq": ("Cut-off marks, median income and the pass mark for a quota are read straight off an ogive.",
             plot(None, 0, 60, 0, 60, step=10,
                  pts=[(10, 4, ""), (20, 12, ""), (30, 28, ""), (40, 46, ""), (50, 56, ""), (60, 60, "")],
                  lines=[(0, 0, 10, 4), (10, 4, 20, 12), (20, 12, 30, 28), (30, 28, 40, 46),
                         (40, 46, 50, 56), (50, 56, 60, 60)],
                  label="A cumulative frequency curve (ogive)"),
             "Read the median at half the total frequency"),
}

FIGS["maths"] = {
 "approx": (F(["Significant figures start at the first non-zero digit",
               "Decimal places count from the point",
               "Estimate: round each to 1 s.f. first"], label="Approximation"),
            "Estimate before you calculate, and compare after"),
 "surds": (F(["√ab = √a × √b", "Simplify: √50 = 5√2",
              "Rationalise: multiply by the conjugate"], label="Working with surds"),
           "Leave the answer exact unless the question says otherwise"),
 "alg": (F(["Expand the brackets", "Clear the fractions", "Collect the letters",
            "Divide", "Check by substituting"], label="Solving and rearranging"),
         "Changing the subject uses exactly the same moves"),
 "afunc": (F(["Factorise top and bottom", "Cancel common factors",
              "Common denominator to add", "State the forbidden values"],
             label="Algebraic fractions"), "The denominator may never be zero"),
 "geo": (draw.tri(A="A", B="B", C="C", label="Angles in a triangle"),
         "Exterior angle = the sum of the two opposite interior angles"),
 "loci": (F(["Equidistant from 2 points → perpendicular bisector",
             "Equidistant from 2 lines → angle bisector",
             "Fixed distance from a point → a circle"], label="The three standard loci"),
          "Describe the locus in words as well as drawing it"),
 "prob": (draw.piefig([("Win 2", 2), ("Draw 1", 1), ("Lose 3", 3)], label="Outcomes of a match"),
          "Mutually exclusive: add. Independent: multiply"),
 "intfac": (draw.tree("84", ["2 × 42", "2 × 21", "3 × 7"], label="Prime factor tree",
                      sub="84 = 2² × 3 × 7"),
            "H.C.F. × L.C.M. = the product of the two numbers"),
}

# ===================================================================== WASSCE SCIENCE
PACK["science"] = {
 "measure": ("Every laboratory report, drug dose and engineering drawing depends on reading an instrument "
             "properly and recording the right unit.",
             F(["Observe", "Hypothesis", "Fair test: one variable",
                "Measure and record", "Conclude"], label="Scientific method"),
             "Control every variable except the one you are testing"),
 "living": ("Deciding whether a specimen is alive, and what it needs, underlies farming, medicine and "
            "conservation.",),
 "classify": ("Pest control, fisheries management and disease tracing all start with correct classification.",
              T("CLASSIFICATION", ["Kingdom → phylum → class",
                                   "Order → family → genus → species",
                                   "Binomial name: Homo sapiens"], label="The hierarchy"),
              "Give the reason for the group, not just the name"),
 "cells": ("Tissue culture, disease diagnosis and plant propagation all work at the level of the cell.",),
 "matter": ("Separating a mixture, choosing a solvent and understanding why a gas can be compressed.",
            PT("gas"), "Gas particles are far apart and move fast in all directions"),
 "acids": ("Liming acid soils, treating water, neutralising stomach acid and testing with indicators.",
           draw.phscale(10, "lime water"), "Acid + base → salt + water"),
 "metals": ("Why iron rusts and aluminium does not, why zinc coats a roofing sheet, and how a sacrificial "
            "anode protects a tank.",
            F(["Iron + oxygen + water", "Rust (hydrated iron oxide)",
               "Prevent: paint, oil, galvanise, alloy"], label="Rusting"),
            "Rusting needs BOTH air and water"),
 "water": ("Treating drinking water, dealing with hard water in boilers, and preparing solutions of known "
           "concentration.",
           draw.labware("distil"), "Distillation separates pure water from dissolved salts"),
 "soil": ("Soil testing, liming, drainage, rotation and conservation on a slope are a farmer's working "
          "science.",),
 "organic": ("Petrol, kerosene, plastics, soap, alcohol and vinegar all come from organic chemistry.",
             F(["Crude oil", "Fractional distillation",
                "Petrol, kerosene, diesel, bitumen", "Plastics and more"], label="From crude oil"),
             "Separated by boiling point, lightest at the top"),
 "air": ("Combustion, rusting, the nitrogen cycle on a farm and the weather forecast.",
         C(["Nitrogen in air", "Fixed by bacteria and lightning",
            "Taken up by plants", "Decay and denitrification"], centre="NITROGEN CYCLE",
           label="The nitrogen cycle"),
         "Legumes carry the fixing bacteria in their root nodules"),
 "hydro": ("Why a stream dries up, why a town floods, and why galamsey ruins a river for a generation.",
           C(["Evaporation", "Condensation", "Precipitation", "Run-off"], centre="WATER CYCLE",
             label="The water cycle"), "Nothing is added and nothing lost — only moved"),
 "pests": ("Knowing a pest's life cycle tells you exactly which stage to attack, and which pesticide at "
           "which time.",
           C(["Egg", "Larva", "Pupa", "Adult"], centre="COMPLETE METAMORPHOSIS",
             label="Life cycle of an insect pest"), "Break the cycle at its weakest stage"),
 "crop": ("Land preparation, spacing, weeding, fertiliser, harvesting and storage decide whether a farm "
          "makes money.",),
 "animal": ("Housing, feeding, breeding and disease control in poultry, cattle and fish farming.",),
 "nutrition": ("Planning a balanced diet on a budget, reading a food label and recognising deficiency "
               "diseases.",
               F(["Mouth: amylase on starch", "Stomach: pepsin on protein",
                  "Small intestine: all completed", "Absorbed by the villi"], label="Digestion"),
               "Bile emulsifies fat — it is not an enzyme"),
 "respcirc": ("Why athletes train, why smoking damages the lungs, and what blood pressure and anaemia mean.",
              F(["Alveoli: O₂ in, CO₂ out", "Blood carries it",
                 "Cells respire: energy released", "CO₂ back to the lungs"], label="From air to cell"),
              "Breathing is physical; respiration is chemical"),
 "excskel": ("Kidney health, water balance, posture and reflex actions in first aid.",),
 "repro": ("Family planning, maternal health, plant breeding and grafting in horticulture.",),
 "photo": ("Why shade reduces yield, why leaves are green, and why forests are called the lungs of the "
           "earth.",
           draw.plantfig(), "Carbon dioxide + water → glucose + oxygen, in light"),
 "energy": ("Choosing between a generator and solar, understanding a power bill, and the national energy mix.",
            F(["Chemical", "Electrical", "Mechanical", "Light and heat"], label="Energy transformations"),
            "Energy is conserved — it only changes form"),
 "heat": ("Cooking, refrigeration, insulation of a roof, and why a bridge is built with expansion joints.",
          F(["Conduction: solids", "Convection: fluids",
             "Radiation: no medium needed"], label="Heat transfer"), "A vacuum flask blocks all three"),
 "light": ("Spectacles, cameras, periscopes, fibre optics and why a swimming pool looks shallower than it is.",
           draw.reflectfig(35), "Angle of incidence = angle of reflection"),
 "sound": ("Hearing loss from loud speakers, ultrasound scans, sonar and the acoustics of a hall.",),
 "elec": ("House wiring, fuses, earthing, a motor, a transformer and the cost of a unit of electricity.",
          draw.circuitfig(label="A series circuit"),
          "Parallel keeps the others working when one lamp fails"),
 "electron": ("Phones, solar inverters, logic gates and the chips in every appliance.",
              F(["Input signal", "Transistor / gate", "Processing", "Output"],
                label="An electronic system"), "A diode lets current pass one way only"),
 "eco": ("Overfishing, deforestation, pesticide build-up and why a predator matters to a farm.",
         F(["Producers", "Herbivores", "Carnivores", "Decomposers"], label="Energy flow"),
         "Only about a tenth of the energy passes to the next level"),
 "force": ("Vehicle braking distances, hydraulic jacks, floating and sinking, and why a tractor has wide "
           "tyres.",
           F(["Pressure = force ÷ area", "Liquids transmit pressure equally",
              "Upthrust = weight of fluid displaced"], label="Pressure and upthrust"),
           "That is why a hydraulic jack lifts a car with one hand"),
 "machines": ("Pulleys on a building site, gears on a bicycle, ramps and levers — and why no machine is "
              "100% efficient.",
              draw.leverfig(1, label="A first-class lever"),
              "M.A. = load ÷ effort; efficiency = (M.A. ÷ V.R.) × 100%"),
 "health": ("Immunisation schedules, malaria prevention, food hygiene and first aid at home and at work.",),
 "genes": ("Why a child resembles a parent, sickle-cell counselling, improved seed and livestock breeds.",
           T("INHERITANCE", ["Genes carried on chromosomes",
                             "Dominant and recessive alleles",
                             "Punnett square predicts the ratio"], label="Variation and inheritance"),
           "Sickle-cell: two carriers have a 1 in 4 risk each pregnancy"),
 "env": ("Climate change, plastic waste, galamsey and air quality — the science behind every policy "
         "argument you will hear.",
         C(["Reduce", "Reuse", "Recycle"], centre="WASTE", label="The three Rs"),
         "Prevention is always cheaper than cleaning up"),
 "rocks": ("Quarrying, building stone, cement, and where to look for minerals and groundwater.",
           C(["Igneous", "Sedimentary", "Metamorphic"], centre="ROCK CYCLE", label="The rock cycle"),
           "Heat, pressure and weathering keep turning one into another"),
 "farmtools": ("Choosing, using and maintaining tools decides how long they last and how safe the work is.",
               F(["Clean after use", "Dry it", "Oil the metal", "Store under cover"],
                 label="Care of farm tools"), "Rust is the commonest cause of a short tool life"),
 "teeth": ("Brushing, fluoride, diet and why sugar between meals is worse than sugar with them.",
           F(["Bacteria + sugar", "Acid on the enamel", "Decay", "Brush, rinse, limit sugar"],
             label="How tooth decay happens"), "Toothpaste is mildly basic for exactly this reason"),
 "hormone": ("Diabetes, thyroid problems, growth and the changes of adolescence are all hormones.",
             T("HORMONES", ["Insulin: lowers blood sugar",
                            "Adrenaline: fight or flight",
                            "Thyroxine: rate of metabolism"], label="Chemical messengers"),
             "Slower than nerves, but their effects last longer"),
 "preserve": ("Drying fish, smoking meat, refrigeration, salting and canning — how a surplus harvest "
              "becomes income instead of waste.",
              F(["Remove water", "Remove air", "Add salt or sugar",
                 "Lower the temperature"], label="Ways to preserve food"),
              "Every method attacks what the micro-organisms need"),
 "magnet": ("Loudspeakers, motors, generators, the compass and the magnetic strip on a card.",
            F(["Current in a coil", "Magnetic field", "Soft iron core",
               "Electromagnet: bells, relays, cranes"], label="Electromagnetism"),
            "Switch the current off and the magnetism goes"),
}

FIGS["science"] = {
 "living": (F(["Movement", "Respiration", "Sensitivity", "Growth",
               "Reproduction", "Excretion", "Nutrition"], label="MRS GREN"),
            "All seven, or it is not alive"),
 "cells": (draw.cellfig("animal", label="An animal cell"),
           "No cell wall, no chloroplast, no large vacuole"),
 "soil": (F(["Rock weathers", "Humus from decay", "Water and air in the gaps",
             "Organisms at work"], label="What soil is made of"),
          "Loam drains yet holds water — the farmer's best soil"),
 "crop": (C(["Land preparation", "Planting", "Weeding and fertiliser",
             "Pest control", "Harvest and storage"], centre="CROP CYCLE", label="Growing a crop"),
          "Most losses happen after harvest, in storage"),
 "animal": (T("ANIMAL PRODUCTION", ["Housing: dry, airy, clean",
                                    "Feeding: balanced ration and water",
                                    "Health: vaccination and dipping",
                                    "Breeding and records"], label="Good husbandry"),
            "A dirty, damp house is where disease starts"),
 "excskel": (T("REMOVING WASTE", ["Kidneys: urea and water",
                                  "Lungs: carbon dioxide",
                                  "Skin: sweat"], label="Excretion"),
             "Excretion removes waste the body MADE; egestion removes undigested food"),
 "repro": (F(["Flower", "Pollination", "Fertilisation",
              "Fruit and seed", "Germination"], label="Reproduction in a flowering plant"),
           "Pollination is the transfer; fertilisation is the fusion"),
 "sound": (F(["Vibration", "Through a medium", "Ear-drum vibrates", "Heard"],
             label="How sound travels"),
           "Pitch from frequency, loudness from amplitude"),
 "health": (F(["Agent (germ)", "Route: air, water, food, vector",
               "New host", "Break any link"], label="The chain of infection"),
            "Immunisation protects the host before the germ arrives"),
}

# ===================================================================== WASSCE SOCIAL STUDIES
PACK["social"] = {
 "envcomp": ("Every siting decision — a farm, a house, a factory, a dump — is a decision about the "
             "environment your community depends on.",
             T("ENVIRONMENT", ["Physical: land, water, air, climate",
                               "Human-made: roads, towns, dams",
                               "Social: people, customs, institutions"], label="The components"),
             "Damage one and the other two follow"),
 "degrad": ("Galamsey, bush burning, sand winning and deforestation — and the laws and agencies meant to "
            "stop them.",
            F(["Vegetation removed", "Soil exposed", "Erosion and silting",
               "Yields fall, water fails"], label="How degradation spreads"),
            "Reclamation costs far more than prevention"),
 "popn": ("Census figures decide where the next school, clinic and borehole go — and show which "
          "districts are being left behind.",
          draw.pyramidfig(["0-14: very wide", "15-59: working age", "60+: narrow"],
                          label="A youthful population pyramid"),
          "A young population means schools now, jobs soon"),
 "sanit": ("Cholera, typhoid and malaria are all decided by water, toilets and drainage — the cheapest "
           "health policy there is.",
           F(["Safe water", "Proper toilets", "Waste collected",
              "Drains cleared"], label="Environmental health"),
           "Hand-washing with soap breaks the commonest route"),
 "disaster": ("Floods, fires, earth tremors and epidemics: preparation, warning, response and recovery.",
              C(["Prevent and prepare", "Warn", "Respond", "Recover and rebuild"],
                centre="DISASTER CYCLE", label="Managing a disaster"),
              "NADMO co-ordinates, but the first response is always local"),
 "culture": ("Festivals that fund development, crafts that earn a living, and the courage to drop practices "
             "that deny rights.",),
 "social": ("How a person becomes a member of society — and why the peer group can pull against the home.",
            T("AGENTS", ["Family: first and strongest",
                         "School: knowledge and rules",
                         "Peer group, religion, the media"], label="Socialisation"),
            "Values learnt early are the ones that last"),
 "adol": ("The decisions of these few years — study, company, self-control — set the options for the "
          "next forty.",),
 "family": ("Marriage types, responsible parenthood, and why broken homes cost children most.",),
 "educ": ("Education raises the individual's income and the nation's productivity at the same time — "
          "including technical and vocational routes.",),
 "nation": ("Nation building is practical: pay tax, protect public property, keep the peace, buy Ghanaian.",
            T("NATION BUILDING", ["National symbols and history",
                                  "Unity across tribe and religion",
                                  "Work, taxes and law",
                                  "Peace and security"], label="What builds a nation"),
            "Independence 6 March 1957; republic 1 July 1960"),
 "constit": ("Your protection against arbitrary power: the supreme law that binds even Parliament.",),
 "citizen": ("Rights come with duties — and knowing both is what makes a citizen rather than a subject.",
             F(["Rights: life, liberty, speech, property",
                "Duties: obey the law, pay tax, vote",
                "Report abuse: CHRAJ, the courts"], label="Citizenship"),
             "A right you cannot name is a right you cannot defend"),
 "democracy": ("Why Parliament vets nominees and the courts can void a law — and why that protects you.",
               T("THREE ARMS", ["Executive: implements",
                                "Legislature: makes laws",
                                "Judiciary: interprets"], label="Separation of powers"),
               "Checks and balances prevent any one arm taking over"),
 "elect": ("Registering, voting in secret, accepting the result or going to court — the whole democratic "
           "bargain in four steps.",
           F(["Register", "Campaign", "Vote in secret",
              "Count publicly", "Transfer power"], label="An election"),
           "Over 50% of valid votes is needed for the presidency"),
 "local": ("The assembly decides the gutter, the market, the clinic and the feeder road in YOUR district.",),
 "leader": ("Accountability means explaining what was done with the money — at a club, an assembly or a "
            "ministry.",),
 "conflict": ("Land and chieftaincy disputes close schools and markets; dialogue, elders and the courts are "
              "the way out.",
              F(["Dialogue", "Mediation by elders", "Arbitration",
                 "The courts"], label="Resolving conflict peacefully"),
              "Each step is cheaper than the violence it prevents"),
 "corrupt": ("Every diverted cedi is a classroom not built — and refusing to pay a bribe is half the cure.",
             T("WHO FIGHTS IT", ["Office of the Special Prosecutor",
                                 "CHRAJ and EOCO",
                                 "Auditor-General and Parliament's PAC",
                                 "The media and citizens"], label="Anti-corruption bodies"),
             "Transparency: published accounts and open procurement"),
 "intl": ("ECOWAS opens a market of hundreds of millions to a Ghanaian trader; the UN and AU bring peace, "
          "aid and a voice.",),
 "economy": ("Why raw cocoa earns little and processed cocoa earns much more — the argument behind "
             "industrial policy.",
             F(["PRIMARY: farming, mining", "SECONDARY: processing",
                "TERTIARY: services"], label="Sectors of the economy"),
             "Value addition keeps the money and the jobs at home"),
 "money": ("Budgeting, saving, borrowing wisely and understanding interest — personal finance you will "
           "use from your first salary.",
           F(["Income", "Needs first", "Save a fixed share",
              "Then wants"], label="A simple personal budget"),
           "Pay yourself first: save before you spend"),
 "entre": ("Self-employment is where most Ghanaian jobs are — and records, discipline and customer care "
           "decide who survives.",),
 "unemp": ("Why graduates are jobless while employers cannot find skills — and what training, "
           "entrepreneurship and policy can do.",
           T("UNEMPLOYMENT", ["Structural: wrong skills",
                              "Seasonal: farming off-season",
                              "Frictional: between jobs",
                              "Disguised: too many on one farm"], label="Types of unemployment"),
           "Skills training attacks the structural kind directly"),
 "sci": ("Mobile money, irrigation, telemedicine and e-government — and the maintenance culture they "
         "need.",),
 "sustain": ("Using today's resources without robbing your own children — the test behind every "
             "environmental law.",
             C(["Economy", "Society", "Environment"], centre="SUSTAINABLE DEVELOPMENT",
               label="The three pillars"), "A project must stand on all three"),
 "tour": ("Castles, parks and festivals turn into income for drivers, guides, cooks and craftsmen.",),
 "trade": ("As a consumer: know your rights, check weights and prices, and keep the receipt.",
           F(["Production", "Distribution", "Exchange", "Consumption"],
             label="Goods from farm to consumer"), "Every middleman adds a cost and a service"),
 "probs": ("Teenage pregnancy, drug abuse, armed robbery and streetism — causes, effects and what "
           "actually works.",),
 "planning": ("National plans only work when citizens take part: public hearings, assembly meetings and "
              "holding leaders to the plan.",
              F(["Identify needs", "Plan and budget", "Implement",
                 "Monitor and evaluate"], label="Development planning"),
              "Citizens belong at every stage, not only at voting"),
 "identity": ("Knowing who you are \u2014 your family, language, faith, abilities and goals \u2014 is what lets you set your own course instead of following whoever shouts loudest. Self-esteem is built by keeping the promises you make to yourself.",),
 "gender": ("Equal access to school, work and leadership — and why girls' education changes a whole "
            "family's future.",),
 "chief": ("Chiefs hold land in trust, settle disputes and mobilise for development alongside the assembly.",),
 "rights": ("Human rights, children's rights and the bodies that enforce them — knowledge that protects "
            "you and others.",),
 "religion": ("Living peacefully among faiths, and the shared moral ground that holds a plural society "
              "together.",),
}

FIGS["social"] = {
 "culture": (T("CULTURE", ["Language, dress, food, music",
                           "Festivals, rites, chieftaincy",
                           "Beliefs and values"], label="What culture includes"),
             "Learned, shared, and always changing"),
 "adol": (F(["Physical change", "New emotions", "Peer pressure",
             "Goals and self-control"], label="Adolescence"), "Set the goal first; the 'no' becomes easier"),
 "family": (T("FAMILY", ["Nuclear and extended",
                         "Patrilineal and matrilineal",
                         "Roles, duties and support"], label="Marriage and family"),
            "Responsible parenthood: the number you can truly care for"),
 "educ": (F(["KG 2", "Primary 6", "JHS 3", "SHS / TVET 3", "Tertiary"], label="The education ladder"),
          "Technical and vocational routes lead to work sooner"),
 "constit": (F(["1992 Constitution", "7 January 1993", "Fourth Republic",
                "Supreme law — all else is void"], label="Constitutional rule"),
             "Entrenched clauses need a referendum to change"),
 "local": (T("LOCAL GOVERNMENT", ["16 regions",
                                  "Metropolitan / Municipal / District Assemblies",
                                  "Town and area councils", "Unit committees"],
             label="Decentralisation"), "The assembly is the highest <b>political</b> authority in the district"),
 "leader": (T("GOOD LEADERSHIP", ["Honesty and selflessness",
                                  "Fairness and tolerance",
                                  "Hard work and vision",
                                  "Accountability"], label="Qualities"),
            "Followership matters too: honest advice, then co-operation"),
 "intl": (T("GHANA BELONGS TO", ["UN (1945)", "AU (2002, from OAU 1963)",
                                 "ECOWAS (1975)", "The Commonwealth"], label="International bodies"),
          "ECOWAS: free movement and trade in West Africa"),
 "entre": (C(["Spot the opportunity", "Raise capital", "Produce",
              "Sell and keep records", "Reinvest"], centre="BUSINESS", label="The business cycle"),
           "Separate business money from household money"),
 "sci": (F(["Science asks why", "Technology applies it",
            "Industry and services grow", "Maintenance keeps it alive"],
           label="Science and development"), "Trained people matter more than new machines"),
 "tour": (T("ATTRACTIONS", ["Historical: castles, forts, palaces",
                            "Natural: Kakum, Mole, Wli, Lake Volta",
                            "Cultural: festivals, crafts, food"], label="Tourism in Ghana"),
          "Protect the site, train guides, share the income"),
 "probs": (F(["Poverty and idleness", "Weak homes and peer pressure",
              "Drug abuse, crime, early pregnancy",
              "Education, jobs, counselling"], label="Social problems and their roots"),
           "Treat the cause, not only the symptom"),
 "identity": (T("WHO AM I?", ["Family, language and culture",
                              "Faith and values",
                              "Abilities and interests",
                              "Goals for the next five years"], label="Self-identity"),
              "Identity is built, not born"),
 "gender": (F(["Equal access to school", "Equal access to work",
               "Equal voice in leadership",
               "Educated girls → healthier, smaller families"], label="Gender equality"),
            "This is development policy, not only fairness"),
 "chief": (T("CHIEFTAINCY", ["Custodian of land and stools",
                             "Settles disputes",
                             "Mobilises for development",
                             "House of Chiefs"], label="The role of chiefs"),
           "Chiefs and assemblies work side by side"),
 "rights": (F(["Right", "Duty that goes with it",
               "Breach → report", "CHRAJ, courts, DOVVSU"], label="Rights in practice"),
            "Children's rights: name, care, education, protection"),
 "religion": (T("LIVING TOGETHER", ["Freedom of worship",
                                    "Shared moral ground",
                                    "Respect in speech and media",
                                    "Peace councils"], label="Religion in a plural society"),
              "Tolerance is a civic skill, not just a private virtue"),
}

# ===================================================================== WASSCE ENGLISH
PACK["english"] = {
 "syn": ("A sharper word makes an essay shorter and stronger — and comprehension often asks for one "
         "directly.",
         T("CHOOSING A WORD", ["Nearest in meaning IN THIS SENTENCE",
                               "Watch the register: formal or informal",
                               "Read the whole sentence first"], label="Synonyms in context"),
         "The best synonym is the one that could replace it exactly"),
 "ant": ("Contrast is how arguments are built: 'not permanent but temporary' says more than either word "
         "alone.",
         F(["un- (unhappy)", "in-/im-/il-/ir- (impossible, illegal)",
            "dis- (disobey)", "mis- (misunderstand)"], label="Opposites with prefixes"),
         "Learn each word with its opposite"),
 "idiom": ("Newspapers, radio and speeches run on idioms; using one correctly lifts an essay, "
           "misusing it sinks a sentence.",),
 "reg": ("The words of medicine, law, farming, sport and the market — examiners test whether you can "
         "match words to the field.",
         T("REGISTER", ["Medicine: diagnosis, prescription, ward",
                        "Law: plaintiff, verdict, adjourn",
                        "Farming: harrow, fallow, yield",
                        "Sport: fixture, penalty, half-time"], label="Vocabulary of fields"),
         "Use the field's own words and your writing sounds informed"),
 "form": ("Filling forms, writing applications and avoiding the slips — their/there, advice/advise — "
          "that cost marks everywhere.",
          F(["Verb → noun: decide → decision",
             "Noun → adjective: danger → dangerous",
             "Adjective → adverb: careful → carefully"], label="Word formation"),
          "Ask which part of speech the gap needs"),
 "fig": ("Figures of speech are what the examiner means by 'expression' — one or two, well placed.",
         T("DEVICES", ["Simile and metaphor", "Personification and hyperbole",
                       "Alliteration and onomatopoeia", "Irony and symbolism"],
           label="Figures of speech"), "Name it, then explain the effect"),
 "tense": ("Narrating an event, reporting what was said and writing a CV all depend on keeping the tense "
           "consistent.",
           F(["Stated past time → simple past",
              "since / for / already → present perfect",
              "Earlier of two past events → past perfect"], label="Sequence of tenses"),
           "Never mix 'yesterday' with 'have'"),
 "concord": ("Formal writing is judged on it: 'The list of names IS on the board.'",
             F(["Find the subject", "Ignore the words between",
                "each / every / one of → singular",
                "either…or, neither…nor → nearer subject"], label="Concord"),
             "Cross out the phrase in between and the choice is obvious"),
 "pron": ("'Between you and me' and 'my colleague and I' appear in letters and interviews constantly.",),
 "prep": ("Phrasal verbs — put up with, look down on, give up — are everywhere in speech and in "
          "comprehension passages.",),
 "adj": ("Describing a product, a candidate or a scene — and never writing 'more better'.",),
 "tags": ("Conditionals run every negotiation: 'if you deliver today, I will pay tomorrow.'",
          F(["Type 1: If + present → will",
             "Type 2: If + past → would",
             "Type 3: If + had + p.p. → would have"], label="The three conditionals"),
          "Type 3 is for the past that cannot be changed"),
 "clause": ("Varying sentence length and type is what gives a composition its rhythm — and its marks.",),
 "punct": ("A misplaced comma can change a contract. In the exam it is the cheapest mark to keep.",),
 "voice": ("Reports, notices and scientific writing use the passive when the doer is unknown or "
           "unimportant.",),
 "vowel": ("Paper 3 tests sound, not spelling: eight rhymes with late, tough rhymes with stuff.",
           F(["Say it aloud", "Listen to the sound", "Match sounds, not letters"],
             label="Vowel sounds and rhymes"), "/ɪ/ as in bit versus /iː/ as in beat"),
 "cons": ("Ship and sip, thin and then, van and fan — pairs that change meaning completely.",
          T("CONSONANT TRAPS", ["/ʃ/ ship vs /s/ sip",
                                "/θ/ thin vs /ð/ then",
                                "/v/ van vs /f/ fan",
                                "Silent letters: knee, write, hour"], label="Consonants"),
          "Sugar begins with the sound of sh"),
 "stress": ("Stress changes meaning: a RE-cord but to re-CORD; and emphatic stress answers a different "
            "question each time.",
            F(["TA-ble (first)", "be-GIN (second)", "pho-TO-gra-pher (second)",
               "Emphatic stress answers 'which one?'"], label="Word and emphatic stress"),
            "Say the word aloud and feel which part is stronger"),
 "comp": ("Reading a contract, a notice or an article and saying exactly what it means — the most "
          "transferable skill in the syllabus.",
          F(["Read once for sense", "Read the question",
             "Find the exact lines", "Answer in your own words"], label="Comprehension method"),
          "Count the marks: four marks usually means four points"),
 "summary": ("Condensing a long report into the points that answer one question is a workplace skill.",
             F(["Read the question FIRST", "Underline only what answers it",
                "One point per sentence", "No opinions, no repetition"], label="Summary"),
             "Examiners mark the first points only — choose them deliberately"),
 "essay": ("Letters, articles, reports and speeches — the forms you will write after school as much as "
           "in it.",
           draw.letterfig(label="Formal letter layout"),
           "'Dear Sir' → 'Yours faithfully'; a named person → 'Yours sincerely'"),
 "errors": ("The commonest Ghanaian English slips — 'I am coming' for 'I will be back', 'off the light' "
            "— are fine in speech but cost marks in writing.",
            F(["Off the light → switch off the light",
               "I am coming → I will be back",
               "Borrow me → lend me"], label="Spoken habits to avoid in writing"),
            "Write the standard form; keep the local form for conversation"),
 "report": ("Minutes of a meeting, an accident report, a report of a school event — facts, in order, "
            "in the past tense.",
            F(["What, where, when", "Who took part", "What happened, in order",
               "Conclusion or recommendation"], label="Writing a report"),
            "A reader who was absent must be able to follow it"),
 "listen": ("Following announcements, instructions and a lecture is the skill Paper 3 is really testing.",
            F(["Listen for the key word", "Note the number or name",
               "Do not write everything", "Check the question first"], label="Listening comprehension"),
            "Read the questions before the passage is played"),
}

FIGS["english"] = {
 "idiom": (T("IDIOMS", ["Cannot be taken literally",
                        "'in hot water' = in trouble",
                        "Never change the words",
                        "Learn inside a sentence"], label="Idioms and collocations"),
           "Collocations: heavy rain, strong tea — fixed partners"),
 "pron": (T("PRONOUNS", ["Subject: I, we, he, she, they",
                         "Object: me, us, him, her, them",
                         "After a preposition → object"], label="Which form?"),
          "Drop the other person and your ear decides"),
 "prep": (T("PHRASAL VERBS", ["put up with = tolerate",
                              "look down on = despise",
                              "give up = stop trying",
                              "call off = cancel"], label="Prepositions and phrasal verbs"),
          "Learn them as whole expressions, never word by word"),
 "adj": (F(["Two → comparative", "Three or more → superlative",
            "Long words take more / most", "Never both at once"], label="Comparison"),
         "Order: opinion, size, age, shape, colour, origin, material"),
 "clause": (T("SENTENCES", ["Simple: one clause",
                            "Compound: two main clauses",
                            "Complex: main + subordinate",
                            "Phrase: no verb"], label="Clauses and sentence types"),
            "Vary the type and the writing stops sounding flat"),
 "punct": (F(["Capitals", "Commas in a list", "Apostrophe: possession or omission",
              "Quotation marks for speech"], label="Punctuation checklist"),
           "The comma goes inside the quotation marks"),
 "voice": (F(["Object becomes subject", "Add the right form of BE",
              "Past participle", "'by' the doer, or drop it"], label="Active → passive"),
           "Keep the tense exactly as it was"),
}

FIGS["bscience"] = {
 "repro": (F(["Childhood", "Adolescence: rapid growth, hormones",
              "Good hygiene, diet, sleep", "Responsible choices"],
             label="Growing up"), "Every change is normal, and timing differs from person to person"),
 "tech": (F(["Science finds out how", "Technology builds with it",
             "Mobile money, solar, vaccines", "Manage the cost: e-waste, safety"],
            label="Science into technology"), "Useful only when it is maintained and understood"),
}
