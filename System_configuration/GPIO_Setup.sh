#!/bin/bash

#Copyright (C) 2015 Barajas D. Paul <Paul.Barajas@linux.com>

install_source(){
    grep "$1" /etc/modules > /dev/null

    if [ $? -eq 0 ]; then
        echo "$1 was found"
    else
        echo "$1" >> /etc/modules
    fi
}


if [ "${USER}" != "root" ]; then
    echo "Please run as root"
    exit
fi

apt-get install python-dev
apt-get install python-rpi.gpio
apt-get install python-smbus

#Setting Up I2C

install_source "i2c-bcm2708" && install_source "i2c-dev"
apt-get install i2c-tools

#Setting Up SPI

install_source "spidev"

if [ ! -e /usr/local/lib/python2.7/dist-packages/spidev.so ]; then
    PWD=`pwd`
    cd GPIO_Utilities/py-spidev
    python setup.py install
    cd ${PWD}
fi
