import time
import paho.mqtt.client as mqtt
import json

device_id = "D45454"
topic_input = "temperature/data"
topic_out = "robots/alert"
alert = ""



def on_connect(client, userdata, flags, rc):
    print(f"{device_id} Connected with result code: {rc}")
    client.subscribe("temperature/data")


def on_publish(client, userdata, msg):
    print(f"Message published {alert}")


def on_message(client, userdata, msg):
    received_msg = json.loads(msg.payload.decode())
    message = int(received_msg.get("message"))
    print(f"Received message from IIOT Sensor: {received_msg}")
    if message > 500:
        alert = "Turning ON"
    elif message < 500:
        alert = "Turning OFF"
    else:
        alert = "Unrecognized message"

    data = {
        "device_id": device_id,
        "timestamp": time.time(),
        "message": alert
    }
    json_data = json.dumps(data)
    client.publish(topic_out, json_data)


broker_address = "127.0.0.1"
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, 1883, 60)
client.loop_forever()
