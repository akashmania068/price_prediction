import pandas as pd

## Checking time taken to read the dataset
# import timeit
#
# time = timeit.timeit(stmt="""pd.read_excel("Dataset/train.xlsx", header=0, usecols=[0, 2, 3, 4, 5, 6, 7])""",
#                      setup="import pandas as pd",
#                      number=2)
# print(time) # takes approx. 110 seconds to read the dataset

dataset = pd.read_excel(io="Dataset/train.xlsx", header=0)

x_train = dataset.iloc[:, dataset.columns != 'price'].values
y_train = dataset.iloc[:, 5].values
