import serial
import time

ser = serial.Serial("/dev/ttyUSB0",9600)

if ser.is_open:
	print("port open success")
	send_data = bytes.fromhex('05 03 00 00 00 0B 04 0D')
	print(send_data)
	ser.write(send_data)
	time.sleep(0.1)
	len_return_data = ser.inWaiting()
	if len_return_data:
		return_data = ser.read(len_return_data)
		str_return_data = str(return_data.hex())
		feedback_data = int(str_return_data[-6:-2],16)
		print(feedback_data)
	else:
         print("empty")   
else:
	print("port open failed")
