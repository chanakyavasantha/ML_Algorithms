# 2.Method of finding minimum in a uni-model using : EXHAUSTIVE SEARCH METHOD
import math
u = 10
def function(x):
    return (u**2)*(math.sin((math.pi/180)*x)**2)/9.8


a = 0
b = 90
delta = (b-a)/10000
# initialisation
x1 = a+delta
x2 = x1+delta
x3 = x1+2*delta
count = 0
while x3 <= b:
    count += 1
    if function(x2) < function(x1) and function(x2) < function(x3):
        break
    else:
        x1 = x2
        x2 = x3
        x3 += delta
print(x1,x3,end=" ")
print(count)




