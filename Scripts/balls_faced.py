# Plot of the number of deliveries faced by Tendulkar, Dravid, Laxman, Pujara, and Ponting in Tests.
import matplotlib.pyplot as plt 
players = ['Tendulkar', 'Dravid', 'Laxman', 'Pujara', 'Ponting']
bf = [5493, 5432, 4480, 4469, 4428]
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'30',
         'ytick.labelsize':'30'}
plt.rcParams.update(params)
plt.bar(players, bf, color = '#b80606')
plt.show()
