import pandas as pd

input_string_lejlighed = """2.5        obj_rmse_xgb       True     MAD = 0.1663    244  72.32 sec
2.5        obj_rmse_xgb       False    MAD = 0.1746    218  50.92 sec
2.5        obj_logcos_xgb     True     MAD = 0.1642    347  73.44 sec
2.5        obj_logcos_xgb     False    MAD = 0.1515    630  84.16 sec
2.5        obj_cauchy_xgb     True     MAD = 0.1609    393  81.73 sec
2.5        obj_cauchy_xgb     False    MAD = 0.1449    887 113.06 sec
2.5        obj_welsch_xgb     True     MAD = 0.1627    253  60.59 sec
2.5        obj_welsch_xgb     False    MAD = 0.1485    936 128.29 sec
2.5        obj_fair_xgb       True     MAD = 0.1641    180  46.86 sec
2.5        obj_fair_xgb       False    MAD = 0.1566    343  51.79 sec
5          obj_rmse_xgb       True     MAD = 0.1631    291  81.73 sec
5          obj_rmse_xgb       False    MAD = 0.1792    381  77.54 sec
5          obj_logcos_xgb     True     MAD = 0.1607    260  60.00 sec
5          obj_logcos_xgb     False    MAD = 0.1519    698  93.17 sec
5          obj_cauchy_xgb     True     MAD = 0.1599    296  64.28 sec
5          obj_cauchy_xgb     False    MAD = 0.1476    776  96.33 sec
5          obj_welsch_xgb     True     MAD = 0.1608    245  56.41 sec
5          obj_welsch_xgb     False    MAD = 0.1470    947 117.25 sec
5          obj_fair_xgb       True     MAD = 0.1609    228  54.06 sec
5          obj_fair_xgb       False    MAD = 0.1576    372  53.34 sec
10         obj_rmse_xgb       True     MAD = 0.1601    285  79.76 sec
10         obj_rmse_xgb       False    MAD = 0.1716    274  60.62 sec
10         obj_logcos_xgb     True     MAD = 0.1631    230  53.11 sec
10         obj_logcos_xgb     False    MAD = 0.1572    391  56.58 sec
10         obj_cauchy_xgb     True     MAD = 0.1611    266  57.87 sec
10         obj_cauchy_xgb     False    MAD = 0.1457    822  99.76 sec
10         obj_welsch_xgb     True     MAD = 0.1644    214  51.62 sec
10         obj_welsch_xgb     False    MAD = 0.1493    760  95.78 sec
10         obj_fair_xgb       True     MAD = 0.1572    364  74.50 sec
10         obj_fair_xgb       False    MAD = 0.1556    349  51.09 sec
20         obj_rmse_xgb       True     MAD = 0.1637    246  72.23 sec
20         obj_rmse_xgb       False    MAD = 0.1760    589 109.39 sec
20         obj_logcos_xgb     True     MAD = 0.1609    374  78.22 sec
20         obj_logcos_xgb     False    MAD = 0.1606    301  48.06 sec
20         obj_cauchy_xgb     True     MAD = 0.1614    257  58.74 sec
20         obj_cauchy_xgb     False    MAD = 0.1439    932 113.70 sec
20         obj_welsch_xgb     True     MAD = 0.1607    279  62.62 sec
20         obj_welsch_xgb     False    MAD = 0.1502    856 107.61 sec
20         obj_fair_xgb       True     MAD = 0.1595    355  74.21 sec
20         obj_fair_xgb       False    MAD = 0.1519    458  64.79 sec
None       obj_rmse_xgb       True     MAD = 0.1555    657 156.80 sec
None       obj_rmse_xgb       False    MAD = 0.1680    362  73.33 sec
None       obj_logcos_xgb     True     MAD = 0.1582    361  75.48 sec
None       obj_logcos_xgb     False    MAD = 0.1627    283  44.37 sec
None       obj_cauchy_xgb     True     MAD = 0.1567    418  81.86 sec
None       obj_cauchy_xgb     False    MAD = 0.1468   1015 122.91 sec
None       obj_welsch_xgb     True     MAD = 0.1592    292  63.07 sec
None       obj_welsch_xgb     False    MAD = 0.1480    767  95.76 sec
None       obj_fair_xgb       True     MAD = 0.1583    349  72.35 sec
None       obj_fair_xgb       False    MAD = 0.1541    390  55.72 sec"""


input_string_villa = """2.5        obj_rmse_xgb       True     MAD = 0.2008    363 278.22 sec
2.5        obj_rmse_xgb       False    MAD = 0.1904    905 483.43 sec
2.5        obj_logcos_xgb     True     MAD = 0.2016    346 205.98 sec
2.5        obj_logcos_xgb     False    MAD = 0.1900   1003 363.83 sec
2.5        obj_cauchy_xgb     True     MAD = 0.1990    348 205.56 sec
2.5        obj_cauchy_xgb     False    MAD = 0.1871   1163 402.70 sec
2.5        obj_welsch_xgb     True     MAD = 0.1971    572 303.31 sec
2.5        obj_welsch_xgb     False    MAD = 0.1891    923 339.45 sec
2.5        obj_fair_xgb       True     MAD = 0.1956    520 280.49 sec
2.5        obj_fair_xgb       False    MAD = 0.1857   1062 376.42 sec
5          obj_rmse_xgb       True     MAD = 0.1987    607 407.82 sec
5          obj_rmse_xgb       False    MAD = 0.1855   1558 743.87 sec
5          obj_logcos_xgb     True     MAD = 0.1995    510 288.47 sec
5          obj_logcos_xgb     False    MAD = 0.1870    984 367.14 sec
5          obj_cauchy_xgb     True     MAD = 0.2000    345 206.30 sec
5          obj_cauchy_xgb     False    MAD = 0.1869    964 376.79 sec
5          obj_welsch_xgb     True     MAD = 0.2029    368 231.03 sec
5          obj_welsch_xgb     False    MAD = 0.1877   1014 396.51 sec
5          obj_fair_xgb       True     MAD = 0.1968    394 228.59 sec
5          obj_fair_xgb       False    MAD = 0.1836   1455 504.40 sec
10         obj_rmse_xgb       True     MAD = 0.2010    414 300.63 sec
10         obj_rmse_xgb       False    MAD = 0.1887    904 454.11 sec
10         obj_logcos_xgb     True     MAD = 0.1992    572 303.38 sec
10         obj_logcos_xgb     False    MAD = 0.1874   1162 419.55 sec
10         obj_cauchy_xgb     True     MAD = 0.1992    424 235.73 sec
10         obj_cauchy_xgb     False    MAD = 0.1859   1139 398.62 sec
10         obj_welsch_xgb     True     MAD = 0.2032    343 201.51 sec
10         obj_welsch_xgb     False    MAD = 0.1879    938 351.34 sec
10         obj_fair_xgb       True     MAD = 0.1942   1026 497.91 sec
10         obj_fair_xgb       False    MAD = 0.1847   1216 418.67 sec
20         obj_rmse_xgb       True     MAD = 0.1978    545 371.84 sec
20         obj_rmse_xgb       False    MAD = 0.1885   1140 550.22 sec
20         obj_logcos_xgb     True     MAD = 0.1995    424 240.85 sec
20         obj_logcos_xgb     False    MAD = 0.1871   1263 454.61 sec
20         obj_cauchy_xgb     True     MAD = 0.2000    382 216.07 sec
20         obj_cauchy_xgb     False    MAD = 0.1848   1251 438.63 sec
20         obj_welsch_xgb     True     MAD = 0.2004    454 250.98 sec
20         obj_welsch_xgb     False    MAD = 0.1881    869 317.98 sec
20         obj_fair_xgb       True     MAD = 0.1963    606 313.83 sec
20         obj_fair_xgb       False    MAD = 0.1812   1996 701.26 sec
None       obj_rmse_xgb       True     MAD = 0.1936    985 630.98 sec
None       obj_rmse_xgb       False    MAD = 0.1874   1169 568.49 sec
None       obj_logcos_xgb     True     MAD = 0.1992    373 220.56 sec
None       obj_logcos_xgb     False    MAD = 0.1862   2003 694.18 sec
None       obj_cauchy_xgb     True     MAD = 0.1989    415 237.47 sec
None       obj_cauchy_xgb     False    MAD = 0.1864   1073 392.36 sec
None       obj_welsch_xgb     True     MAD = 0.1947    846 422.70 sec
None       obj_welsch_xgb     False    MAD = 0.1855   1137 399.37 sec
None       obj_fair_xgb       True     MAD = 0.1988    417 231.13 sec
None       obj_fair_xgb       False    MAD = 0.1839   1597 540.69 sec"""

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
    dicts[obj] = dicts[obj].replace('ccrrc', 'ccrc').replace('& Time [$s$] ', '').replace(r'begin{table}[]', r'begin{margintable}')


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

  s = s.replace('OBJ', f"{obj.capitalize()}-{type_str}")
  
  if remove_time:
    s = s.replace('table', 'margintable')


  dicts[obj] += s

  print(f"\n %{obj}:")
  print(dicts[obj])


