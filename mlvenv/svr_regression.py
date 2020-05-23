# Polynomial Regression Example
import numpy as mp
import matplotlib.pyplot as plt
import pandas as pd

# get the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
Y = dataset.iloc[:, -1].values