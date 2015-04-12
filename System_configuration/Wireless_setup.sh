#!/bin/bash

#Copyright (C) 2015 Barajas D. Paul <Paul.Barajas@linux.com>

PWD=`pwd`
BACKUP_FOLDER="${PWD}/wireless_setting/restore_interface_system"

if [ "${USER}" != "root" ]; then
    echo "Please run as root"
    exit
fi

#create backup system 

mkdir ${BACKUP_FOLDER}
cp /etc/default/ifplugd ${BACKUP_FOLDER}
cp /etc/network/interfaces ${BACKUP_FOLDER}
cp /etc/rc.local ${BACKUP_FOLDER}

#copy files with the ip static

cp ${PWD }/wireless_setting/ifplugd /etc/default/
cp ${PWD }/wireless_setting/interfaces /etc/network/
cp ${PWD }/rc.local /etc

