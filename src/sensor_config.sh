#!/bin/sh
ICOUNTER=0
PID=""
CBRUSHPID=""
while [ $ICOUNTER -lt 5 ]
do
    python ./BrushlessMod/BrushlessCentral.py ${ICOUNTER}
    CBRUSHPID=$$
    ./sensor_state.sh &  2> test.txt
    PID=$$
    echo -en "...PID..>>>>>$PID"
    sleep 1m
    kill -9 $PID
    kill -9 $CBRUSHPID
    sleep 1s
    if [ kill -0 $CBRUSHPID ];then
        kill -9 $CBRUSHPID
    fi
    if [ kill -0 $PID ]; then
        kill-9 $PID
    fi
    echo -en "......>>>>$ICOUNTER"
    ICOUNTER=$((ICOUNTER+1))
done
