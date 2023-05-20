import pandas as pd
from scipy import stats
import statistics
import math
import numpy as np
df = pd.read_csv('rp10-10a.csv',delimiter=",")  

waga_przed = df['przed']
waga_po = df['po']
roznica_wag =  waga_przed-waga_po 
#print(roznica_wag)#r wag
print(sum(roznica_wag)/16,"r wag")#srednia r wag

rozsr=sum(roznica_wag)/16
alpha = 0.05 #kiedy wypierdolka
fredom=len(waga_po)-1
print(fredom)

sdev= np.var(roznica_wag)

print(sdev,"sdev")

import math 

print((rozsr-0)/(math.sqrt(sdev)/math.sqrt(fredom)),"tval")#2.

t_statistic, p_value = stats.ttest_rel(waga_przed, waga_po )

print("wartosc T",t_statistic)
print("Wartość p: ", p_value)


print(rozsr+tval*(sdev/math.sqrt(fredom)))
print(rozsr-tval*(sdev/math.sqrt(fredom)))
t_statistic, p_value = stats.ttest_rel(waga_przed, waga_po )

print("wartosc T",t_st)
print("Wartość p: ", p_value)
