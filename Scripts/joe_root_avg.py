import pandas as pd 
import matplotlib.pyplot as plt 
mts = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
avg = [93, 40.23, 45.63, 55.02, 54.06, 53.19, 53.76, 52.18, 49.51, 48.40, 50.33]
plt.rcParams.update({'font.size': 42})
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'15'}
plt.plot(mts, avg, color = "red", linewidth = 7)
# plt.xlabel("Matches")
# plt.ylabel("Average")
plt.show()
