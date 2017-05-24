import time, threading
import paho.mqtt.client as mqtt
from datetime import datetime

# creo le variabili di host e topic
mqtt_host = "192.168.1.232"
mqtt_port = 1883
mqtt_topic = "IoT/Test"

# funzione di callback per connettersi al topic
def on_connect(client, userdata, flags, rc):
  print("Subscribe on topic {}".format(topic_temperature))
  client.subscribe(topic_temperature)
  client.subscribe(topic_lightset)

# funzione di callback per la lettura di un messaggio sul topic
def on_message(client, userdata, msg):
  # msg contiene il payload di quanto presente sul topic, va convertito in striga e codificato
  message = str(msg.payload.decode(encoding="utf-8"))

# pubblico quancosa ogni n secondi sul topic
def updateRead():
  try:
    client.publish(topic_temperature, temp)
    print("Publish on topic {}".format(topic_temperature))
  except:
    print("Impossible to publish!")

try:
  # inizializzo MQTT
  client = mqtt.Client()
  client.on_connect = on_connect
  client.on_message = on_message
  client.connect(mqtt_host, mqtt_port, mqtt_topic)
  client.loop_start()
except:
  print("Impossible to get anything!")

def init():
  # creo un thred che viene eseguito ogni 10 secondi e che richiama la funzione init
  threading.Timer(10, init).start()
  updateRead()

init()
