import sympy as sp
import pylatex as pl
import utils.ode as ode
import utils.testFunctions as tf

# create document
doc = pl.Document("test")
# add math package
doc.packages.append(pl.Package('amsmath'))

# declare variable functions
x, y = sp.symbols('x, y')

# declare ecuations
equationA = (1*x - 0.2*x*y)
equationB = (0.5*x*y - 0.2*y)

# print
doc.append(pl.NoEscape("equations"))
doc.append(pl.NoEscape(sp.latex(equationA, mode="equation*")))
doc.append(pl.NoEscape(sp.latex(equationB, mode="equation*")))

# declare system of ecuations
equationSystem = (equationA, equationB)

# print
doc.append(pl.NoEscape("equation system"))
doc.append(pl.NoEscape(sp.latex(equationSystem, mode="equation*")))

# solve for initial values 1, 5
dsolveResult = ode.solveNonLinearOde("RK45", equationSystem, [x, y], [1, 5], 40, 100)

# print
doc.append(pl.NoEscape("dsolve equation system with initial values 1, 5"))
doc.append(pl.NoEscape(sp.latex(dsolveResult.t, mode="equation*")))
doc.append(pl.NoEscape(sp.latex(dsolveResult.y[0], mode="equation*")))
doc.append(pl.NoEscape(sp.latex(dsolveResult.y[1], mode="equation*")))

# plot in file
tf.PlotInFile("image1", doc, dsolveResult)

# generate PDF
doc.generate_pdf('latexOutput', clean_tex=False)