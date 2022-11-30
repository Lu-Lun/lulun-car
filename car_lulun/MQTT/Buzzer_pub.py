# send message
from paho.mqtt import client as mqtt_client
import RPi.GPIO as GPIO
import time
import json

broker = "43.138.181.197"
port=1883
keepalive=60
topic="/mqtt/voice"
client_id="python-mqtt-pub-Buzzer"
user="admin"
pwd="lulun123"

VOICE_GPIO = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(VOICE_GPIO,GPIO.OUT)
GPIO.output(VOICE_GPIO,1)


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
        msg = {"switch":str(GPIO.input(VOICE_GPIO))}
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
    
    
    
    
    
    
    
    

