# Polynomial Regression Example
import numpy as mp
import matplotlib.pyplot as plt
import pandas as pd

# get the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
Y = dataset.iloc[:, -1].values

# Get the linear regression model
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,Y)

# Fit the linear model
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures( degree = 2)
X_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly, Y)
poly_reg2 = PolynomialFeatures ( degree = 4)
X_poly2 = poly_reg2.fit_transform(X)
lin_reg3 = LinearRegression()
lin_reg3 .fit(X_poly2, Y)

# Plot the pure linear model
plt.scatter(X, Y, color='black')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.plot(X, lin_reg2.predict(X_poly), color='red')
plt.plot(X, lin_reg3.predict(X_poly2), color='green')
plt.title('Truth or Bluff')
plt.xlabel('Position Level')
plt.ylabel('Salary ($ Millions)')
plt.show()

