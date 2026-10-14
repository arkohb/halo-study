"""BECE Integrated Science - Forces and energy; Humans and the environment."""
from core import *
import draw

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}
D, F = "D. Forces & energy", "E. Humans & the environment"

# ------------------------------------------------------------------ energy
topic("energy", "Energy, its forms & transformation", D, [
  "Energy is the ability to do work; its unit is the <b>joule (J)</b>.",
  "Forms: heat, light, sound, electrical, chemical, mechanical (kinetic and potential), nuclear and solar.",
  "Energy can be changed from one form to another but cannot be created or destroyed "
  "(the law of conservation of energy).",
  "Examples of transformation: a torch — chemical → electrical → light and heat; a fan — electrical → mechanical; "
  "a solar panel — solar → electrical; a loudspeaker — electrical → sound.",
  "<b>Renewable</b> sources never run out: solar, wind, water (hydro), biomass. "
  "<b>Non-renewable</b> sources are used up: coal, crude oil, natural gas.",
])
O("The unit of energy is the",
  ["joule", "newton", "watt", "ampere"],
  ["The newton measures force, the watt power and the ampere current.", "Energy is measured in <b>joules</b>."],
  ok=True)
O("In an electric fan, electrical energy is changed mainly into",
  ["mechanical energy", "chemical energy", "light energy", "nuclear energy"],
  ["The blades turn, which is movement.",
   "So electrical energy becomes <b>mechanical (kinetic) energy</b>, with a little heat and sound."],
  ok=True)
O("Which of the following is a renewable source of energy?",
  ["Wind", "Coal", "Crude oil", "Natural gas"],
  ["Coal, oil and gas are fossil fuels and will be used up.",
   "<b>Wind</b> keeps blowing, so it is renewable."],
  ok=True)
O("The energy change that takes place in a dry cell in use is",
  ["chemical to electrical", "electrical to chemical",
   "light to electrical", "heat to mechanical"],
  ["A dry cell contains chemicals that react when the circuit is closed.",
   "The change is <b>chemical to electrical</b>."],
  ok=True)
O("A stone held high above the ground possesses",
  ["potential energy", "kinetic energy", "sound energy", "chemical energy"],
  ["It is not moving, so it has no kinetic energy yet, but it can do work when released.",
   "Energy stored because of position is <b>potential energy</b>."],
  ok=True)
T("(a) State the law of conservation of energy. (b) Name the energy changes that take place when a girl switches on an "
  "electric lamp powered by a solar panel. (c) Give two advantages and one disadvantage of solar energy in Ghana.",
  ["(a) <b>Energy can neither be created nor destroyed; it can only be changed from one form to another.</b>",
   "(b) <b>Solar (light) energy → electrical energy</b> (in the panel) <b>→ light energy and heat energy</b> (in the lamp).",
   "(c) Advantages: it is <b>renewable and free once installed</b>, and it <b>causes no air pollution</b>; it also "
   "reaches villages that the national grid has not. "
   "Disadvantage: it <b>works only in daylight</b> (so batteries are needed at night) and the equipment is expensive to buy."],
  marks=9, fig=draw.flow(["Sunlight (solar)", "Solar panel → electrical", "Lamp → light + heat"],
                         label="Energy changes in a solar lamp"))
extras("energy",
  plain="Energy is never used up — it only changes form. When you say a battery is 'dead', its chemical energy has simply "
        "become electrical, then light, heat and sound, and finally spread out as warmth in the room. Tracking those changes is what most exam questions ask.",
  examples=[
    E("Trace the energy changes when a boy eats kenkey and then climbs a hill.",
      "Step 1. The food holds chemical energy, released by respiration in his cells.",
      "Step 2. His muscles convert it into mechanical (kinetic) energy as he walks, plus heat.",
      "Step 3. As he rises, that becomes <b>potential energy stored because of his height</b>."),
    E("Why is a hydro dam described as a renewable energy source?",
      "Step 1. The dam uses falling water to turn turbines.",
      "Step 2. The water is replaced by rain through the water cycle, driven by the sun.",
      "Step 3. Since the supply <b>renews itself naturally</b>, it is a renewable source — unlike the diesel in a generator.")])

# ------------------------------------------------------------------ heat
topic("heat", "Heat & temperature", D, [
  "<b>Heat</b> is a form of energy that flows from a hotter to a colder body; "
  "<b>temperature</b> is the degree of hotness, measured in °C.",
  "Heat travels by <b>conduction</b> (through solids, particle to particle), <b>convection</b> (in liquids and gases, "
  "by the movement of the fluid itself) and <b>radiation</b> (in straight lines, needing no material at all).",
  "Metals are good conductors; wood, plastic, air, water and cloth are poor conductors (insulators).",
  "Heating makes most substances <b>expand</b> and cooling makes them contract. "
  "That is why gaps are left between railway lines and in bridges.",
  "Dark, dull surfaces absorb and emit radiation well; shiny, light surfaces reflect it — "
  "which is why a flask is silvered and why light clothing is cooler in the sun.",
])
O("Heat travels from the sun to the earth by",
  ["radiation", "conduction", "convection", "evaporation"],
  ["Space is almost empty, so there are no particles to carry heat by conduction or convection.",
   "Heat reaches us by <b>radiation</b>."],
  ok=True)
O("The transfer of heat through a metal spoon placed in hot soup is by",
  ["conduction", "convection", "radiation", "insulation"],
  ["The particles of the metal vibrate and pass energy on to their neighbours.",
   "That is <b>conduction</b>."],
  ok=True)
O("Which of the following is a poor conductor of heat?",
  ["Wood", "Copper", "Aluminium", "Iron"],
  ["Copper, aluminium and iron are metals and conduct well.",
   "<b>Wood</b> is a poor conductor, which is why cooking spoons are made of it."],
  ok=True)
O("Gaps are left between sections of a concrete bridge because the concrete",
  ["expands when heated", "contracts when heated", "absorbs water", "becomes lighter in the sun"],
  ["In the heat of the day the sections become longer.",
   "The gaps allow for this, since the concrete <b>expands when heated</b> and would crack or buckle without room to move."],
  ok=True)
O("A vacuum flask keeps liquids hot mainly because the vacuum",
  ["prevents conduction and convection", "prevents radiation",
   "makes the liquid boil", "reflects sound"],
  ["There are no particles in the vacuum to carry heat from one wall to the other.",
   "So the vacuum <b>prevents conduction and convection</b>, while the silvered surfaces deal with radiation."],
  ok=True)
T("(a) State two differences between heat and temperature. (b) Describe an experiment to show that water is a poor "
  "conductor of heat. (c) Explain why it is more comfortable to wear white clothes than black clothes on a sunny day.",
  ["(a) Heat is a <b>form of energy</b> and is measured in <b>joules</b>; temperature is the <b>degree of hotness</b> "
   "and is measured in <b>degrees Celsius</b>. A cup and a bucket of water at the same temperature contain very "
   "different amounts of heat.",
   "(b) Hold a test tube of water at an angle and heat it <b>near the top</b>, with a small piece of ice held down at "
   "the bottom by a piece of gauze. <b>The water at the top boils while the ice at the bottom takes a long time to "
   "melt</b>, showing that water conducts heat very poorly.",
   "(c) White surfaces <b>reflect</b> most of the radiation falling on them, while black surfaces <b>absorb</b> it. "
   "So less of the sun's heat reaches the body through white clothing, and the wearer feels cooler."],
  marks=10, fig=draw.flow(["CONDUCTION: through solids, particle to particle",
                           "CONVECTION: moving liquids and gases",
                           "RADIATION: straight lines, no material needed"], label="Three ways heat travels"))
extras("heat",
  plain="Heat always flows the same way: from hot to cold, never the other way. The three methods are easy to tell apart "
        "by what carries the heat — a solid (conduction), a moving fluid (convection) or nothing at all (radiation).",
  examples=[
    E("Why does a ceiling fan help on a hot day, even though it does not cool the air?",
      "Step 1. The fan sets the air moving across your skin.",
      "Step 2. Moving air carries away the warm, moist layer next to your skin and speeds up evaporation of sweat.",
      "Step 3. Evaporation takes heat from your body, so <b>you feel cooler although the room temperature is unchanged</b>."),
    E("Why is the freezing compartment placed at the TOP of a refrigerator?",
      "Step 1. Air cooled by the freezer becomes denser and sinks.",
      "Step 2. Warmer air from below rises to take its place and is cooled in turn.",
      "Step 3. This <b>convection current</b> cools the whole fridge — which would not happen if the freezer were at the bottom.")])

# ------------------------------------------------------------------ light
topic("light", "Light", D, [
  "Light travels in <b>straight lines</b> and very fast. It is a form of energy we can see with.",
  "An opaque object blocks light and forms a shadow; translucent objects let some light through; "
  "transparent objects let light pass clearly.",
  "<b>Reflection</b>: the angle of incidence equals the angle of reflection. "
  "A plane mirror gives an image that is the same size, upright, laterally inverted, as far behind the mirror "
  "as the object is in front, and virtual.",
  "<b>Refraction</b> is the bending of light as it passes from one medium to another. "
  "It makes a stick in water look bent and a pool look shallower than it is.",
  "White light is a mixture of seven colours, which a prism separates: red, orange, yellow, green, blue, indigo, violet. "
  "A rainbow is formed in the same way by raindrops.",
])
O("The image formed in a plane mirror is",
  ["virtual and laterally inverted", "real and inverted",
   "real and magnified", "virtual and upside down"],
  ["The image cannot be caught on a screen, and left and right appear swapped.",
   "So it is <b>virtual and laterally inverted</b> — and the same size as the object."],
  ok=True)
O("The bending of light as it passes from air into water is called",
  ["refraction", "reflection", "dispersion", "diffraction"],
  ["Light changes speed when it enters a denser medium, and so changes direction.",
   "That bending is <b>refraction</b>."],
  ok=True)
O("A ray of light strikes a plane mirror at an angle of incidence of 30°. The angle of reflection is",
  ["30°", "60°", "15°", "90°"],
  ["The law of reflection states that the angle of incidence equals the angle of reflection.",
   "So the angle of reflection is <b>30°</b>."],
  v=30)
O("The separation of white light into its seven colours by a prism is called",
  ["dispersion", "reflection", "refraction", "absorption"],
  ["Each colour is refracted by a slightly different amount, so they spread out.",
   "The spreading is called <b>dispersion</b>."],
  ok=True)
O("Shadows are formed because light",
  ["travels in straight lines", "travels very fast",
   "can be reflected", "is a form of energy"],
  ["If light could bend round an object there would be no sharp shadow.",
   "Shadows prove that light <b>travels in straight lines</b>."],
  ok=True)
T("(a) State the two laws of reflection of light. (b) List four properties of the image formed by a plane mirror. "
  "(c) Explain why a pencil placed in a glass of water appears bent at the surface.",
  ["(a) First law: <b>the incident ray, the reflected ray and the normal at the point of incidence all lie in the same "
   "plane</b>. Second law: <b>the angle of incidence equals the angle of reflection</b>.",
   "(b) The image is <b>the same size as the object</b>; <b>as far behind the mirror as the object is in front</b>; "
   "<b>upright but laterally inverted</b>; and <b>virtual</b> (it cannot be formed on a screen).",
   "(c) Light from the part of the pencil under the water is <b>refracted</b> as it passes from water into air, because "
   "it speeds up and changes direction. The eye traces the rays back in straight lines, so that part of the pencil "
   "appears to be in a different place — and the pencil looks bent at the water surface."],
  marks=10, fig=draw.raysfig("reflect", label="Reflection at a plane mirror"))
extras("light",
  plain="Almost everything about light follows from one fact: it travels in straight lines. Shadows, pinhole cameras, "
        "eclipses and the laws of reflection are all consequences of it. Refraction is the one case where the line changes direction — when the light changes speed.",
  examples=[
    E("A girl stands 2 m in front of a plane mirror. How far is she from her image?",
      "Step 1. The image is as far behind the mirror as the object is in front: 2 m behind.",
      "Step 2. The distance from the girl to her image is 2 m + 2 m.",
      "Step 3. = <b>4 m</b>."),
    E("Why do the letters on an ambulance appear reversed when written on the front?",
      "Step 1. Drivers ahead see the ambulance in their rear-view mirror.",
      "Step 2. A plane mirror reverses left and right (lateral inversion).",
      "Step 3. So the word is <b>painted reversed, in order to read correctly in the mirror</b>.")])

# ------------------------------------------------------------------ sound
topic("sound", "Sound", D, [
  "Sound is produced by <b>vibrating</b> objects and travels as a wave through a material medium "
  "(solid, liquid or gas). It cannot travel through a vacuum.",
  "Sound travels fastest in solids, more slowly in liquids and slowest in gases. "
  "In air it travels at about 330–340 m/s — far slower than light.",
  "<b>Pitch</b> depends on frequency (how fast the vibration is); <b>loudness</b> depends on amplitude "
  "(how big the vibration is).",
  "An <b>echo</b> is sound reflected from a hard surface. Soft materials absorb sound, which is why a room with "
  "curtains has little echo.",
  "Noise pollution harms hearing, disturbs sleep and interferes with study. It is reduced by silencers on vehicles, "
  "planting trees, siting factories away from homes, and lowering the volume of loudspeakers.",
])
O("Sound is produced by",
  ["vibrating objects", "hot objects", "moving air only", "reflecting surfaces"],
  ["Pluck a string or strike a drum and you can see or feel the movement.",
   "Sound is produced by <b>vibrating objects</b>."],
  ok=True)
O("Sound cannot travel through",
  ["a vacuum", "water", "steel", "air"],
  ["Sound needs particles to pass the vibration along.",
   "A <b>vacuum</b> has no particles, so sound cannot travel through it — which is why space is silent."],
  ok=True)
O("In which medium does sound travel fastest?",
  ["A solid", "A liquid", "A gas", "A vacuum"],
  ["The closer the particles, the faster the vibration is handed on.",
   "So sound travels fastest in <b>a solid</b> such as steel."],
  ok=True)
O("The loudness of a sound depends on its",
  ["amplitude", "frequency", "wavelength", "speed"],
  ["Frequency decides the pitch — how high or low the note is.",
   "Loudness depends on the <b>amplitude</b>, the size of the vibration."],
  ok=True)
O("A boy shouts towards a cliff and hears the echo 2 seconds later. If sound travels at 340 m/s, how far away is the cliff?",
  ["340 m", "680 m", "170 m", "1 360 m"],
  ["In 2 s the sound travels to the cliff and back: distance = 340 × 2 = 680 m.",
   "That is the journey there and back, so the cliff is 680 ÷ 2 = <b>340 m</b> away."],
  v=340 * 2 / 2, nv=[340, 680, 170, 1360])
T("(a) State two differences between sound and light. (b) Describe an experiment to show that sound needs a material "
  "medium to travel. (c) State three effects of noise pollution and two ways of reducing it.",
  ["(a) Sound needs a <b>material medium</b> and cannot travel through a vacuum, while light travels through a vacuum. "
   "Sound travels at about <b>340 m/s in air</b>, while light travels at about <b>300 000 000 m/s</b> — which is why "
   "lightning is seen before thunder is heard.",
   "(b) Place a ringing electric bell inside a bell jar connected to a vacuum pump. The bell is heard clearly at first. "
   "As the air is pumped out, <b>the sound grows fainter and finally cannot be heard, although the hammer is still seen "
   "striking</b>. Letting the air back in brings the sound back — so sound needs a medium.",
   "(c) Effects: <b>damage to hearing</b> (even deafness after long exposure); <b>loss of sleep and rest</b>; "
   "<b>difficulty in concentrating, so school work suffers</b>; it also raises stress and blood pressure. "
   "Reduction: <b>fit silencers to vehicles and machines</b>; <b>plant trees as a sound barrier and keep loudspeaker "
   "volumes low, especially at night</b>."],
  marks=11)
extras("sound",
  plain="Sound is a vibration passed from particle to particle, which is why it dies out in a vacuum while light carries "
        "on. Two words worth keeping apart: pitch (how high the note is — frequency) and loudness (how strong it is — amplitude).",
  examples=[
    E("Why do you see lightning before you hear the thunder?",
      "Step 1. Both start at the same moment in the same place.",
      "Step 2. Light travels at about 300 000 km/s; sound at only about 340 m/s.",
      "Step 3. So <b>the light arrives almost instantly while the sound takes about 3 seconds for every kilometre</b>."),
    E("A girl claps her hands 85 m from a wall. How long before she hears the echo? (Speed of sound = 340 m/s)",
      "Step 1. The sound travels to the wall and back: 85 × 2 = 170 m.",
      "Step 2. Time = distance ÷ speed = 170 ÷ 340.",
      "Step 3. = <b>0.5 seconds</b>.")])

# ------------------------------------------------------------------ electricity
topic("elec", "Electricity & magnetism", D, [
  "An electric current is a flow of charge. It flows only in a <b>complete (closed) circuit</b>.",
  "Circuit parts: cell or battery (supplies energy), switch (completes or breaks the circuit), "
  "lamp or other appliance (uses the energy), connecting wires, fuse (safety).",
  "<b>Series</b>: components in one loop — the same current passes through each, and if one lamp fails all go out. "
  "<b>Parallel</b>: separate branches — each works on its own, which is how house wiring is done.",
  "Conductors (metals, graphite, salt solution) let current pass; insulators (rubber, plastic, dry wood, glass) do not.",
  "A magnet attracts iron, steel, cobalt and nickel. Like poles repel and unlike poles attract. "
  "A current in a coil makes an <b>electromagnet</b>, used in bells, relays and cranes.",
  "Safety: never touch switches with wet hands, use the correct fuse, earth metal appliances, and do not overload a socket.",
])
O("For an electric current to flow, the circuit must be",
  ["complete", "made of copper only", "connected to a magnet", "exposed to light"],
  ["If there is any break — a gap, an open switch, a loose wire — the current stops.",
   "The circuit must be <b>complete</b>."],
  ok=True)
O("Which of the following is an insulator?",
  ["Rubber", "Copper", "Graphite", "Salt solution"],
  ["Copper and graphite conduct, and salt solution conducts because of its ions.",
   "<b>Rubber</b> does not conduct, which is why it covers electrical wires."],
  ok=True)
O("In a series circuit of three lamps, one lamp burns out. What happens to the others?",
  ["They all go off", "They burn more brightly", "They are unaffected", "Only one goes off"],
  ["A series circuit is a single loop, so a break anywhere stops the current everywhere.",
   "<b>They all go off</b> — which is why houses are wired in parallel instead."],
  ok=True)
O("When the north pole of one magnet is brought near the north pole of another, they",
  ["repel each other", "attract each other", "lose their magnetism", "become electromagnets"],
  ["Like poles repel; unlike poles attract.", "Two north poles <b>repel each other</b>."],
  ok=True)
O("The main purpose of a fuse in a circuit is to",
  ["melt and break the circuit when the current is too large", "increase the current",
   "store electrical energy", "change the direction of the current"],
  ["A fuse is a thin wire designed to be the weakest point.",
   "It <b>melts and breaks the circuit when the current is too large</b>, protecting the appliance and preventing fire."],
  ok=True)
T("(a) Draw a simple circuit diagram containing a cell, a switch and two lamps in parallel. "
  "(b) State two differences between a series and a parallel arrangement. "
  "(c) Describe how you would make an electromagnet, and give two of its uses. "
  "(d) State two safety precautions in the use of electricity at home.",
  ["(a) The diagram shows the cell and switch in the main line, with the two lamps on separate branches side by side.",
   "(b) In <b>series</b> there is one path, the same current flows through every component, and a break stops them all. "
   "In <b>parallel</b> there are several paths, the current divides between them, and each branch works independently.",
   "(c) Wind insulated copper wire closely round an iron nail and connect the ends to a cell through a switch. "
   "When the switch is closed the nail becomes a magnet and picks up pins; when it is opened the magnetism disappears. "
   "Uses: <b>electric bells</b>, <b>relays and circuit breakers</b>, <b>cranes for lifting scrap iron</b>, loudspeakers.",
   "(d) Any two of: <b>never touch switches or appliances with wet hands</b>; <b>use the correct fuse rating</b>; "
   "<b>do not overload a socket with many appliances</b>; <b>replace worn or frayed cables</b>; <b>earth metal appliances</b>."],
  marks=12, fig=draw.circuitfig(label="A simple circuit"))
extras("elec",
  plain="Electricity is a flow, so it needs an unbroken path — that one idea explains switches, fuses and why a loose wire "
        "stops everything. Magnetism and electricity are linked: a current always makes a magnetic field, which is what makes bells, motors and cranes possible.",
  examples=[
    E("Why are the lights in a house wired in parallel rather than in series?",
      "Step 1. In series, one blown bulb breaks the only path and everything goes dark.",
      "Step 2. In parallel, each lamp has its own path from the supply.",
      "Step 3. So <b>each lamp can be switched on and off on its own, and one failing does not affect the others</b>."),
    E("A pupil connects a cell to a torch bulb with a piece of dry thread instead of wire. The bulb does not light. Why?",
      "Step 1. For a current to flow, the whole path must be made of conductors.",
      "Step 2. Dry thread is an insulator.",
      "Step 3. <b>No current can flow through the thread, so the circuit is effectively broken</b> and the bulb stays dark.")])

# ------------------------------------------------------------------ force & motion
topic("force", "Force & motion", D, [
  "A force is a push or a pull, measured in <b>newtons (N)</b> with a spring balance. "
  "It can change the shape, speed or direction of a body.",
  "Types: gravitational, frictional, magnetic, electrostatic, muscular, upthrust, tension.",
  "<b>Mass</b> is the amount of matter in a body (kg) and does not change with place. "
  "<b>Weight</b> is the pull of gravity on that mass (N) and changes with place. Weight = mass × 10 (on earth).",
  "<b>Friction</b> opposes motion. It is useful for walking, writing and braking, but wastes energy and wears parts. "
  "It is reduced by oil, grease, ball bearings and smooth surfaces.",
  "Pressure = force ÷ area. A sharp knife and a thin heel exert great pressure because the area is small; "
  "a tractor's wide tyres reduce pressure so it does not sink.",
])
O("The unit of force is the",
  ["newton", "joule", "kilogram", "watt"],
  ["The kilogram measures mass and the joule energy.", "Force is measured in <b>newtons</b>."],
  ok=True)
O("Calculate the weight of a boy of mass 50 kg. [Take g = 10 N/kg]",
  ["500 N", "50 N", "5 N", "5 000 N"],
  ["Weight = mass × g = 50 × 10.", "= <b>500 N</b>."],
  v=50 * 10, nv=[500, 50, 5, 5000])
O("Which of the following is a use of friction?",
  ["Walking without slipping", "Wearing out of tyres",
   "Loss of energy in machines", "Overheating of engines"],
  ["The last three are disadvantages of friction.",
   "<b>Walking without slipping</b> is only possible because of friction between shoe and ground."],
  ok=True)
O("A force of 200 N acts on an area of 4 m². Calculate the pressure.",
  ["50 N/m^{2}", "800 N/m^{2}", "204 N/m^{2}", "0.02 N/m^{2}"],
  ["Pressure = force ÷ area = 200 ÷ 4.", "= <b>50 N/m²</b>."],
  v=200 / 4, nv=[50, 800, 204, 0.02])
O("The mass of an object taken to the moon",
  ["remains the same", "becomes smaller", "becomes larger", "becomes zero"],
  ["Mass is the quantity of matter in the body and does not depend on gravity.",
   "So the mass <b>remains the same</b>, although the weight becomes less because the moon's gravity is weaker."],
  ok=True)
T("(a) State three differences between mass and weight. (b) Give two advantages and two disadvantages of friction. "
  "(c) Explain why a nail driven into wood goes in point first rather than head first.",
  ["(a) Mass is the <b>quantity of matter</b>, measured in <b>kilograms</b> with a beam balance, and is the "
   "<b>same everywhere</b>. Weight is the <b>force of gravity</b> on the body, measured in <b>newtons</b> with a spring "
   "balance, and <b>changes from place to place</b>.",
   "(b) Advantages: it allows us to <b>walk and grip things</b>, and it lets <b>brakes stop a vehicle</b>. "
   "Disadvantages: it <b>wastes energy as heat</b>, and it <b>wears out moving parts</b> such as tyres and bearings.",
   "(c) Pressure = force ÷ area. The point has a <b>very small area</b>, so the same hammer blow produces a very "
   "<b>large pressure</b> at the tip, enough to push the wood fibres apart. The head has a large area, so the same force "
   "gives a small pressure and the nail would not enter."],
  marks=10)
extras("force",
  plain="Force changes things: it starts motion, stops it, or changes shape or direction. Two formulas carry most of the "
        "marks — weight = mass × 10, and pressure = force ÷ area. The second explains knives, nails, high heels and tractor tyres.",
  examples=[
    E("Why does a tractor have very wide tyres?",
      "Step 1. The tractor is heavy, so the downward force is large.",
      "Step 2. Pressure = force ÷ area, so a bigger area gives a smaller pressure.",
      "Step 3. Wide tyres spread the weight, so <b>the pressure on the soft ground is low and the tractor does not sink</b>."),
    E("An astronaut has a mass of 70 kg. Find her weight on earth (g = 10 N/kg) and say what happens to it on the moon.",
      "Step 1. Weight on earth = 70 × 10 = <b>700 N</b>.",
      "Step 2. The moon's gravity is about one sixth of the earth's.",
      "Step 3. Her weight there would be about <b>117 N</b>, but her <b>mass is still 70 kg</b>.")])

# ------------------------------------------------------------------ environment
topic("envcare", "Pollution & caring for the environment", F, [
  "<b>Air pollution</b>: smoke from vehicles, factories and burning refuse; it causes chest diseases and acid rain. "
  "Carbon dioxide and other greenhouse gases cause global warming.",
  "<b>Water pollution</b>: sewage, refuse, farm chemicals and <i>galamsey</i> (illegal small-scale mining) that fills "
  "rivers with mud and mercury. It spreads disease and kills fish.",
  "<b>Land pollution</b>: plastic waste, refuse dumps and chemicals. Plastic does not decay, blocks gutters "
  "and causes flooding.",
  "Deforestation (for timber, farming and charcoal) causes soil erosion, drying of streams and loss of wildlife. "
  "The answer is afforestation — planting trees — and the use of improved stoves and gas instead of charcoal.",
  "The three Rs: <b>reduce, reuse, recycle</b>. Separate waste, compost organic waste, and never burn plastic.",
])
O("Which of the following is a cause of air pollution?",
  ["Burning refuse in the open", "Planting trees along roads",
   "Sweeping the compound", "Fetching water from a borehole"],
  ["Burning releases smoke and poisonous gases into the air.",
   "So <b>burning refuse in the open</b> pollutes the air."],
  ok=True)
O("Illegal small-scale mining (galamsey) harms rivers mainly by",
  ["filling them with mud and mercury", "making them flow faster",
   "cooling the water", "increasing the number of fish"],
  ["Washing ore in or near the river releases silt and the mercury used to extract the gold.",
   "So galamsey <b>fills rivers with mud and mercury</b>, making the water unsafe and killing fish."],
  ok=True)
O("A major effect of cutting down forests is",
  ["soil erosion", "more rainfall", "cooler temperatures", "deeper soil"],
  ["Tree roots bind the soil and the canopy breaks the force of the rain.",
   "Without them, rain washes the topsoil away: <b>soil erosion</b>."],
  ok=True)
O("Which of these wastes does NOT decay easily and so should be recycled?",
  ["Plastic bottles", "Cassava peels", "Dry leaves", "Food remains"],
  ["Peels, leaves and food remains rot and can be composted.",
   "<b>Plastic bottles</b> remain for many years, so they must be reused or recycled."],
  ok=True)
O("The best way for a community to reduce flooding caused by waste is to",
  ["stop dumping refuse in gutters and drains", "build higher walls",
   "cut down the trees along the river", "dig deeper pit latrines"],
  ["Blocked drains cannot carry away storm water.",
   "So the community should <b>stop dumping refuse in gutters and drains</b>, and clear them regularly."],
  ok=True)
T("(a) Define pollution. (b) State three effects of water pollution in your community. "
  "(c) Describe four things pupils in your school can do to protect the environment. "
  "(d) Explain the meaning of the three Rs.",
  ["(a) <b>Pollution is the addition of harmful substances to the environment — air, water or land — in amounts that "
   "damage living things.</b>",
   "(b) Any three of: <b>outbreaks of cholera, typhoid and diarrhoea</b>; <b>death of fish and other water life</b>, so "
   "fishermen lose their living; <b>water becomes expensive to treat</b> or unusable; <b>crops irrigated with it may be "
   "contaminated</b>.",
   "(c) <b>Plant and care for trees</b> on the school compound; <b>keep separate bins and compost the organic waste</b>; "
   "<b>stop using single-use plastic bags and pick up litter</b>; <b>clear the gutters and remove stagnant water</b>; "
   "form an environment club and teach the community.",
   "(d) <b>Reduce</b> — use less in the first place, for example refusing an unnecessary plastic bag. "
   "<b>Reuse</b> — use the same item again, such as refilling a water bottle. "
   "<b>Recycle</b> — send materials such as plastic, metal and paper to be made into new products."],
  marks=12, fig=draw.cyclefig(["Reduce", "Reuse", "Recycle"], centre="WASTE", label="The three Rs"))
extras("envcare",
  plain="Every environmental problem in this topic is caused by people, which means people can solve it. The science is "
        "simple cause and effect: remove the trees and the soil goes; block the gutter and the town floods; wash ore in the river and the water is poisoned.",
  examples=[
    E("A town's gutters are choked with plastic. Explain, step by step, how this leads to malaria.",
      "Step 1. The blocked gutters hold water instead of carrying it away.",
      "Step 2. Still water is exactly where the Anopheles mosquito lays its eggs.",
      "Step 3. The larvae develop into adults that bite people, so <b>malaria cases rise</b> — and the same still water also breeds cholera risk when it floods."),
    E("Why is planting trees described as the cheapest way to fight global warming?",
      "Step 1. Global warming is driven by excess carbon dioxide in the air.",
      "Step 2. Trees absorb carbon dioxide during photosynthesis and lock the carbon in wood.",
      "Step 3. So <b>every growing tree removes CO₂ at no cost</b>, besides shading the soil and reducing erosion.")])

# ------------------------------------------------------------------ science, technology & society
topic("tech", "Science, technology & society", F, [
  "Technology is the use of scientific knowledge to solve practical problems.",
  "In the home: refrigerators preserve food, gas stoves and improved cook-stoves save fuel, "
  "mobile phones and radio carry information, solar lamps light homes off the grid.",
  "In agriculture: tractors, irrigation pumps, improved seeds, fertilisers and storage silos raise food production.",
  "In health: vaccines, X-rays, laboratory tests and treated nets save lives.",
  "Technology brings problems too: pollution, electronic waste, accidents, loss of some jobs and over-use of screens. "
  "Used wisely — with safety rules, maintenance and proper disposal — the benefits are far greater.",
])
O("Technology may best be described as",
  ["the application of scientific knowledge to solve practical problems",
   "the orderly study of nature to find out how and why things happen",
   "the collection and recording of accurate measurements in the laboratory",
   "the use of computers and the internet in offices and schools"],
  ["Science finds out how things work; technology puts that knowledge to use.",
   "So technology is <b>the application of scientific knowledge to solve practical problems</b>."],
  ok=True)
O("Which of the following has most improved the preservation of food in the home?",
  ["The refrigerator", "The radio", "The electric fan", "The torch"],
  ["Cooling slows down the growth of the bacteria and fungi that spoil food.",
   "So the <b>refrigerator</b> has most improved food preservation."],
  ok=True)
O("The use of irrigation in farming makes it possible to",
  ["grow crops in the dry season", "harvest without weeding",
   "grow crops without soil", "stop all pests"],
  ["Irrigation supplies water when the rains fail or stop.",
   "So farmers can <b>grow crops in the dry season</b> and get more than one harvest a year."],
  ok=True)
O("One disadvantage of technology is",
  ["increased pollution of the environment", "faster communication",
   "better medical care", "higher food production"],
  ["The other three are benefits.",
   "<b>Increased pollution of the environment</b> — including electronic waste — is a real disadvantage that must be managed."],
  ok=True)
O("Which technology has done most to reduce deaths from malaria in Ghana?",
  ["Insecticide-treated nets and rapid test kits", "Television sets",
   "Motorbikes", "Electric fans"],
  ["Nets prevent bites and rapid tests allow early, correct treatment.",
   "So <b>insecticide-treated nets and rapid test kits</b> have had the greatest effect."],
  ok=True)
T("(a) State the difference between science and technology. (b) Give three ways in which technology has improved "
  "health care in Ghana. (c) State two problems created by technology and suggest how each can be reduced.",
  ["(a) <b>Science</b> is the organised study of the natural world to find out how and why things happen; "
   "<b>technology</b> is the use of that knowledge to make tools, machines and methods that solve practical problems.",
   "(b) Any three of: <b>vaccines</b> prevent diseases such as measles and polio; <b>X-rays and scans</b> allow doctors "
   "to see inside the body; <b>laboratory tests</b> identify diseases quickly and correctly; <b>mobile phones and "
   "ambulances</b> bring help faster; <b>refrigeration</b> keeps vaccines and blood safe.",
   "(c) Problem 1: <b>pollution and electronic waste</b> — reduce it by proper disposal and recycling centres, and by "
   "repairing rather than replacing equipment. "
   "Problem 2: <b>accidents and injuries from machines and vehicles</b> — reduce them by training operators, enforcing "
   "safety rules and maintaining equipment. (Over-use of phones, which takes time from study and sleep, is another "
   "acceptable answer, reduced by agreed limits on screen time.)"],
  marks=10)
extras("tech",
  plain="Science asks 'why?'; technology asks 'what can we build with that?'. Nearly every object in your home is a piece "
        "of technology resting on some piece of science — and each one brings benefits and costs that have to be weighed.",
  examples=[
    E("A village is given solar lamps to replace kerosene lanterns. State two scientific and two social benefits.",
      "Step 1. Scientific: the solar panel converts light energy to electrical energy, so no fuel is burnt — "
      "there is <b>no indoor smoke and no fire risk</b>.",
      "Step 2. Social: pupils can <b>study longer in the evening</b>, and families <b>save the money</b> once spent on kerosene.",
      "Step 3. The cost is the initial price of the lamps and the need to replace batteries after a few years."),
    E("Why must old mobile phones and batteries not be thrown into a refuse dump?",
      "Step 1. They contain heavy metals such as lead, cadmium and mercury.",
      "Step 2. In a dump these leak into the soil and then into groundwater.",
      "Step 3. They poison water and crops, so <b>they should be taken to a recognised collection or recycling point</b>.")])
