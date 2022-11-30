#!/bin/sh

python3 /home/pi/Desktop/car_lulun/server.py &

python3 /home/pi/Desktop/car_lulun/MQTT/Buzzer_pub.py &
python3 /home/pi/Desktop/car_lulun/MQTT/Buzzer_sub.py &
python3 /home/pi/Desktop/car_lulun/MQTT/FAN_pub.py &
python3 /home/pi/Desktop/car_lulun/MQTT/FAN_sub.py &
python3 /home/pi/Desktop/car_lulun/MQTT/LED_pub.py &
python3 /home/pi/Desktop/car_lulun/MQTT/LED_sub.py &
python3 /home/pi/Desktop/car_lulun/MQTT/MQ2_pub.py &

cd mjpg-streamer/mjpg-streamer-experimental/
./mjpg_streamer -i "input_uvc.so -d /dev/video2" -o "output_http.so -w ./www -p 1112"  &

cd mjpg-streamer/mjpg-streamer-experimental/
./mjpg_streamer -i "input_uvc.so -d /dev/video0" -o "output_http.so -w ./www -p 1111"  &


cd /home/pi/Desktop/car_lulun/frp_0.29.0_linux_arm/ 
sudo ./frpc -c frpc.ini &

cd /usr/local/nginx/sbin/
sudo ./nginx & 


ffmpeg -rtsp_transport tcp -i  rtsp://admin:lulun123456@192.168.1.64:554/h264/ch2/main/av_stream -c copy -f flv rtmp://127.0.0.1:1935/myapp/home &
