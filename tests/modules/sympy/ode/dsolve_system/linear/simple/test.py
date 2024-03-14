import sympy as sp
import pylatex as pl
import utils.testFunctions as tf

# create document
doc = pl.Document("test")
# add math package
doc.packages.append(pl.Package('amsmath'))

# declare variable symbols
t = sp.symbols('t')
# declare variable functions
x, y = sp.symbols('x, y', cls = sp.Function)

# declare ecuations
equationA = sp.Eq(sp.Derivative(x(t),t), (x(t) + y(t)))
equationB = sp.Eq(sp.Derivative(y(t),t), (x(t) + y(t)))

# print
doc.append(pl.NoEscape("equations"))
doc.append(pl.NoEscape(sp.latex(equationA, mode="equation*")))
doc.append(pl.NoEscape(sp.latex(equationB, mode="equation*")))

# declare system of ecuations
equationSystem = (equationA, equationB)

# print
doc.append(pl.NoEscape("equation system"))
doc.append(pl.NoEscape(sp.latex(equationSystem, mode="equation*")))

# solve for initial values 0, 0
dsolveResult = sp.solvers.ode.systems.dsolve_system(equationSystem, funcs=[x(t),y(t)], ics={x(0): 0, y(0): 0})

# print
doc.append(pl.NoEscape("dsolve equation system with initial values 0, 0"))
doc.append(pl.NoEscape(sp.latex(dsolveResult[0][0], mode="equation*")))
doc.append(pl.NoEscape(sp.latex(dsolveResult[0][1], mode="equation*")))

# evaluate and plot
tf.EvaluateAndPlot("image1", doc, dsolveResult[0][0], dsolveResult[0][1], t)

# solve for initial values 1, 2
dsolveResult = sp.solvers.ode.systems.dsolve_system(equationSystem, funcs=[x(t),y(t)], ics={x(0): 1, y(0): 2})

# print
doc.append(pl.NoEscape("dsolve equation system with initial values 1, 2"))
doc.append(pl.NoEscape(sp.latex(dsolveResult[0][0], mode="equation*")))
doc.append(pl.NoEscape(sp.latex(dsolveResult[0][1], mode="equation*")))

# evaluate and plot
tf.EvaluateAndPlot("image2", doc, dsolveResult[0][0], dsolveResult[0][1], t)

# generate PDF
doc.generate_pdf('latexOutput', clean_tex=False)