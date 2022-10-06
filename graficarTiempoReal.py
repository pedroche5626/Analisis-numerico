# Importing Libraries
import serial
import time
import json
import pickle
import matplotlib.pyplot as plt
%matplotlib notebook

fig, ax = plt.subplots()


arduino = serial.Serial(port='COM3', baudrate=9600)
time.sleep(2)
datos = list()

xAxis = list()
yAxis = list()
n=0
while ( n < 10):
    rawString = arduino.readline()
    my_json = rawString.decode('utf8').replace("'", '"')
    my_json = my_json.replace("\r\n","")
    my_json = json.loads(my_json)
    yAxis.append( my_json['Valor'])
    xAxis.append(my_json['Timestamp'])
    datos.append(my_json)
    
    
    plt.cla()
    ax.plot(xAxis,yAxis)
  
    fig.canvas.draw()
    
        
    
    n+=1
print("complete")
arduino.close()



with open('DatosSensor.json', 'wb') as fp:
    pickle.dump(datos, fp)
