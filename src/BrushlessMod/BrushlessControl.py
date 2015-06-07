import RPi.GPIO as GPIO
import time
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import GPIO_PORT

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PORT.BRUSHLESS_LEFT_PWM,GPIO.OUT)
p = GPIO.PWM(GPIO_PORT.BRUSHLESS_LEFT_PWM,50)
p.start(4)
test=4
time.sleep(2)
try:
    while True:
        test=test +.5
        print test
        p.ChangeDutyCycle(test)
        time.sleep(2)
        if test == int(8.0):
            p.stop()
            GPIO.cleanup()
            exit()
 
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

