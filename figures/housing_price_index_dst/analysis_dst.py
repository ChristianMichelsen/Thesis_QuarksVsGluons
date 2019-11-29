import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

plt.style.use("/Volumes/hep/QuarksVsGluons/matplotlibrc")  # bmh
# mpl.rcParams['mathtext.fontset'] = 'cm'

is_wide = True


if is_wide:
    figsize = (12, 4)
    name_str = 'wide'
else:
    figsize = (6, 6)
    name_str = 'tall'


file = 'price_index_sales_of_property.xlsx'
df_DK  = pd.read_excel(file, 'Danmark')
df_CPH = pd.read_excel(file, 'København')

index = pd.to_datetime(df_DK.columns[1:])

df_houses = pd.DataFrame({'DK': df_DK.iloc[0, 1:], 'CPH': df_CPH.iloc[0, 1:]}, index=index, dtype=float)
df_aparts = pd.DataFrame({'DK': df_DK.iloc[1, 1:], 'CPH': df_CPH.iloc[1, 1:]}, index=index, dtype=float)


if True:
    df_houses.loc[:, 'DK']  /= df_houses.loc['2000-01-01', 'DK'] / 100
    df_houses.loc[:, 'CPH'] /= df_houses.loc['2000-01-01', 'CPH'] / 100

    df_aparts.loc[:, 'DK']  /= df_aparts.loc['2000-01-01', 'DK'] / 100
    df_aparts.loc[:, 'CPH'] /= df_aparts.loc['2000-01-01', 'CPH'] / 100


# df_houses.plot()
# df_aparts.plot()

def plot(df, ax, col, sigma, color, ls, label):
    ax.plot(df.index.values,
        df[col], ls=ls, color=color, label=label, lw=2)

    ax.fill_between(df.index.values, 
                    df[col]-sigma, 
                    df[col]+sigma,
                    color=color, alpha=0.1
                    )



# https://www.dst.dk/da/Statistik/Analyser/visanalyse?cid=27505

signa_multiplier = 2

sigma_house = 1.1 * signa_multiplier
sigma_apart = 1.7 * signa_multiplier

# Create the plot space upon which to plot the data
fig, ax = plt.subplots(figsize=figsize)

# Add the x-axis and the y-axis to the plot
plot(df_houses, ax, 'DK', sigma_house, 'C1', '-', 'Houses: DK')
plot(df_houses, ax, 'CPH', sigma_house, 'C1', '--', 'Houses: CPH')
plot(df_aparts, ax, 'DK', sigma_apart, 'C0', '-', 'Apartments: DK')
plot(df_aparts, ax, 'CPH', sigma_apart, 'C0', '--', 'Apartments: CPH')


# ax.plot(df_houses.index.values,
#         df_houses['CPH'], '--', color='C1', label='Houses: CPH', lw=3)
# ax.plot(df_aparts.index.values,
#         df_aparts['DK'], '-', color='C0', label='Apartments: DK', lw=3)
# ax.plot(df_aparts.index.values,
#         df_aparts['CPH'], '--', color='C0', label='Apartments: CPH', lw=3)

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Price Index",
       title="")

ax.legend()

# Clean up the x axis dates (reviewed in lesson 4)
# ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
# ax.xaxis.set_major_formatter(DateFormatter("%m/%d"))

fig.tight_layout()

fig.savefig(f'housingindex_{name_str}.pdf' , dpi=600)