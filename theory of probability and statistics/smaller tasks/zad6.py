tab1 = []
tab2 = []

for i in range(1, 101):
    if i % 2 == 0 or i % 3 == 0:
        tab1.append(1)
    else:
        tab1.append(0)
        
    if i % 3 == 0:
        tab2.append(1)
    else:
        tab2.append(0)

xy = []
x2 = []
y2 = []

for i in range(0, 100):
    xy.append(tab1[i] * tab2[i])
    x2.append(tab1[i] * tab1[i])
    y2.append(tab2[i] * tab2[i])

n = 100
import math as mt
odp = (n*sum(xy)-(sum(tab1)*sum(tab2)))
odp2=mt.sqrt((n*sum(x2)-(sum(tab1)*sum(tab1)))*(n*sum(y2)-(sum(tab2)*sum(tab2))))
print(odp,odp2)
# po skroceniu 
print(33,67)
from numpy import mean
xsredni=mean(tab1)
ysredni=mean(tab2)
sum=0
for i in range(0,100):
    sum+=(tab1[i]-xsredni)*(tab2[i]-ysredni)
conv= sum
print(conv)
sum2=0
sum3=0
import math
for i in range(0,100):
    sum2+=(tab1[i]-xsredni)*(tab1[i]-xsredni)
    sum3+=(tab2[i]-ysredni)*(tab2[i]-ysredni)
cos=math.sqrt(sum2)*math.sqrt(sum3)
print(cos)
print(conv/cos)
print(33/67)
 
 
a=0 
b=0
for i in range(0,100):
    a+=mean(xy)-(mean(tab1)*mean(tab2))
    b+= math.sqrt(mean(x2)-mean(tab1)*mean(tab1))*math.sqrt(mean(y2)-mean(tab2)*mean(tab2))
print(a)
print(b)