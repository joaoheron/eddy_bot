window_id=$(wmctrl -l | awk '/Google Chrome/ {print strtonum($1)}')
xdotool -c $window_id