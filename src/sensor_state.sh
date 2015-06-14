#!/bin/sh
sResults="RESULTS"

python Oxygen_Mod/rpi_i2c_sample_code.py "wake"
python Ph_Mod/rpi_i2c_sample_code.py "wake"

sleep 3
mkdir -p $sResults
echo "${sResults}/Test.txt"
python Oxygen_Mod/rpi_i2c_sample_code.py R >>  "${sResults}/Oxygen_Results.txt"
python Ph_Mod/rpi_i2c_sample_code.py R >> "${sResults}/Ph_Results.txt"
python TempMod/lm35_temp.py R >> "${sResults}/Temp_Results.txt"


sleep 5

python Oxygen_Mod/rpi_i2c_sample_code.py SLEEP
python Ph_Mod/rpi_i2c_sample_code.py SLEEP
