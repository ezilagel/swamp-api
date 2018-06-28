#!/bin/bash

#app_path='/home/pi/apps/git/swamp-api'
house_temp_call='/usr/bin/python therm.py -t'
set_cool_temp_call='/usr/bin/python therm.py -s'
therm_mode_call='/usr/bin/python therm.py -m'
fan_status_call='/usr/bin/python therm.py -f'

#cd $app_path

clear

while true; do

	house_temp=$($house_temp_call)
	set_cool_temp=$($set_cool_temp_call)
	therm_mode=$($therm_mode_call)
	fan_status=$($fan_status_call)
	clear

	if [ "$therm_mode" == "3" ]
	then
		echo "Cooling Requested"
		echo "Requested Temp:" $set_cool_temp
		echo "Is Fan ON? " $fan_status
		if [ "$fan_status" == "True" ]
		then
			temp_diff=$(( $house_temp - $set_cool_temp ))
			echo "Temp Difference:" $temp_diff
			if (( $temp_diff < 2  ))
			then
				echo "Low Cool"
				curl -X GET 192.168.3.234/swamp/low-cool > /dev/null 2>&1
			elif (( $temp_diff > 1  ))
			then
				echo "High Cool"
                                curl -X GET 192.168.3.234/swamp/high-cool > /dev/null 2>&1
			fi
		else
			echo "Swamp Cooler Off"
			curl -X GET 192.168.3.234/swamp/off > /dev/null 2>&1
		fi
	else
		echo "Swamp Cooler Off"
		curl -X GET 192.168.3.234/swamp/off > /dev/null 2>&1
	fi
	echo "Current Temp:" $house_temp
	sleep 60
done
