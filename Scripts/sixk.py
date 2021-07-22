# Fastest to 6,000 runs for Sri Lanka in Tests.
import matplotlib.pyplot as plt 
import numpy as np 
x = [1, 2, 3, 4, 5, 6]
y = [117, 119, 120, 123, 125, 134]

params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'25'}
plt.rcParams.update(params)
plt.yticks(np.arange(117, 136, step = 1))

plt.scatter(x,y)
plt.show()
