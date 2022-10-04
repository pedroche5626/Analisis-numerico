
import numpy as py
import math
import matplotlib.pyplot as plt
def funcion3(x):
    fx=math.log(2*x,math.e) - 20
    return fx

a=1
b= 10
step = 0.1
array = py.arange(a,b,step)
xAxis = list(array)
yAxis = list()

for i in array:
    yAxis.append(funcion3(i))

plt.plot(xAxis,yAxis, color='maroon', marker='o')
    
