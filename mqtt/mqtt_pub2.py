import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_Outside")
client.connect(mqttBroker)

while True:
    randNumber = randrange(10)
    client.publish("Temperature", randNumber)
    print("Just Print "+str(randNumber)+" to topic Temperature")
    time.sleep(1)
