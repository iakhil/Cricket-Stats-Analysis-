import pandas as pd 
data = pd.read_csv('hadlee2.csv')
wickets = data['Wickets']
w = 0
m = 0  
for i in range(len(wickets)):
	w += wickets[i]
	if w >= 300:
		break
date = data['Year']
print(date[61])
print(w)
