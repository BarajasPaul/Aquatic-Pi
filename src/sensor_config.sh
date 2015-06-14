#!/bin/sh
ICOUNTER=0
PID=""

while [ $ICOUNTER -lt 5 ]
do
    ./sensor_state.sh &  2> test.txt
    PID=$$
    echo -en "...PID..>>>>>$PID"
    sleep 1m
    kill -9 $PID
    echo -en "......>>>>$ICOUNTER"
    ICOUNTER=$((ICOUNTER+1))

done
