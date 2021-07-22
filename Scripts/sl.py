# Plot runs of the top six run-scorers for Sri Lanka in Tests 
import matplotlib.pyplot as plt 
import numpy as np 

x = [1, 2, 3, 4, 5, 6]
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'30'}
plt.rcParams.update(params)
runs = [12400, 11814, 6973, 6361, 6008, 5502]
plt.yticks(np.arange(1000, 16000, step = 500))
plt.scatter(x, runs, 520)
plt.show()

