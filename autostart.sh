#! /bin/bash
ibus-daemon -d &
source $HOME/.config/qtile/.init-scripts/enable-touchpad-click.sh &&
source $HOME/.config/qtile/.init-scripts/toggle-touchpad.sh 1 &
source $HOME/.config/qtile/.init-scripts/initscreen.sh &
nitrogen --restore &
