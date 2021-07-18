#!/bin/bash
# close_chrome_xdo.sh - Script closes all chrome tabs

window_id=$(wmctrl -l | awk '/Google Chrome/ {print strtonum($1)}')

while [ ! -z "$window_id" ]
do
	xdotool key Ctrl+w
	sleep 2
    window_id=$(wmctrl -l | awk '/Google Chrome/ {print strtonum($1)}')
done
