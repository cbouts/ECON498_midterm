import pandas as pd
import numpy as np



# read the data from each csv to determine what percentage of each column is missing

filename = 'cmc_deeplink.csv'
df = pd.read_csv(filename)
print("------- % Data Missing in " + filename + "--------")
for col in df.columns:
		pct_missing = np.mean(df[col].isnull())
		print('{} - {}%'.format(col, round(pct_missing*100)))

filename_2 = 'cmc_dataset.csv'
df = pd.read_csv(filename_2)
print("------- % Data Missing in " + filename_2 + "--------")
for col in df.columns:
		pct_missing = np.mean(df[col].isnull())
		print('{} - {}%'.format(col, round(pct_missing*100)))

filename_3 = 'coingecko_dataset.csv'
df = pd.read_csv(filename_3)
print("------- % Data Missing in " + filename_3 + "--------")
for col in df.columns:
		pct_missing = np.mean(df[col].isnull())
		print('{} - {}%'.format(col, round(pct_missing*100)))

# screenshot of terminal output will be included in analysis to motivate the decisions I made about data analysis.