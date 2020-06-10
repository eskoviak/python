# Import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# set the datetime datatype
#datedt = np.dtype('M')

# load the dataset
dataset = pd.read_csv('time_series_covid19_confirmed_us.csv')
#print(dataset)

# because the column headings are in row 0, they are included
y = dataset.iloc[267 , 11:].values
#y = dataset.iloc[269, 11:].values

print(len(y))