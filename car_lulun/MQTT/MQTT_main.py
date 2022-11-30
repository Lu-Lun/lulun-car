import Buzzer_pub
import Buzzer_sub
import FAN_pub
import FAN_sub
import LED_pub
import LED_sub
import MQ2_pub
import RPi.GPIO as GPIO

def destroy():
	GPIO.cleanup()

if __name__ == '__main__':
	try:
		Buzzer_pub.init()
		Buzzer_sub.init()
		FAN_pub.init()
		FAN_sub.init()
		LED_pub.init()
		LED_sub.init()
		MQ2_pub.init()
		
		
	except Exception:
		print(Exception)
	finally:
		destroy()
