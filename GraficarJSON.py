import serial
import time
import json
import pickle
import matplotlib.pyplot as plt


with open('DatosSensor.json', 'rb') as f:
    datos = pickle.load(f)

xAxis = list()
yAxis = list()

for elemento in datos:
    if(elemento['Sensor'] == 'Humedad'):
        xAxis.append(elemento['Timestamp'])
        yAxis.append(elemento['Valor'])


plt.plot(xAxis,yAxis, color='orange', marker='*')
plt.xlabel('Timestamp')
plt.ylabel('Valor de la Humedad')
plt.grid(True)
plt.show()
