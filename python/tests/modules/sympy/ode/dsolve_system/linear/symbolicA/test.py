import sympy as sp
from sympy.abc import x
import pylatex as pl
import utils.testFunctions as tf

# create document
doc = pl.Document("test")
# add math package
doc.packages.append(pl.Package('amsmath'))

# declare variable symbols
t = sp.symbols('t')
a = sp.symbols('a')
b = sp.symbols('b')
c = sp.symbols('c')
d = sp.symbols('d')
e = sp.symbols('e')
f = sp.symbols('f')
# declare variable functions
x, y = sp.symbols('x, y', cls = sp.Function)

# declare ecuations
equationA = sp.Eq(sp.Derivative(x(t),t), (a*x(t) + b*y(t) + c))
equationB = sp.Eq(sp.Derivative(y(t),t), (d*x(t) + e*y(t) + f))

# evaluate terms
equationA = equationA.subs({a : 2, b : 5, c : 11})
equationB = equationB.subs({d : 3, e : 7, f : 13})

# print
doc.append(pl.NoEscape("equations"))
doc.append(pl.NoEscape(sp.latex(equationA, mode="equation*")))
doc.append(pl.NoEscape(sp.latex(equationB, mode="equation*")))

# declare system of ecuations
equationSystem = (equationA, equationB)

# print
doc.append(pl.NoEscape("equation system"))
doc.append(pl.NoEscape(sp.latex(equationSystem, mode="equation*")))

# solve
dsolveResult = sp.solvers.ode.systems.dsolve_system(equationSystem, funcs=[x(t),y(t)], ics={x(0): 0, y(0): 0})

# print
doc.append(pl.NoEscape("dsolve equation system with initial values 0, 0"))
doc.append(pl.NoEscape(sp.latex(dsolveResult[0][0], mode="equation*")))
doc.append(pl.NoEscape(sp.latex(dsolveResult[0][1], mode="equation*")))

# evaluate and plot
tf.EvaluateAndPlot("image1", doc, dsolveResult[0][0], dsolveResult[0][1], t)

# solve
dsolveResult = sp.solvers.ode.systems.dsolve_system(equationSystem, funcs=[x(t),y(t)], ics={x(0): 1, y(0): 2})

# print
doc.append(pl.NoEscape("dsolve equation system with initial values 1, 2"))
doc.append(pl.NoEscape(sp.latex(dsolveResult[0][0], mode="equation*")))
doc.append(pl.NoEscape(sp.latex(dsolveResult[0][1], mode="equation*")))

# evaluate and plot
tf.EvaluateAndPlot("image2", doc, dsolveResult[0][0], dsolveResult[0][1], t)

# generate PDF
doc.generate_pdf('latexOutput', clean_tex=False)