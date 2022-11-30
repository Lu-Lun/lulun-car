# send message
from paho.mqtt import client as mqtt_client
import RPi.GPIO as GPIO
import time
import json

broker = "43.138.181.197"
port=1883
keepalive=60
topic="/mqtt/led"
client_id="python-mqtt-pub-LED"
user="admin"
pwd="lulun123"

LED_R = 18
LED_G = 19
LED_B = 20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_R,GPIO.OUT)
GPIO.setup(LED_G,GPIO.OUT)
GPIO.setup(LED_B,GPIO.OUT)

GPIO.output(LED_R,0)
GPIO.output(LED_G,0)
GPIO.output(LED_B,0)


def connect_mqtt():
    def on_connect(client,userdata,flags,rc):
        if rc == 0:
            print("Connected to MQTT OK!")
        else:
            print("Failed to connect,return code%d\n",rc)
    
    client = mqtt_client.Client(client_id=client_id,clean_session=False)
    client.username_pw_set(user,pwd)
    client.on_connect=on_connect
    client.connect(broker,port,keepalive)
    return client
    


def publish(client):
    while True:
        time.sleep(4)
        msg = {
               "LED_R":str(GPIO.input(LED_R)),
               'LED_G':str(GPIO.input(LED_G)),
               'LED_B':str(GPIO.input(LED_B))
              }
        
        msg = json.dumps(msg).encode('utf-8')
        result = client.publish(topic,msg)
        status = result[0]
        if status==0:
            print(f"Send `{msg}` to `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

def init():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

init()


    
    
    
    
    
    
    
    


