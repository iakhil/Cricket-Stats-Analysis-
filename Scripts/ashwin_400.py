import matplotlib.pyplot as plt 
import numpy as np
#Plotting year-wise
# x = list(range(2011, 2022))
# plt.xticks(np.arange(2011, 2022, step = 1))
# axes = plt.gca()
# axes.set_xticklabels(x, rotation = 0, fontsize = 20)
# wickets = [26, 37, 41, 10, 62, 72, 56, 38, 20, 13, 26]
# axes.set_yticklabels(wickets,rotation = 0, fontsize = 20)
# plt.plot(x, wickets, linewidth = 5)
# plt.xlabel("Year", fontsize = 25)
# plt.ylabel("Wickets", fontsize = 25)
# plt.show()

#Plotting opposition-wise
# teams = ['AFG', 'AUS', 'BAN', 'ENG', 'NZ','SA', 'SL', 'WI']
# wkts = [5, 89, 16, 80, 48, 53, 50, 60]
# plt.bar(teams, wkts)
# plt.xlabel("Team", fontsize = 25)
# plt.ylabel("Wickets", fontsize = 25)
# axes = plt.gca()
# axes.set_xticklabels(teams, rotation = 0, fontsize = 20)
# axes.set_yticklabels(wkts, rotation = 0, fontsize = 20)
# plt.show()
wk = [196, 205]
labels = ['Home', 'Away']
colors = ['#fcba03', '#210505']
plt.pie(wk, colors = colors)
plt.show()