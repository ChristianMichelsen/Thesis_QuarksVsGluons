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



x = np.linspace(0.0, 10, 1000)

fig, ax = plt.subplots(figsize=(6, 4))
ax.quiver(0, 0, 1, 1, units = 'xy', scale = 1)
ax.axis('equal')
ax.set(x)















# ax.plot(x, y_train, '-', label='Training')
# ax.plot(x, y_val, '-', label='Validation')
# ax.axvline(0.5, 0, 0.9, ls='--', c='k', lw=2)

# ax.text(0.47, 0.8, 'Underfitting', 
#         horizontalalignment='right',
#         verticalalignment='center', 
#         transform=ax.transAxes,
#         fontsize=18,
#         )
# ax.text(0.53, 0.8, 'Overfitting', 
#         horizontalalignment='left',
#         verticalalignment='center', 
#         transform=ax.transAxes,
#         fontsize=18,
#         )

# ax.set(xlabel=fr'Complexity of $h$', 
#        ylabel=r'$R_\mathrm{emp}(h)$', 
#        xlim=(0, 1), ylim=(0, 0.6))
# ax.legend(loc='lower left', frameon=False)

# arrowed_spines(fig, ax)
# fig.tight_layout()

# if save_plots:
#     fig.savefig('overfitting.pdf', dpi=600)