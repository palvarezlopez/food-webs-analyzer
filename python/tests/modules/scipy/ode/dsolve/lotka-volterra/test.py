import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import pylatex as pl

alpha = 1 # 1/day
beta = 0.2 # 1/wolves/day
delta = 0.5 # 1/rabbits/day
gamma = 0.2 # 1/day

def diffeq(t,pop):
  x,y = pop
  return [alpha*x-beta*x*y,
          delta*x*y-gamma*y]

sol = sp.integrate.solve_ivp(diffeq,
                             t_span = [0,40],
                             y0=[1,5],
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