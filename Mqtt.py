import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
########################################
broker_address="35.170.242.54"
port = 8080

client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address,port) #connect to broker
client.loop_start() #start the loop
client.subscribe("Equipo1")
client.publish("Equipo1","que tal")
time.sleep(4) # wait
client.loop_stop() #stop the loop
