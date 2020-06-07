# Import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# load the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# For SVR
y = y.reshape(len(y), 1)

# Split the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# For SVR (not needed in Linear)
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X_train = sc_X.fit_transform(X_train)
y_train = sc_y.fit_transform(y_train)

# Train the model  Linear Regression
#from sklearn.linear_model import LinearRegression
#regressor = LinearRegression()
#regressor.fit(X_train, y_train)

# Train the model SVR
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X_train, y_train)

# Predict the end of the world
y_pred = regressor.predict(X_test)
#np.set_printoptions(precision=2)
#print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

# Evaluate
from sklearn.metrics import r2_score
#print("polynomial linear regression r2:" + r2_score(y_test, y_pred))
#print("SVR r2: " + str(r2_score(y_test, y_pred)))
print(r2_score(y_test, y_pred))