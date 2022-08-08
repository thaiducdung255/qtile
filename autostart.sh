#! /bin/bash
ibus-daemon -d &
source $HOME/.config/qtile/.init-scripts/enable-touchpad-click.sh &&
source $HOME/.config/qtile/.init-scripts/toggle-touchpad.sh 1 &
source $HOME/.config/qtile/.init-scripts/initscreen.sh &
[ -v ENABLE_XMODMAP ] && [ -s "/usr/bin/xmodmap" ] && xmodmap $HOME/.config/xmodmap/xmodmap &
[ -s /usr/bin/nitrogen ] && nitrogen --restore &
