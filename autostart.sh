#! /bin/bash
ibus-daemon &
xscreensaver -nosplash &
source $HOME/.config/qtile/.init-scripts/enable-touchpad-click.sh &
xmodmap $HOME/.config/qtile/.init-scripts/xmodmap &
nitrogen --restore &
