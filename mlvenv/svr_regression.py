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

# Visualising the SVR results
plt.scatter(sc_X.inverse_transform(X), sc_Y.inverse_transform(Y), color = 'red')
plt.plot(sc_X.inverse_transform(X), sc_Y.inverse_transform(regressor.predict(X)), color = 'blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualising the SVR results (for higher resolution and smoother curve)
# X_grid = np.arange(min(sc_X.inverse_transform(X)), max(sc_X.inverse_transform(X)), 0.1)
# X_grid = X_grid.reshape((len(X_grid), 1))
# plt.scatter(sc_X.inverse_transform(X), sc_y.inverse_transform(y), color = 'red')
# plt.plot(X_grid, sc_y.inverse_transform(regressor.predict(sc_X.transform(X_grid))), color = 'blue')
# plt.title('Truth or Bluff (SVR)')
# plt.xlabel('Position level')
# plt.ylabel('Salary')
# plt.show()