# receive
import RPi.GPIO as GPIO
import time
import json
import paho.mqtt.client as mqtt_client

broker = "43.138.181.197"
port=1883
keepalive=60
topic="/mqtt/led"
client_id="python-mqtt-sub-LED"
user="admin"
pwd="lulun123"

LED_R = 18
LED_G = 19
LED_B = 10


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_R,GPIO.OUT)
GPIO.setup(LED_G,GPIO.OUT)
GPIO.setup(LED_B,GPIO.OUT)
GPIO.output(LED_R,0)
GPIO.output(LED_G,0)
GPIO.output(LED_B,0)

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
        R = switch["LED_R"]
        G = switch["LED_G"]
        B = switch["LED_B"]
        
        change(R,G,B)
        
    client.subscribe(topic)
    client.on_message = on_message

def change(R,G,B):
	if R == '1':
		GPIO.output(LED_R,1)
	if G == '1':
		GPIO.output(LED_G,1)
	if B == '1':
		GPIO.output(LED_B,1)

def init():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


init()
