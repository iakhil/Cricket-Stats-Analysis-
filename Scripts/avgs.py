import matplotlib.pyplot as plt 
inns = [0, 1, 2, 3, 4]
smith = [62.84, 62.31, 62.31, 61.78, 61.33]
mayank = [57.29, 54.88, 52.47, 49.85, 47.85]
marnus = [63.43, 62.75, 60.48, 60, 58.81]
plt.title("Average vs Innings", fontsize = 20)
plt.xlabel("Innings", fontsize = 18)
plt.ylabel("Average", fontsize = 18)
ax = plt.axes()
ax.set_facecolor('lightseagreen')
plt.plot(inns, smith, linewidth = 8, label = "Smith", color = 'white')
plt.legend()
plt.plot(inns, mayank, linewidth = 8, label = "Agarwal", color = 'yellow')
plt.legend(fontsize = 2)
plt.plot(inns, marnus, linewidth = 8, label = "Labuschagne", color = "lawngreen")
plt.legend()
plt.show()