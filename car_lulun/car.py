# coding:utf-8
import RPi.GPIO as gpio
import time
from websocket_server import WebsocketServer

R = 23  # 定义右轮信号控制针脚
L = 24  # 定义左轮信号控制针脚

gpio.setwarnings(False)  # 去掉警告信息
gpio.setmode(gpio.BCM)  # 设置引脚为BCM编码模式
gpio.setup(R, gpio.OUT)  # PWM功能控制引脚(右轮)
gpio.setup(L, gpio.OUT)  # PWM功能控制引脚(左轮)
PWMR = gpio.PWM(R, 50)  # 设置R为PWM功能，并且设置频率为50HZ，也就是PWM周期是20ms
PWML = gpio.PWM(L, 50)  # 设置L为PWM功能，并且设置频率为50HZ，也就是PWM周期是20ms

STOP = 7.18  # 停止参数
STANDARD = 7.18  # 标准PWM百分比
INCREMENT = 1.4  # 调整电机增量参数
MAX = 8.6  # 最大PWM百分比
MIN = 4.8  # 最小PWM百分比

PWMR.start(STANDARD)  # 启动R的PWM
PWML.start(STANDARD)  # 启动L的PWM

speed_change_direct = 20
speed_normal = 46


# 后退PWM调节参数
def back_action(speed):
    if speed <= 0:
        return STOP
    if speed >= 100:
        return MIN
    else:
        return STANDARD - speed * 0.01 * (STANDARD - MIN)


# 前进PWM调节函数
def head_action(speed):
    if speed <= 0:
        return STOP
    if speed >= 100:
        return MAX
    else:
        return STANDARD + speed * 0.01 * (MAX - STANDARD)


# 双轮电机PWM调参
def move(PWM_L, PWM_R):
    try:
        PWMR.ChangeDutyCycle(PWM_L)  # 调制PWMR周期
        PWML.ChangeDutyCycle(PWM_R)  # 调制PWML周期
    except KeyboardInterrupt:
        gpio.cleanup()  # 释放引脚资源


def stop_move():
    move(STOP, STOP)


def action(key, speed):
    speed = int(speed)
    if speed >46:
        speed = 46
    if speed <0:
        speed = 0
        
    if key == 'w':
        move(head_action(speed), head_action(speed))
        time.sleep(0.1)
    elif key == 's':
        move(back_action(speed), back_action(speed))
        time.sleep(0.1)
    elif key == 'a':
        move(head_action(10), head_action(speed_normal))
        time.sleep(0.1)
    elif key == 'd':
        move(head_action(speed_normal), head_action(10))
        time.sleep(0.1)
    else:
        stop_move()
