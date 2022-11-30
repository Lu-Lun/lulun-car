# receive
import RPi.GPIO as GPIO
import time
import json
import paho.mqtt.client as mqtt_client

broker = "43.138.181.197"
port=1883
keepalive=60
topic="/mqtt/fan"
client_id="python-mqtt-sub-Fan"
user="admin"
pwd="lulun123"

FAN_GPIO = 21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_GPIO,GPIO.OUT)
GPIO.output(FAN_GPIO,0)

switch = 0 

def connect_mqtt():
    def on_connect(client, userdata ,flags,rc):
        if rc == 0:
            print("Connected to MQTT OK!")
        else:
            print("Failed to connct,return cide %d\n",rc)
    
    client = mqtt_client.Client(client_id=client_id,clean_session=False)
    client.username_pw_set(user,pwd)
    client.on_connect = on_connect
    client.connect(broker,port,keepalive)
    return client

def subscribe(client:mqtt_client):
    def on_message(client,usedata,msg):
        global switch
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        switch = msg.payload.decode('utf-8')
        # 将json 转化成字典
        switch = json.loads(switch)
        switch = switch["switch"]
        motor(switch)
    client.subscribe(topic)
    client.on_message = on_message

def motor(switch):
    if switch == "1":
        # yes
        GPIO.output(FAN_GPIO, 1)
    else:
        # no
        GPIO.output(FAN_GPIO, 0)

def init():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


init()







