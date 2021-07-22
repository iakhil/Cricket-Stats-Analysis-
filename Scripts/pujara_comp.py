import matplotlib.pyplot as plt 
x = [1, 2]
bf = [1258, 928]
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'35'}
plt.rcParams.update(params)
plt.bar(x, bf, width = 0.1, color = '#ad271d')
plt.xticks([1, 2])
#plt.bar(x, z, width = 1)
plt.show()