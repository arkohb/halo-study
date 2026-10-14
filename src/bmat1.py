"""BECE Mathematics - Strand A: Number (place value to everyday arithmetic)."""
from core import *
import draw
from fractions import Fraction as Fr
import sympy as sp

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}
N = "A. Number"

# ------------------------------------------------------------------ 1
topic("whole", "Whole numbers & place value", N, [
  "Each column in a number has a <b>place value</b>: units, tens, hundreds, thousands, ten thousands, hundred thousands, millions.",
  "<b>Place value</b> of a digit = what the column is worth. <b>Value</b> of the digit = digit × place value.",
  "To round: look at the digit to the <i>right</i> of the place you are rounding to. 5 or more → round up; 4 or less → leave it.",
])
O("What is the place value of 7 in 4 783 102?",
  ["Hundred thousands", "Ten thousands", "Millions", "Thousands"],
  ["Write the columns from the right: 2 units, 0 tens, 1 hundred, 3 thousands, 8 ten thousands, 7 hundred thousands, 4 millions.",
   "So 7 sits in the <b>hundred thousands</b> column."],
  ok=(4783102 // 100000 % 10 == 7))
O("Round 48 672 to the nearest thousand.",
  ["49 000", "48 000", "50 000", "48 700"],
  ["The thousands digit is 8 (48 672).", "The digit to its right is 6, and 6 is 5 or more, so round the 8 up to 9.",
   "48 672 ≈ <b>49 000</b>."],
  v=49000, nv=[49000, 48000, 50000, 48700])
O("Find the sum of the value of 5 and the value of 8 in 3 584.",
  ["580", "13", "508", "5 080"],
  ["In 3 584 the 5 is in the hundreds column, so its value is 5 × 100 = 500.",
   "The 8 is in the tens column, so its value is 8 × 10 = 80.", "500 + 80 = <b>580</b>."],
  v=580, nv=[580, 13, 508, 5080])
O("Round 0.4867 to two decimal places.",
  ["0.49", "0.48", "0.487", "0.5"],
  ["Two decimal places means we keep 0.48 and look at the next digit, which is 6.",
   "6 is 5 or more, so the 8 becomes 9: <b>0.49</b>."],
  v=0.49)
O("Which of these numbers is two million, fifty thousand and six?",
  ["2 050 006", "2 500 006", "2 050 600", "2 005 006"],
  ["Two million → 2 in the millions column.", "Fifty thousand → 5 in the ten thousands column, 0 thousands.",
   "Six → 6 units, with zeros in the hundreds and tens: <b>2 050 006</b>."],
  ok=(2050006 == 2000000 + 50000 + 6))
T("(a) Write 7 806 043 in words. (b) Round it to the nearest hundred thousand. (c) Write the value of the 8 in the number.",
  ["(a) Seven million, eight hundred and six thousand, and forty-three.",
   "(b) The hundred thousands digit is 8 and the digit after it is 0, so it stays: <b>7 800 000</b>.",
   "(c) The 8 is in the hundred thousands column, so its value is 8 × 100 000 = <b>800 000</b>."],
  marks=6, ok=(round(7806043, -5) == 7800000))
extras("whole",
  plain="Every digit in a number is worth something different depending on the column it sits in. In 352 the 3 is not "
        "just 'three' — it is three hundreds. Knowing the columns is what makes rounding, money and measurement easy.",
  examples=[
    E("In the number 6 429, what is the value of the 4?",
      "Step 1. Name the columns from the right: 9 units, 2 tens, 4 hundreds, 6 thousands.",
      "Step 2. The 4 is in the hundreds column.",
      "Step 3. Value = 4 × 100 = <b>400</b>. (Its place value is 'hundreds'; its value is 400.)"),
    E("Round 7 451 to the nearest hundred.",
      "Step 1. The hundreds digit is 4 (7 4 51).",
      "Step 2. The digit to its right is 5, which is '5 or more', so round up.",
      "Step 3. 7 451 ≈ <b>7 500</b>.")],
  fig=draw.flow(["Millions", "Hundred thousands", "Ten thousands", "Thousands", "Hundreds", "Tens", "Units"],
                label="Place value columns", note="4 783 102 → 4 | 7 | 8 | 3 | 1 | 0 | 2"))

# ------------------------------------------------------------------ 2
topic("bodmas", "Order of operations (BODMAS)", N, [
  "<b>B</b>rackets, <b>O</b>f (powers), <b>D</b>ivision, <b>M</b>ultiplication, <b>A</b>ddition, <b>S</b>ubtraction.",
  "Division and multiplication rank equally — do them left to right. The same is true of addition and subtraction.",
  "Work the innermost bracket first when brackets sit inside brackets.",
])
O("Simplify: 18 + 6 ÷ 3 × 2 − 4",
  ["18", "12", "20", "6"],
  ["Division and multiplication first, left to right: 6 ÷ 3 = 2, then 2 × 2 = 4.",
   "Now 18 + 4 − 4 = <b>18</b>."],
  v=18 + 6 / 3 * 2 - 4)
O("Simplify: 4 + 3 × (10 − 6)",
  ["16", "28", "22", "13"],
  ["Bracket first: 10 − 6 = 4.", "Then multiply: 3 × 4 = 12.", "Then add: 4 + 12 = <b>16</b>."],
  v=4 + 3 * (10 - 6))
O("Simplify: (8 + 4)^{2} ÷ 6",
  ["24", "20", "36", "144"],
  ["Bracket first: 8 + 4 = 12.", "Power next: 12² = 144.", "Divide: 144 ÷ 6 = <b>24</b>."],
  v=(8 + 4) ** 2 / 6)
O("Simplify: 20 − 2[3 + 2(4 − 1)]",
  ["2", "14", "38", "−2"],
  ["Inner bracket: 4 − 1 = 3, so 2(3) = 6.", "Square bracket: 3 + 6 = 9.", "Then 2 × 9 = 18, and 20 − 18 = <b>2</b>."],
  v=20 - 2 * (3 + 2 * (4 - 1)))
O("Simplify: 6 × 3 − 8 ÷ 2",
  ["14", "5", "20", "7"],
  ["Multiply and divide first: 6 × 3 = 18 and 8 ÷ 2 = 4.", "Then subtract: 18 − 4 = <b>14</b>."],
  v=6 * 3 - 8 / 2)
T("Simplify: 3 + 4 × (12 − 7) − 15 ÷ 5",
  ["Bracket first: 12 − 7 = 5.", "Multiplication and division next: 4 × 5 = 20 and 15 ÷ 5 = 3.",
   "Now work from the left: 3 + 20 − 3 = <b>20</b>."],
  marks=4, ok=(3 + 4 * (12 - 7) - 15 / 5 == 20))
extras("bodmas",
  plain="When a sum has several operations in it, everybody must work it in the same order, or we would all get different "
        "answers. BODMAS is that agreed order. The common mistake is working strictly from left to right — that gives the wrong answer.",
  examples=[
    E("Simplify 10 + 2 × 5.",
      "Step 1. Multiplication comes before addition, so do 2 × 5 = 10 first.",
      "Step 2. 10 + 10 = <b>20</b>.",
      "Step 3. Note that working left to right would give 12 × 5 = 60, which is wrong."),
    E("Simplify 36 ÷ (2 + 4) × 3.",
      "Step 1. Bracket: 2 + 4 = 6.",
      "Step 2. Division and multiplication rank equally, so go left to right: 36 ÷ 6 = 6.",
      "Step 3. 6 × 3 = <b>18</b>.")],
  fig=draw.flow(["Brackets", "Of (powers)", "Division", "Multiplication", "Addition", "Subtraction"],
                label="BODMAS order"))

# ------------------------------------------------------------------ 3
topic("facmul", "Factors, multiples, HCF & LCM", N, [
  "A <b>factor</b> divides a number exactly; a <b>multiple</b> is the number multiplied by 1, 2, 3, …",
  "A <b>prime number</b> has exactly two factors: 1 and itself. 1 is not prime.",
  "<b>HCF</b> = product of the common prime factors (use the smaller power). <b>LCM</b> = product of all prime factors (use the larger power).",
  "Word clue: 'at the same time again' → LCM; 'largest equal groups' → HCF.",
])
O("Find the H.C.F. of 24 and 36.",
  ["12", "6", "72", "4"],
  ["24 = 2 × 2 × 2 × 3 and 36 = 2 × 2 × 3 × 3.", "Common factors: 2 × 2 × 3 = <b>12</b>."],
  v=sp.igcd(24, 36))
O("Find the L.C.M. of 6, 8 and 12.",
  ["24", "48", "12", "96"],
  ["6 = 2 × 3,  8 = 2³,  12 = 2² × 3.", "Take the highest power of each prime: 2³ × 3 = <b>24</b>."],
  v=sp.ilcm(6, 8, 12))
O("Which of the following is a prime number?",
  ["61", "51", "57", "91"],
  ["51 = 3 × 17, 57 = 3 × 19 and 91 = 7 × 13, so all three have more than two factors.",
   "61 can only be divided by 1 and 61, so <b>61</b> is prime."],
  ok=(sp.isprime(61) and not any(sp.isprime(m) for m in (51, 57, 91))))
O("Express 84 as a product of its prime factors.",
  ["2^{2} × 3 × 7", "2 × 3^{2} × 7", "2^{2} × 21", "4 × 3 × 7"],
  ["Divide by primes: 84 ÷ 2 = 42, 42 ÷ 2 = 21, 21 ÷ 3 = 7, 7 ÷ 7 = 1.",
   "So 84 = 2 × 2 × 3 × 7 = <b>2² × 3 × 7</b>. (4 × 3 × 7 is not accepted because 4 is not prime.)"],
  ok=(sp.factorint(84) == {2: 2, 3: 1, 7: 1}))
O("What is the smallest number that both 15 and 20 divide exactly?",
  ["60", "30", "300", "45"],
  ["This is the L.C.M. 15 = 3 × 5 and 20 = 2² × 5.", "L.C.M. = 2² × 3 × 5 = <b>60</b>."],
  v=sp.ilcm(15, 20))
T("Three church bells ring at intervals of 6 minutes, 9 minutes and 12 minutes. They ring together at 6:00 a.m. "
  "(a) After how many minutes will they next ring together? (b) At what time will that be?",
  ["(a) They ring together at a time that is a multiple of 6, 9 and 12, so find the L.C.M.",
   "6 = 2 × 3,  9 = 3²,  12 = 2² × 3  →  L.C.M. = 2² × 3² = <b>36 minutes</b>.",
   "(b) 6:00 a.m. + 36 minutes = <b>6:36 a.m.</b>"],
  marks=6, ok=(sp.ilcm(6, 9, 12) == 36))
extras("facmul",
  plain="HCF and LCM both come out of prime factors. Think of HCF as 'what do they share' (it is never bigger than the "
        "numbers) and LCM as 'where do they meet' (it is never smaller than the numbers). That check alone catches most mistakes.",
  examples=[
    E("Find the HCF and LCM of 18 and 30.",
      "Step 1. Prime factors: 18 = 2 × 3 × 3 and 30 = 2 × 3 × 5.",
      "Step 2. HCF — multiply what they share: 2 × 3 = <b>6</b>.",
      "Step 3. LCM — take every prime at its highest power: 2 × 3² × 5 = <b>90</b>.",
      "Step 4. Check: HCF × LCM = 6 × 90 = 540 = 18 × 30. ✓"),
    E("A trader has 48 oranges and 60 mangoes. She wants to make identical bundles with nothing left over. "
      "What is the greatest number of bundles she can make?",
      "Step 1. 'Greatest number of equal groups' means HCF.",
      "Step 2. 48 = 2⁴ × 3,  60 = 2² × 3 × 5  →  HCF = 2² × 3 = <b>12</b>.",
      "Step 3. Each bundle then has 48 ÷ 12 = 4 oranges and 60 ÷ 12 = 5 mangoes.")],
  fig=draw.tree("84", ["2 × 42", "2 × 21", "3 × 7"], label="Prime factor tree for 84",
                sub="84 = 2² × 3 × 7"))

# ------------------------------------------------------------------ 4
topic("frac", "Fractions", N, [
  "To add or subtract, make the denominators the same (use the L.C.M.), then work with the numerators.",
  "To multiply, multiply tops and bottoms. To divide, <b>turn the second fraction upside down and multiply</b>.",
  "Change a mixed number to an improper fraction before multiplying or dividing.",
  "'of' means multiply: ¾ of 48 means ¾ × 48.",
])
O("Simplify: " + F(2, 3) + " + " + F(1, 4),
  [F(11, 12), F(3, 7), F(5, 12), F(3, 12)],
  ["The L.C.M. of 3 and 4 is 12.", "2/3 = 8/12 and 1/4 = 3/12.", "8/12 + 3/12 = <b>11/12</b>."],
  v=Fr(11, 12), nv=[Fr(11, 12), Fr(3, 7), Fr(5, 12), Fr(3, 12)])
O("Find " + F(3, 4) + " of 48 oranges.",
  ["36", "12", "64", "16"],
  ["'of' means multiply: 3/4 × 48.", "48 ÷ 4 = 12, then 12 × 3 = <b>36</b> oranges."],
  v=36)
O("Simplify: 2" + F(1, 2) + " × 1" + F(1, 3),
  ["3" + F(1, 3), "2" + F(1, 6), "3" + F(1, 2), "2" + F(5, 6)],
  ["Change to improper fractions: 2½ = 5/2 and 1⅓ = 4/3.",
   "5/2 × 4/3 = 20/6 = 10/3 = <b>3⅓</b>."],
  v=Fr(10, 3), nv=[Fr(10, 3), Fr(13, 6), Fr(7, 2), Fr(17, 6)])
O("Simplify: " + F(5, 8) + " ÷ " + F(1, 4),
  ["2" + F(1, 2), F(5, 32), "1" + F(1, 2), "3" + F(1, 3)],
  ["Turn the second fraction over and multiply: 5/8 × 4/1.",
   "= 20/8 = 5/2 = <b>2½</b>."],
  v=Fr(5, 2), nv=[Fr(5, 2), Fr(5, 32), Fr(3, 2), Fr(10, 3)])
O("Which of these fractions is the largest?",
  [F(2, 3), F(3, 5), F(7, 12), F(5, 9)],
  ["Use a common denominator of 180: 2/3 = 120/180, 3/5 = 108/180, 7/12 = 105/180, 5/9 = 100/180.",
   "The largest numerator wins, so <b>2/3</b> is the largest."],
  ok=(max([Fr(2, 3), Fr(3, 5), Fr(7, 12), Fr(5, 9)]) == Fr(2, 3)))
T("A farmer uses " + F(1, 3) + " of his land for maize and " + F(2, 5) + " for cassava. The rest is used for vegetables. "
  "(a) What fraction is used for vegetables? (b) If the farm is 45 acres, how many acres are under vegetables?",
  ["(a) Maize + cassava = 1/3 + 2/5. The L.C.M. of 3 and 5 is 15, so 5/15 + 6/15 = 11/15.",
   "Vegetables = 1 − 11/15 = <b>4/15</b>.",
   "(b) 4/15 of 45 = 45 ÷ 15 × 4 = 3 × 4 = <b>12 acres</b>."],
  marks=6, ok=(1 - Fr(1, 3) - Fr(2, 5) == Fr(4, 15) and Fr(4, 15) * 45 == 12))
extras("frac",
  plain="A fraction is just a division waiting to happen: 3/4 means 3 ÷ 4. You can only add or subtract fractions when the "
        "pieces are the same size, which is why we find a common denominator first. Multiplying and dividing need no common denominator at all.",
  examples=[
    E("Simplify 3" + F(1, 4) + " − 1" + F(2, 3) + ".",
      "Step 1. Change to improper fractions: 3¼ = 13/4 and 1⅔ = 5/3.",
      "Step 2. L.C.M. of 4 and 3 is 12: 13/4 = 39/12 and 5/3 = 20/12.",
      "Step 3. 39/12 − 20/12 = 19/12 = <b>1" + F(7, 12) + "</b>."),
    E("A tank is " + F(3, 5) + " full. 24 litres more fills it completely. How much does the tank hold?",
      "Step 1. The 24 litres is the empty part: 1 − 3/5 = 2/5 of the tank.",
      "Step 2. So 2/5 of the tank = 24 litres.",
      "Step 3. 1/5 of the tank = 24 ÷ 2 = 12 litres, so the whole tank = 12 × 5 = <b>60 litres</b>.")])

# ------------------------------------------------------------------ 5
topic("decper", "Decimals & percentages", N, [
  "Per cent means 'out of a hundred'. To change a fraction to a percentage, multiply by 100.",
  "To find a percentage of a quantity, change the percentage to a fraction or decimal and multiply.",
  "When multiplying decimals, count the decimal places in the question — the answer has the same number.",
  "A percentage increase of 25% means the new value is 125% of the old one.",
])
O("Simplify: 0.6 × 0.05",
  ["0.03", "0.3", "0.003", "3.0"],
  ["Ignore the points first: 6 × 5 = 30.",
   "The question has 1 + 2 = 3 decimal places, so the answer needs 3: 0.030 = <b>0.03</b>."],
  v=0.6 * 0.05)
O("Express " + F(3, 8) + " as a percentage.",
  ["37.5%", "38%", "3.75%", "24%"],
  ["Multiply by 100: 3/8 × 100 = 300/8.", "300 ÷ 8 = <b>37.5%</b>."],
  v=37.5)
O("Find 15% of GH¢2 400.",
  ["GH¢360", "GH¢240", "GH¢36", "GH¢1 600"],
  ["15% = 15/100.", "15/100 × 2 400 = 15 × 24 = <b>GH¢360</b>."],
  v=360, nv=[360, 240, 36, 1600])
O("Increase 80 by 25%.",
  ["100", "105", "95", "120"],
  ["25% of 80 = 1/4 × 80 = 20.", "80 + 20 = <b>100</b>. (Or: 125% of 80 = 1.25 × 80 = 100.)"],
  v=80 * 1.25)
O("Express 45 as a percentage of 60.",
  ["75%", "67%", "133%", "15%"],
  ["Write it as a fraction first: 45/60 = 3/4.", "3/4 × 100 = <b>75%</b>."],
  v=45 / 60 * 100)
T("A shirt is sold for GH¢120 after a discount of 20% on the marked price. "
  "(a) Find the marked price. (b) How much money was saved?",
  ["(a) After a 20% discount the customer pays 80% of the marked price.",
   "So 80% of the marked price = GH¢120, which means 1% = 120 ÷ 80 = GH¢1.50.",
   "Marked price = 1.50 × 100 = <b>GH¢150</b>.",
   "(b) Saving = 150 − 120 = <b>GH¢30</b> (which is indeed 20% of 150)."],
  marks=6, ok=(close(120 / 0.8, 150)))
extras("decper",
  plain="Percentages, decimals and fractions are three ways of writing the same thing: 50% = 0.5 = ½. Shops, taxes, "
        "interest and school marks all use percentages, so being able to swap between the three forms quickly is worth a lot of marks.",
  examples=[
    E("A trader bought a bag of rice for GH¢240 and sold it for GH¢288. Find the percentage profit.",
      "Step 1. Profit = 288 − 240 = GH¢48.",
      "Step 2. Percentage profit is always worked on the <b>cost</b> price: 48/240 × 100.",
      "Step 3. 48/240 = 1/5, and 1/5 × 100 = <b>20%</b>."),
    E("Change 0.125 to a fraction in its lowest terms, and then to a percentage.",
      "Step 1. 0.125 = 125/1000 (three decimal places → three zeros).",
      "Step 2. Divide top and bottom by 125: 125/1000 = <b>1/8</b>.",
      "Step 3. As a percentage: 0.125 × 100 = <b>12.5%</b>.")])

# ------------------------------------------------------------------ 6
topic("integers", "Integers (directed numbers)", N, [
  "On the number line, numbers get smaller as you move left. So −7 is less than −3.",
  "Adding a negative moves left; subtracting a negative moves right: 5 − (−3) = 5 + 3 = 8.",
  "For × and ÷ : same signs give +, different signs give −.",
  "Temperature, profit/loss, and height above or below sea level all use directed numbers.",
])
O("Simplify: (−8) + (+3)",
  ["−5", "−11", "5", "11"],
  ["Start at −8 on the number line and move 3 steps to the right.", "You land on <b>−5</b>."],
  v=-5)
O("Simplify: (−6) × (−4)",
  ["24", "−24", "10", "−10"],
  ["Two negative signs multiplied give a positive.", "6 × 4 = 24, so the answer is <b>24</b>."],
  v=24)
O("Simplify: (−20) ÷ 4 + 3",
  ["−2", "−8", "2", "8"],
  ["Division first: (−20) ÷ 4 = −5 (different signs give a negative).", "Then −5 + 3 = <b>−2</b>."],
  v=-20 / 4 + 3)
O("Which of these numbers is the smallest?",
  ["−7", "−3", "0", "2"],
  ["On the number line the further left a number is, the smaller it is.",
   "−7 lies furthest to the left, so <b>−7</b> is the smallest."],
  ok=(min(-7, -3, 0, 2) == -7))
O("The temperature in a cold store rose from −4 °C to 9 °C. By how many degrees did it rise?",
  ["13 °C", "5 °C", "−13 °C", "36 °C"],
  ["Rise = final − initial = 9 − (−4).", "Subtracting a negative means adding: 9 + 4 = <b>13 °C</b>."],
  v=9 - (-4), nv=[13, 5, -13, 36])
T("Simplify: (−5) + (−3) × 2 − (−4)",
  ["Multiplication first: (−3) × 2 = −6.", "Now (−5) + (−6) − (−4).",
   "Subtracting −4 is the same as adding 4: −5 − 6 + 4.", "= −11 + 4 = <b>−7</b>."],
  marks=4, ok=((-5) + (-3) * 2 - (-4) == -7))
extras("integers",
  plain="Think of a thermometer standing on its side. Positive numbers are to the right of zero, negative numbers to the "
        "left. Adding moves you right, subtracting moves you left — and two minus signs next to each other cancel out and push you right.",
  examples=[
    E("Simplify (−12) − (−5).",
      "Step 1. Two minus signs together become a plus: (−12) + 5.",
      "Step 2. Start at −12 and move 5 steps right.",
      "Step 3. You land on <b>−7</b>.",
      fig=draw.numline(-14, 2, marks=[(-12, "−12"), (-7, "−7")], label="From −12, move 5 right")),
    E("A trader made a loss of GH¢35 on Monday and a profit of GH¢80 on Tuesday. What was the overall result?",
      "Step 1. Write the loss as −35 and the profit as +80.",
      "Step 2. Total = −35 + 80.",
      "Step 3. = <b>+45</b>, that is a profit of GH¢45.")],
  fig=draw.numline(-8, 8, marks=[(-7, "−7"), (0, "0"), (2, "2")], label="The integer number line"))

# ------------------------------------------------------------------ 7
topic("ratio", "Ratio, rate & proportion", N, [
  "A ratio compares quantities of the same kind and has no units. Always simplify by dividing by the H.C.F.",
  "To share in a ratio: add the parts, divide the total by that sum, then multiply by each part.",
  "<b>Direct proportion</b>: more of one → more of the other (cost of books). <b>Inverse</b>: more of one → less of the other (workers and time).",
  "A map scale of 1 : 50 000 means 1 cm on the map stands for 50 000 cm on the ground.",
])
O("Share GH¢600 between Ama and Kofi in the ratio 2 : 3. How much does Kofi get?",
  ["GH¢360", "GH¢240", "GH¢300", "GH¢400"],
  ["Total parts = 2 + 3 = 5, so one part = 600 ÷ 5 = GH¢120.",
   "Kofi has 3 parts: 3 × 120 = <b>GH¢360</b>."],
  v=600 * 3 / 5, nv=[360, 240, 300, 400])
O("Express the ratio 36 : 48 in its lowest terms.",
  ["3 : 4", "4 : 3", "6 : 8", "9 : 12"],
  ["The H.C.F. of 36 and 48 is 12.", "36 ÷ 12 = 3 and 48 ÷ 12 = 4, so the ratio is <b>3 : 4</b>."],
  ok=(Fr(36, 48) == Fr(3, 4)))
O("If 5 exercise books cost GH¢40, what is the cost of 8 such books?",
  ["GH¢64", "GH¢48", "GH¢56", "GH¢72"],
  ["This is direct proportion. One book costs 40 ÷ 5 = GH¢8.", "8 books cost 8 × 8 = <b>GH¢64</b>."],
  v=8 * 40 / 5, nv=[64, 48, 56, 72])
O("Three workers can clear a plot in 8 days. How long would 4 workers take, working at the same rate?",
  ["6 days", "10 days", "11 days", "4 days"],
  ["This is inverse proportion: more workers means fewer days.",
   "Total work = 3 × 8 = 24 worker-days.", "With 4 workers: 24 ÷ 4 = <b>6 days</b>."],
  v=3 * 8 / 4, nv=[6, 10, 11, 4])
O("On a map of scale 1 : 50 000, two towns are 4 cm apart. Find the actual distance between them in kilometres.",
  ["2 km", "20 km", "0.2 km", "200 km"],
  ["Actual distance = 4 × 50 000 = 200 000 cm.",
   "100 000 cm = 1 km, so 200 000 cm = <b>2 km</b>."],
  v=2, nv=[2, 20, 0.2, 200])
T("108 oranges are shared among Abena, Baba and Comfort in the ratio 2 : 3 : 4. "
  "(a) How many oranges does each receive? (b) What percentage of the oranges does Baba receive?",
  ["(a) Total parts = 2 + 3 + 4 = 9, so one part = 108 ÷ 9 = 12 oranges.",
   "Abena: 2 × 12 = <b>24</b>;  Baba: 3 × 12 = <b>36</b>;  Comfort: 4 × 12 = <b>48</b>.",
   "Check: 24 + 36 + 48 = 108. ✓",
   "(b) Baba's share = 36/108 = 1/3, and 1/3 × 100 = <b>33⅓%</b>."],
  marks=8, ok=(24 + 36 + 48 == 108 and Fr(36, 108) == Fr(1, 3)))
extras("ratio",
  plain="Sharing in a ratio is always the same three moves: add the parts, find what one part is worth, then multiply. "
        "The only trap is deciding whether a problem is direct (both go up together) or inverse (one goes up as the other comes down).",
  examples=[
    E("A sum of money is shared between two brothers in the ratio 5 : 7. The younger gets GH¢250. Find the total sum.",
      "Step 1. The smaller share (5 parts) is GH¢250.",
      "Step 2. One part = 250 ÷ 5 = GH¢50.",
      "Step 3. Total parts = 5 + 7 = 12, so the total = 12 × 50 = <b>GH¢600</b>."),
    E("A car uses 9 litres of fuel to travel 72 km. How far can it go on 15 litres?",
      "Step 1. Direct proportion: more fuel, more distance.",
      "Step 2. Rate = 72 ÷ 9 = 8 km per litre.",
      "Step 3. 15 × 8 = <b>120 km</b>.")])

# ------------------------------------------------------------------ 8
topic("indices", "Indices & standard form", N, [
  "a^m × a^n = a^{m+n};  a^m ÷ a^n = a^{m−n};  (a^m)^n = a^{mn}.",
  "a^0 = 1 for any number except 0, and a^{−n} = 1 ÷ a^n.",
  "<b>Standard form</b>: A × 10^n where 1 ≤ A < 10. Large numbers give a positive n, small numbers a negative n.",
])
O("Simplify: 2^{3} × 2^{4}",
  ["128", "64", "4 096", "256"],
  ["Same base, so add the powers: 2³ × 2⁴ = 2⁷.", "2⁷ = <b>128</b>."],
  v=2 ** 7)
O("Simplify: 5^{0} + 3^{2}",
  ["10", "9", "14", "15"],
  ["Any number to the power 0 is 1, so 5⁰ = 1.", "3² = 9, so 1 + 9 = <b>10</b>."],
  v=5 ** 0 + 3 ** 2)
O("Write 0.00045 in standard form.",
  ["4.5 × 10^{−4}", "4.5 × 10^{4}", "45 × 10^{−5}", "4.5 × 10^{−3}"],
  ["Move the point to just after the first non-zero digit: 4.5.",
   "The point moved 4 places to the right, so the power is −4: <b>4.5 × 10⁻⁴</b>."],
  ok=(close(4.5e-4, 0.00045)))
O("Simplify: (2^{3})^{2}",
  ["64", "32", "16", "128"],
  ["Power of a power: multiply the indices. (2³)² = 2⁶.", "2⁶ = <b>64</b>."],
  v=(2 ** 3) ** 2)
O("Evaluate: 2^{−2}",
  [F(1, 4), "−4", F(1, 2), "4"],
  ["A negative index means 'one over': 2⁻² = 1/2².", "= <b>1/4</b>."],
  v=Fr(1, 4), nv=[Fr(1, 4), -4, Fr(1, 2), 4])
T("Simplify, leaving your answer as a whole number: (3^{2} × 3^{4}) ÷ 3^{3}",
  ["Numerator: same base, add the powers: 3² × 3⁴ = 3⁶.",
   "Now divide: 3⁶ ÷ 3³ = 3^{6−3} = 3³.", "3³ = 3 × 3 × 3 = <b>27</b>."],
  marks=4, ok=((3 ** 2 * 3 ** 4) // 3 ** 3 == 27))
extras("indices",
  plain="An index (or power) is a short way of writing repeated multiplication: 2⁵ means 2 × 2 × 2 × 2 × 2. The three laws "
        "are easy to remember if you think about what they mean — multiplying means you have more 2s, so the powers add.",
  examples=[
    E("Simplify " + F("a^{5} × a^{2}", "a^{3}") + ".",
      "Step 1. Top: a⁵ × a² = a⁷ (add the powers).",
      "Step 2. Now divide: a⁷ ÷ a³ = a^{7−3}.",
      "Step 3. = <b>a⁴</b>."),
    E("The mass of a grain of sand is 0.000 006 5 kg. Write this in standard form.",
      "Step 1. The first non-zero digit is 6, so A = 6.5.",
      "Step 2. Count how far the point moves to get from 0.0000065 to 6.5 — six places to the right.",
      "Step 3. Moving right means a negative power: <b>6.5 × 10⁻⁶ kg</b>.")])

# ------------------------------------------------------------------ 9
topic("sets", "Sets & Venn diagrams", N, [
  "n(A) means the number of members of set A. ∪ means union (everything), ∩ means intersection (the overlap).",
  "n(A ∪ B) = n(A) + n(B) − n(A ∩ B). Subtracting the overlap stops you counting it twice.",
  "A set with n members has 2^n subsets.",
  "An empty (null) set has no members and is written { } or ∅.",
])
O("If n(A) = 12, n(B) = 15 and n(A ∩ B) = 5, find n(A ∪ B).",
  ["22", "27", "32", "17"],
  ["n(A ∪ B) = n(A) + n(B) − n(A ∩ B).", "= 12 + 15 − 5 = <b>22</b>."],
  v=12 + 15 - 5)
O("If P = {2, 4, 6, 8} and Q = {4, 6, 8, 10}, find P ∩ Q.",
  ["{4, 6, 8}", "{2, 10}", "{2, 4, 6, 8, 10}", "{4, 6}"],
  ["The intersection is the members found in <b>both</b> sets.",
   "4, 6 and 8 appear in both, so P ∩ Q = <b>{4, 6, 8}</b>."],
  ok=({2, 4, 6, 8} & {4, 6, 8, 10} == {4, 6, 8}))
O("How many subsets has the set {a, b, c, d}?",
  ["16", "8", "4", "15"],
  ["A set with n members has 2ⁿ subsets.", "Here n = 4, so 2⁴ = <b>16</b> subsets."],
  v=2 ** 4)
O("In a class of 40 pupils, 25 play football, 18 play volleyball and 7 play both. How many play neither game?",
  ["4", "11", "8", "15"],
  ["Pupils who play at least one game = 25 + 18 − 7 = 36.",
   "Neither = 40 − 36 = <b>4</b>."],
  v=40 - (25 + 18 - 7))
O("Which of the following is a null set?",
  ["{x : x is a prime number between 24 and 28}", "{x : x is an even prime number}",
   "{x : x is a factor of 6}", "{x : x is a multiple of 3 less than 10}"],
  ["25, 26 and 27 are all composite, so there is no prime between 24 and 28 — that set is empty.",
   "The others have members: {2}, {1, 2, 3, 6} and {3, 6, 9}.",
   "So the null set is <b>{x : x is a prime number between 24 and 28}</b>."],
  ok=(not any(sp.isprime(k) for k in (25, 26, 27))))
T("In a group of 60 students, 35 study Mathematics, 30 study Science and 12 study both. "
  "(a) Illustrate the information on a Venn diagram. (b) How many study Mathematics only? (c) How many study neither subject?",
  ["(a) Draw two overlapping circles inside a rectangle. Put 12 in the overlap.",
   "(b) Mathematics only = 35 − 12 = <b>23</b>.",
   "Science only = 30 − 12 = 18.",
   "(c) Students studying at least one = 23 + 12 + 18 = 53, so neither = 60 − 53 = <b>7</b>."],
  marks=8, fig=draw.venn2("Maths", "Science", 23, 12, 18, outside=7, label="Venn diagram for the 60 students"),
  ok=(60 - ((35 - 12) + 12 + (30 - 12)) == 7))
extras("sets",
  plain="A set is simply a collection. Venn diagrams turn word problems into pictures: draw the circles, fill the "
        "<b>overlap first</b>, then subtract to get the 'only' regions. Filling the overlap first is the single most useful habit here.",
  examples=[
    E("In a class of 30, 20 like rice and 14 like yam. Every pupil likes at least one. How many like both?",
      "Step 1. Use n(A ∪ B) = n(A) + n(B) − n(A ∩ B). Everyone likes at least one, so n(A ∪ B) = 30.",
      "Step 2. 30 = 20 + 14 − n(both) = 34 − n(both).",
      "Step 3. n(both) = 34 − 30 = <b>4 pupils</b>."),
    E("List the members of {x : x is a factor of 12} and say how many subsets it has.",
      "Step 1. Factors of 12: 1, 2, 3, 4, 6, 12 — six members.",
      "Step 2. Number of subsets = 2ⁿ = 2⁶.",
      "Step 3. = <b>64 subsets</b>.")],
  fig=draw.venn2("Football", "Volleyball", 18, 7, 11, outside=4, label="40 pupils: football and volleyball"))

# ------------------------------------------------------------------ 10
topic("patterns", "Number patterns & sequences", N, [
  "Look first at the <b>difference</b> between terms. A constant difference means the rule is linear.",
  "If the common difference is d and the first term is a, the nth term is a + (n − 1)d.",
  "Also look out for squares (1, 4, 9, 16), cubes (1, 8, 27) and <b>multiplying</b> patterns, where each term is multiplied by the same number: 2, 4, 8, 16 (×2 each time) or 2, 6, 18, 54 (×3 each time).",
])
O("What is the next term in the sequence 3, 7, 11, 15, …?",
  ["19", "18", "20", "22"],
  ["The difference is 4 each time (7 − 3 = 4, 11 − 7 = 4).", "15 + 4 = <b>19</b>."],
  v=19)
O("What is the next term in the sequence 1, 4, 9, 16, …?",
  ["25", "20", "24", "32"],
  ["These are square numbers: 1², 2², 3², 4².", "The next is 5² = <b>25</b>."],
  v=25)
O("Find the nth term of the sequence 5, 8, 11, 14, …",
  ["3n + 2", "2n + 3", "3n − 2", "n + 3"],
  ["The common difference is 3, so the rule contains 3n.",
   "When n = 1, 3n = 3 but the term is 5, so we add 2.", "nth term = <b>3n + 2</b>. Check n = 4: 12 + 2 = 14. ✓"],
  ok=(all(3 * i + 2 == t for i, t in zip([1, 2, 3, 4], [5, 8, 11, 14]))))
O("What is the next term in the sequence 2, 6, 18, 54, …?",
  ["162", "108", "72", "216"],
  ["Each term is multiplied by 3 (6 ÷ 2 = 3, 18 ÷ 6 = 3).", "54 × 3 = <b>162</b>."],
  v=54 * 3)
O("Find the 10th term of the sequence 7, 10, 13, 16, …",
  ["34", "37", "31", "30"],
  ["First term a = 7 and common difference d = 3.",
   "nth term = a + (n − 1)d = 7 + 9 × 3.", "= 7 + 27 = <b>34</b>."],
  v=7 + 9 * 3)
T("The pattern below is made with sticks: 1 square uses 4 sticks, 2 squares in a row use 7 sticks, 3 squares use 10 sticks. "
  "(a) How many sticks are needed for 4 squares? (b) Write a formula for the number of sticks, S, needed for n squares. "
  "(c) How many squares can be made with 61 sticks?",
  ["(a) The sticks go up by 3 each time (4, 7, 10), so 4 squares need 10 + 3 = <b>13 sticks</b>.",
   "(b) Common difference 3 → S = 3n + c. When n = 1, S = 4, so 3 + c = 4 and c = 1. Hence <b>S = 3n + 1</b>.",
   "(c) Put S = 61: 3n + 1 = 61, so 3n = 60 and n = <b>20 squares</b>."],
  marks=8, ok=(3 * 4 + 1 == 13 and (61 - 1) // 3 == 20))
extras("patterns",
  plain="Finding the rule of a sequence is detective work. Write the differences underneath the terms. If they are all the "
        "same, the rule is 'difference × n + something'. If they are not, check for squares, cubes or a multiplying pattern.",
  examples=[
    E("Find the nth term of 2, 9, 16, 23, …",
      "Step 1. Differences: 7, 7, 7 — constant, so the rule starts with 7n.",
      "Step 2. When n = 1, 7n = 7, but the first term is 2. That is 5 less.",
      "Step 3. nth term = <b>7n − 5</b>. Check n = 3: 21 − 5 = 16. ✓"),
    E("The nth term of a sequence is n² + 1. Write down the first four terms.",
      "Step 1. n = 1: 1 + 1 = 2.    n = 2: 4 + 1 = 5.",
      "Step 2. n = 3: 9 + 1 = 10.   n = 4: 16 + 1 = 17.",
      "Step 3. The sequence is <b>2, 5, 10, 17</b>.")])

# ------------------------------------------------------------------ 11
topic("money", "Profit, loss, interest & household bills", N, [
  "Profit = selling price − cost price. Percentage profit or loss is always worked on the <b>cost price</b>.",
  "Simple interest I = (P × R × T) ÷ 100, where P is the principal, R the rate per year and T the time in years.",
  "Amount = principal + interest.",
  "Hire purchase total = deposit + (number of instalments × instalment). It is always more than the cash price.",
])
O("A trader bought an article for GH¢60 and sold it for GH¢75. Find the percentage profit.",
  ["25%", "20%", "15%", "80%"],
  ["Profit = 75 − 60 = GH¢15.", "Percentage profit = 15/60 × 100 = <b>25%</b>."],
  v=15 / 60 * 100)
O("Find the simple interest on GH¢800 for 3 years at 5% per annum.",
  ["GH¢120", "GH¢40", "GH¢240", "GH¢1 200"],
  ["I = PRT ÷ 100 = (800 × 5 × 3) ÷ 100.", "= 12 000 ÷ 100 = <b>GH¢120</b>."],
  v=800 * 5 * 3 / 100, nv=[120, 40, 240, 1200])
O("An article bought for GH¢50 was sold for GH¢40. Find the percentage loss.",
  ["20%", "25%", "10%", "80%"],
  ["Loss = 50 − 40 = GH¢10.", "Percentage loss = 10/50 × 100 = <b>20%</b> (worked on the cost price)."],
  v=10 / 50 * 100)
O("A salesman earns 8% commission on his sales. How much does he earn on sales of GH¢2 500?",
  ["GH¢200", "GH¢250", "GH¢160", "GH¢320"],
  ["Commission = 8% of 2 500 = 8/100 × 2 500.", "= 8 × 25 = <b>GH¢200</b>."],
  v=0.08 * 2500, nv=[200, 250, 160, 320])
O("A household used 120 units of electricity in a month at GH¢1.50 per unit. Find the bill.",
  ["GH¢180.00", "GH¢80.00", "GH¢121.50", "GH¢150.00"],
  ["Bill = units × rate = 120 × 1.50.", "= <b>GH¢180.00</b>."],
  v=120 * 1.5)
T("A refrigerator is sold for GH¢1 100 cash, or on hire purchase for a deposit of GH¢300 and 12 monthly instalments of GH¢85. "
  "(a) Find the total hire purchase price. (b) How much more is the hire purchase price than the cash price? "
  "(c) Express this extra amount as a percentage of the cash price, to the nearest whole number.",
  ["(a) Instalments = 12 × 85 = GH¢1 020. Total = 300 + 1 020 = <b>GH¢1 320</b>.",
   "(b) Extra = 1 320 − 1 100 = <b>GH¢220</b>.",
   "(c) 220/1 100 × 100 = <b>20%</b>."],
  marks=8, ok=(300 + 12 * 85 == 1320 and close((1320 - 1100) / 1100 * 100, 20)))
extras("money",
  plain="This is the maths you will use every week of your life — buying, selling, saving and paying bills. Two rules carry "
        "most of the marks: percentage profit and loss are always based on the <b>cost</b> price, and simple interest is PRT over 100.",
  examples=[
    E("Kofi deposits GH¢1 500 in a bank at 4% per annum simple interest. How much will he have after 5 years?",
      "Step 1. I = PRT ÷ 100 = (1 500 × 4 × 5) ÷ 100.",
      "Step 2. = 30 000 ÷ 100 = GH¢300 interest.",
      "Step 3. Amount = principal + interest = 1 500 + 300 = <b>GH¢1 800</b>."),
    E("A trader sold a radio for GH¢270, making a profit of 20%. Find the cost price.",
      "Step 1. Selling price = cost price + 20% of cost price = 120% of the cost price.",
      "Step 2. So 120% of the cost = 270, which means 1% = 270 ÷ 120 = GH¢2.25.",
      "Step 3. Cost price = 2.25 × 100 = <b>GH¢225</b>. (Check: 20% of 225 = 45, and 225 + 45 = 270. ✓)")])

# ------------------------------------------------------------------ 12
topic("approx", "Approximation & estimation", N, [
  "<b>Significant figures</b> start counting from the first non-zero digit.",
  "Decimal places are counted from the point. Round using the digit immediately to the right.",
  "To <b>estimate</b>, round each number to 1 significant figure first, then work the sum in your head.",
  "Keep the same number of zeros as place-holders when rounding whole numbers: 6 843 ≈ 6 800 (nearest hundred).",
])
O("Round 0.004987 to two significant figures.",
  ["0.0050", "0.0049", "0.00", "0.005987"],
  ["The first significant figure is 4 (the zeros in front do not count), the second is 9.",
   "The next digit is 8, so round the 9 up — it becomes 10, carrying into the 4.", "Answer: <b>0.0050</b>."],
  v=0.005, tol=1e-6)
O("Round 6 843 to the nearest hundred.",
  ["6 800", "6 900", "7 000", "6 840"],
  ["The hundreds digit is 8. The digit to its right is 4, which is less than 5, so the 8 stays.",
   "Replace the remaining digits with zeros: <b>6 800</b>."],
  v=6800, nv=[6800, 6900, 7000, 6840])
O("Estimate the value of 49 × 21 by first rounding each number to one significant figure.",
  ["1 000", "900", "1 100", "1 029"],
  ["49 ≈ 50 and 21 ≈ 20.", "50 × 20 = <b>1 000</b>. (The exact answer, 1 029, is close to it.)"],
  v=50 * 20, nv=[1000, 900, 1100, 1029])
O("Express 3.14159 correct to three decimal places.",
  ["3.142", "3.141", "3.14", "3.1416"],
  ["Three decimal places means keeping 3.141, then looking at the next digit, 5.",
   "5 means round up, so the last digit becomes 2: <b>3.142</b>."],
  v=3.142)
O("A length was measured as 24.6 cm. Give this length to the nearest centimetre.",
  ["25 cm", "24 cm", "24.5 cm", "30 cm"],
  ["The whole number part is 24 and the first decimal is 6.",
   "6 is 5 or more, so round up: <b>25 cm</b>."],
  v=25, nv=[25, 24, 24.5, 30])
T("(a) Round 0.08564 to three significant figures. (b) By rounding each number to one significant figure, "
  "estimate the value of (29.8 × 4.9) ÷ 0.98.",
  ["(a) The significant figures are 8, 5, 6, 4. Keeping three gives 0.0856, and the next digit is 4, so it stays: <b>0.0856</b>.",
   "(b) Round first: 29.8 ≈ 30, 4.9 ≈ 5 and 0.98 ≈ 1.",
   "(30 × 5) ÷ 1 = <b>150</b>. (The exact answer is 149.0, so the estimate is good.)"],
  marks=6, ok=(close(round(0.08564, 6), 0.08564) and 30 * 5 / 1 == 150))
extras("approx",
  plain="Rounding is about giving a sensible answer, not a long one. Estimating is your safety net in the exam: round "
        "everything to one significant figure, work it in your head, and if your calculated answer is nowhere near the estimate, something went wrong.",
  examples=[
    E("Round 45 678 to (i) 2 significant figures, (ii) the nearest thousand.",
      "Step 1. (i) The first two significant figures are 4 and 5. The next digit is 6, so round the 5 up to 6.",
      "Step 2. Keep the place-holders: <b>46 000</b>.",
      "Step 3. (ii) The thousands digit is 5 and the next digit is 6, so round up: <b>46 000</b> again."),
    E("Estimate " + F("8.1 × 19.6", "3.9") + " to one significant figure.",
      "Step 1. Round each number: 8.1 ≈ 8, 19.6 ≈ 20, 3.9 ≈ 4.",
      "Step 2. (8 × 20) ÷ 4 = 160 ÷ 4.",
      "Step 3. = <b>40</b>.")])
