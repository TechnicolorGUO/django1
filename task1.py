import paho.mqtt.client as mqtt
import time
import Adafruit_DHT


mqtt_broker = 'broker.hivemq.com'
mqtt_port = 1883
mqtt_qos = 1

mqtt_client = mqtt.Client('iot-22103456d')
mqtt_client.connect(mqtt_broker, mqtt_port)
print("Connect to MQTT broker")

mqtt_topic = "iot/22103456d"


DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

def mqtt_on_message(client, userdata, msg):
    d_msg = str(msg.payload.decode("utf-8")) # Decode the message
    print("Received message on topic %s : %s" % (msg.topic, d_msg))

mqtt_client.subscribe(mqtt_topic, mqtt_qos) # topic=iot/student_ID, qos=1
mqtt_client.on_message = mqtt_on_message
mqtt_client.loop_start()

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN) # Read the temperature
    mqtt_client.publish(mqtt_topic, temperature, mqtt_qos) # Publish a message
    print("Publishing message %s to topic %s" % (temperature, mqtt_topic))
    time.sleep(2) #Sleep 2 seconds
    
    
