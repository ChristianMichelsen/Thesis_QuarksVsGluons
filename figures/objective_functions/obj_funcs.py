import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.style.use("/Volumes/hep/QuarksVsGluons/matplotlibrc")  # bmh
# mpl.rcParams['mathtext.fontset'] = 'cm'

save_plots = True

def arrowed_spines(fig, ax):

    xmin, xmax = ax.get_xlim() 
    ymin, ymax = ax.get_ylim()

    # removing the default axis on all sides:
    for side in ['bottom','right','top','left']:
        ax.spines[side].set_visible(False)

    # removing the axis ticks
    plt.xticks([]) # labels 
    plt.yticks([])
    ax.xaxis.set_ticks_position('none') # tick markers
    ax.yaxis.set_ticks_position('none')

    # get width and height of axes object to compute 
    # matching arrowhead length and width
    dps = fig.dpi_scale_trans.inverted()
    bbox = ax.get_window_extent().transformed(dps)
    width, height = bbox.width, bbox.height

    # manual arrowhead width and length
    hw = 1./20.*(ymax-ymin) 
    hl = 1./20.*(xmax-xmin)
    lw = 1. # axis line width
    ohg = 0.3 # arrow overhang

    # compute matching arrowhead length and width
    yhw = hw/(ymax-ymin)*(xmax-xmin)* height/width 
    yhl = hl/(xmax-xmin)*(ymax-ymin)* width/height

    # draw x and y axis
    ax.arrow(xmin, 0, xmax-xmin, 0., fc='k', ec='k', lw = lw, 
             head_width=hw, head_length=hl, overhang = ohg, 
             length_includes_head= True, clip_on = False) 

    ax.arrow(0, ymin, 0., ymax-ymin, fc='k', ec='k', lw = lw, 
             head_width=yhw, head_length=yhl, overhang = ohg, 
             length_includes_head= True, clip_on = False)


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
ax.set(xlabel=r'$y-\hat{y}$', ylabel=r'$\ell(y, \hat{y})$', ylim=(0, 8))

# arrowed_spines(fig, ax)

# Shrink current axis's height by 10% on the bottom
box = ax.get_position()
ax.set_position([box.x0, 
                box.y0 + box.height * 0.1, 
                box.width, 
                box.height * 0.9])

# Put a legend below current axis
ax.legend(loc='lower center', bbox_to_anchor=(0.5, 1.05),
        fancybox=False, shadow=False, ncol=3, frameon=False)
fig.tight_layout()




fig2, ax2 = plt.subplots(figsize=(6, 4))

x = np.linspace(0, 2, 1000)

for name, loss in losses.items():
    ax2.plot(x, loss(x), '-', label=name, lw=4)
ax2.set(xlabel=r'$y-\hat{y}$', ylabel=r'$\ell(y, \hat{y})$', ylim=(0, 1.5))

box = ax2.get_position()
ax2.set_position([box.x0, 
                box.y0 + box.height * 0.1, 
                box.width, 
                box.height * 0.9])

# Put a legend below current axis
ax2.legend(loc='lower center', bbox_to_anchor=(0.5, 1.05),
        fancybox=False, shadow=False, ncol=3, frameon=False)
fig2.tight_layout()


if save_plots:
    fig.savefig('objective_functions.pdf', dpi=600, bbox_inches="tight")
    fig2.savefig('objective_functions_zoom.pdf', dpi=600, bbox_inches="tight")