import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
data = pd.read_csv('klimat.csv',delimiter=';')

X = data[['Dług', 'Szer']]  
y = data['Temp'] 
regression = LinearRegression()
regression.fit(X, y)


print('dl:', regression.coef_[0])
print('szer:', regression.coef_[1])
print('dla  0 0 :', regression.intercept_)
