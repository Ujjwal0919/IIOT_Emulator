import time
import paho.mqtt.client as mqtt
import json


# Connect to the Flask-SocketIO server

device_id = "D12345"
topic = "temperature/data"


def on_connect(client, userdata, flags, rc):
    print(f"{device_id} Connected with result code: {rc}")


def on_publish(client, userdata, msg):
    print(f"Message published {data}")


def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")


broker_address = "127.0.0.1"
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.connect(broker_address, 1883, 60)
client.loop_start()

while True:
    message = input("Enter message to publish (or 'q' to quit): ")
    if message == "q":
        break
    data = {
        "device_id": device_id,
        "timestamp": time.time(),
        "message": message
    }
    json_data = json.dumps(data)
    client.publish(topic, json_data)

client.loop_stop()
client.disconnect()
