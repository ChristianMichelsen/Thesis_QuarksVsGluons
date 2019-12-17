import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.style.use("/Volumes/hep/QuarksVsGluons/matplotlibrc")  # bmh
# mpl.rcParams['mathtext.fontset'] = 'cm'

save_plots = True

def ae(z):
    return np.sqrt(np.square(z))


def se(z):
    return np.square(z)


def logcosh(z):
    return np.log(np.cosh(z))

def cauchy(z):
    C = 0.1
    C = 1
    return np.log(0.5*(z/C)**2 + 1)

def welsch(z):
    C = 0.1
    C = 1
    return 1 - np.exp(-0.5*(z/C)**2)

def fair(z):
    c = 100
    c = 1
    return c**2 * (np.abs(z) / c - np.log(np.abs(z)/c + 1))

losses = {'SE': se, 'AE': ae, 'LogCosh': logcosh, r'Cauchy': cauchy, r'Welsch': welsch, r'Fair': fair}


fig, ax = plt.subplots(figsize=(9, 6))

x = np.linspace(0, 7, 1000)

for name, loss in losses.items():
    ax.plot(x, loss(x), '-', label=name, lw=3)
ax.legend()
ax.set(ylim=(0, 8))
ax.set_xlabel(r'$y-\hat{y}$', fontsize=30)
ax.set_ylabel(r'$\ell(y, \hat{y})$', fontsize=30)


# arrowed_spines(fig, ax)

# Shrink current axis's height by 10% on the bottom
box = ax.get_position()
ax.set_position([box.x0, 
                box.y0 + box.height * 0.1, 
                box.width, 
                box.height * 0.9])

# Put a legend below current axis
ax.legend(loc='lower center', bbox_to_anchor=(0.5, 1.05),
        fancybox=False, shadow=False, ncol=3, frameon=False, fontsize=24)
fig.tight_layout()




fig2, ax2 = plt.subplots(figsize=(6, 4))

x = np.linspace(0, 2, 1000)

for name, loss in losses.items():
    ax2.plot(x, loss(x), '-', label=name, lw=4)
# ax2.set(xlabel=r'$y-\hat{y}$', ylabel=r'$\ell(y, \hat{y})$', ylim=(0, 1.5))
ax2.set(ylim=(0, 1.5))
ax2.set_xlabel(r'$y-\hat{y}$', fontsize=30)
ax2.set_ylabel(r'$\ell(y, \hat{y})$', fontsize=30)



box = ax2.get_position()
ax2.set_position([box.x0, 
                box.y0 + box.height * 0.1, 
                box.width, 
                box.height * 0.9])

# Put a legend below current axis
ax2.legend(loc='lower center', bbox_to_anchor=(0.5, 1.05),
        fancybox=False, shadow=False, ncol=2, frameon=False, fontsize=20)
fig2.tight_layout()


if save_plots:
    fig.savefig('objective_functions.pdf', dpi=600, bbox_inches="tight")
    fig2.savefig('objective_functions_zoom.pdf', dpi=600, bbox_inches="tight")