import pandas as pd 
data = pd.read_csv('ashwin_lyon.csv')
#wickets = data.loc[:,['Wkts']]
#print(wickets[0])
#newwkts = data.loc[:, ['newwkts']]
pd.set_option('display.max_rows', None)
ashwin = data['WktsAshwin']
lyon = data['WktsLyon']
ashwin_total = data['AshwinTotal']
lyon_total = data['LyonTotal']
#adata.insert(7, "NewWkts", [], True)
for i in range(0, len(lyon)-1):
	lyon_total[i+1] = lyon_total[i] + lyon[i+1]
	ashwin_total[i+1] = ashwin_total[i] + ashwin[i+1]
print(lyon_total)
print(ashwin_total)