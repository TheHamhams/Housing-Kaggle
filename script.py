import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

X = pd.read_csv('test.csv', index_col=0)
X_train_full = pd.read_csv('train.csv', index_col=0)

print(X.describe())
#print(X.info())

X.drop(['MiscFeature', 'Fence', 'PoolQC', 'Alley'], axis=1, inplace=True)

print(X.info())