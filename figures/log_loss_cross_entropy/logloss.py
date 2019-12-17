import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.style.use("/Volumes/hep/QuarksVsGluons/matplotlibrc")  # bmh

save_plots = True


def logloss(true_label, predicted_prob):
  if true_label == 1:
    return -np.log(predicted_prob)
  else:
    return -np.log(1 - predicted_prob)


x = np.linspace(1e-3, 1-1e-3, 1000)
y_0 = logloss(0, x)
y_1 = logloss(1, x)

fig, ax = plt.subplots(figsize=(4,4))
ax.plot(x, y_0, '-', label=r'$y=0$')
ax.plot(x, y_1, '-', label=r'$y=1$')
ax.set_xlabel(r"$\hat{y}$", fontsize=30)
ax.set_ylabel(r"$\ell_\mathrm{log}$", fontsize=30)

ax.legend(loc='upper center', fontsize=20)

fig.tight_layout()

if save_plots:
    fig.savefig(f'logloss.pdf', dpi=600, bbox_inches='tight', pad_inches=0)


# box = ax.get_position()

# ax.set_position([box.x0, 
#         box.y0 + box.height * 0.1, 
#         box.width, 
#         box.height * 0.9])

# # Put a legend below current axis
# ax.legend(loc='lower center', bbox_to_anchor=(0.45, 1.01),
#         fancybox=False, shadow=False, ncol=1, frameon=False,
#         fontsize=20)
