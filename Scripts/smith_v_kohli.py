import matplotlib.pyplot as plt 
x = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
smith = [0, 2, 7, 13, 17, 23, 23, 26, 26, 27]
kohli = [3, 5, 9, 11, 15, 20, 25, 26, 27, 27]
plt.plot(x, kohli, linewidth = 7)
plt.xticks([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021], fontsize = 20)
plt.yticks(1, fontsize = 20)
plt.plot(x, smith,'r', linewidth = 7)
plt.xlabel("Year", fontsize = 30)
plt.ylabel("Centuries", fontsize = 30)
#plt.xlim(2012, 2021)
#plt.ylim(0, 29)
plt.legend(["Kohli"])
plt.legend(["Kohli", "Smith"], loc = "lower right", fontsize = 20)
plt.show()