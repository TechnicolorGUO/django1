import paho.mqtt.client as mqtt
from .models import Event
import json

ID='3' # Sensor ID
mqtt_broker = 'broker.hivemq.com' # Broker
mqtt_port = 1883 # Default
mqtt_qos = 1 # Quality of Service = 1
mqtt_topic = "iot/sensor"

def mqtt_on_message(client, userdata, msg):
    # Do something
    d_msg = str(msg.payload.decode("utf-8"))
    iotData = json.loads(d_msg)
    if iotData["id"] == ID:
        print("Received message on topic %s : %s" % (msg.topic, iotData))
        p = Event(node_id=iotData["id"], node_loc=iotData["loc"], temp=float(iotData["temp"]) )
        p.save()

mqtt_client = mqtt.Client("django-22103456d") # Create a Client Instance
mqtt_client.on_message = mqtt_on_message
mqtt_client.connect(mqtt_broker, mqtt_port) # Establish a connection to a broker
print("Connect to MQTT broker")
mqtt_client.subscribe(mqtt_topic, mqtt_qos)

mqtt_client.loop_start()