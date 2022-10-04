import numpy as py
import math
import matplotlib.pyplot as plt
def funcion3(x):
    ban=1
    
    if( math.pow(x,2)-9 > 0.0000001 or math.pow(x,2)-9 < -0.00001 ):
        fx=(x+2)/(math.pow(x,2)-9)
    else:
        fx = 0
        ban=0
        
        
    
    return fx,ban

a=-10
b= 10
step = 0.1
array = py.arange(a,b,step)
xAxis = list()
yAxis = list()

for i in array:
        fx,ban = funcion3(i)
        if( ban > 0):        
            xAxis.append(i)
            yAxis.append(fx)
    
        
        

plt.plot(xAxis,yAxis, color='maroon', marker='o')
