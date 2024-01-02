import json
import paho.mqtt.client as mqtt
import time

temp = 200.0
ID = '3'

iotDic = {}
iotDic["id"] = ID
iotDic["temp"] = str(temp)
iotDic["loc"] = 'w502g'

jsonData = json.dumps(iotDic)

mqtt_topic = "iot/sensor"

mqtt_broker = 'broker.hivemq.com'
mqtt_port = 1883
mqtt_qos = 1
mqtt_client = mqtt.Client('iot-22103456d')
mqtt_client.connect(mqtt_broker, mqtt_port)
print("Connect to MQTT broker")
while True:
    mqtt_client.publish(mqtt_topic, jsonData, mqtt_qos) # Publish a message
    print("Publishing message", jsonData ,"to topic", mqtt_topic)
    time.sleep(2)