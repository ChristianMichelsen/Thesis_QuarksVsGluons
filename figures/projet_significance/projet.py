import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.special import expit, logit
from scipy.stats import norm, expon

plt.style.use("/Volumes/hep/QuarksVsGluons/matplotlibrc")  # bmh

save_plots = True

xrange=(-5, 7)

x = np.linspace(*xrange, 1000)

N = 100000
N_b = 40000
l = np.random.normal(0, 1, N)
b = np.r_[np.random.normal(0, 0.95, N), np.random.exponential(5, N_b)]

weight = 0.8
weights = np.r_[np.ones(N), weight*np.ones(N_b)]

fig, ax = plt.subplots(figsize=(4,6))

# ax.plot(x, y_l, '-', label=r'$uds$', lw=2.5)
# ax.plot(x, y_b, '-', label=r'$b$', lw=2.5)
ax.hist(l, 100, range=xrange, histtype='step', label=r'$uds$')
ax.hist(b, 100, weights=weights, range=xrange, histtype='step', label=r'$b$')

ax.set_xlabel(r"$\mathcal{S}$", fontsize=30)
ax.set_ylabel("Counts")

ax.set(xlim=xrange)

ax.legend(loc='upper center', fontsize=20)



box = ax.get_position()

ax.set_position([box.x0, 
        box.y0 + box.height * 0.1, 
        box.width, 
        box.height * 0.9])

# Put a legend below current axis
ax.legend(loc='lower center', bbox_to_anchor=(0.45, 1.01),
        fancybox=False, shadow=False, ncol=1, frameon=False,
        fontsize=24)


fig.tight_layout()

if save_plots:
    fig.savefig(f'projet_significance.pdf', dpi=600, bbox_inches='tight', pad_inches=0)
