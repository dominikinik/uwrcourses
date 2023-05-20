import pandas as pd
import numpy as np
from scipy import stats

data = pd.read_csv('rp10-11a.csv',delimiter=';')

group1 = data['pier']
group2 = data['dru']


t, p = stats.ttest_ind(group1, group2)


print("Grupa 1 - średnia: ", np.mean(group1))
print("Grupa 2 - średnia: ", np.mean(group2))
print("Wartość t: ", t)
print("Wartość p: ", p)


alpha = 0.05  

if p < alpha:
    print("Wartość p jest mniejsza od poziomu istotności. Odrzucamy hipotezę zerową.")
    print("Dodatkowy czynnik ma istotny wpływ na wydajność uprawy.")
else:
    print("Wartość p nie jest mniejsza od poziomu istotności. Nie ma wystarczających dowodów na odrzucenie hipotezy zerowej.")
    print("Nie ma istotnego wpływu dodatkowego czynnika na wydajność uprawy.")

