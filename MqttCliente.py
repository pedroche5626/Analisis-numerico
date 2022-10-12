import paho.mqtt.client

topic = 'Analisis2'



client = paho.mqtt.client.Client(client_id='Observador1', clean_session=False)
client.connect(host='35.170.242.54', port=8080)



msg = 'Hola'
client.publish(topic,msg)
