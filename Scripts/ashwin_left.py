import matplotlib.pyplot as plt 
labels = 'Left-handed batsmen', 'Right-Handed Batsmen'
sizes = [193, 183]
plt.pie(sizes, labels = labels)
plt.axis('equal')
plt.show()
