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
equationA = 2*x - 3*y + 5*x*y + 19
equationB = 7*y - 11*x + 13*x*y + 23

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
dsolveResult = ode.solveNonLinearOde("RK45", equationSystem, [x, y], [0, 0], 10, 10)

# print
doc.append(pl.NoEscape("dsolve equation system with initial values 0, 0"))
doc.append(pl.NoEscape(sp.latex(dsolveResult.t, mode="equation*")))
doc.append(pl.NoEscape(sp.latex(dsolveResult.y[0], mode="equation*")))
doc.append(pl.NoEscape(sp.latex(dsolveResult.y[1], mode="equation*")))

# plot in file
tf.PlotInFile("image1", doc, dsolveResult)

# solve for initial values 1, 2
dsolveResult = ode.solveNonLinearOde("RK45", equationSystem, [x, y], [1, 2], 10, 10)

# print
doc.append(pl.NoEscape("dsolve equation system with initial values 1, 2"))
doc.append(pl.NoEscape(sp.latex(dsolveResult.t, mode="equation*")))
doc.append(pl.NoEscape(sp.latex(dsolveResult.y[0], mode="equation*")))
doc.append(pl.NoEscape(sp.latex(dsolveResult.y[1], mode="equation*")))

# plot in file
tf.PlotInFile("image2", doc, dsolveResult)

# generate PDF
doc.generate_pdf('latexOutput', clean_tex=False)