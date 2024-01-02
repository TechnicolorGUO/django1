import paho.mqtt.client as mqtt
import time
import Adafruit_DHT

from RPLCD.i2c import CharLCD

mqtt_broker = 'broker.hivemq.com'
mqtt_port = 1883
mqtt_qos = 1
mqtt_client = mqtt.Client('iot-22103456d')
mqtt_client.connect(mqtt_broker, mqtt_port)
print("Connect to MQTT broker")

mqtt_topic = "iot/22103456d"

lcd = CharLCD('PCF8574',0x27)
lcd.cursor_pos=(1,0)

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
d_msg = ''

def mqtt_on_message(client, userdata, msg):
    global d_msg
    d_msg = str(msg.payload.decode("utf-8")) # Decode the message
    print("Received message on topic %s : %s" % (msg.topic, d_msg))


mqtt_client.subscribe(mqtt_topic, mqtt_qos) # topic=iot/student_ID, qos=1
mqtt_client.on_message = mqtt_on_message
mqtt_client.loop_start()

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN) # Read the temperature
    if d_msg == 'H':
        lcd.clear()
        h = str(humidity)
        lcd.write_string(h)
    elif d_msg == 'T':
        lcd.clear()
        t = str(temperature)
        lcd.write_string(t)
    print("Temperature = %s Humidity =  %s" % (temperature, humidity))
    time.sleep(2) #Sleep 2 seconds
    lcd.clear()