#!/bin/bash
# follow_xdo.sh - Script follows @user on TikTok
url="https://www.tiktok.com/@$1"

google-chrome $url -incognito & 
sleep 3

# Click on Follow button
xdotool mousemove 1150 265
xdotool click 1
sleep 3

xdotool key Ctrl+w
