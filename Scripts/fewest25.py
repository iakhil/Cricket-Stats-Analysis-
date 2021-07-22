import matplotlib.pyplot as plt 
player = ['Bradman', 'Smith','Tendulkar','Kohli','Gavaskar']
inns = [70, 136, 141, 141, 154]
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.bar(player, inns, color = 'crimson')
plt.xlabel('Player', fontsize = 20)
plt.ylabel('Innings', fontsize = 20)
plt.show()