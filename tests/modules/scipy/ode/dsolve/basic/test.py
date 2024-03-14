import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import pylatex as pl

# function that returns dy/dt
def model(y,t):
    k = 0.3
    dydt = -k * y
    return dydt

# initial condition
y0 = 5

# time points
t = np.linspace(0,20)

# solve ODE
y = odeint(model,y0,t)

# plot results
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('y(t)')

# save as figure
plt.savefig("image1.png")

# create document
doc = pl.Document("test")

# put figure in latex doc
with doc.create(pl.Figure(position='h!')) as figure:
    figure.add_image("image1.png", width='300px')

# generate PDF
doc.generate_pdf('latexOutput', clean_tex=False)    