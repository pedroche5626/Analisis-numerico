import paho.mqtt.client
import serial
import time
import json

arduino = serial.Serial(port='COM3', baudrate=9600)
time.sleep(2)

topic = 'Todos'

def on_connect(client, userdata, flags, rc):
    print('connected (%s)' % client._client_id)
    client.subscribe(topic=topic, qos=2)

def on_message(client, userdata, message):
    rawString = message.payload
    msg = rawString.decode('utf8').replace("'", '"')
    print(msg)
    arduino.write(msg.encode())
   
    

def main():
    client = paho.mqtt.client.Client(client_id='Obervador1234', clean_session=False)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host='35.170.242.54', port=8080)
    client.loop_forever()

if __name__ == '__main__':
    main()

sys.exit(0)
