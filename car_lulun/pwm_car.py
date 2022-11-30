#coding:utf-8
import RPi.GPIO as gpio
import time
R = 1  #设置红色灯接到第16脚(BCM编码模式)
gpio.setwarnings(False)  #去掉警告信息
gpio.setmode(gpio.BCM)  #设置引脚为BCM编码模式
gpio.setup(R,gpio.OUT)  #PWM功能控制引脚，需要改引脚设置为输出
PWMR = gpio.PWM(R,50)  #设置R为PWM功能，并且设置频率为50HZ，也就是PWM周期是20ms
PWMR.start(0)  #启动R 的PWM
try:  #捕捉ctrl+c按键
   while 1:
       #R慢慢变亮
       for dc in range(0,100,5): #定义循环变量dc从0~100，每次增加5
           PWMR.ChangeDutyCycle(dc)  #调制PWM周期
           print("增加")
           time.sleep(0.5)
       time.sleep(0.5)
       #R慢慢变暗
       for dc in range(100,0,-5): #循环变量从100~0，每次递减5
           PWMR.ChangeDutyCycle(dc)  #调制PWM周期
           print("降低")
           time.sleep(0.5)
       time.sleep(5)
except KeyboardInterrupt:
   gpio.cleanup() #释放引脚资源
