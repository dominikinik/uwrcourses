import pandas as pd
from sklearn.linear_model import LinearRegression
from  scipy import stats
import numpy as np
data = pd.read_csv("klimat.csv",delimiter=';')

X =data['Wys']
y = data['Temp']
slope, intercept, z, s, a = stats.linregress(X, y)

print('a', slope)
print('b:', intercept)

X = X.values.reshape(-1, 1)
y = y.values

regressor = LinearRegression()
regressor.fit(X, y)


print('a:', regressor.coef_[0])
print('b:', regressor.intercept_)

