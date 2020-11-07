# import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

dataset_1 = pd.read_csv("market_cap_cmc.csv")
dataset_2 = pd.read_csv("market_cap_gecko.csv")

x=[]
y=[]

for row in dataset_1:
	list1=[1]
	# array1=np.array(list1)
	print(list1)
	# x.append(list1)


# with open('market_cap_cmc.csv','r') as csvfile:
# 	plots = csv.reader(csvfile, delimiter=',')
# 	for row in plots:
# 		list1=[row[1]]
# 		array1=np.array(list1)
# 		# print(array1)
# 		x.append(array1)

# with open('market_cap_gecko.csv','r') as csvfile:
# 	plots = csv.reader(csvfile, delimiter=',')
# 	for row in plots:
# 		list2=[row[1]]
# 		array2=np.array(list2)
# 		y.append(array2)
# # print(x.ndim + "----" + y.ndim)

# plt.plot(x,y, marker="o")
# plt.title('Market Cap Means')
# plt.xlabel('coinmarket.com market cap mean')
# plt.ylabel('coingecko.com market cap mean')

# plt.show()