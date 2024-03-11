import ternary as tn
import matplotlib as mpl
import random as rd
import math

# set default figure parameters
mpl.rcParams['figure.dpi'] = 200
mpl.rcParams['figure.figsize'] = (4, 4)

# get proportion values values (
def functionProportions(proportions):
    s = 0.
    for i in range(len(proportions)):
        try:
            s += proportions[i] * rd.randint(0, 100)
        except ValueError:
            continue
    return -1. * s

# create figure with scale 1
figure, tax = tn.figure(scale=100)
# set size
figure.set_size_inches(10, 8)
# create heatmap
tax.heatmapf(functionProportions, boundary=True, style="triangular")
# set line boundary
tax.boundary(linewidth=2.0)
# set title
tax.set_title("proportion values Heatmap")
# set ticks format
tax.ticks(axis='lbr', linewidth=1, multiple=10)
# clear default matplotlibs ticks
tax.clear_matplotlib_ticks()
# Set Axis labels and Title
fontsize = 8
tax.left_corner_label("Donor-Control", fontsize=fontsize)
tax.right_corner_label("Recipient", fontsize=fontsize)
tax.top_corner_label("Lotka-Volterra", fontsize=fontsize)
# plot
#tax.show()
# save as figure
tax.savefig("image0.png")