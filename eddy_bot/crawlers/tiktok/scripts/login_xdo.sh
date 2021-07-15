#!/bin/bash
# login_xdo.sh - Script logs in TikTok using environment variables TIKTOK_USER and TIKTOK_PASSWORD
login_method="cellphone/email/google/facebook/twitter"
url="https://www.tiktok.com/"

# Open browser and set focus
google-chrome $url -incognito -new-window & 
sleep 3

# Maximize browser window
window_id=$(wmctrl -l | awk '/Google Chrome/ {print strtonum($1)}')
xdotool windowsize $window_id 100% 100%
sleep 3

# Click on Log In button
xdotool mousemove 1400 100
xdotool click 1
sleep 3

# Click on Log In method
xdotool mousemove 900 400
xdotool click 1
sleep 2

# Click on Log In with username or email
xdotool mousemove 1000 320
xdotool click 1
sleep 2

# Click on username field
xdotool mousemove 900 380
xdotool click 1

# Fill login information
xte "str $TIKTOK_USER"
xte "key Tab"
xte "str $TIKTOK_PASSWORD"
sleep 2

# Click on Log In button
xdotool mousemove 900 550
xdotool click 1

sleep 10 # Solve catpcha
