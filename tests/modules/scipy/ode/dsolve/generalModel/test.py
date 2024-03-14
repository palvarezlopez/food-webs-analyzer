import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import pylatex as pl

# general model parameters
sr = 0.3
sd = 0.2
Cd1ik = 0.1
Cd1ki = 0.2
Cr1ik = 0.5
Cr1ki = 0.3
Cl1ik = 0.6
Cl1ki = 0.8
q1 = 0.4
r1 = 0.5
p1 = 0.2
Cd2ik = 0.3
Cd2ki = 0.5
Cr2ik = 0.1
Cr2ki = 0.9
Cl2ik = 0.2
Cl2ki = 0.4
q2 = 0.1
r2 = 0.4
p2 = 0.7

# differential equations
def diffeq(t, pop):
    b1,b2 = pop

    eq1 = (sd * (Cd1ik * b1 - Cd1ki * b2) + sr * (Cr1ik * b2 - Cr1ki * b1) + (1 - sd - sr) * (Cl1ik * b1 * b2 - Cl1ki * b1 * b2)) - (q1 + r1) * b1 + p1
    eq2 = (sd * (Cd2ik * b2 - Cd2ki * b1) + sr * (Cr2ik * b1 - Cr2ki * b2) + (1 - sd - sr) * (Cl2ik * b2 * b1 - Cl2ki * b2 * b1)) - (q2 + r2) * b2 + p2

    return [eq1, eq2]

sol = sp.integrate.solve_ivp(diffeq,
                             t_span = [0,400],
                             y0=[1,5],
                             method='RK45',
                             t_eval=np.linspace(0,40,100))

plt.plot(sol.t, sol.y.T,'-')
plt.legend(['Rabbits','Wolves'])
plt.xlabel('Time [days]')
plt.ylabel('Population [#]')

# save as figure
plt.savefig("image1.png")

# create document
doc = pl.Document("test")

# put figure in latex doc
with doc.create(pl.Figure(position='h!')) as figure:
    figure.add_image("image1.png", width='300px')

# generate PDF
doc.generate_pdf('latexOutput', clean_tex=False)    