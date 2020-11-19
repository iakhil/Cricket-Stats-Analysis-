import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 
kallis = pd.read_csv("kallis_stats.csv")
stokes = pd.read_csv("stokes.csv")
stokes_inn1 = stokes['Inn_1']
stokes_inn2 = stokes['Inn_2']
stokes_inn1 = stokes_inn1.apply(pd.to_numeric, errors = 'coerce')
stokes_inn1.dropna()
stokes_inn2 = stokes_inn2.apply(pd.to_numeric, errors = 'coerce')
stokes_inn2.dropna()
print("Number of runs scored by Stokes: ", sum(stokes_inn1) + sum(stokes_inn2))
kallis_runs = kallis['Runs']
kallis_runs = kallis_runs[:67].apply(pd.to_numeric, errors = 'coerce')
kallis_runs = kallis_runs.dropna()
print("Runs scored by Kallis: ", sum(kallis_runs))
kbat = kallis['Inn_2']
k1bat = kallis['Inn_1']
sbat = stokes['Inn_1']
s1bat = stokes['Inn_2']
inns = range(67)
# plt.plot(inns, stokes_runs, label = 'Stokes')
# plt.xlabel('Matches')
# plt.ylabel('Runs')
# plt.legend()
# plt.plot(inns, kallis_runs[:67], label = 'Kallis')
# plt.xlabel('Matches')
# plt.ylabel('Runs')
# plt.legend()
# plt.show()
kallis_bowling = pd.read_csv('kallis_bowling.csv')
stokes_bowling = pd.read_csv('stokes_bowling.csv')
kallis_wkts = kallis_bowling['Wkts']
kallis_wkts = kallis_wkts.apply(pd.to_numeric, errors = 'coerce')
kallis_wkts = kallis_wkts.dropna()
stokes_wkts = stokes_bowling['Wkts'].apply(pd.to_numeric, errors = 'coerce')
stokes_wkts = stokes_wkts.dropna()
print("Number of wickets taken by Kallis: ", sum(kallis_wkts[:67]))
print("Number of wickets taken by Ben Stokes: ", sum(stokes_wkts))
# plt.plot(inns, stokes_wkts)
# plt.plot(inns, kallis_wkts[:67])
# plt.show()
# for i in range(67):
# 	kallis_runs.append(kallis['Runs'][i])
# 	stokes_runs.append(stokes['Runs'][i])
# matches = [range(0,67)]
# plt.plot(matches, stokes_runs)
# plt.plot(matches, kallis_runs)
# print(stokes.head())
# print(kallis.head())
# k = kbat.str.contains('DNB')
# k1 = k1bat.str.contains('DNB')
# for i in range(len(k)):
# 	if k[i]: 
# 		kbat[i] = -1
# 	if k1[i]:
# 		k1bat[i] = -1 
# s1 = s1bat.str.contains('DNB')
# for i in range(len(s1)):
# 	if s1[i]:
# 		s1[i] = -1
# ducks = 0


# for i in range(len(k)):
# 	if kbat[i] == 0:
# 		ducks += 1
# 	if k1bat[i] == 0:
# 		ducks += 1
# print(ducks) 
# for i in range(len(k)):
# 	if k1bat[i] == 0:
# 		ducks += 1
# 	if kbat[i] == 0:
# 		ducks += 1
# print("Ducks scored by Kallis are:", ducks)
