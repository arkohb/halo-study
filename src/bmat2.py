"""BECE Mathematics - Strands B, C, D: Algebra, Geometry & Measurement, Handling Data."""
from core import *
import draw
from fractions import Fraction as Fr
import sympy as sp

E = lambda q, *steps, **kw: {"q": q, "steps": list(steps), "fig": kw.get("fig")}
B, C, D = "B. Algebra", "C. Geometry & Measurement", "D. Handling Data"
X = sp.Symbol('x')

# ------------------------------------------------------------------ algebra
topic("algexp", "Algebraic expressions & substitution", B, [
  "Only <b>like terms</b> can be added or subtracted: 5a + 3a = 8a, but 5a + 3b stays as it is.",
  "To substitute, replace each letter with its value and put brackets round negative numbers.",
  "Remember that 2x² means 2 × x × x — square first, then multiply by 2.",
])
O("If x = 3 and y = −2, evaluate 2x^{2} − 3y.",
  ["24", "12", "0", "30"],
  ["2x² = 2 × 3² = 2 × 9 = 18.", "−3y = −3 × (−2) = +6.", "18 + 6 = <b>24</b>."],
  v=2 * 3 ** 2 - 3 * (-2))
O("Simplify: 5a − 3b − 2a + 7b",
  ["3a + 4b", "3a − 4b", "7a + 4b", "3a + 10b"],
  ["Collect the a terms: 5a − 2a = 3a.", "Collect the b terms: −3b + 7b = +4b.", "So the answer is <b>3a + 4b</b>."],
  ok=(sp.expand(5 * sp.Symbol('a') - 3 * sp.Symbol('b') - 2 * sp.Symbol('a') + 7 * sp.Symbol('b'))
      == 3 * sp.Symbol('a') + 4 * sp.Symbol('b')))
O("Expand: 3(2x − 5)",
  ["6x − 15", "6x − 5", "5x − 15", "6x + 15"],
  ["Multiply everything inside the bracket by 3.", "3 × 2x = 6x and 3 × (−5) = −15.", "So <b>6x − 15</b>."],
  ok=(sp.expand(3 * (2 * X - 5)) == 6 * X - 15))
O("If p = 4 and q = 5, evaluate 3pq − p^{2}.",
  ["44", "76", "26", "56"],
  ["3pq = 3 × 4 × 5 = 60.", "p² = 4² = 16.", "60 − 16 = <b>44</b>."],
  v=3 * 4 * 5 - 4 ** 2)
O("Simplify: 4(x + 2) − 2(x − 3)",
  ["2x + 14", "2x + 2", "6x + 2", "2x − 14"],
  ["Expand each bracket: 4x + 8 and −2x + 6 (note that −2 × −3 = +6).",
   "Collect like terms: 4x − 2x = 2x and 8 + 6 = 14.", "So <b>2x + 14</b>."],
  ok=(sp.expand(4 * (X + 2) - 2 * (X - 3)) == 2 * X + 14))
T("Given that m = 2 and n = −3, evaluate (a) 2m^{2} − mn + n^{2}, (b) " + F("3m − n", "m + n") + ".",
  ["(a) 2m² = 2 × 4 = 8.",
   "−mn = −(2)(−3) = +6.   n² = (−3)² = +9.",
   "Total = 8 + 6 + 9 = <b>23</b>.",
   "(b) Numerator: 3(2) − (−3) = 6 + 3 = 9.  Denominator: 2 + (−3) = −1.",
   "So the value is 9 ÷ (−1) = <b>−9</b>."],
  marks=6, ok=(2 * 4 + 6 + 9 == 23 and (3 * 2 - (-3)) / (2 + (-3)) == -9))
extras("algexp",
  plain="Algebra is arithmetic with letters standing in for numbers we do not know yet. The two skills examiners test most "
        "are collecting like terms (tidying up) and substitution (putting numbers back in). Always put negative values in brackets when substituting.",
  examples=[
    E("Simplify 7x − 2(3x − 4).",
      "Step 1. Expand the bracket, watching the signs: −2 × 3x = −6x and −2 × (−4) = +8.",
      "Step 2. The expression is now 7x − 6x + 8.",
      "Step 3. Collect like terms: <b>x + 8</b>."),
    E("If a = −2, b = 3, find the value of a²b − ab².",
      "Step 1. a²b = (−2)² × 3 = 4 × 3 = 12.",
      "Step 2. ab² = (−2) × 3² = −2 × 9 = −18.",
      "Step 3. 12 − (−18) = 12 + 18 = <b>30</b>.")])

topic("factorise", "Expansion & factorisation", B, [
  "To factorise, take out the <b>highest common factor</b> of every term: 6x + 9 = 3(2x + 3).",
  "Expanding two brackets: multiply each term in the first by each term in the second (FOIL).",
  "Difference of two squares: a² − b² = (a − b)(a + b).",
  "Factorising by grouping: ax + ay + bx + by = a(x + y) + b(x + y) = (a + b)(x + y).",
])
O("Factorise: 6x + 9",
  ["3(2x + 3)", "3(2x + 9)", "6(x + 3)", "9(x + 1)"],
  ["The H.C.F. of 6 and 9 is 3.", "6x ÷ 3 = 2x and 9 ÷ 3 = 3, so the answer is <b>3(2x + 3)</b>."],
  ok=(sp.expand(3 * (2 * X + 3)) == 6 * X + 9))
O("Expand: (x + 3)(x + 4)",
  ["x^{2} + 7x + 12", "x^{2} + 12x + 7", "x^{2} + 7x + 7", "x^{2} + 12"],
  ["x × x = x²;  x × 4 = 4x;  3 × x = 3x;  3 × 4 = 12.",
   "Collect the middle terms: 4x + 3x = 7x.", "So <b>x² + 7x + 12</b>."],
  ok=(sp.expand((X + 3) * (X + 4)) == X ** 2 + 7 * X + 12))
O("Factorise: x^{2} − 16",
  ["(x − 4)(x + 4)", "(x − 4)^{2}", "(x − 8)(x + 2)", "x(x − 16)"],
  ["This is a difference of two squares, since 16 = 4².",
   "a² − b² = (a − b)(a + b), so x² − 16 = <b>(x − 4)(x + 4)</b>."],
  ok=(sp.factor(X ** 2 - 16) == (X - 4) * (X + 4)))
O("Factorise: ax + ay + bx + by",
  ["(a + b)(x + y)", "(a + x)(b + y)", "ab(x + y)", "(a + b)(x − y)"],
  ["Group in pairs: a(x + y) + b(x + y).",
   "Now (x + y) is a common factor: <b>(a + b)(x + y)</b>."],
  ok=(sp.factor(sp.expand((sp.Symbol('a') + sp.Symbol('b')) * (X + sp.Symbol('y'))))
      == (sp.Symbol('a') + sp.Symbol('b')) * (X + sp.Symbol('y'))))
O("Expand: (2x − 1)(x + 5)",
  ["2x^{2} + 9x − 5", "2x^{2} − 9x − 5", "2x^{2} + 11x − 5", "2x^{2} + 9x + 5"],
  ["2x × x = 2x²;  2x × 5 = 10x;  −1 × x = −x;  −1 × 5 = −5.",
   "Middle terms: 10x − x = 9x.", "So <b>2x² + 9x − 5</b>."],
  ok=(sp.expand((2 * X - 1) * (X + 5)) == 2 * X ** 2 + 9 * X - 5))
T("Factorise completely: (a) 12ab − 18a^{2}, (b) x^{2} − 5x + 6.",
  ["(a) The H.C.F. of 12ab and 18a² is 6a.",
   "12ab ÷ 6a = 2b and 18a² ÷ 6a = 3a, so the answer is <b>6a(2b − 3a)</b>.",
   "(b) Look for two numbers that multiply to give +6 and add to give −5: these are −2 and −3.",
   "So x² − 5x + 6 = <b>(x − 2)(x − 3)</b>. Check by expanding: x² − 3x − 2x + 6 = x² − 5x + 6. ✓"],
  marks=6, ok=(sp.factor(X ** 2 - 5 * X + 6) == (X - 2) * (X - 3)))
extras("factorise",
  plain="Expanding and factorising are opposites. Expanding removes brackets; factorising puts them back. After "
        "factorising, always expand your answer in your head to check you get back where you started.",
  examples=[
    E("Factorise 15x²y − 25xy².",
      "Step 1. Numbers: the H.C.F. of 15 and 25 is 5.",
      "Step 2. Letters: both terms contain x and y, so xy comes out too. The H.C.F. is 5xy.",
      "Step 3. 15x²y ÷ 5xy = 3x and 25xy² ÷ 5xy = 5y, giving <b>5xy(3x − 5y)</b>."),
    E("Expand (3x − 2)².",
      "Step 1. (3x − 2)² means (3x − 2)(3x − 2) — never just square each term.",
      "Step 2. 3x × 3x = 9x²;  3x × (−2) = −6x;  (−2) × 3x = −6x;  (−2)(−2) = +4.",
      "Step 3. = <b>9x² − 12x + 4</b>.")])

topic("equations", "Linear equations", B, [
  "Do the same thing to both sides to keep the balance: add, subtract, multiply or divide.",
  "Clear brackets first, then fractions (multiply through by the L.C.M.), then collect letters on one side.",
  "Always check your answer by putting it back into the original equation.",
  "For simultaneous equations, add the equations if the signs of one letter are opposite, subtract if they are the same.",
])
O("Solve: 3x − 7 = 11",
  ["6", "4", "18", "−6"],
  ["Add 7 to both sides: 3x = 18.", "Divide both sides by 3: x = <b>6</b>.", "Check: 3(6) − 7 = 11. ✓"],
  v=6)
O("Solve: " + F("2x", "3") + " = 8",
  ["12", "16", "5" + F(1, 3), "24"],
  ["Multiply both sides by 3: 2x = 24.", "Divide by 2: x = <b>12</b>."],
  v=12, nv=[12, 16, Fr(16, 3), 24])
O("Solve: 5(x − 2) = 3x + 4",
  ["7", "3", "−7", "1"],
  ["Expand: 5x − 10 = 3x + 4.", "Take 3x from both sides: 2x − 10 = 4.",
   "Add 10: 2x = 14, so x = <b>7</b>."],
  v=sp.solve(sp.Eq(5 * (X - 2), 3 * X + 4), X)[0])
O("Solve: " + F("x", "4") + " + 3 = 7",
  ["16", "4", "28", "40"],
  ["Subtract 3 from both sides: x/4 = 4.", "Multiply both sides by 4: x = <b>16</b>."],
  v=16)
O("If x + y = 12 and x − y = 4, find the value of y.",
  ["4", "8", "6", "16"],
  ["Subtract the second equation from the first: (x + y) − (x − y) = 12 − 4, so 2y = 8.",
   "Therefore y = <b>4</b> (and x = 8)."],
  v=4)
T("(a) The sum of three consecutive whole numbers is 72. Find the numbers. "
  "(b) I think of a number, multiply it by 3 and subtract 5. The result is 25. What is the number?",
  ["(a) Let the smallest number be n. The three numbers are n, n + 1 and n + 2.",
   "n + (n + 1) + (n + 2) = 72  →  3n + 3 = 72  →  3n = 69  →  n = 23.",
   "The numbers are <b>23, 24 and 25</b>. Check: 23 + 24 + 25 = 72. ✓",
   "(b) Let the number be x. Then 3x − 5 = 25.",
   "3x = 30, so x = <b>10</b>."],
  marks=8, ok=(23 + 24 + 25 == 72 and sp.solve(sp.Eq(3 * X - 5, 25), X)[0] == 10))
extras("equations",
  plain="An equation is a balance: whatever you do to one side you must do to the other. Work in this order — brackets, "
        "fractions, letters to one side, numbers to the other, then divide. The last step of every solution should be a check.",
  examples=[
    E("Solve " + F("x + 1", "2") + " + " + F("x", "3") + " = 4.",
      "Step 1. The L.C.M. of 2 and 3 is 6, so multiply every term by 6.",
      "Step 2. 3(x + 1) + 2x = 24  →  3x + 3 + 2x = 24.",
      "Step 3. 5x = 21, so x = <b>4.2</b> (or 21/5). Check: 5.2/2 + 4.2/3 = 2.6 + 1.4 = 4. ✓"),
    E("The length of a rectangle is 3 cm more than its width and the perimeter is 26 cm. Find the width.",
      "Step 1. Let the width be w, so the length is w + 3.",
      "Step 2. Perimeter = 2(length + width) = 2(w + 3 + w) = 26.",
      "Step 3. 2(2w + 3) = 26  →  4w + 6 = 26  →  4w = 20  →  w = <b>5 cm</b> (length 8 cm).")])

topic("inequal", "Inequalities", B, [
  "Solve an inequality exactly like an equation, with one extra rule.",
  "The rule: when you multiply or divide both sides by a <b>negative</b> number, turn the inequality sign round.",
  "On a number line, use an open circle (○) for &lt; or &gt; and a filled circle (●) for ≤ or ≥.",
])
O("Solve: 2x + 3 < 11",
  ["x < 4", "x > 4", "x < 7", "x < 14"],
  ["Subtract 3: 2x < 8.", "Divide by 2 (a positive number, so the sign stays): <b>x < 4</b>."],
  ok=(sp.solve(2 * X + 3 < 11, X).as_set() == sp.Interval.open(-sp.oo, 4)))
O("Solve: −3x ≥ 12",
  ["x ≤ −4", "x ≥ −4", "x ≤ 4", "x ≥ 4"],
  ["Divide both sides by −3.", "Dividing by a negative number reverses the sign: <b>x ≤ −4</b>.",
   "Check with x = −5: −3(−5) = 15, and 15 ≥ 12. ✓"],
  ok=(-3 * (-5) >= 12 and not (-3 * (-3) >= 12)))
O("What is the largest integer that satisfies 4x − 1 < 19?",
  ["4", "5", "6", "3"],
  ["Add 1: 4x < 20, so x < 5.", "x must be less than 5, so the largest integer is <b>4</b>."],
  v=4)
O("Solve: " + F("x", "2") + " + 1 ≥ 4",
  ["x ≥ 6", "x ≥ 3", "x ≤ 6", "x ≥ 10"],
  ["Subtract 1: x/2 ≥ 3.", "Multiply both sides by 2: <b>x ≥ 6</b>."],
  ok=(6 / 2 + 1 >= 4 and not (5 / 2 + 1 >= 4)))
O("Which of the following is NOT a solution of 3x − 2 ≤ 10?",
  ["5", "4", "0", "−2"],
  ["Solve first: 3x ≤ 12, so x ≤ 4.", "4, 0 and −2 all satisfy x ≤ 4, but <b>5</b> does not."],
  v=5)
T("Solve the inequality 5 − 2x > 1 and show your answer on a number line.",
  ["Subtract 5 from both sides: −2x > −4.",
   "Divide both sides by −2 — and reverse the sign because −2 is negative: <b>x < 2</b>.",
   "On the number line, draw an open circle at 2 (because 2 itself is not included) and shade to the left.",
   "Check with x = 0: 5 − 0 = 5, and 5 > 1. ✓"],
  marks=6, fig=draw.numline(-4, 6, seg=(None, 2, False, False), label="x < 2"),
  ok=(5 - 2 * 0 > 1 and not (5 - 2 * 3 > 1)))
extras("inequal",
  plain="An inequality says one side is bigger than the other, so the answer is a <b>range</b> of numbers rather than a "
        "single one. Everything works as it does for equations until you divide by a negative number — then the sign flips.",
  examples=[
    E("Solve 7 − 3x ≤ 1 and state the smallest value of x.",
      "Step 1. Subtract 7: −3x ≤ −6.",
      "Step 2. Divide by −3 and reverse the sign: x ≥ 2.",
      "Step 3. The smallest value of x is <b>2</b>."),
    E("Find the integers that satisfy both x > −2 and x ≤ 3.",
      "Step 1. x > −2 means x can be −1, 0, 1, 2, … (not −2 itself).",
      "Step 2. x ≤ 3 cuts it off at 3, and 3 is included.",
      "Step 3. The integers are <b>−1, 0, 1, 2, 3</b>.",
      fig=draw.numline(-4, 5, seg=(-2, 3, False, True), label="−2 < x ≤ 3"))])

topic("relmap", "Relations, mappings & functions", B, [
  "A mapping links each member of one set to exactly one member of another set.",
  "f(x) is read 'f of x'. f(4) means 'replace x with 4'.",
  "If a mapping is x → ax + b, use two given pairs to form two equations and find a and b.",
  "The set you start from is the <b>domain</b>; the answers you get are the <b>range</b> (images).",
])
O("If f(x) = 2x + 3, find f(4).",
  ["11", "9", "14", "24"],
  ["Replace x with 4: f(4) = 2(4) + 3.", "= 8 + 3 = <b>11</b>."],
  v=2 * 4 + 3)
O("Under the mapping x → 3x − 1, what is the image of 5?",
  ["14", "15", "16", "2"],
  ["Image = 3(5) − 1.", "= 15 − 1 = <b>14</b>."],
  v=3 * 5 - 1)
O("If f(x) = x^{2} − 1, find f(−3).",
  ["8", "−8", "10", "−10"],
  ["f(−3) = (−3)² − 1. Squaring a negative gives a positive: (−3)² = 9.", "9 − 1 = <b>8</b>."],
  v=(-3) ** 2 - 1)
O("A mapping is defined by x → ax + b. If 1 → 5 and 2 → 8, find the rule.",
  ["x → 3x + 2", "x → 2x + 3", "x → 3x − 2", "x → 5x"],
  ["From 1 → 5: a + b = 5.  From 2 → 8: 2a + b = 8.",
   "Subtract: a = 3, and then b = 5 − 3 = 2.", "So the rule is <b>x → 3x + 2</b>. Check: 2 → 6 + 2 = 8. ✓"],
  ok=(3 * 1 + 2 == 5 and 3 * 2 + 2 == 8))
O("If g(x) = " + F("x + 1", "2") + ", find g(7).",
  ["4", "3" + F(1, 2), "8", "7" + F(1, 2)],
  ["g(7) = (7 + 1) ÷ 2.", "= 8 ÷ 2 = <b>4</b>."],
  v=4, nv=[4, Fr(7, 2), 8, Fr(15, 2)])
T("A function is defined by f(x) = 4x − 3. (a) Find f(0) and f(3). (b) Find the value of x for which f(x) = 13. "
  "(c) Copy and complete the table for x = −1, 0, 1, 2.",
  ["(a) f(0) = 4(0) − 3 = <b>−3</b>.   f(3) = 4(3) − 3 = 12 − 3 = <b>9</b>.",
   "(b) Put f(x) = 13: 4x − 3 = 13  →  4x = 16  →  x = <b>4</b>.",
   "(c) x = −1 → 4(−1) − 3 = −7;  x = 0 → −3;  x = 1 → 1;  x = 2 → 5.",
   "So the table reads <b>−7, −3, 1, 5</b>."],
  marks=8, ok=(4 * 0 - 3 == -3 and sp.solve(sp.Eq(4 * X - 3, 13), X)[0] == 4))
extras("relmap",
  plain="Think of a function as a machine: you drop a number in, the machine does something to it, and a new number comes "
        "out. f(x) = 2x + 3 is the machine 'double it, then add three'. f(4) just asks what comes out when 4 goes in.",
  examples=[
    E("If f(x) = 5 − 2x, find (i) f(−1), (ii) the value of x for which f(x) = 0.",
      "Step 1. (i) f(−1) = 5 − 2(−1) = 5 + 2 = <b>7</b>.",
      "Step 2. (ii) Put 5 − 2x = 0, so 2x = 5.",
      "Step 3. x = <b>2.5</b>."),
    E("The mapping x → x² + k sends 3 to 13. Find k, then find the image of 5.",
      "Step 1. 3² + k = 13, so 9 + k = 13 and k = 4.",
      "Step 2. The rule is x → x² + 4.",
      "Step 3. Image of 5 = 25 + 4 = <b>29</b>.")],
  fig=draw.flow(["Input x = 4", "Multiply by 2 → 8", "Add 3 → 11", "Output f(4) = 11"],
                label="Function machine for f(x) = 2x + 3"))

topic("graphs", "Coordinates & linear graphs", B, [
  "A point is written (x, y): x across first, then y up or down.",
  "The four quadrants run anticlockwise from the top right: (+,+), (−,+), (−,−), (+,−).",
  "Gradient = change in y ÷ change in x. In y = mx + c, m is the gradient and c is where the line cuts the y-axis.",
  "Midpoint of (x₁, y₁) and (x₂, y₂) = ((x₁ + x₂)/2, (y₁ + y₂)/2).",
])
O("Which of these points lies on the line y = 2x + 1?",
  ["(3, 7)", "(3, 5)", "(2, 3)", "(1, 4)"],
  ["Test each point in y = 2x + 1.", "For (3, 7): 2(3) + 1 = 7 ✓. The others do not fit.",
   "So <b>(3, 7)</b> lies on the line."],
  ok=(2 * 3 + 1 == 7 and 2 * 2 + 1 != 3))
O("Find the gradient of the line joining (1, 2) and (3, 8).",
  ["3", "2", "4", F(1, 3)],
  ["Gradient = (change in y) ÷ (change in x) = (8 − 2) ÷ (3 − 1).", "= 6 ÷ 2 = <b>3</b>."],
  v=3, nv=[3, 2, 4, Fr(1, 3)])
O("In which quadrant does the point (−3, 4) lie?",
  ["Second", "First", "Third", "Fourth"],
  ["x is negative and y is positive — that is above the x-axis and to the left of the y-axis.",
   "That is the <b>second</b> quadrant."],
  ok=(-3 < 0 and 4 > 0))
O("At what point does the line y = 3x − 6 cross the y-axis?",
  ["(0, −6)", "(2, 0)", "(0, 6)", "(−6, 0)"],
  ["On the y-axis, x = 0.", "y = 3(0) − 6 = −6, so the line crosses at <b>(0, −6)</b>."],
  ok=(3 * 0 - 6 == -6))
O("Find the midpoint of the line joining (2, 3) and (6, 7).",
  ["(4, 5)", "(8, 10)", "(2, 2)", "(3, 4)"],
  ["Average the x values: (2 + 6) ÷ 2 = 4.", "Average the y values: (3 + 7) ÷ 2 = 5.", "Midpoint = <b>(4, 5)</b>."],
  ok=((2 + 6) / 2 == 4 and (3 + 7) / 2 == 5))
T("(a) Copy and complete the table for y = 2x − 1 for x = −2, −1, 0, 1, 2, 3. "
  "(b) Using a scale of 2 cm to 1 unit on both axes, draw the graph. (c) Use your graph to find y when x = 1.5.",
  ["(a) x = −2 → 2(−2) − 1 = −5;  x = −1 → −3;  x = 0 → −1;  x = 1 → 1;  x = 2 → 3;  x = 3 → 5.",
   "(b) Plot the six points and join them with a straight line — if one point is out of line, you have made an arithmetic slip.",
   "(c) Read up from x = 1.5 to the line and across: <b>y = 2</b>. (Check: 2(1.5) − 1 = 2. ✓)"],
  marks=10, fig=plot(lambda t: 2 * t - 1, -3, 4, -6, 6,
                     pts=[(-2, -5, ""), (0, -1, ""), (2, 3, ""), (3, 5, "")], label="y = 2x − 1"),
  ok=(2 * 1.5 - 1 == 2))
extras("graphs",
  plain="A graph turns a rule into a picture. For a straight line you only need a table of a few points: work out y for "
        "each x, plot the points, and join them with a ruler. If a point does not line up, the arithmetic for that point is wrong.",
  examples=[
    E("Find the gradient and y-intercept of the line 2y = 6x + 8.",
      "Step 1. Make y the subject by dividing everything by 2: y = 3x + 4.",
      "Step 2. Compare with y = mx + c.",
      "Step 3. Gradient m = <b>3</b> and the line cuts the y-axis at <b>(0, 4)</b>."),
    E("The points A(1, 1) and B(5, 9) are joined. Find the gradient and the midpoint.",
      "Step 1. Gradient = (9 − 1) ÷ (5 − 1) = 8 ÷ 4 = <b>2</b>.",
      "Step 2. Midpoint x = (1 + 5) ÷ 2 = 3.",
      "Step 3. Midpoint y = (1 + 9) ÷ 2 = 5, so the midpoint is <b>(3, 5)</b>.")])

# ------------------------------------------------------------------ geometry
topic("angles", "Angles & parallel lines", C, [
  "Angles on a straight line add up to 180°; angles at a point add up to 360°.",
  "Vertically opposite angles are equal.",
  "With parallel lines: corresponding angles (F-shape) are equal, alternate angles (Z-shape) are equal, "
  "and co-interior angles (C- or U-shape) add up to 180°.",
  "The three angles of a triangle add up to 180°.",
])
O("Two angles on a straight line are 3x and 2x + 30. Find x.",
  ["30", "36", "25", "150"],
  ["Angles on a straight line add up to 180°: 3x + 2x + 30 = 180.",
   "5x = 150, so x = <b>30</b>."],
  v=sp.solve(sp.Eq(3 * X + 2 * X + 30, 180), X)[0])
O("What is the complement of 37°?",
  ["53°", "143°", "63°", "37°"],
  ["Complementary angles add up to 90°.", "90 − 37 = <b>53°</b>."],
  v=90 - 37, nv=[53, 143, 63, 37])
O("Angles at a point are 90°, 120°, 70° and x. Find x.",
  ["80°", "90°", "100°", "70°"],
  ["Angles at a point add up to 360°.", "90 + 120 + 70 = 280, so x = 360 − 280 = <b>80°</b>."],
  v=360 - 280, nv=[80, 90, 100, 70])
O("In a right-angled triangle, one of the acute angles is 35°. Find the other acute angle.",
  ["55°", "65°", "45°", "145°"],
  ["The three angles add up to 180° and one of them is 90°.",
   "So the two acute angles add up to 90°: 90 − 35 = <b>55°</b>."],
  v=90 - 35, nv=[55, 65, 45, 145])
O("Two parallel lines are cut by a transversal. One of a pair of co-interior angles is 115°. Find the other.",
  ["65°", "115°", "75°", "245°"],
  ["Co-interior (allied) angles between parallel lines add up to 180°.", "180 − 115 = <b>65°</b>."],
  v=180 - 115, nv=[65, 115, 75, 245])
T("A straight line (a transversal) crosses two parallel lines PQ and RS, making an angle of 72° with PQ. "
  "Find, giving a reason for each answer, (a) the corresponding angle at RS, (b) the co-interior angle at RS, "
  "(c) the angle vertically opposite the 72° angle.",
  ["(a) Corresponding angles between parallel lines are equal, so the angle is <b>72°</b>.",
   "(b) Co-interior angles add up to 180°, so the angle is 180 − 72 = <b>108°</b>.",
   "(c) Vertically opposite angles are equal, so the angle is <b>72°</b>.",
   "In the exam, the reason earns as much credit as the number — always write it down."],
  marks=6, ok=(180 - 72 == 108))
extras("angles",
  plain="Nearly every angle question is solved with one of four facts: straight line 180°, point 360°, triangle 180°, or a "
        "parallel-line rule. Write the fact you are using next to each step — BECE marking schemes award marks for the reason.",
  examples=[
    E("The angles of a triangle are x, 2x and 3x. Find the largest angle.",
      "Step 1. Angles in a triangle add up to 180°: x + 2x + 3x = 180.",
      "Step 2. 6x = 180, so x = 30.",
      "Step 3. The angles are 30°, 60° and 90°, so the largest is <b>90°</b>.",
      fig=draw.tri(A="x", B="2x", C="3x", label="Triangle with angles x, 2x, 3x")),
    E("One angle of an isosceles triangle is 40° and it is the angle between the two equal sides. Find the other angles.",
      "Step 1. The other two angles are equal. Call each y.",
      "Step 2. 40 + y + y = 180, so 2y = 140.",
      "Step 3. y = <b>70°</b>, so the angles are 40°, 70° and 70°.")])

topic("shapes", "Triangles & polygons", C, [
  "Sum of interior angles of an n-sided polygon = (n − 2) × 180°.",
  "Sum of exterior angles of any polygon = 360°. For a regular polygon, each exterior angle = 360° ÷ n.",
  "Interior angle + exterior angle = 180°.",
  "Triangles: equilateral (3 equal sides), isosceles (2 equal), scalene (none equal), right-angled (one 90° angle).",
])
O("Find the sum of the interior angles of a hexagon.",
  ["720°", "360°", "540°", "1 080°"],
  ["Sum = (n − 2) × 180° with n = 6.", "= 4 × 180 = <b>720°</b>."],
  v=(6 - 2) * 180, nv=[720, 360, 540, 1080])
O("Find the size of each exterior angle of a regular pentagon.",
  ["72°", "60°", "108°", "36°"],
  ["Exterior angles of any polygon add up to 360°.", "360 ÷ 5 = <b>72°</b>."],
  v=360 / 5, nv=[72, 60, 108, 36])
O("The angles of a triangle are 2x, 3x and 4x. Find the largest angle.",
  ["80°", "40°", "60°", "90°"],
  ["2x + 3x + 4x = 180, so 9x = 180 and x = 20.",
   "The angles are 40°, 60° and 80°, so the largest is <b>80°</b>."],
  v=4 * 20, nv=[80, 40, 60, 90])
O("A triangle has all three sides equal. What is it called?",
  ["Equilateral", "Isosceles", "Scalene", "Right-angled"],
  ["Triangles are named by their sides: three equal, two equal, or none equal.",
   "All three sides equal (and all three angles 60°) describes an <b>equilateral</b> triangle."],
  ok=True)
O("Each exterior angle of a regular polygon is 24°. How many sides has the polygon?",
  ["15", "12", "24", "18"],
  ["Number of sides = 360 ÷ exterior angle.", "360 ÷ 24 = <b>15 sides</b>."],
  v=360 / 24)
T("Each interior angle of a regular polygon is 150°. (a) Find the size of each exterior angle. "
  "(b) How many sides has the polygon? (c) Find the sum of its interior angles.",
  ["(a) Interior + exterior = 180°, so the exterior angle = 180 − 150 = <b>30°</b>.",
   "(b) n = 360 ÷ 30 = <b>12 sides</b>.",
   "(c) Sum = (n − 2) × 180 = 10 × 180 = <b>1 800°</b>. (Check: 12 × 150 = 1 800. ✓)"],
  marks=6, ok=(360 // 30 == 12 and (12 - 2) * 180 == 1800 == 12 * 150))
extras("shapes",
  plain="Polygon questions almost always come back to two numbers: 180(n − 2) for the inside angles altogether, and 360 "
        "for the outside angles altogether. Decide which one the question needs, and the rest is arithmetic.",
  examples=[
    E("The sum of the interior angles of a polygon is 1 440°. How many sides has it?",
      "Step 1. Use (n − 2) × 180 = 1 440.",
      "Step 2. n − 2 = 1 440 ÷ 180 = 8.",
      "Step 3. n = <b>10 sides</b> (a decagon)."),
    E("Find each interior angle of a regular octagon.",
      "Step 1. Exterior angle = 360 ÷ 8 = 45°.",
      "Step 2. Interior angle = 180 − 45.",
      "Step 3. = <b>135°</b>. (Check with the other method: (8 − 2) × 180 ÷ 8 = 1 080 ÷ 8 = 135. ✓)")])

topic("pythag", "Pythagoras' theorem", C, [
  "In a right-angled triangle, (hypotenuse)² = (one side)² + (other side)².",
  "The hypotenuse is the longest side and always lies opposite the right angle.",
  "To find a shorter side, subtract: side² = hyp² − other².",
  "Useful triples to recognise: 3-4-5, 5-12-13, 8-15-17, 7-24-25 (and their multiples, like 6-8-10).",
])
O("A right-angled triangle has sides 6 cm and 8 cm about the right angle. Find the hypotenuse.",
  ["10 cm", "14 cm", "48 cm", "28 cm"],
  ["h² = 6² + 8² = 36 + 64 = 100.", "h = √100 = <b>10 cm</b>."],
  v=10, nv=[10, 14, 48, 28])
O("A ladder 13 m long leans against a wall with its foot 5 m from the wall. How far up the wall does it reach?",
  ["12 m", "8 m", "18 m", "144 m"],
  ["The ladder is the hypotenuse: height² = 13² − 5².", "= 169 − 25 = 144, so the height = √144 = <b>12 m</b>."],
  v=12, nv=[12, 8, 18, 144])
O("Which of the following can be the sides of a right-angled triangle?",
  ["7, 24, 25", "5, 6, 7", "4, 5, 6", "6, 7, 10"],
  ["Test the largest side against the other two: 7² + 24² = 49 + 576 = 625, and 25² = 625. ✓",
   "The other sets fail the test, so <b>7, 24, 25</b> is the right-angled set."],
  ok=(7 ** 2 + 24 ** 2 == 25 ** 2 and 5 ** 2 + 6 ** 2 != 7 ** 2))
O("A rectangle measures 9 cm by 12 cm. Find the length of its diagonal.",
  ["15 cm", "21 cm", "108 cm", "13 cm"],
  ["The diagonal splits the rectangle into two right-angled triangles.",
   "d² = 9² + 12² = 81 + 144 = 225.", "d = √225 = <b>15 cm</b>."],
  v=15, nv=[15, 21, 108, 13])
O("In a right-angled triangle the hypotenuse is 25 cm and one other side is 7 cm. Find the third side.",
  ["24 cm", "18 cm", "32 cm", "26 cm"],
  ["side² = 25² − 7² = 625 − 49 = 576.", "side = √576 = <b>24 cm</b>."],
  v=24, nv=[24, 18, 32, 26])
T("A man walks 9 km due north and then 12 km due east. (a) Sketch his journey. (b) How far is he from his starting point? "
  "(c) What is the total distance he actually walked?",
  ["(a) The two legs meet at a right angle, so the journey makes a right-angled triangle.",
   "(b) d² = 9² + 12² = 81 + 144 = 225, so d = √225 = <b>15 km</b> from the start.",
   "(c) Distance walked = 9 + 12 = <b>21 km</b> — which is more than the direct distance, as it must be."],
  marks=8, fig=draw.tri(a="12 km", b="15 km", c="9 km", A="Start", B="", C="", right=True,
                        label="9 km north then 12 km east"),
  ok=(9 ** 2 + 12 ** 2 == 15 ** 2))
extras("pythag",
  plain="Pythagoras only works in right-angled triangles. Find the right angle first, then name the hypotenuse (opposite "
        "that angle). Add the squares when hunting for the hypotenuse; subtract when hunting for a shorter side.",
  examples=[
    E("Find the height of an isosceles triangle with equal sides 13 cm and base 10 cm.",
      "Step 1. The height cuts the base in half, giving a right-angled triangle with hypotenuse 13 and base 5.",
      "Step 2. h² = 13² − 5² = 169 − 25 = 144.",
      "Step 3. h = <b>12 cm</b>."),
    E("A rectangular field is 40 m long and its diagonal is 50 m. Find its width.",
      "Step 1. w² = 50² − 40² (the diagonal is the hypotenuse).",
      "Step 2. = 2 500 − 1 600 = 900.",
      "Step 3. w = √900 = <b>30 m</b>.")])

topic("perim", "Perimeter & area of plane shapes", C, [
  "Rectangle: area = l × w, perimeter = 2(l + w). Square: area = s², perimeter = 4s.",
  "Triangle: area = ½ × base × height. The height must be perpendicular to the base.",
  "Parallelogram: area = base × height. Trapezium: area = ½(a + b) × h, where a and b are the parallel sides.",
  "For a compound shape, cut it into rectangles and triangles, work out each, then add.",
])
O("Find the area of a triangle with base 12 cm and height 5 cm.",
  ["30 cm^{2}", "60 cm^{2}", "17 cm^{2}", "34 cm^{2}"],
  ["Area = ½ × base × height = ½ × 12 × 5.", "= <b>30 cm²</b>."],
  v=0.5 * 12 * 5, nv=[30, 60, 17, 34])
O("Find the area of a trapezium whose parallel sides are 8 cm and 12 cm and whose height is 5 cm.",
  ["50 cm^{2}", "100 cm^{2}", "25 cm^{2}", "480 cm^{2}"],
  ["Area = ½(a + b) × h = ½(8 + 12) × 5.", "= ½ × 20 × 5 = <b>50 cm²</b>."],
  v=0.5 * (8 + 12) * 5, nv=[50, 100, 25, 480])
O("Find the perimeter of a rectangle 15 m long and 9 m wide.",
  ["48 m", "135 m", "24 m", "54 m"],
  ["Perimeter = 2(l + w) = 2(15 + 9).", "= 2 × 24 = <b>48 m</b>."],
  v=2 * (15 + 9), nv=[48, 135, 24, 54])
O("Find the area of a parallelogram with base 14 cm and height 6 cm.",
  ["84 cm^{2}", "42 cm^{2}", "40 cm^{2}", "20 cm^{2}"],
  ["Area of a parallelogram = base × height = 14 × 6.", "= <b>84 cm²</b>."],
  v=14 * 6, nv=[84, 42, 40, 20])
O("A square has an area of 81 cm². Find its perimeter.",
  ["36 cm", "81 cm", "18 cm", "324 cm"],
  ["Side = √81 = 9 cm.", "Perimeter = 4 × 9 = <b>36 cm</b>."],
  v=36, nv=[36, 81, 18, 324])
T("A rectangular football field measures 40 m by 25 m. (a) Find its area. "
  "(b) Find the cost of fencing all round it at GH¢12 per metre. "
  "(c) A path 1 m wide is made inside the field along the two longer sides. Find the total area of the path.",
  ["(a) Area = 40 × 25 = <b>1 000 m²</b>.",
   "(b) Perimeter = 2(40 + 25) = 2 × 65 = 130 m. Cost = 130 × 12 = <b>GH¢1 560</b>.",
   "(c) Each path is 40 m by 1 m = 40 m², and there are two of them: 2 × 40 = <b>80 m²</b>."],
  marks=9, ok=(40 * 25 == 1000 and 2 * (40 + 25) * 12 == 1560))
extras("perim",
  plain="Perimeter is the distance round the edge (measured in cm, m, km); area is the space inside (measured in cm², m²). "
        "If your answer to an area question has no little 2 on the unit, you have probably found the perimeter by mistake.",
  examples=[
    E("A compound shape is made of a 10 cm by 6 cm rectangle with a triangle of base 10 cm and height 4 cm on top. Find its area.",
      "Step 1. Rectangle: 10 × 6 = 60 cm².",
      "Step 2. Triangle: ½ × 10 × 4 = 20 cm².",
      "Step 3. Total area = 60 + 20 = <b>80 cm²</b>."),
    E("The area of a rectangle is 96 cm² and its length is 12 cm. Find its perimeter.",
      "Step 1. Width = area ÷ length = 96 ÷ 12 = 8 cm.",
      "Step 2. Perimeter = 2(12 + 8).",
      "Step 3. = <b>40 cm</b>.")])

topic("circles", "Circles: circumference & area", C, [
  "Circumference = 2πr = πd.  Area = πr².",
  "Always use the value of π the question gives you. If none is given, use 22/7 when the radius is a multiple of 7 (the 7s cancel) and 3.14 otherwise.",
  "Diameter = 2 × radius, so radius = diameter ÷ 2. Mixing the two up is the commonest error.",
  "Perimeter of a semicircle = πr + 2r (the curved part plus the diameter).",
])
O("Find the circumference of a circle of radius 7 cm. [Take π = 22/7]",
  ["44 cm", "22 cm", "154 cm", "88 cm"],
  ["C = 2πr = 2 × 22/7 × 7.", "The 7s cancel: 2 × 22 = <b>44 cm</b>."],
  v=2 * Fr(22, 7) * 7, nv=[44, 22, 154, 88])
O("Find the area of a circle of radius 14 cm. [Take π = 22/7]",
  ["616 cm^{2}", "88 cm^{2}", "308 cm^{2}", "154 cm^{2}"],
  ["A = πr² = 22/7 × 14 × 14.", "14 ÷ 7 = 2, so A = 22 × 2 × 14 = <b>616 cm²</b>."],
  v=Fr(22, 7) * 14 * 14, nv=[616, 88, 308, 154])
O("The circumference of a circle is 66 cm. Find its diameter. [Take π = 22/7]",
  ["21 cm", "10.5 cm", "42 cm", "33 cm"],
  ["C = πd, so 66 = 22/7 × d.", "d = 66 × 7 ÷ 22 = <b>21 cm</b>."],
  v=66 * 7 / 22, nv=[21, 10.5, 42, 33])
O("Find the area of a circle of diameter 20 cm. [Take π = 3.14]",
  ["314 cm^{2}", "1 256 cm^{2}", "62.8 cm^{2}", "157 cm^{2}"],
  ["Radius = 20 ÷ 2 = 10 cm (not 20 — this is the usual trap).",
   "A = πr² = 3.14 × 10 × 10 = <b>314 cm²</b>."],
  v=3.14 * 100, nv=[314, 1256, 62.8, 157])
O("Find the perimeter of a semicircle of radius 7 cm. [Take π = 22/7]",
  ["36 cm", "22 cm", "44 cm", "29 cm"],
  ["Curved part = half the circumference = ½ × 2 × 22/7 × 7 = 22 cm.",
   "Add the diameter: 22 + 14 = <b>36 cm</b>. (Forgetting the straight edge is the common slip.)"],
  v=Fr(22, 7) * 7 + 14, nv=[36, 22, 44, 29])
T("A circular garden has a radius of 10.5 m. [Take π = 22/7] "
  "(a) Find the distance round the garden. (b) Find its area. "
  "(c) A wire fence is put round it at GH¢15 per metre. Find the cost.",
  ["(a) C = 2πr = 2 × 22/7 × 10.5 = 2 × 22 × 1.5 = <b>66 m</b>.",
   "(b) A = πr² = 22/7 × 10.5 × 10.5 = 22 × 1.5 × 10.5 = <b>346.5 m²</b>.",
   "(c) Cost = 66 × 15 = <b>GH¢990</b>."],
  marks=9, fig=draw.circlefig("centre", angles=["r = 10.5 m", ""], label="Circular garden"),
  ok=(close(float(2 * Fr(22, 7) * Fr(21, 2)), 66) and close(float(Fr(22, 7) * Fr(21, 2) ** 2), 346.5)))
extras("circles",
  plain="Only two formulas matter here: C = 2πr for the distance round, A = πr² for the space inside. The marks are lost "
        "not on the formula but on using the diameter where the radius belongs — so write r = … as your first line every time.",
  examples=[
    E("The area of a circle is 154 cm². Find its radius. [π = 22/7]",
      "Step 1. πr² = 154, so (22/7)r² = 154.",
      "Step 2. r² = 154 × 7 ÷ 22 = 49.",
      "Step 3. r = √49 = <b>7 cm</b>."),
    E("A bicycle wheel of diameter 70 cm makes 100 complete turns. How far does it travel, in metres? [π = 22/7]",
      "Step 1. One turn covers the circumference: C = πd = 22/7 × 70 = 220 cm.",
      "Step 2. 100 turns = 100 × 220 = 22 000 cm.",
      "Step 3. 100 cm = 1 m, so the distance = <b>220 m</b>.")])

topic("volume", "Volume & surface area of solids", C, [
  "Cuboid: volume = l × w × h; total surface area = 2(lw + lh + wh).",
  "Cube of side s: volume = s³, surface area = 6s².",
  "Cylinder: volume = πr²h; curved surface area = 2πrh; total surface area = 2πrh + 2πr².",
  "Capacity: 1 000 cm³ = 1 litre, and 1 m³ = 1 000 litres.",
])
O("Find the volume of a cuboid 5 cm by 4 cm by 3 cm.",
  ["60 cm^{3}", "12 cm^{3}", "47 cm^{3}", "94 cm^{3}"],
  ["Volume = l × w × h = 5 × 4 × 3.", "= <b>60 cm³</b>."],
  v=60, nv=[60, 12, 47, 94])
O("Find the volume of a cylinder of radius 7 cm and height 10 cm. [Take π = 22/7]",
  ["1 540 cm^{3}", "440 cm^{3}", "220 cm^{3}", "770 cm^{3}"],
  ["V = πr²h = 22/7 × 7 × 7 × 10.", "One 7 cancels: 22 × 7 × 10 = <b>1 540 cm³</b>."],
  v=Fr(22, 7) * 49 * 10, nv=[1540, 440, 220, 770])
O("Find the total surface area of a cube of side 4 cm.",
  ["96 cm^{2}", "64 cm^{2}", "16 cm^{2}", "24 cm^{2}"],
  ["A cube has 6 square faces, each 4 × 4 = 16 cm².", "Total = 6 × 16 = <b>96 cm²</b>."],
  v=6 * 16, nv=[96, 64, 16, 24])
O("The volume of a cube is 125 cm³. Find the length of one edge.",
  ["5 cm", "25 cm", "15 cm", "12.5 cm"],
  ["Volume of a cube = s³, so s³ = 125.", "s = ∛125 = <b>5 cm</b>."],
  v=5, nv=[5, 25, 15, 12.5])
O("A rectangular tank measures 2 m by 1.5 m by 1 m. Find its capacity in litres.",
  ["3 000 litres", "300 litres", "3 litres", "30 000 litres"],
  ["Volume = 2 × 1.5 × 1 = 3 m³.", "1 m³ = 1 000 litres, so the capacity = <b>3 000 litres</b>."],
  v=3000, nv=[3000, 300, 3, 30000])
T("A closed cylindrical tin has radius 3.5 cm and height 20 cm. [Take π = 22/7] "
  "(a) Find its volume. (b) Find its curved surface area. (c) Find the total surface area.",
  ["(a) V = πr²h = 22/7 × 3.5 × 3.5 × 20. Since 3.5 × 3.5 = 12.25, V = 22/7 × 12.25 × 20 = <b>770 cm³</b>.",
   "(b) Curved surface = 2πrh = 2 × 22/7 × 3.5 × 20 = <b>440 cm²</b>.",
   "(c) The two circular ends add 2πr² = 2 × 22/7 × 12.25 = 77 cm².",
   "Total surface area = 440 + 77 = <b>517 cm²</b>."],
  marks=9, fig=draw.solidfig("cylinder", labels=["r = 3.5 cm", "h = 20 cm"], label="Closed cylinder"),
  ok=(close(float(Fr(22, 7) * Fr(7, 2) ** 2 * 20), 770) and close(float(2 * Fr(22, 7) * Fr(7, 2) * 20), 440)))
extras("volume",
  plain="Volume answers are in cubic units (cm³, m³) because you multiply three lengths; surface area answers are in square "
        "units because you are adding up flat faces. For a cylinder, picture unrolling the curved surface into a rectangle 2πr long and h high.",
  examples=[
    E("How many cubes of side 2 cm fit into a box 8 cm by 6 cm by 4 cm?",
      "Step 1. Volume of the box = 8 × 6 × 4 = 192 cm³.",
      "Step 2. Volume of one small cube = 2³ = 8 cm³.",
      "Step 3. Number of cubes = 192 ÷ 8 = <b>24 cubes</b>."),
    E("A cylindrical bucket of radius 10 cm holds 6 280 cm³ of water. Find the depth of the water. [π = 3.14]",
      "Step 1. V = πr²h, so 6 280 = 3.14 × 100 × h.",
      "Step 2. 3.14 × 100 = 314, so h = 6 280 ÷ 314.",
      "Step 3. h = <b>20 cm</b>.")])

topic("construct", "Geometric construction & loci", C, [
  "Constructions are done with a ruler and a pair of compasses only — never measure an angle with a protractor when the question says 'construct'.",
  "Equilateral triangle construction gives 60°. Bisecting 60° gives 30°; bisecting a right angle gives 45°.",
  "The locus of points equidistant from two fixed points is the <b>perpendicular bisector</b> of the line joining them.",
  "The locus of points equidistant from two intersecting lines is the <b>bisector of the angle</b> between them.",
  "Leave all your construction arcs showing — they earn marks.",
])
O("Which instruments are used to construct an angle of 60° exactly?",
  ["A ruler and a pair of compasses", "A protractor only", "A set square and a pencil", "A protractor and a ruler"],
  ["A 60° angle comes from constructing an equilateral triangle, which needs only arcs of equal radius.",
   "So you need <b>a ruler and a pair of compasses</b>."],
  ok=True)
O("The locus of points equidistant from two fixed points A and B is",
  ["the perpendicular bisector of AB", "a circle through A and B", "the line AB itself", "the bisector of angle A"],
  ["Every point on the perpendicular bisector is the same distance from A as from B.",
   "So the locus is <b>the perpendicular bisector of AB</b>."],
  ok=True)
O("An angle of 90° is bisected. What is the size of each new angle?",
  ["45°", "30°", "60°", "22.5°"],
  ["To bisect means to cut into two equal parts.", "90 ÷ 2 = <b>45°</b>."],
  v=45)
O("Which of these angles can NOT be constructed using only a ruler and a pair of compasses?",
  ["50°", "45°", "60°", "90°"],
  ["90° comes from a perpendicular, 60° from an equilateral triangle and 45° from bisecting 90°.",
   "<b>50°</b> cannot be built from these, so it needs a protractor."],
  v=50)
O("The locus of points equidistant from two intersecting straight lines is",
  ["the bisector of the angle between them", "a circle", "a perpendicular bisector", "a straight line parallel to both"],
  ["Points on an angle bisector are the same perpendicular distance from both arms of the angle.",
   "So the locus is <b>the bisector of the angle between them</b>."],
  ok=True)
T("Using a ruler and a pair of compasses only, construct triangle ABC in which AB = 8 cm, angle ABC = 60° and "
  "angle BAC = 45°. Measure and write down the length of AC. Describe your steps.",
  ["Step 1. Draw a line and mark AB = 8 cm on it with the ruler.",
   "Step 2. At B, construct 60°: with centre B draw an arc cutting AB, then from that point step the same radius round to "
   "get the 60° direction, and draw the line.",
   "Step 3. At A, construct 90° (perpendicular to AB), then bisect it to get 45°, and draw that line.",
   "Step 4. The two lines meet at C — that completes the triangle.",
   "Step 5. Measure AC with your ruler. It should be about <b>7.2 cm</b> (the third angle is 75°).",
   "Leave every arc on the paper: the examiner awards marks for the construction marks, not only the final triangle."],
  marks=10, ok=(180 - 60 - 45 == 75))
extras("construct",
  plain="A construction is a drawing made only with a ruler and compasses. The compasses are what make it exact. Two "
        "constructions give you almost all the angles you will be asked for: the equilateral triangle (60°) and the perpendicular (90°), plus bisecting either of them.",
  examples=[
    E("How would you construct an angle of 30°?",
      "Step 1. First construct 60° using equal arcs (the equilateral-triangle method).",
      "Step 2. Now bisect that 60° angle: place the compasses at the vertex and draw an arc cutting both arms.",
      "Step 3. From those two crossing points draw equal arcs; join the vertex to where they meet. Each half is <b>30°</b>."),
    E("A goat is tied to a post with a rope 4 m long in an open field. Describe the locus of the goat's possible positions.",
      "Step 1. The goat can move to any point at most 4 m from the post.",
      "Step 2. The boundary of that region is a circle of radius 4 m.",
      "Step 3. The locus is therefore <b>a circular region (disc) of radius 4 m centred on the post</b>.")])

topic("transform", "Rigid motion & enlargement", C, [
  "A <b>translation</b> slides a shape. Adding the vector (a, b) sends (x, y) to (x + a, y + b).",
  "<b>Reflection</b> in the x-axis: (x, y) → (x, −y). In the y-axis: (x, y) → (−x, y).",
  "<b>Rotation</b> of 90° anticlockwise about the origin: (x, y) → (−y, x). A rotation of 180°: (x, y) → (−x, −y).",
  "<b>Enlargement</b> with centre the origin and scale factor k: (x, y) → (kx, ky). Translation, reflection and rotation do not change size; enlargement does.",
])
O("Find the image of the point (3, 2) after a reflection in the x-axis.",
  ["(3, −2)", "(−3, 2)", "(2, 3)", "(−3, −2)"],
  ["Reflecting in the x-axis keeps x and changes the sign of y.", "So (3, 2) → <b>(3, −2)</b>."],
  ok=True)
O("The point (1, 4) is translated by the vector " + V(2, "−3") + ". Find its image.",
  ["(3, 1)", "(3, 7)", "(−1, 7)", "(2, −3)"],
  ["Add the vector to the coordinates: (1 + 2, 4 + (−3)).", "= <b>(3, 1)</b>."],
  ok=((1 + 2, 4 - 3) == (3, 1)))
O("Find the image of (2, 0) after a rotation of 90° anticlockwise about the origin.",
  ["(0, 2)", "(0, −2)", "(−2, 0)", "(2, 0)"],
  ["A 90° anticlockwise rotation sends (x, y) to (−y, x).", "So (2, 0) → (0, 2), that is <b>(0, 2)</b>."],
  ok=True)
O("Find the image of (−5, 6) after a reflection in the y-axis.",
  ["(5, 6)", "(−5, −6)", "(5, −6)", "(6, −5)"],
  ["Reflecting in the y-axis changes the sign of x and keeps y.", "So (−5, 6) → <b>(5, 6)</b>."],
  ok=True)
O("The point (2, −1) is enlarged with centre the origin and scale factor 3. Find its image.",
  ["(6, −3)", "(5, 2)", "(6, −1)", "(2, −3)"],
  ["Multiply both coordinates by the scale factor 3.", "(2 × 3, −1 × 3) = <b>(6, −3)</b>."],
  ok=((2 * 3, -1 * 3) == (6, -3)))
T("Triangle ABC has vertices A(1, 1), B(4, 1) and C(1, 3). "
  "(a) Find the image A′B′C′ after a reflection in the x-axis. "
  "(b) Find the image A″B″C″ after translating ABC by the vector " + V("−2", 4) + ". "
  "(c) Which of the two transformations changes the area of the triangle?",
  ["(a) Reflection in the x-axis: (x, y) → (x, −y).",
   "A′(1, −1),  B′(4, −1),  C′(1, −3).",
   "(b) Translation by (−2, 4): (x, y) → (x − 2, y + 4).",
   "A″(−1, 5),  B″(2, 5),  C″(−1, 7).",
   "(c) <b>Neither</b> — reflection and translation are rigid motions, so the area stays ½ × 3 × 2 = 3 square units. "
   "Only an enlargement would change the area."],
  marks=9, ok=(0.5 * 3 * 2 == 3))
extras("transform",
  plain="A transformation moves a shape to a new position. Three of them — translation, reflection and rotation — are "
        "'rigid': the shape keeps its size and shape, only its position changes. Enlargement is the odd one out, because it makes the shape bigger or smaller.",
  examples=[
    E("Find the image of (4, −2) after a rotation of 180° about the origin.",
      "Step 1. A 180° rotation sends (x, y) to (−x, −y).",
      "Step 2. x = 4 → −4 and y = −2 → +2.",
      "Step 3. The image is <b>(−4, 2)</b>."),
    E("A triangle of area 6 cm² is enlarged by scale factor 2. Find the area of the image.",
      "Step 1. Lengths are multiplied by 2.",
      "Step 2. Area is multiplied by the square of the scale factor: 2² = 4.",
      "Step 3. New area = 6 × 4 = <b>24 cm²</b>.")])

topic("bearing", "Bearings", C, [
  "A bearing is measured from <b>north</b>, turning <b>clockwise</b>, and is always written with three figures: 045°, not 45°.",
  "North = 000°, East = 090°, South = 180°, West = 270°.",
  "Back bearing: if the first bearing is less than 180°, add 180°; if it is more than 180°, subtract 180°.",
  "Always draw a north arrow at each point before you start working.",
])
O("What is the bearing of due west?",
  ["270°", "090°", "180°", "360°"],
  ["A bearing is always measured <b>clockwise from north</b> and written with three figures.",
   "Start at north and turn clockwise: east 090°, south 180°, west <b>270°</b>."],
  v=270)
O("The bearing of B from A is 050°. What is the bearing of A from B?",
  ["230°", "310°", "130°", "050°"],
  ["The first bearing is less than 180°, so add 180°.", "50 + 180 = <b>230°</b>."],
  v=50 + 180)
O("What is the bearing of the direction south-east?",
  ["135°", "045°", "225°", "315°"],
  ["South-east is halfway between south (180°) and east (090°).", "(90 + 180) ÷ 2 = <b>135°</b>."],
  v=135)
O("B is on a bearing of 120° from A. What is the bearing of A from B?",
  ["300°", "240°", "060°", "120°"],
  ["120° is less than 180°, so add 180°.", "120 + 180 = <b>300°</b>."],
  v=120 + 180)
O("Bearings are measured",
  ["from north in a clockwise direction", "from north in an anticlockwise direction",
   "from east in a clockwise direction", "from south in a clockwise direction"],
  ["By agreement, every bearing starts at north and turns clockwise.",
   "So bearings are measured <b>from north in a clockwise direction</b>."],
  ok=True)
T("A fisherman sails 8 km from P on a bearing of 090° to Q, then 6 km from Q on a bearing of 180° to R. "
  "(a) Sketch the journey. (b) How far is R from P? (c) What kind of angle is PQR?",
  ["(a) From P go due east 8 km to Q, then due south 6 km to R.",
   "(b) East and south are at right angles, so use Pythagoras: PR² = 8² + 6² = 64 + 36 = 100.",
   "PR = √100 = <b>10 km</b>.",
   "(c) Angle PQR is between the westward direction back to P and the southward direction to R, so it is a "
   "<b>right angle (90°)</b>."],
  marks=8, fig=draw.compass([(90, "Q, 8 km", 0.9), (180, "R", 0.7)], label="P to Q to R"),
  ok=(8 ** 2 + 6 ** 2 == 10 ** 2))
extras("bearing",
  plain="A bearing answers the question 'in which direction?' with a number instead of a word. The two rules that matter: "
        "always start from north and turn clockwise, and always write three figures. Sketch a north arrow first — most lost marks come from not drawing it.",
  examples=[
    E("The bearing of Q from P is 215°. Find the bearing of P from Q.",
      "Step 1. 215° is more than 180°, so subtract 180°.",
      "Step 2. 215 − 180 = 35.",
      "Step 3. Written with three figures, the bearing is <b>035°</b>."),
    E("A boy walks 5 km due north then 5 km due east. Find his bearing from the starting point.",
      "Step 1. Sketch it: the path makes a right-angled triangle with equal legs.",
      "Step 2. Equal legs mean the direct line makes 45° with the north direction.",
      "Step 3. The bearing is therefore <b>045°</b> (and the distance is 5√2 ≈ 7.1 km).")])

topic("measure", "Time, speed & measurement", C, [
  "Speed = distance ÷ time;  distance = speed × time;  time = distance ÷ speed.",
  "To change km/h to m/s, multiply by 1 000 and divide by 3 600 (that is, divide by 3.6).",
  "Average speed = <b>total</b> distance ÷ <b>total</b> time, including stops — never the average of the speeds.",
  "Metric units: 1 km = 1 000 m, 1 m = 100 cm, 1 kg = 1 000 g, 1 litre = 1 000 ml.",
])
O("Change 2.5 hours to minutes.",
  ["150", "125", "250", "205"],
  ["1 hour = 60 minutes.", "2.5 × 60 = <b>150 minutes</b>."],
  v=150)
O("A car travels 180 km in 3 hours. Find its average speed.",
  ["60 km/h", "540 km/h", "45 km/h", "90 km/h"],
  ["Speed = distance ÷ time = 180 ÷ 3.", "= <b>60 km/h</b>."],
  v=60, nv=[60, 540, 45, 90])
O("Express 72 km/h in metres per second.",
  ["20 m/s", "72 m/s", "200 m/s", "12 m/s"],
  ["72 km = 72 000 m and 1 hour = 3 600 s.", "72 000 ÷ 3 600 = <b>20 m/s</b>."],
  v=20, nv=[20, 72, 200, 12])
O("How far does a bus travel in 2½ hours at an average speed of 50 km/h?",
  ["125 km", "100 km", "20 km", "250 km"],
  ["Distance = speed × time = 50 × 2.5.", "= <b>125 km</b>."],
  v=50 * 2.5, nv=[125, 100, 20, 250])
O("A bus leaves Accra at 08:45 and reaches Kumasi at 11:20. How long did the journey take?",
  ["2 hours 35 minutes", "3 hours 35 minutes", "2 hours 45 minutes", "3 hours 25 minutes"],
  ["From 08:45 to 11:45 would be 3 hours, but the bus arrives 25 minutes earlier.",
   "3 hours − 25 minutes = <b>2 hours 35 minutes</b>."],
  ok=((11 * 60 + 20) - (8 * 60 + 45) == 155))
T("A cyclist rides 24 km from his village to town at 16 km/h, rests for 30 minutes, and returns at 12 km/h. "
  "(a) How long did the outward journey take? (b) How long did the return journey take? "
  "(c) Find his average speed for the whole journey, including the rest.",
  ["(a) Time = distance ÷ speed = 24 ÷ 16 = 1.5 hours (<b>1 h 30 min</b>).",
   "(b) Time = 24 ÷ 12 = <b>2 hours</b>.",
   "(c) Total distance = 24 + 24 = 48 km. Total time = 1.5 + 0.5 + 2 = 4 hours.",
   "Average speed = 48 ÷ 4 = <b>12 km/h</b>. (Note it is not the average of 16 and 12, because of the rest and the different times.)"],
  marks=9, ok=(close(48 / (24 / 16 + 0.5 + 24 / 12), 12)))
extras("measure",
  plain="Distance, speed and time are three faces of one triangle: cover the one you want and the triangle tells you what "
        "to do with the other two. The one rule students forget is that average speed uses the <b>totals</b>, so a rest adds time but no distance.",
  examples=[
    E("A train covers 150 km at 50 km/h and the next 150 km at 75 km/h. Find the average speed for the whole trip.",
      "Step 1. First part: 150 ÷ 50 = 3 hours. Second part: 150 ÷ 75 = 2 hours.",
      "Step 2. Total distance = 300 km, total time = 5 hours.",
      "Step 3. Average speed = 300 ÷ 5 = <b>60 km/h</b> — not 62.5, the average of the two speeds."),
    E("Change 15 m/s to km/h.",
      "Step 1. Going from m/s to km/h, multiply by 3 600 and divide by 1 000 — that is, multiply by 3.6.",
      "Step 2. 15 × 3.6.",
      "Step 3. = <b>54 km/h</b>.")])

# ------------------------------------------------------------------ data
topic("stats", "Mean, median, mode & charts", D, [
  "<b>Mean</b> = total ÷ how many. <b>Median</b> = middle value when the data is arranged in order. <b>Mode</b> = the value that appears most often.",
  "With an even number of values, the median is the mean of the two middle ones.",
  "From a frequency table: mean = Σ(fx) ÷ Σf.",
  "In a pie chart, the whole circle is 360°, so each category's angle = (its frequency ÷ total) × 360°.",
])
O("Find the mean of 4, 8, 6, 10 and 12.",
  ["8", "10", "40", "6"],
  ["Total = 4 + 8 + 6 + 10 + 12 = 40.", "There are 5 numbers, so the mean = 40 ÷ 5 = <b>8</b>."],
  v=40 / 5)
O("Find the median of 3, 7, 9, 4 and 11.",
  ["7", "9", "6.8", "4"],
  ["Arrange in order first: 3, 4, 7, 9, 11.", "The middle value is <b>7</b>."],
  v=7)
O("Find the mode of 2, 3, 3, 5, 7, 3 and 8.",
  ["3", "5", "4.4", "8"],
  ["The mode is the value that occurs most often.", "3 appears three times, more than any other value, so the mode is <b>3</b>."],
  v=3)
O("In a pie chart, what angle represents 25% of the total?",
  ["90°", "25°", "180°", "100°"],
  ["The whole pie is 360°.", "25% of 360 = ¼ × 360 = <b>90°</b>."],
  v=0.25 * 360, nv=[90, 25, 180, 100])
O("The mean of 5 numbers is 12. Find their total.",
  ["60", "17", "12", "2.4"],
  ["Mean = total ÷ how many, so total = mean × how many.", "= 12 × 5 = <b>60</b>."],
  v=12 * 5)
T("The marks scored by 20 pupils in a test are given in the table below.<br>"
  "Mark: 2 (3 pupils), 3 (5 pupils), 4 (6 pupils), 5 (4 pupils), 6 (2 pupils).<br>"
  "(a) Find the mode. (b) Find the median. (c) Calculate the mean mark. (d) Draw a bar chart for the data.",
  ["(a) The highest frequency is 6, which belongs to the mark 4, so the mode is <b>4</b>.",
   "(b) With 20 pupils, the median is the mean of the 10th and 11th marks.",
   "Counting up: 3 pupils scored 2 (1st–3rd), 5 scored 3 (4th–8th), 6 scored 4 (9th–14th).",
   "Both the 10th and 11th pupils scored 4, so the median is <b>4</b>.",
   "(c) Σ(fx) = (2×3) + (3×5) + (4×6) + (5×4) + (6×2) = 6 + 15 + 24 + 20 + 12 = 77.",
   "Mean = 77 ÷ 20 = <b>3.85</b>.",
   "(d) Draw bars of equal width with heights 3, 5, 6, 4, 2, leaving gaps between them, and label both axes."],
  marks=12, fig=draw.barfig([("2", 3), ("3", 5), ("4", 6), ("5", 4), ("6", 2)],
                            label="Marks scored by 20 pupils", ylab="pupils"),
  ok=(close((2 * 3 + 3 * 5 + 4 * 6 + 5 * 4 + 6 * 2) / 20, 3.85)))
extras("stats",
  plain="Mean, median and mode are three different ways of saying 'the typical value'. Mean is the fair share, median is "
        "the middle one once you line the data up, and mode is the most popular. The commonest exam slip is forgetting to put the data in order before finding the median.",
  examples=[
    E("The mean age of 6 pupils is 13 years. One pupil aged 18 leaves. Find the mean age of those remaining.",
      "Step 1. Total age of the 6 pupils = 13 × 6 = 78 years.",
      "Step 2. After the 18-year-old leaves: 78 − 18 = 60 years shared among 5 pupils.",
      "Step 3. New mean = 60 ÷ 5 = <b>12 years</b>."),
    E("In a survey of 60 people, 20 chose rice. What angle would rice have in a pie chart?",
      "Step 1. Fraction choosing rice = 20/60 = 1/3.",
      "Step 2. Angle = 1/3 × 360°.",
      "Step 3. = <b>120°</b>.",
      fig=draw.piefig([("Rice", 20), ("Yam", 15), ("Banku", 15), ("Other", 10)], label="Food survey of 60 people"))])

topic("prob", "Probability", D, [
  "Probability = (number of favourable outcomes) ÷ (total number of possible outcomes).",
  "Every probability lies between 0 (impossible) and 1 (certain).",
  "P(not A) = 1 − P(A).",
  "Always simplify your fraction, and never write a probability bigger than 1.",
])
O("A fair coin is tossed once. What is the probability of getting a head?",
  [F(1, 2), F(1, 4), "1", F(1, 3)],
  ["There are 2 equally likely outcomes: head or tail.", "Only one of them is a head, so P(head) = <b>1/2</b>."],
  v=Fr(1, 2), nv=[Fr(1, 2), Fr(1, 4), 1, Fr(1, 3)])
O("A bag contains 3 red and 5 blue balls. One ball is picked at random. Find the probability that it is red.",
  [F(3, 8), F(3, 5), F(5, 8), F(1, 3)],
  ["Total balls = 3 + 5 = 8.", "Red balls = 3, so P(red) = <b>3/8</b>."],
  v=Fr(3, 8), nv=[Fr(3, 8), Fr(3, 5), Fr(5, 8), Fr(1, 3)])
O("A fair die is rolled once. What is the probability of getting a number greater than 4?",
  [F(1, 3), F(1, 2), F(1, 6), F(2, 3)],
  ["The numbers greater than 4 are 5 and 6 — that is 2 outcomes out of 6.",
   "P = 2/6 = <b>1/3</b>."],
  v=Fr(1, 3), nv=[Fr(1, 3), Fr(1, 2), Fr(1, 6), Fr(2, 3)])
O("A bag contains 3 red and 5 blue balls. Find the probability that a ball picked at random is NOT red.",
  [F(5, 8), F(3, 8), F(1, 2), F(5, 3)],
  ["P(red) = 3/8, and P(not red) = 1 − P(red).", "1 − 3/8 = <b>5/8</b> (which is also 5 blue out of 8)."],
  v=Fr(5, 8), nv=[Fr(5, 8), Fr(3, 8), Fr(1, 2), Fr(5, 3)])
O("In a class of 20 pupils, 12 are girls. If a pupil is chosen at random, find the probability that a boy is chosen.",
  [F(2, 5), F(3, 5), F(1, 2), F(8, 12)],
  ["Boys = 20 − 12 = 8.", "P(boy) = 8/20 = <b>2/5</b>."],
  v=Fr(2, 5), nv=[Fr(2, 5), Fr(3, 5), Fr(1, 2), Fr(8, 12)])
T("A box contains 4 white, 6 black and 5 green identical beads. One bead is picked at random. Find the probability that it is "
  "(a) green, (b) not white, (c) white or black. Give each answer as a fraction in its lowest terms.",
  ["Total beads = 4 + 6 + 5 = 15.",
   "(a) P(green) = 5/15 = <b>1/3</b>.",
   "(b) P(white) = 4/15, so P(not white) = 1 − 4/15 = <b>11/15</b>.",
   "(c) White or black = 4 + 6 = 10 beads, so P = 10/15 = <b>2/3</b>.",
   "Check: the three answers are each between 0 and 1, and P(green) + P(not green) = 1/3 + 2/3 = 1. ✓"],
  marks=9, ok=(Fr(5, 15) == Fr(1, 3) and 1 - Fr(4, 15) == Fr(11, 15) and Fr(10, 15) == Fr(2, 3)))
extras("prob",
  plain="Probability measures how likely something is, on a scale from 0 to 1. Count the outcomes you want, count all the "
        "outcomes there are, and write the first over the second. If the question says 'not', work out the ordinary probability first and take it from 1.",
  examples=[
    E("A letter is chosen at random from the word MATHEMATICS. Find the probability that it is M.",
      "Step 1. Count the letters: M-A-T-H-E-M-A-T-I-C-S — that is 11 letters in all.",
      "Step 2. M appears twice.",
      "Step 3. P(M) = <b>2/11</b>."),
    E("The probability that it rains tomorrow is 0.35. What is the probability that it does not rain?",
      "Step 1. Use P(not A) = 1 − P(A).",
      "Step 2. 1 − 0.35.",
      "Step 3. = <b>0.65</b>.")])
