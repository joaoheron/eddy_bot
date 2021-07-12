#!/bin/bash
# login_xdo.sh - script logs into TikTok

url="https://www.tiktok.com/"
email=""
pwd=""
 
google-chrome $url &
 
# wait for the page to open, the set focus to it
sleep 2
# wmctrl -a "Tiktok - Chromium"
# sleep 1 # allow time to get focus before sending keys
# window_id = wmctrl -l | awk '/Google Chrome/ {print $1}'
window_id=$(wmctrl -l | awk '/Google Chrome/ {print strtonum($1)}')
xdotool key alt+super+Up
# xdotool windowsize $window_id 100% 100%
echo "sleepy sleep"
# xdotool windowminimize <window_id>
xdotool mousemove 1000 1000
xdotool click 2
sleep 2
xdotool click 3
sleep 2

xdotool mousemove 100 100 
xdotool click 2
sleep 2

# xdotool click 3
# sleep 2

# xdotool mousemove 20 500
# xdotool click 2
# sleep 2

# xdotool click 3
# sleep 2

# xdotool mousemove 500 20
# xdotool click 2
# sleep 2

# xdotool click 3

# sleep 100

# xte "str $email"
# xte "str $pwd"
# xte "key Tab"
# xte "key Tab"
# xte "key Tab"
# xte "key Tab"
# xte "key Tab"
xte "key Return"
 
echo "Netflix Login Done..."