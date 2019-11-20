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

model1 = True


if model1:
    x = np.linspace(0.0, 0.9, 1000)
else:
    x = np.linspace(0.0, 1.1, 1000)

y_train = np.exp(-3*x) /2 
y_val = x**2 - 1*x + 0.52
y_complexity = x**0.9 / 3

fig, ax = plt.subplots(figsize=(6, 4))

ax.plot(x, y_train, '-', label='Training' if model1 else 'Training Error')
if model1:
    ax.plot(x, y_val, '-', label='Validation')
else:
    ax.plot(x, y_complexity, '-', label='Complexity')
    ax.plot(x, y_complexity+y_train, '-', label='Validation Error')

xmin = x[np.argmin(y_complexity+y_train)]
ax.axvline(xmin, 0, 0.9, ls='--', c='k', lw=2)

ax.text(xmin-0.03, 0.8, 'Underfitting', 
        horizontalalignment='right',
        verticalalignment='center', 
        transform=ax.transAxes,
        fontsize=18,
        )
ax.text(xmin+0.03, 0.8, 'Overfitting', 
        horizontalalignment='left',
        verticalalignment='center', 
        transform=ax.transAxes,
        fontsize=18,
        )

ax.set(xlabel=fr'Complexity of $\mathcal{H}$', 
       ylabel=r'$R_\mathrm{emp}(h)$' if model1 else '',
       xlim=(0, 1), ylim=(0, 0.6))
ax.legend(loc='lower left', frameon=False)



if not model1:

    box = ax.get_position()

    if True:

        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

        # Put a legend to the right of the current axis
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)

    if False:
        # Shrink current axis's height by 10% on the bottom
        ax.set_position([box.x0, box.y0 + box.height * 0.1,
                        box.width, box.height * 0.9])

        # Put a legend below current axis
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
                fancybox=True, shadow=True, ncol=1)

    if False:
        ax.set_position([box.x0, 
                box.y0 + box.height * 0.1, 
                box.width, 
                box.height * 0.9])

        # Put a legend below current axis
        ax.legend(loc='lower center', bbox_to_anchor=(0.5, 1.05),
                fancybox=False, shadow=False, ncol=1, frameon=False)

arrowed_spines(fig, ax)

fig.tight_layout()

if save_plots:
    s = f'overfitting_1.pdf' if model1 else f'overfitting_2.pdf'
    fig.savefig(s, dpi=600)