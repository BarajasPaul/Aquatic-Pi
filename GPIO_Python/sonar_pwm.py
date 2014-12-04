#!/usr/bin/python
import time
import RPi.GPIO as GPIO


def measure():
    stop = time.time()
    start = time.time()

    while GPIO.input(GPIO_PWM)==0:
        start = time.time()
    while GPIO.input(GPIO_PWM)==1:
        stop = time.time()

    elapsed = stop-start
    distance = (elapsed * 34300)/2
    return distance


GPIO_PWM = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PWM,GPIO.IN)

try:
  while True:
    distance = measure()
    print "Distance : %.1f" % distance
    time.sleep(.5)

except KeyboardInterrupt:
  GPIO.cleanup()
