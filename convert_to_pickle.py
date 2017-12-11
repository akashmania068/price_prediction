'''
    Converting train and test excel files into pickle files
'''

import pandas as pd

train_data = pd.read_excel(io="Dataset/train.xlsx", header=0)
train_data.to_pickle("train.pkl")

test_data = pd.read_excel(io="Dataset/test.xlsx", header=0)
test_data.to_pickle("test.pkl")

'''
    Comparing time taken to read the dataset in excel and pickle format
    (You can comment the below code if you don't want to check the time)
'''

import timeit

time_excel = timeit.timeit(stmt="""pd.read_excel("Dataset/train.xlsx", header=0)""",
                     setup="import pandas as pd",
                     number=2)
print("Time to read Excel File : ", time_excel) # takes approx. 130 seconds to read the dataset

time_pickle = timeit.timeit(stmt="""pd.read_pickle("train.pkl")""",
                     setup="import pandas as pd",
                     number=2)
print("Time to read Pickle File : ", time_pickle) # takes approx. 7.45 seconds to read the dataset
