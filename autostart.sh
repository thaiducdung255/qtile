#! /bin/bash
ibus-daemon &
xscreensaver -nosplash &
source $HOME/.config/qtile/.init-scripts/enable-touchpad-click.sh &&
source $HOME/.config/qtile/.init-scripts/toggle-touchpad.sh 1 &
xmodmap $HOME/.config/qtile/.init-scripts/xmodmap &
xmodmap $HOME/.config/qtile/.init-scripts/initscreen.sh &
nitrogen --restore &
