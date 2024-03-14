import sympy as sp
import pylatex as pl
import utils.ode as ode
import utils.testFunctions as tf

# create document
doc = pl.Document("test")
# add math package
doc.packages.append(pl.Package('amsmath'))

# declare variable symbols
t = sp.symbols('t')
# declare variable functions
x, y = sp.symbols('x, y')

# general model
donorControlA = (0.7*x - 0.2*y)
recipientA = (0.5*y - 0.1*x)
lotkaVolterraA = (0.3*x*y - 0.7*x*y)
exportsA = 0.6*x
donorControlB = (0.6*y - 0.4*x)
recipientB = (0.8*x - 0.2*y)
lotkaVolterraB = (0.45*x*y - 0.6*x*y)
exportsB = 0.5*y

# declare ecuations
equationA = donorControlA + recipientA + lotkaVolterraA - exportsA + 1.3
equationB = donorControlB + recipientB + lotkaVolterraB - exportsB + 2.1

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