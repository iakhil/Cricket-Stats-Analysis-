# Script to find cummulative wickets of Ashwin in Tests.
import pandas as pd 
data = pd.read_csv('ashwin.csv')
#wickets = data.loc[:,['Wkts']]
#print(wickets[0])
#newwkts = data.loc[:, ['newwkts']]
wickets = data['Wkts']
newwkts = data['NewWkts']
#adata.insert(7, "NewWkts", [], True)
for i in range(0, len(wickets)-1):
	newwkts[i+1] = newwkts[i] + wickets[i+1]
print(newwkts[72])
