from urllib import response

import paho.mqtt.client as mqtt
import json
import time


device_id = "D34651"
topic = "robots/alert"


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code: {rc}")
    client.subscribe(topic)


def on_message(client, userdata, msg):
    received_msg = json.loads(msg.payload.decode())
    message = received_msg.get("message")
    print(f" Subscribed Message {received_msg}")


broker_address = "127.0.0.1"
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, 1883, 60)
client.loop_forever()
