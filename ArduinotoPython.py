# Importing Libraries
import serial
import time
import json
import pickle


arduino = serial.Serial(port='COM3', baudrate=9600)
time.sleep(2)
datos = list()

n=0
while ( n < 1):
    rawString = arduino.readline()
    my_json = rawString.decode('utf8').replace("'", '"')
    my_json = my_json.replace("\r\n","")
    my_json = json.loads(my_json)
    datos.append(my_json)
        
    
    n+=1
print("complete")
arduino.close()

with open('DatosSensor.json', 'wb') as fp:
    pickle.dump(datos, fp)
