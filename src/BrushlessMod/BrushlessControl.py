import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
p = GPIO.PWM(26,50)
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

