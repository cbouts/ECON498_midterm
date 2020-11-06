from sklearn import linear_model
import pandas as pd


dataset = pd.read_csv("cmc_dataset.csv")
# print(dataset)
sorted_dataset = dataset.sort_values(by=['name','time'], ascending=True)
print(sorted_dataset)

target = sorted_dataset.iloc[:,0].values
# first number is inclusive, second is not. so if we want to get from 3 to 8 we need to do 3:9
# [columns,rows]
# this puts it into a long array

data = sorted_dataset.iloc[:,3:8]

