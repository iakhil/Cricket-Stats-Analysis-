import pandas as pd
import matplotlib.pyplot as plt 
sachin = pd.read_csv("sachin_data.csv")
cook = pd.read_csv("cook_data.csv")
cook_runs = cook['Runs']
sachin_runs = sachin['Runs']
sachin_runs = sachin_runs[0:len(cook_runs)]
print(f"Length of C: {len(cook_runs)}")
print(f"Length of S: {len(sachin_runs)}")
matches = range(1, 162)
print(matches.shape)
# plt.plot(matches, sachin)
# plt.show()
