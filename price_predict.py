import pandas as pd

# import timeit
#
# time = timeit.timeit(stmt="""pd.read_excel("Dataset/train.xlsx", header=0, usecols=[0, 2, 3, 4, 5, 6, 7])""",
#                      setup="import pandas as pd",
#                      number=2)
# print(time)

dataset = pd.read_excel("Dataset/train.xlsx", header=0, usecols=[0, 2, 3, 4, 5, 6, 7])

x_train = dataset.iloc[:, dataset.columns != 'price'].values
y_train = dataset.iloc[:, 5].values

print(x_train)
print(y_train)
