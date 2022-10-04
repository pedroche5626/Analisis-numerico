import numpy as py
import math
import matplotlib.pyplot as plt

def funcion1(x):
        fx = x*x+2*x - 20
        return fx
    
yAxis = list()
xAxis = list()

for i in range(-10,10):
    xAxis.append(i)
    yAxis.append(funcion1(i))

    
## LINE GRAPH ##
plt.plot(xAxis,yAxis, color='maroon', marker='o')
plt.xlabel('x')
plt.ylabel('y')
