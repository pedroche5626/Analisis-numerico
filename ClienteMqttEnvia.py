import paho.mqtt.client
import time

topic = 'Equipo1'

def on_connect(client, userdata, flags, rc):
    print('connected (%s)' % client._client_id)
    client.subscribe(topic=topic, qos=2)

def on_message(client, userdata, message):
    rawString = message.payload
    msg = rawString.decode('utf8').replace("'", '"')
    print(msg)


client = paho.mqtt.client.Client(client_id='P3131', clean_session=False)
client.on_connect = on_connect
client.on_message = on_message
client.connect(host='35.170.242.54', port=8080)
client.loop_start() 
time.sleep(2)


while True:
    msg = input('Dame angulo: ')
    client.publish(topic,msg)
