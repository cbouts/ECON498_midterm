import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

dataset = pd.read_csv('cmc_dataset.csv')
# sorted_dataset = dataset.sort_values(by=['name','time'], ascending=True)
grouped = dataset.groupby('name')
for i in grouped:
	price = 

