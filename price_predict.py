import pandas as pd

dataset = pd.read_excel("Dataset/train.xlsx", header=0, usecols=[0, 2, 3, 4, 5, 6, 7])

x_train = dataset.iloc[:, dataset.columns != 'price']
y_train = dataset.iloc[:, 5]

print(y_train)
