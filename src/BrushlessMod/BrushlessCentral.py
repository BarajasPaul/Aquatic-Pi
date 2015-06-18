import RPi.GPIO as GPIO
import time
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import GPIO_PORT


sys.arg[0]=BrushlessCentral.py
sys.arg[1]= TimeCounter

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PORT.BRUSHLESS_CENTRAL_PWM,GPIO.OUT)
p = GPIO.PWM(GPIO_PORT.BRUSHLESS_LEFT_PWM,50)
p.start(4)
time.sleep(2)
DutyCycleValue=4.8+(TimeCounter*.4)
try:
    while True:
        p.ChangeDutyCycle(DutyCycleValue)
        time.sleep(2)
        if DutyCycleValue > int(6.4):
            p.stop()
            GPIO.cleanup()
            exit()
 
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

