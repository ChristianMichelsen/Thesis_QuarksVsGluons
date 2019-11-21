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


from sklearn.datasets import make_regression
from sklearn.linear_model import Ridge
from iminuit import Minuit
from iminuit import minimize

np.random.seed(42)
# np.random.seed(34)

delta_x = 0

N = 9
x = np.linspace(delta_x, 2+delta_x, N)
xx = np.linspace(0, 2+2*delta_x, 1000)
y = np.random.normal(0, 10, N) #+ 30*(x-1)**2


z = np.polyfit(x, y, N)
f = np.poly1d(z)


fig, ax = plt.subplots(figsize=(6, 4))

ax.plot(x, y, 'ko')
# ax.plot(xx, f(xx), '-', lw=2)

lamb = 0

L = 2

for lamb in [0, 0.001, 0.1, 10]:

    # lamb = 0.0

    def least_squares_np(par):  # par is a numpy array here 
        fx = np.polyval(par, x) 

        reg = lamb*(par**2).sum() if L==2 else lamb*np.abs(par).sum()

        return np.sum((y - fx) ** 2) + reg

    m = Minuit.from_array_func(least_squares_np, z, errordef=1, pedantic=False)
    m.migrad()

    # print(m.values)
    # print(m.errors)

    z_fit = m.np_values()
    f_fit = np.poly1d(z_fit)
    y_fit = f_fit(xx)
    # print("")
    beta_sum = (z_fit**2).sum()
    # print()
    fit_val = least_squares_np(z_fit)
    
    if False:
        print("\n\n")
        print(lamb)
        print(fit_val)
        print(z)


    s2 = int(np.log10(beta_sum))
    s1 = int(np.round(beta_sum / 10**s2))
    
    # s = fr"$\lambda = {lamb:.3f}    $" + "\t" + fr"$|\beta|^2 = {s1} \times 10^{s2}$"
    s_lamb = fr"${lamb:.3f}$" if lamb < 10 else fr"${lamb:.2f}$"
    s = fr"$\lambda = $"+s_lamb+fr"$, \quad |\beta|^2 = {s1} \times 10^{s2}$"

    ax.plot(xx, y_fit, '-', lw=2, label=s) #r'$\lambda = $'+f'{lamb:.4f}')

ax.set(xlabel=r'$x$', ylabel=r'$f(x)$', 
    #    ylim=(-20, 50),
       )
ax.legend()

box = ax.get_position()

ax.set_position([box.x0, 
        box.y0 + box.height * 0.1, 
        box.width, 
        box.height * 0.9])

# Put a legend below current axis
ax.legend(loc='lower center', bbox_to_anchor=(0.5, 1.01),
        fancybox=False, shadow=False, ncol=2, frameon=False,
        fontsize=15)


# fig


# arrowed_spines(fig, ax)

# fig.tight_layout()

if save_plots:
    s = f'ridge.pdf' if L==2 else 'lasso.pdf'
    fig.savefig(s, dpi=600, bbox_inches='tight', pad_inches=0.1)