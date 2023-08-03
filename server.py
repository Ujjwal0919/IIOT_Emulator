import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker!")
    client.subscribe("#") 


def on_publish(client, userdata, mid):
    print("Message published")


def on_message(client, userdata, msg):
    print("Received message:")
    print("Topic: " + msg.topic)
    print("Message: " + msg.payload.decode())
    print("Timestamp: " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


client = mqtt.Client()


client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message


broker_address = "localhost"  
broker_port = 1883  
client.connect(broker_address, broker_port)


client.loop_forever()