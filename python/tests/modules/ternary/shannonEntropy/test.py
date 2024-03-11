import ternary as tn
import matplotlib as mpl
import math

# set default figure parameters
mpl.rcParams['figure.dpi'] = 200
mpl.rcParams['figure.figsize'] = (4, 4)

# compute shannon entropy
def shannon_entropy(p):
    """Computes the Shannon Entropy at a distribution in the simplex."""
    s = 0.
    for i in range(len(p)):
        try:
            s += p[i] * math.log(p[i])
        except ValueError:
            continue
    return -1. * s

scale = 60
figure, tax = tn.figure(scale=scale)
figure.set_size_inches(10, 8)
tax.heatmapf(shannon_entropy, boundary=True, style="triangular")
tax.boundary(linewidth=2.0)
tax.set_title("Shannon Entropy Heatmap")
tax.ticks(axis='lbr', linewidth=1, multiple=5)
tax.clear_matplotlib_ticks()
tax.get_axes().axis('off')
# save as figure
tax.savefig("image0.png")