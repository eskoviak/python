# Import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# set the datetime datatype
datedt = np.dtype('M')

# load the dataset
dataset = pd.read_csv('time_series_covid19_confirmed_us.csv')
print(dataset.dtypes)

X = dataset.iloc[0 , 12:].to_numpy(datedt)
#y = dataset.iloc[269, 12:].values

print(X)