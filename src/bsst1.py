"""BECE Social Studies - Section A: The environment."""
from core import *
import draw

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}
A = "A. The environment"

topic("envtypes", "The environment and its components", A, [
  "The environment is everything around us — living and non-living, natural and made by people.",
  "The <b>physical (natural) environment</b>: land, water, air, climate, soil, plants and animals.",
  "The <b>human-made environment</b>: houses, roads, schools, markets, factories, dams.",
  "The <b>social environment</b>: the people around us and their customs, language, beliefs and institutions "
  "(family, school, church, mosque, chieftaincy).",
  "People depend on the environment for food, water, shelter, medicine and work — so damaging it damages ourselves.",
])
O("Which of the following belongs to the physical environment?",
  ["A river", "A school building", "A market", "A football stadium"],
  ["The other three were all built by people.", "<b>A river</b> occurs naturally, so it is part of the physical environment."],
  ok=True)
O("The customs, beliefs and language of the people around us form part of the",
  ["social environment", "physical environment", "built environment", "natural vegetation"],
  ["These are features of the people, not of the land.", "They form part of the <b>social environment</b>."],
  ok=True)
O("The main reason why human beings must protect the environment is that",
  ["we depend on it for food, water and shelter", "it looks beautiful",
   "the law says so", "tourists like to see it"],
  ["The deepest reason is survival, not appearance.",
   "<b>We depend on it for food, water and shelter</b>, so harming it harms us."],
  ok=True)
O("Which of these is an example of the human-made environment?",
  ["The Akosombo Dam", "Lake Bosomtwe", "The Kwahu Scarp", "The harmattan wind"],
  ["Lake Bosomtwe, the scarp and the harmattan are natural features.",
   "<b>The Akosombo Dam</b> was built by people."],
  ok=True)
O("The study of the environment is important to a pupil because it helps him to",
  ["use resources wisely and protect them", "pass examinations only",
   "travel to other countries", "avoid farming work"],
  ["Knowledge of the environment is meant to guide behaviour.",
   "It helps him to <b>use resources wisely and protect them</b> for the future."],
  ok=True)
T("(a) What is the environment? (b) Name the three components of the environment and give two examples of each. "
  "(c) Explain three ways in which the people of your community depend on their physical environment.",
  ["(a) <b>The environment is everything that surrounds us — natural and human-made, living and non-living — "
   "together with the people and institutions among whom we live.</b>",
   "(b) <b>Physical (natural)</b>: rivers, forests, soil, climate. "
   "<b>Human-made</b>: roads, houses, schools, dams. "
   "<b>Social</b>: the family, the school, religious bodies, the chieftaincy and the customs of the people.",
   "(c) Any three, explained: <b>farming</b> — the soil and rainfall produce the food and cash crops the community "
   "lives on; <b>water</b> — rivers, streams and boreholes supply drinking water and water for washing and irrigation; "
   "<b>building and fuel</b> — timber, bamboo, clay, sand and firewood come from the surroundings; "
   "<b>work and income</b> — fishing, mining, lumbering and tourism all depend directly on natural features."],
  marks=10, fig=draw.tree("ENVIRONMENT", ["Physical: land, water, air, plants",
                                          "Human-made: roads, houses, dams",
                                          "Social: people, customs, institutions"],
                          label="Components of the environment"))
extras("envtypes",
  plain="Social Studies begins with the environment because everything else — how we farm, where we settle, how we govern "
        "ourselves — grows out of it. Remember the three parts (physical, human-made, social) and you can answer most questions in this section.",
  examples=[
    E("A pupil says the school is part of the physical environment. Is she right?",
      "Step 1. The school <i>building</i> was put up by people, so it belongs to the human-made environment.",
      "Step 2. The school as a <i>community</i> of teachers, pupils and rules belongs to the social environment.",
      "Step 3. So she is <b>wrong on both counts</b> — the physical environment is what occurs naturally."),
    E("Explain how a bush fire affects all three components of the environment.",
      "Step 1. Physical: it destroys plants and animals, exposes the soil to erosion and dries up streams.",
      "Step 2. Human-made: it burns farms, houses and electricity poles.",
      "Step 3. Social: <b>families lose their livelihood, children drop out of school, and disputes break out</b> over the damage.")])

topic("mapping", "Ghana's position & map reading", A, [
  "Ghana lies in <b>West Africa</b>, on latitudes about 4°N to 11°N and longitudes 3°W to 1°E. "
  "The Greenwich Meridian (0°) passes through Ghana, near Tema.",
  "Neighbours: <b>Burkina Faso</b> to the north, <b>Togo</b> to the east, <b>Côte d'Ivoire</b> to the west, "
  "and the <b>Gulf of Guinea (Atlantic Ocean)</b> to the south.",
  "Ghana has 16 administrative regions, and Accra is the national capital.",
  "A map needs a <b>title</b>, a <b>key (legend)</b>, a <b>scale</b> and a <b>north arrow</b>.",
  "<b>Latitude</b> lines run east–west and measure distance north or south of the equator; "
  "<b>longitude</b> lines run north–south and measure distance east or west of Greenwich.",
])
O("Ghana shares its northern boundary with",
  ["Burkina Faso", "Togo", "Côte d'Ivoire", "Mali"],
  ["Togo is to the east and Côte d'Ivoire to the west; Ghana does not touch Mali.",
   "To the north lies <b>Burkina Faso</b>."],
  ok=True)
O("The Greenwich Meridian is a line of",
  ["longitude", "latitude", "altitude", "equator"],
  ["It runs from north to south through Greenwich in England and passes through Ghana near Tema.",
   "It is a line of <b>longitude</b>, numbered 0°."],
  ok=True)
O("Which of the following is NOT essential on a map?",
  ["The name of the person who drew it", "A key", "A scale", "A title"],
  ["Title, key, scale and north arrow are the four essentials.",
   "<b>The name of the person who drew it</b> is not essential."],
  ok=True)
O("The body of water to the south of Ghana is the",
  ["Gulf of Guinea", "Mediterranean Sea", "Indian Ocean", "Red Sea"],
  ["Ghana's southern coastline faces the Atlantic.", "That part of the Atlantic is the <b>Gulf of Guinea</b>."],
  ok=True)
O("Lines of latitude measure distance",
  ["north or south of the equator", "east or west of Greenwich",
   "above sea level", "along a coastline"],
  ["Longitude measures east and west; height is measured as altitude.",
   "Latitude measures distance <b>north or south of the equator</b>."],
  ok=True)
T("(a) State the countries that share boundaries with Ghana, naming the direction of each. "
  "(b) Name the four essential features of a map and state the use of each. "
  "(c) Give two advantages to Ghana of lying close to the equator and on the Greenwich Meridian.",
  ["(a) <b>North — Burkina Faso; East — Togo; West — Côte d'Ivoire; South — the Gulf of Guinea</b> (Atlantic Ocean).",
   "(b) <b>Title</b> — tells what the map shows. <b>Key (legend)</b> — explains the symbols used. "
   "<b>Scale</b> — allows real distances to be worked out from the map. <b>North arrow</b> — shows direction.",
   "(c) Lying near the equator gives Ghana a <b>warm climate all year and two rainy seasons in the south</b>, which "
   "supports crops such as cocoa and oil palm. Lying on the Greenwich Meridian means Ghana's time is <b>GMT</b>, which "
   "is <b>convenient for trade and communication</b> with Europe and the Americas, and the southern coastline gives "
   "access to ports for shipping."],
  marks=12, fig=draw.compass([(0, "Burkina Faso", 0.95), (90, "Togo", 0.8), (180, "Gulf of Guinea", 0.9),
                              (270, "Côte d'Ivoire", 0.8)], label="Ghana and its neighbours"))
extras("mapping",
  plain="Knowing where Ghana sits explains a great deal: the heat and rain come from being near the equator, the ports "
        "from the southern coastline, and the time zone from the Greenwich Meridian. Learn the four neighbours with their directions — that question appears again and again.",
  examples=[
    E("A map has a scale of 1 cm to 20 km. Two towns are 6.5 cm apart on the map. How far apart are they?",
      "Step 1. Each centimetre stands for 20 km.",
      "Step 2. Multiply: 6.5 × 20.",
      "Step 3. = <b>130 km</b>."),
    E("Why does Ghana not have four seasons like Europe?",
      "Step 1. The four-season pattern comes from being far from the equator, where the tilt of the earth makes a big difference.",
      "Step 2. Ghana lies between about 4°N and 11°N, so the sun is nearly overhead all year.",
      "Step 3. Temperatures stay high, and the year is divided instead into <b>wet and dry seasons</b>.")])

topic("settle", "Settlement patterns & urbanisation", A, [
  "A settlement is a place where people live. <b>Rural</b> settlements are small and depend on farming; "
  "<b>urban</b> settlements are large, with many services and non-farming work.",
  "Patterns: <b>nucleated</b> (clustered round a market, church or water point), <b>dispersed</b> (scattered farmsteads) "
  "and <b>linear</b> (strung out along a road, river or railway).",
  "Factors that decide where people settle: water supply, fertile land, security, good drainage, trade routes, "
  "minerals, and government decisions.",
  "<b>Rural–urban migration</b> is the movement of people, especially the young, from villages to towns in search of "
  "work, schooling and amenities.",
  "Effects on towns: overcrowding, slums, pressure on water and sanitation, unemployment, crime. "
  "Effects on villages: loss of labour, ageing population, farms left uncultivated.",
])
O("A settlement in which buildings are strung out along a main road is described as",
  ["linear", "nucleated", "dispersed", "circular"],
  ["Nucleated settlements cluster, and dispersed ones scatter.",
   "Buildings following a road form a <b>linear</b> settlement."],
  ok=True)
O("Which of the following is the most important factor in the siting of early settlements?",
  ["Availability of water", "Nearness to an airport",
   "Availability of electricity", "Presence of a cinema"],
  ["People cannot live without water, and the other things did not exist in early times.",
   "<b>Availability of water</b> was the key factor."],
  ok=True)
O("The movement of young people from villages to cities is called",
  ["rural–urban migration", "emigration", "urban–rural migration", "immigration"],
  ["Emigration and immigration refer to movement between countries.",
   "Movement from village to city within a country is <b>rural–urban migration</b>."],
  ok=True)
O("One effect of rural–urban migration on the villages is",
  ["shortage of farm labour", "overcrowding in the schools",
   "growth of slums", "high rent for rooms"],
  ["The last three are problems of the towns that receive the migrants.",
   "The village is left with a <b>shortage of farm labour</b>, so food production falls."],
  ok=True)
O("Which of these is a feature of an urban settlement?",
  ["Many people engaged in non-farming work", "Most people farming",
   "Houses very far apart", "No electricity or water supply"],
  ["Farming and scattered housing are rural features.",
   "In a town, <b>many people are engaged in non-farming work</b> — trade, services, industry and offices."],
  ok=True)
T("(a) State three differences between a rural and an urban settlement. "
  "(b) Give four reasons why young people migrate from villages to the cities. "
  "(c) Suggest three measures the government can take to reduce rural–urban migration.",
  ["(a) <b>Population</b>: rural settlements are small, urban ones large and dense. "
   "<b>Occupation</b>: rural people are mainly farmers and fishermen; urban people work in trade, industry and services. "
   "<b>Services</b>: towns have hospitals, banks, pipe-borne water, electricity and secondary schools, which many "
   "villages lack.",
   "(b) Any four of: <b>to look for paid work</b>; <b>to continue their education</b>; <b>to enjoy social amenities</b> "
   "such as electricity, water and entertainment; <b>to join relatives already in the city</b>; <b>to escape hard farm "
   "work or family disputes</b>; <b>to get better health care</b>.",
   "(c) <b>Provide social amenities in the rural areas</b> — water, electricity, clinics and good schools. "
   "<b>Create jobs in the villages</b> by supporting agriculture, agro-processing factories and rural credit. "
   "<b>Improve feeder roads and markets</b> so farmers can sell at good prices and need not move away. "
   "(Decentralising government offices and industries is another valid answer.)"],
  marks=12)
extras("settle",
  plain="Where people live is never an accident: water, land, security and trade decide it. The same logic explains "
        "migration today — people move towards work, schools and services, so the surest way to keep them in the villages is to put those things there.",
  examples=[
    E("Why did many old towns in Ghana grow up around markets?",
      "Step 1. A market brought traders from far around on a regular day.",
      "Step 2. Services grew to serve them — lodging, food sellers, craftsmen, later schools and clinics.",
      "Step 3. People settled permanently near that activity, so the settlement became <b>nucleated around the market</b>."),
    E("A city's water supply cannot meet demand and slums are spreading. Name the likely cause and one solution.",
      "Step 1. Rapid population growth in the city, mostly from rural–urban migration.",
      "Step 2. Services were planned for far fewer people.",
      "Step 3. Solutions: <b>expand the water and housing supply, and at the same time develop the rural areas</b> so that fewer people need to come.")])

topic("popn", "Population growth & its effects", A, [
  "Population means the number of people living in a place. Ghana conducts a <b>census</b> every ten years "
  "to count the people and collect information about them.",
  "Population grows through <b>births</b> and <b>immigration</b>, and falls through <b>deaths</b> and <b>emigration</b>.",
  "A high birth rate results from early marriage, large-family customs, low use of family planning and "
  "the wish for help on the farm.",
  "Effects of rapid growth: pressure on schools, hospitals, housing, water and land; unemployment; "
  "overcrowding; damage to the environment.",
  "Census data is used to plan schools, hospitals, roads and water supply, to share national resources, "
  "and to create constituencies.",
])
O("A census is the official counting of",
  ["the people in a country", "the money in the banks",
   "the houses in a town only", "the farms in a district"],
  ["Housing and agriculture may be counted alongside, but the central purpose is people.",
   "A census counts <b>the people in a country</b> and collects data about them."],
  ok=True)
O("In Ghana, a population census is normally conducted every",
  ["ten years", "two years", "five years", "twenty years"],
  ["The pattern of Ghana's censuses — 1960, 1970, 1984, 2000, 2010, 2021 — is roughly decennial.",
   "A census is held about every <b>ten years</b>."],
  ok=True)
O("Which of the following increases the population of a country?",
  ["Immigration", "Emigration", "A high death rate", "Family planning"],
  ["Emigration and deaths reduce the population, and family planning lowers the birth rate.",
   "<b>Immigration</b> — people coming in to settle — increases it."],
  ok=True)
O("A major effect of rapid population growth on education is",
  ["overcrowded classrooms", "fewer pupils per teacher",
   "more free textbooks", "shorter school hours"],
  ["More children arrive than the schools were built for.",
   "The result is <b>overcrowded classrooms</b>, and a shortage of teachers, desks and books."],
  ok=True)
O("Census figures are most useful to the government for",
  ["planning social services", "collecting taxes from individuals",
   "arresting criminals", "choosing a national anthem"],
  ["A census is confidential and is not used against individuals.",
   "Its main use is <b>planning social services</b> — schools, clinics, water and roads — and sharing resources fairly."],
  ok=True)
T("(a) Give three reasons why the government of Ghana conducts a population census. "
  "(b) State four effects of rapid population growth on a developing country. "
  "(c) Suggest three ways of controlling rapid population growth.",
  ["(a) <b>To plan social services</b> — to know how many schools, clinics, houses and boreholes are needed and where; "
   "<b>to share national resources fairly</b> among regions and districts, and to create constituencies; "
   "<b>to measure change</b> in the size, age and distribution of the population for future planning.",
   "(b) Any four of: <b>pressure on schools and hospitals</b>; <b>unemployment and underemployment</b>; "
   "<b>housing shortage and slums</b>; <b>pressure on land, food and water</b>; <b>environmental damage</b> through "
   "farming of marginal land and felling of forests; <b>higher government spending</b> on services, leaving less for "
   "investment.",
   "(c) <b>Education</b>, especially of girls, since educated women tend to have fewer children later in life; "
   "<b>family-planning education and services</b> made available and affordable; "
   "<b>enforcing the law on the minimum age of marriage</b> and discouraging early marriage. "
   "(Improving child health also helps, because parents who are confident their children will survive choose to have fewer.)"],
  marks=12)
extras("popn",
  plain="Population questions are about arithmetic meeting planning: if the number of children doubles but the number of "
        "classrooms stays the same, something has to give. That is why the census matters — you cannot plan for people you have not counted.",
  examples=[
    E("A district's population rises from 40 000 to 50 000 in ten years. Find the percentage increase.",
      "Step 1. Increase = 50 000 − 40 000 = 10 000.",
      "Step 2. Percentage increase = (10 000 ÷ 40 000) × 100.",
      "Step 3. = <b>25%</b> — so the district needs about a quarter more classrooms and clinics than before."),
    E("Explain why a country with many young people must invest heavily in education.",
      "Step 1. A young population means a large share of people are still at school age and not yet working.",
      "Step 2. Without school places, they grow up without the skills to find work.",
      "Step 3. Investing in education turns that large young group from <b>a burden into a productive workforce</b>.")])

topic("envprob", "Environmental problems", A, [
  "<b>Soil erosion</b>: the removal of topsoil by water or wind, worsened by overgrazing, bad farming on slopes, "
  "sand winning and the clearing of vegetation.",
  "<b>Deforestation</b>: cutting trees for timber, farming, charcoal and mining. It leads to erosion, "
  "drying of streams, loss of wildlife and hotter local climates.",
  "<b>Bush fires</b>: often started by hunters, farmers clearing land and careless smokers. "
  "They destroy crops, soil organisms, wildlife and even homes.",
  "<b>Flooding</b>: caused by choked gutters, building on waterways, poor drainage and heavy rain on bare ground.",
  "<b>Pollution and galamsey</b>: illegal small-scale mining muddies rivers and adds mercury; "
  "plastic waste blocks drains; vehicle and factory smoke pollutes the air.",
])
O("The washing away of the topsoil by running water is called",
  ["soil erosion", "leaching", "desertification", "sedimentation"],
  ["Leaching is the washing of nutrients down through the soil.",
   "The removal of the topsoil itself is <b>soil erosion</b>."],
  ok=True)
O("Which human activity contributes most to the drying up of streams in a forest area?",
  ["Felling of trees along the banks", "Fishing with nets",
   "Building a bridge", "Swimming in the stream"],
  ["Trees shade the water, hold the banks and help rain soak into the ground.",
   "<b>Felling of trees along the banks</b> therefore dries the stream and silts it up."],
  ok=True)
O("A major cause of flooding in Ghanaian cities is",
  ["dumping refuse in gutters and building on waterways", "too many trees in the city",
   "the use of boreholes", "wide tarred roads"],
  ["Water must have somewhere to go.",
   "<b>Dumping refuse in gutters and building on waterways</b> blocks its path, so it spreads into homes."],
  ok=True)
O("One effect of bush fires on the soil is that it",
  ["destroys organic matter and soil organisms", "adds nitrogen permanently",
   "makes the soil deeper", "increases the humus content"],
  ["The ash gives a brief flush of minerals, but the lasting effect is destruction.",
   "Fire <b>destroys organic matter and soil organisms</b>, leaving the soil bare and easily eroded."],
  ok=True)
O("Galamsey is harmful mainly because it",
  ["pollutes rivers and destroys farmland", "provides employment",
   "produces gold for export", "attracts tourists"],
  ["Employment and gold are the attractions that make it hard to stop, not reasons it is harmful.",
   "It is harmful because it <b>pollutes rivers and destroys farmland</b>, besides causing deadly pit collapses."],
  ok=True)
T("(a) State four causes of soil erosion in Ghana. (b) Describe three effects of deforestation. "
  "(c) Suggest four ways in which a community can reduce flooding.",
  ["(a) <b>Clearing of vegetation</b> for farming and building, leaving the soil bare; <b>farming along slopes</b> "
   "instead of across them; <b>overgrazing</b> by too many animals on one piece of land; <b>bush burning</b>; "
   "<b>sand winning and mining</b>; and heavy rain falling on unprotected ground.",
   "(b) <b>Soil erosion and loss of fertility</b>, because nothing holds the soil or shades it; "
   "<b>streams and rivers dry up or silt up</b>, so water becomes scarce; "
   "<b>loss of wildlife, timber and medicinal plants</b>, and local temperatures rise while rainfall becomes less reliable.",
   "(c) <b>Stop dumping refuse in gutters and drains, and clear them regularly.</b> "
   "<b>Stop building on waterways and demolish structures already there.</b> "
   "<b>Construct and maintain proper drains</b> in new areas. "
   "<b>Plant trees and grass and avoid paving every surface</b>, so that rain can soak in. "
   "(Community education and enforcement of by-laws support all of these.)"],
  marks=12, fig=draw.flow(["Trees cut down", "Soil left bare", "Rain washes topsoil away",
                           "Streams silt up and dry", "Crops fail, people move away"],
                          label="How deforestation leads to hardship"))
extras("envprob",
  plain="Environmental problems in Ghana share one pattern: a short-term gain for a few causes a long-term loss for "
        "everybody. Charcoal pays today and leaves bare soil tomorrow; galamsey pays today and poisons the river for a generation.",
  examples=[
    E("Explain the chain of events from bush burning to food shortage.",
      "Step 1. Fire destroys the grass, trees and soil organisms, leaving the ground bare.",
      "Step 2. The next heavy rain washes the exposed topsoil away, and nutrients go with it.",
      "Step 3. Yields fall on the poorer soil, so <b>less food is produced and prices rise</b>."),
    E("Your community wants to stop erosion on a sloping farm. Suggest two practical measures and why they work.",
      "Step 1. <b>Plant across the slope (contour ploughing)</b> — the ridges act as small barriers that slow the water.",
      "Step 2. <b>Plant cover crops or mulch the ground</b> — the leaves break the force of the raindrops and hold the soil.",
      "Step 3. Both work by the same principle: <b>keep the soil covered and slow the water down</b>.")])

topic("conserve", "Conservation of natural resources", A, [
  "Conservation means using resources wisely so that they are not destroyed and are still available for "
  "future generations.",
  "<b>Renewable</b> resources (forests, water, fish, soil, sunlight) can be replaced if managed; "
  "<b>non-renewable</b> resources (gold, bauxite, oil, manganese) cannot.",
  "Methods: afforestation and reafforestation, selective logging, controlled fishing (closed season, legal net sizes), "
  "crop rotation, terracing, recycling, and forest reserves and national parks.",
  "Institutions: the Forestry Commission, the Environmental Protection Authority (formerly the Environmental "
  "Protection Agency, renamed under the Environmental Protection Act, 2025), the Minerals Commission, "
  "the Water Resources Commission and the Wildlife Division.",
  "Every citizen has a part: plant trees, avoid bush fires, separate waste, report illegal mining and logging.",
])
O("Conservation of natural resources means",
  ["using them wisely so that they last for future generations", "locking them away and never using them",
   "selling them quickly for money", "importing them from other countries"],
  ["Conservation is not the same as non-use.",
   "It means <b>using them wisely so that they last for future generations</b>."],
  ok=True)
O("Which of the following is a non-renewable resource?",
  ["Gold", "Timber", "Fish", "Water"],
  ["Trees can be replanted, fish can breed and water is renewed by the water cycle.",
   "<b>Gold</b>, once mined, cannot be replaced, so it is non-renewable."],
  ok=True)
O("The planting of trees in an area that has never been forested is called",
  ["afforestation", "reafforestation", "deforestation", "irrigation"],
  ["Replanting where forest has been cut is reafforestation.",
   "Planting where there was no forest before is <b>afforestation</b>."],
  ok=True)
O("A closed season for fishing is used to",
  ["allow the fish to breed and increase", "give fishermen a holiday",
   "raise the price of fish", "repair the boats"],
  ["Catching fish while they are spawning destroys the next generation.",
   "A closed season <b>allows the fish to breed and increase</b>, so catches improve later."],
  ok=True)
O("The institution mainly responsible for protecting Ghana's forests is the",
  ["Forestry Commission", "Ghana Education Service",
   "Electricity Company of Ghana", "Ghana Standards Authority"],
  ["Each agency has its own mandate.", "Forests are managed by the <b>Forestry Commission</b>."],
  ok=True)
T("(a) Distinguish between renewable and non-renewable resources, giving two examples of each. "
  "(b) Describe four methods of conserving natural resources in Ghana. "
  "(c) State two roles that pupils can play in conserving the environment.",
  ["(a) <b>Renewable</b> resources can be replaced naturally or by human effort if they are not over-used — for example "
   "<b>timber</b> and <b>fish</b>. <b>Non-renewable</b> resources exist in fixed amounts and cannot be replaced once "
   "used — for example <b>gold</b> and <b>crude oil</b>.",
   "(b) <b>Afforestation and reafforestation</b> — planting trees to replace those felled. "
   "<b>Selective and controlled logging</b> — felling only mature trees, under licence. "
   "<b>Controlled fishing</b> — closed seasons, legal net sizes and a ban on light fishing and dynamite. "
   "<b>Soil conservation on farms</b> — crop rotation, mulching, contour ploughing and terracing. "
   "(Creating forest reserves and national parks, and recycling, are equally valid.)",
   "(c) Pupils can <b>plant and water trees on the school compound and at home</b>, and <b>avoid littering, separate "
   "waste and educate others</b> through an environment or wildlife club."],
  marks=12)
extras("conserve",
  plain="Conservation is the difference between harvesting and destroying. A forest cut selectively keeps producing timber "
        "for ever; a forest cleared completely produces timber once. The test to apply to any practice: will this resource still be there for the next generation?",
  examples=[
    E("A timber firm is told to practise selective logging. Explain what it must do and why.",
      "Step 1. It must fell only mature trees of approved species, marked beforehand, and leave the young ones standing.",
      "Step 2. It must also replant and avoid damaging the remaining trees when hauling logs.",
      "Step 3. This way <b>the forest regenerates and can be harvested again</b>, instead of being lost for good."),
    E("Why is recycling described as a form of conservation?",
      "Step 1. Recycling turns used material back into new products.",
      "Step 2. That means less new raw material — timber, bauxite, crude oil — has to be taken from the earth.",
      "Step 3. So recycling <b>conserves both the resource and the energy</b> needed to extract it, and reduces waste at the same time.")])

topic("culture", "Our culture & cultural practices", A, [
  "Culture is the total way of life of a people: language, dress, food, music, dance, festivals, beliefs, "
  "values, art, crafts and systems of government.",
  "Culture is <b>learned</b> (not inherited), <b>shared</b>, and it <b>changes</b> over time.",
  "<b>Positive practices</b> to be preserved: respect for elders, hospitality, communal labour (<i>nnoboa</i>), "
  "naming and puberty ceremonies that teach responsibility, festivals that unite people and attract tourists.",
  "<b>Negative practices</b> to be discouraged: forced and child marriage, female genital mutilation, "
  "witchcraft accusations, trokosi, harmful widowhood rites, and tribalism.",
  "Culture is preserved through festivals, museums and monuments, teaching of Ghanaian languages, "
  "documentation, chieftaincy and the arts.",
])
O("Culture may best be described as",
  ["the total way of life of a people", "the religion of a people",
   "the language of a people only", "the clothes people wear"],
  ["Religion, language and dress are each only a part of it.",
   "Culture is <b>the total way of life of a people</b>."],
  ok=True)
O("Which of the following shows that culture is learned and not inherited?",
  ["A Ghanaian child raised abroad speaks the language of that country",
   "A child looks very much like the parents and grandparents",
   "Members of one family often share the same blood group",
   "Children in the same family are often of about the same height"],
  ["If culture were inherited, it would pass automatically in the blood.",
   "<b>A Ghanaian child raised abroad speaks the language of that country</b>, which shows culture is learned from the people around us."],
  ok=True)
O("Which of these is a positive cultural practice?",
  ["Communal labour (nnoboa)", "Forced marriage", "Trokosi", "Harmful widowhood rites"],
  ["The other three deny people their rights and should be discouraged.",
   "<b>Communal labour (nnoboa)</b> helps members of a community work one another's farms and build together."],
  ok=True)
O("Festivals are important in Ghanaian culture because they",
  ["unite the people and preserve their history", "give people an excuse not to work",
   "raise the price of food", "replace the need for schools"],
  ["Festivals re-enact history, honour ancestors, raise funds for development and bring citizens home.",
   "So they <b>unite the people and preserve their history</b> — and they attract tourists too."],
  ok=True)
O("Which of the following is the best way of preserving Ghanaian culture?",
  ["Teaching Ghanaian languages and history in schools", "Banning all foreign films",
   "Refusing to use modern technology", "Stopping all travel abroad"],
  ["Culture is preserved by passing it on, not by shutting the world out.",
   "<b>Teaching Ghanaian languages and history in schools</b> passes the culture to the next generation."],
  ok=True)
T("(a) State three characteristics of culture. (b) Give three positive and three negative cultural practices in Ghana. "
  "(c) Explain three ways in which Ghanaian culture can be preserved.",
  ["(a) Culture is <b>learned</b> (we acquire it from the people among whom we grow up); it is <b>shared</b> by the "
   "members of the group; and it is <b>dynamic</b> — it changes over time as people meet new ideas.",
   "(b) Positive: <b>respect for the elderly</b>; <b>hospitality to strangers</b>; <b>communal labour (nnoboa)</b>; "
   "festivals and naming ceremonies that teach values. "
   "Negative: <b>forced or child marriage</b>; <b>female genital mutilation</b>; <b>harmful widowhood rites and "
   "witchcraft accusations</b>; trokosi.",
   "(c) <b>Teaching Ghanaian languages, history and culture in schools</b>, so that children learn them properly. "
   "<b>Celebrating festivals and durbars</b>, and recording them in writing, photographs and film. "
   "<b>Supporting museums, monuments and the arts</b> — kente weaving, adinkra, drumming and dance — and buying "
   "locally made goods, so the crafts survive as livelihoods."],
  marks=12)
extras("culture",
  plain="Culture is not only drumming and kente — it is also how we greet, how we settle disputes and what we think is "
        "right. Because it is learned, it can be improved: we keep what builds the community and drop what denies people their rights.",
  examples=[
    E("A practice forces a young girl to marry an older man chosen by her family. How should it be judged?",
      "Step 1. Ask what it does to the person: it ends her education and denies her choice.",
      "Step 2. It also breaks Ghanaian law, which sets 18 as the minimum age of marriage.",
      "Step 3. It is therefore a <b>negative practice that must be discouraged and reported</b>, whatever its history."),
    E("Explain how a festival such as Homowo or Aboakyer contributes to development.",
      "Step 1. Citizens living elsewhere return home, which revives family and community ties.",
      "Step 2. Money is raised at the durbar for schools, clinics and other projects.",
      "Step 3. Visitors and tourists spend in the town, so <b>traders, drivers and craftsmen all earn</b> — culture becoming income.")])

topic("family", "The family & socialisation", A, [
  "The <b>nuclear family</b> is father, mother and their children. The <b>extended family</b> adds "
  "grandparents, uncles, aunts, cousins, nephews and nieces.",
  "Ghana has <b>patrilineal</b> systems (descent traced through the father, as among the Ewe, Ga and Dagomba) "
  "and <b>matrilineal</b> systems (through the mother, as among the Akan).",
  "Functions of the family: reproduction, care and protection, feeding and shelter, education and socialisation, "
  "religious and moral training, and economic support.",
  "<b>Socialisation</b> is the process of learning the values, norms and behaviour of society. "
  "Agents: the family, the school, peer groups, religious bodies and the media.",
  "Problems of family life include poverty, broken homes, neglect of children and over-crowding; "
  "they are reduced by responsible parenthood, family planning and keeping children in school.",
])
O("A family made up of a father, a mother and their children is",
  ["a nuclear family", "an extended family", "a matrilineal family", "a polygamous family"],
  ["Adding grandparents, uncles and cousins would make it extended.",
   "Father, mother and their children alone form <b>a nuclear family</b>."],
  ok=True)
O("In a matrilineal system of inheritance, property passes through the",
  ["mother's line", "father's line", "eldest son only", "village chief"],
  ["The Akan of Ghana follow this system.", "Property and descent pass through the <b>mother's line</b>."],
  ok=True)
O("The process by which a child learns the values and norms of his society is called",
  ["socialisation", "immigration", "urbanisation", "industrialisation"],
  ["It begins in the family and continues at school and in the community.",
   "The process is <b>socialisation</b>."],
  ok=True)
O("Which of the following is NOT an agent of socialisation?",
  ["The weather", "The family", "The school", "The peer group"],
  ["Family, school and peer group all teach a child how to behave.",
   "<b>The weather</b> teaches nothing, so it is not an agent of socialisation."],
  ok=True)
O("The most important function of the family in the life of a young child is",
  ["care, protection and moral training", "providing pocket money",
   "arranging his marriage", "choosing his career"],
  ["The family is the child's first and closest institution.",
   "Its most important function is <b>care, protection and moral training</b>."],
  ok=True)
T("(a) State three differences between the nuclear and the extended family. "
  "(b) Give four functions of the family. (c) Explain three ways in which the school complements the family "
  "in socialising a child.",
  ["(a) <b>Size and membership</b>: the nuclear family is small (parents and children); the extended family is large and "
   "includes grandparents, uncles, aunts and cousins. "
   "<b>Support</b>: in the extended family many relatives share responsibility for a child; in the nuclear family the "
   "parents carry it alone. "
   "<b>Residence and decision-making</b>: the extended family may live together in a family house and decide matters "
   "jointly through an elder, while the nuclear family is independent.",
   "(b) Any four: <b>reproduction</b> — bringing children into the world; <b>care and protection</b> — food, clothing, "
   "shelter and safety; <b>socialisation</b> — teaching language, values and good behaviour; <b>economic support</b> — "
   "providing for school fees and starting capital; <b>religious and moral training</b>; and support in old age and sickness.",
   "(c) The school <b>teaches knowledge and skills the parents cannot provide</b>, such as reading, mathematics and "
   "science. It <b>teaches a child to live with people outside the family</b> — co-operation, fair play, obedience to "
   "rules and respect for other tribes and religions. It also <b>reinforces the moral values of the home</b> through "
   "discipline, worship and guidance, and it identifies and develops talents."],
  marks=12, fig=draw.tree("FAMILY", ["Nuclear: father, mother, children",
                                     "Extended: + grandparents, uncles, aunts, cousins"],
                          label="Types of family"))
extras("family",
  plain="The family is society in miniature: the first place you learn to speak, share, obey and work. That is why Social "
        "Studies starts here — a child who learns honesty and responsibility at home carries them into the school, the workplace and the nation.",
  examples=[
    E("Why is the extended family sometimes described as a social security system?",
      "Step 1. There is no automatic state support for most people who fall on hard times.",
      "Step 2. In the extended family, relatives take in orphans, support the sick and care for the aged.",
      "Step 3. So the extended family <b>does the work that insurance and pensions do elsewhere</b> — though it can also strain the earners."),
    E("A boy behaves well at home but badly at school. Which agent of socialisation is likely at work, and what should be done?",
      "Step 1. A child who behaves differently away from home is usually influenced by his companions.",
      "Step 2. The <b>peer group</b> is a powerful agent and can pull against the family's values.",
      "Step 3. Parents, teachers and the boy himself must <b>recognise the influence, keep communication open and help him choose better friends</b>.")])
