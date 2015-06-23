# Servo Control
import time
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import GPIO_PORT

print GPIO_PORT.SERVO_PWM_18

def set(property, value):
    try:
        f = open( GPIO_PORT.SERVO_PWM_18 + property, 'w')
        f.write(value)
        f.close()
    except:
        print("Error writing to: " + property + " value: " + value)

def setServo(angle):
    set("servo", str(angle))

set("delayed", "0")
set("mode", "servo")
set("servo_max", "180")
set("active", "1")

delay_period = 0.005
setServo(0)
time.sleep(2)
limit=180
while True:
    for angle in range(0,limit):
        setServo(angle)
        time.sleep(delay_period)
        if angle == 179:
            os.system("../SonarMod/mb7092Analog_Module.py "+ str(180))
    for angle in range(0,limit):
        setServo(limit - angle)
        time.sleep(delay_period)
        if (limit-angle)==1:
            os.system("../SonarMod/mb7092Analog_Module.py "+ str(0))
