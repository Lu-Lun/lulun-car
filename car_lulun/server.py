# -- coding:utf-8 --**
from websocket_server import WebsocketServer
import json
import car
import ast

# Called for every client connecting (after handshake)
def new_client(client, server):
	print("New client connected and was given id %d" % client['id'])
	server.send_message_to_all("Hey all, a new client has joined us")


# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
	# 将json字符串转换成json格式
    print(message)
    info = message.split(':')
    car.action(info[0],info[1])



PORT=1234
server = WebsocketServer(port = PORT,host="0.0.0.0")
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
