import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.special import expit, logit

plt.style.use("/Volumes/hep/QuarksVsGluons/matplotlibrc")  # bmh

save_plots = True


y = np.linspace(-7, 7, 1000)
p = np.linspace(0, 1, 1000)

fig_expit, ax_expit = plt.subplots(figsize=(4,4))
ax_expit.plot(y, expit(y), '-')

ax_expit.set_xlabel(r"$\tilde{y}$", fontsize=30)
ax_expit.set_ylabel(r"$\mathrm{expit}(\tilde{y})$", fontsize=30)
# ax_expit.yaxis.set_major_locator(plt.MaxNLocator(3))
ax_expit.set_yticks([0, 0.5, 1])



# ax.legend(loc='upper center', fontsize=20)

fig_expit.tight_layout()

if save_plots:
    fig_expit.savefig(f'expit.pdf', dpi=600, bbox_inches='tight', pad_inches=0)




fig_logit, ax_logit = plt.subplots(figsize=(4,4))
ax_logit.plot(p, logit(p), '-')

ax_logit.set_xlabel(r"$p$", fontsize=30)
ax_logit.set_ylabel(r"$\mathrm{logit}(p)$", fontsize=30)

# ax.legend(loc='upper center', fontsize=20)

fig_logit.tight_layout()

if save_plots:
    fig_logit.savefig(f'logit.pdf', dpi=600, bbox_inches='tight', pad_inches=0)



# box = ax.get_position()

# ax.set_position([box.x0, 
#         box.y0 + box.height * 0.1, 
#         box.width, 
#         box.height * 0.9])

# # Put a legend below current axis
# ax.legend(loc='lower center', bbox_to_anchor=(0.45, 1.01),
#         fancybox=False, shadow=False, ncol=1, frameon=False,
#         fontsize=20)
