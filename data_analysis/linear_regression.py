from sklearn import linear_model
import pandas as pd


# FOR COINMARKETCAP:

dataset = pd.read_csv("cmc_dataset.csv")
data = dataset.iloc[:,4].values
	#  DETERMINING THE CORRELATION BETWEEN MARKET CAP AND PRICE
target = dataset.iloc[:,6].values
machine = linear_model.LinearRegression()
machine.fit(data.reshape(-1, 1), target)
print("FOR COINMARKETCAP:")
print("linear regression of price on market cap:")
print("intercept: ") 
print(machine.intercept_)
print("coefficient: ")
print(machine.coef_)

	#  DETERMINING THE CORRELATION BETWEEN MARKET CAP AND VOLUME
target_2 = dataset.iloc[:,9].values
machine_2 = linear_model.LinearRegression()
machine_2.fit(data.reshape(-1, 1), target_2)
print("linear regression of volume on market cap:")
print("intercept: ")
print(machine_2.intercept_)
print("coefficient: ")
print(machine_2.coef_)



# FOR COINGECKO:

dataset_2 = pd.read_csv("coingecko_dataset.csv")
data_3 = dataset_2.iloc[:,9].values
	# DETERMINING THE CORRELATION BETWEEN MARKET CAP AND PRICE
target_3 = dataset_2.iloc[:,6]
machine_3 = linear_model.LinearRegression()
machine_3.fit(data_3.reshape(-1, 1), target_3)
print("   ")
print("FOR COINGECKO:")
print("linear regression of price on market cap:")
print("intercept: ")
print(machine_3.intercept_)
print("coefficient: ")
print(machine_3.coef_)
	#  DETERMINING THE CORRELATION BETWEEN MARKET CAP AND VOLUME
target_4 = dataset_2.iloc[:,-1]
machine_4 = linear_model.LinearRegression()
machine_4.fit(data_3.reshape(-1, 1), target_4)
print("linear regression of volume on market cap:")
print("intercept: ")
print(machine_4.intercept_)
print("coefficient: ")
print(machine_4.coef_)










