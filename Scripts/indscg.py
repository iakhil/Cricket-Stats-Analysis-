import matplotlib.pyplot as plt 
labels = 'Rohit', 'Gill', 'Pujara', 'Rahane', 'Pant', 'Vihari', 'Ashwin'
balls = [98, 64, 205, 18, 118, 161, 128]
plt.pie(balls, labels = labels)
plt.axis('equal')
plt.show()
