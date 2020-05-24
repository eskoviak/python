# Polynomial Regression Example
import numpy as mp
import matplotlib.pyplot as plt
import pandas as pd

# get the dataset and reshape Y to 2D array
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
Y = dataset.iloc[:, -1].values  
Y = Y.reshape(len(Y), 1)

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_Y = StandardScaler()
X = sc_X.fit_transform(X)
Y = sc_Y.fit_transform(Y)
#print(Y)

# Train the Data set using the cited kernel
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, Y)

# Predict new value (mind the scaling)
print(sc_Y.inverse_transform(regressor.predict(sc_X.transform([[6.5]]))))