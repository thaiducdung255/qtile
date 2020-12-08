#! /bin/bash
ibus-daemon &
xmodmap ~/.init-scripts/xmodmap &
xscreensaver -nosplash &
source ~/.init-scripts/enable-touchpad-click.sh &
