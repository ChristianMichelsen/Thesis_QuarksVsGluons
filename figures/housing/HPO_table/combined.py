import pandas as pd

input_string_lejlighed = """2.5        obj_rmse_xgb       True     MAD = 0.1664    226 141.33 sec
2.5        obj_rmse_xgb       False    MAD = 0.1770    201 115.78 sec
2.5        obj_logcos_xgb     True     MAD = 0.1595    333  75.88 sec
2.5        obj_logcos_xgb     False    MAD = 0.1523    496  57.56 sec
2.5        obj_cauchy_xgb     True     MAD = 0.1598    293  56.69 sec
2.5        obj_cauchy_xgb     False    MAD = 0.1466    814 101.81 sec
2.5        obj_welsch_xgb     True     MAD = 0.1628    285  64.97 sec
2.5        obj_welsch_xgb     False    MAD = 0.1517    718  90.27 sec
2.5        obj_fair_xgb       True     MAD = 0.1601    229  54.52 sec
2.5        obj_fair_xgb       False    MAD = 0.1577    304  45.37 sec
5          obj_rmse_xgb       True     MAD = 0.1623    301  90.76 sec
5          obj_rmse_xgb       False    MAD = 0.1786    375  82.93 sec
5          obj_logcos_xgb     True     MAD = 0.1606    280  66.47 sec
5          obj_logcos_xgb     False    MAD = 0.1513    734  96.82 sec
5          obj_cauchy_xgb     True     MAD = 0.1610    304  68.73 sec
5          obj_cauchy_xgb     False    MAD = 0.1468    923 110.73 sec
5          obj_welsch_xgb     True     MAD = 0.1600    257  62.70 sec
5          obj_welsch_xgb     False    MAD = 0.1499    702  91.30 sec
5          obj_fair_xgb       True     MAD = 0.1629    205  54.10 sec
5          obj_fair_xgb       False    MAD = 0.1549    343  51.52 sec
10         obj_rmse_xgb       True     MAD = 0.1618    318  97.01 sec
10         obj_rmse_xgb       False    MAD = 0.1893    226  56.09 sec
10         obj_logcos_xgb     True     MAD = 0.1618    367  83.00 sec
10         obj_logcos_xgb     False    MAD = 0.1590    351  52.44 sec
10         obj_cauchy_xgb     True     MAD = 0.1610    266  62.92 sec
10         obj_cauchy_xgb     False    MAD = 0.1450    770  97.11 sec
10         obj_welsch_xgb     True     MAD = 0.1601    272  62.50 sec
10         obj_welsch_xgb     False    MAD = 0.1466    771  99.30 sec
10         obj_fair_xgb       True     MAD = 0.1596    257  61.46 sec
10         obj_fair_xgb       False    MAD = 0.1573    332  47.52 sec
20         obj_rmse_xgb       True     MAD = 0.1626    265  81.01 sec
20         obj_rmse_xgb       False    MAD = 0.1799    687 124.19 sec
20         obj_logcos_xgb     True     MAD = 0.1609    269  62.81 sec
20         obj_logcos_xgb     False    MAD = 0.1587    333  49.76 sec
20         obj_cauchy_xgb     True     MAD = 0.1613    288  65.64 sec
20         obj_cauchy_xgb     False    MAD = 0.1467    967 117.27 sec
20         obj_welsch_xgb     True     MAD = 0.1603    260  61.11 sec
20         obj_welsch_xgb     False    MAD = 0.1486    876 107.35 sec
20         obj_fair_xgb       True     MAD = 0.1608    272  62.64 sec
20         obj_fair_xgb       False    MAD = 0.1537    403  56.82 sec
None       obj_rmse_xgb       True     MAD = 0.1600    405 110.08 sec
None       obj_rmse_xgb       False    MAD = 0.2036     94  32.45 sec
None       obj_logcos_xgb     True     MAD = 0.1595    388  83.23 sec
None       obj_logcos_xgb     False    MAD = 0.1648    268  42.87 sec
None       obj_cauchy_xgb     True     MAD = 0.1601    340  72.92 sec
None       obj_cauchy_xgb     False    MAD = 0.1480    807  99.76 sec
None       obj_welsch_xgb     True     MAD = 0.1584    310  69.70 sec
None       obj_welsch_xgb     False    MAD = 0.1459    973 115.32 sec
None       obj_fair_xgb       True     MAD = 0.1578    344  74.23 sec
None       obj_fair_xgb       False    MAD = 0.1527    453  59.45 sec"""


input_string_villa = """2.5        obj_rmse_xgb       True     MAD = 0.1983    458 339.03 sec
2.5        obj_rmse_xgb       False    MAD = 0.1913    844 439.78 sec
2.5        obj_logcos_xgb     True     MAD = 0.2018    346 223.64 sec
2.5        obj_logcos_xgb     False    MAD = 0.1877   1095 415.89 sec
2.5        obj_cauchy_xgb     True     MAD = 0.1991    434 244.82 sec
2.5        obj_cauchy_xgb     False    MAD = 0.1872   1007 356.45 sec
2.5        obj_welsch_xgb     True     MAD = 0.1960    867 440.06 sec
2.5        obj_welsch_xgb     False    MAD = 0.1897    835 300.14 sec
2.5        obj_fair_xgb       True     MAD = 0.1956    508 278.55 sec
2.5        obj_fair_xgb       False    MAD = 0.1882    862 301.02 sec
5          obj_rmse_xgb       True     MAD = 0.1968    733 478.04 sec
5          obj_rmse_xgb       False    MAD = 0.1888   1126 541.96 sec
5          obj_logcos_xgb     True     MAD = 0.1976    618 331.85 sec
5          obj_logcos_xgb     False    MAD = 0.1847   1601 546.10 sec
5          obj_cauchy_xgb     True     MAD = 0.1999    350 208.87 sec
5          obj_cauchy_xgb     False    MAD = 0.1858   1130 389.74 sec
5          obj_welsch_xgb     True     MAD = 0.2035    301 184.77 sec
5          obj_welsch_xgb     False    MAD = 0.1878    893 312.69 sec
5          obj_fair_xgb       True     MAD = 0.1957    506 278.89 sec
5          obj_fair_xgb       False    MAD = 0.1835   1357 462.49 sec
10         obj_rmse_xgb       True     MAD = 0.1999    434 310.81 sec
10         obj_rmse_xgb       False    MAD = 0.1884    917 444.97 sec
10         obj_logcos_xgb     True     MAD = 0.1990    506 280.97 sec
10         obj_logcos_xgb     False    MAD = 0.1873   1160 400.12 sec
10         obj_cauchy_xgb     True     MAD = 0.1992    436 240.50 sec
10         obj_cauchy_xgb     False    MAD = 0.1850   1183 394.25 sec
10         obj_welsch_xgb     True     MAD = 0.2014    341 200.99 sec
10         obj_welsch_xgb     False    MAD = 0.1869   1113 390.76 sec
10         obj_fair_xgb       True     MAD = 0.1946    875 436.28 sec
10         obj_fair_xgb       False    MAD = 0.1861    954 325.90 sec
20         obj_rmse_xgb       True     MAD = 0.2013    398 286.94 sec
20         obj_rmse_xgb       False    MAD = 0.1867   1206 575.66 sec
20         obj_logcos_xgb     True     MAD = 0.2011    445 269.68 sec
20         obj_logcos_xgb     False    MAD = 0.1876   1313 497.90 sec
20         obj_cauchy_xgb     True     MAD = 0.2003    397 242.91 sec
20         obj_cauchy_xgb     False    MAD = 0.1833   1514 542.05 sec
20         obj_welsch_xgb     True     MAD = 0.2022    338 209.16 sec
20         obj_welsch_xgb     False    MAD = 0.1875   1212 424.32 sec
20         obj_fair_xgb       True     MAD = 0.1943    763 402.40 sec
20         obj_fair_xgb       False    MAD = 0.1840   1256 435.50 sec
None       obj_rmse_xgb       True     MAD = 0.1977    730 505.01 sec
None       obj_rmse_xgb       False    MAD = 0.1876   1264 625.80 sec
None       obj_logcos_xgb     True     MAD = 0.1982    432 258.20 sec
None       obj_logcos_xgb     False    MAD = 0.1842   2151 739.10 sec
None       obj_cauchy_xgb     True     MAD = 0.1992    449 257.72 sec
None       obj_cauchy_xgb     False    MAD = 0.1844   1351 470.12 sec
None       obj_welsch_xgb     True     MAD = 0.1970    579 321.41 sec
None       obj_welsch_xgb     False    MAD = 0.1837   1497 509.49 sec
None       obj_fair_xgb       True     MAD = 0.1973    535 303.87 sec
None       obj_fair_xgb       False    MAD = 0.1844   1337 456.90 sec"""

do_villa = True
remove_time = False

if do_villa:
  input_string = input_string_villa
  type_str = 'villa'
else:
  input_string = input_string_lejlighed
  type_str = 'ejerlejlighed'

print(f"Running on {type_str}! \n\n")



df_org = pd.DataFrame([x.split() for x in input_string.split('\n')])
df_org = df_org.iloc[:, [1, 0, 2, 6, 7, 5]]
df_org.columns = ['obj', 'halflife', 'log10', 'N', 'time', 'MAD']
num_cols = ['N', 'time', 'MAD']
df = df_org[num_cols].apply(pd.to_numeric)
df.loc[:, 'obj'] = df_org['obj']
df.loc[:, 'log10'] = df_org['log10']

idx_mins = []
dfs = [x for _, x in df.groupby('obj')]
for dfi in dfs:
  idx_mins.append(dfi['MAD'].idxmin())

idx_best = df['MAD'].idxmin()
print(f"Best Objective: {df.iloc[idx_best].loc['obj']} \n\n")


dicts = {}
for obj in ['rmse', 'logcosh', 'cauchy', 'welsch', 'fair']:
  dicts[obj] = r"""
\begin{table}[h!]
  \begin{tabular}{@{}ccrrc@{}}
    %\toprule
    Half-life & $\log_{10}$ & $N_\mathrm{trees}$ & Time [$s$] & $f_\mathrm{eval}$ \\""" + "\n" + r"    \midrule" + "\n"

  if remove_time:
    dicts[obj] = dicts[obj].replace('ccrrc', 'ccrc').replace('& Time [$s$] ', '').replace(r'begin{table}[h!]', r'begin{margintable}')


for i, line in enumerate(input_string.splitlines()):
    line = line.replace('MAD = ', '')
    line = line.replace(' sec', '')
    line = line.replace('obj_', '')
    line = line.replace('_xgb', '')
    line = line.replace('logcos', 'logcosh')
    
    # words = line.split()

    halflife, obj, log10, MAD, N, time = line.split()
    

    if not remove_time:
      s = rf"    XX{halflife}YY & {log10} & XX{N}YY & XX{int(float(time))}YY & XX{MAD}YY \\" + "\n"
    else:
      s = rf"    XX{halflife}YY & {log10} & XX{N}YY & XX{MAD}YY \\" + "\n"


    if not i in idx_mins:
      s = s.replace('XX', r'\num{')
      s = s.replace('YY', r'}')
      s = s.replace(r'\num{None}', r'$\infty$')

    else:
      s = s.replace('XX', r'$\mathbf{')
      s = s.replace('YY', r'}$')
      s = s.replace(r'None', r'\infty')
      s = s.replace(r'True', r'\textbf{True}')
      s = s.replace(r'False', r'\textbf{False}')
      s = s.replace(r'$\mathbf{\infty}$', r'$\bm{\infty}$')

    dicts[obj] += s
      


for obj in ['rmse', 'logcosh', 'cauchy', 'welsch', 'fair']:
  s = r"""    %\bottomrule
  \end{tabular}
  \caption{\label{tab:h:HPO_initial_OBJ}OBJ.}
\end{table}"""

  s = s.replace('OBJ', f"{obj.capitalize()}-{type_str}-appendix")
  

  if remove_time:
    s = s.replace('table', 'margintable')
    s = s.replace("-appendix", '')


  dicts[obj] += s

  print(f"\n %{obj}:")
  print(dicts[obj])


