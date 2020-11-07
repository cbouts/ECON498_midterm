from sklearn import linear_model
import pandas as pd
import numpy as np

# GETTING SUMMARY STATISTICS FOR PRICE, MARKET CAP, AND VOLUME:


# FOR COINMARKETCAP:

# market cap:
dataset = pd.read_csv("cmc_dataset.csv")
# sorted_dataset = dataset.sort_values(by=['name','time'], ascending=True)
grouped = dataset.groupby('name')
# appending summary statistics to a dataframe:
df = grouped['market_cap'].agg([np.mean, np.std, np.amin, np.amax])
df.to_csv('market_cap_cmc.csv', header = True)

# volume:
df = grouped['trading_volume-USD'].agg([np.mean, np.std, np.amin, np.amax])
# print(df)
df.to_csv('volume_cmc.csv', header = True)

# price:
# print(grouped['price'].agg([np.mean, np.std, np.amin, np.amax])) 
# appending summary statistics to a dataframe:
df = grouped['price'].agg([np.mean, np.std, np.amin, np.amax])
df.to_csv('price_cmc.csv', header = True)

# FOR COINGECKO:

# market cap:
dataset_2 = pd.read_csv("coingecko_dataset.csv")
grouped = dataset_2.groupby('name')
df = grouped['market_cap'].agg([np.mean, np.std, np.amin, np.amax])
# print(df)
df.to_csv('market_cap_gecko.csv', header = True)

# volume:
	# we know it's in USD like coinmarketcap volume because the API page tells us so.
df = grouped['total_volume'].agg([np.mean, np.std, np.amin, np.amax])
# print(df)
df.to_csv('volume_gecko.csv', header = True)

# price:
df = grouped['current_price'].agg([np.mean, np.std, np.amin, np.amax])
# print(df)
df.to_csv('price_gecko.csv', header = True)






