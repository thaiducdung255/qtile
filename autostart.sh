#! /bin/bash
ibus-daemon &
xmodmap $HOME/.config/qtile/.init-scripts/xmodmap &
xscreensaver -nosplash &
source $HOME/.config/qtile/.init-scripts/enable-touchpad-click.sh &
