# MQTT IIOT Emulator

## Introduction

This project is an MQTT emulator designed for an Industrial Internet of Things (IIOT) scenario. It simulates the process of an IIOT sensor client publishing data to an MQTT broker, which is then analyzed by a cloud analysis component and subscribed to by another component for alert messages. The emulator showcases the flow of data from a client through a broker, to a cloud analysis component, and finally to a subscriber, with threshold-based alert generation.

## Prerequisites

Before running the project, ensure you have the following prerequisites installed:

1. Python 3.x
2. `paho-mqtt` library
3. Internet connection (for installing the required libraries)

### Installing the Required Library

To install the `paho-mqtt` library, run:

```
pip install paho-mqtt
```


## How to Run
1. **Clone the Repository: Clone the repository to your local machine using the following command:
 ```
git clone https://github.com/yourusername/mqtt-iiot-emulator.git
cd mqtt-iiot-emulator
```
2. **Run the MQTT Broker: In one terminal, run the MQTT broker script (Server.py):
```
python Server.py
```
3. **Run the Cloud Analysis Component: In a second terminal, run the cloud analysis script (Cloud_Analysis.py):
```
python Cloud_Analysis.py
```
4. **Run the Subscriber: In a third terminal, run the subscriber script (Subscribe.py):
```
python Subscribe.py
```
5. **Run the IIOT Sensor Client: In a fourth terminal, run the client script (Client.py):
```
python Client.py
```
6. **Publish Messages: Enter messages into the client terminal to publish data. The cloud analysis component will analyze the data and publish alerts based on the threshold computation, which the subscriber will receive.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.
