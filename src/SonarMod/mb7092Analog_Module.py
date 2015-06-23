#!/usr/bin/python

import spidev
import time
 
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import GPIO_PORT
spi = spidev.SpiDev()
spi.open(0, 0)

Angle = sys.argv[1]

def readadc(adcnum):
# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    adcout = ((r[1] & 3) << 8) + r[2]
    return adcout

value = readadc(GPIO_PORT.ANALOG_SONAR)

if Angle == 180:
    f=open("../RESULTS/Sonar180.txt","w")
    f.write("angle:"+str(Angle)+" Value:"+str(value)+"\n")
    f.close()
else:
    f=open("../RESULTS/Sonar0.txt","w")
    f.write("angle:"+str(Angle)+" Value:"+str(value)+"\n")
    f.close()
exit (0)
