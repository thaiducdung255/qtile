#!/usr/bin/env bash
res=$(echo -e "Shutdown\nRestart" | rofi -dmenu -i -p "Power")

case $res in
   Yes)
      shutdown now
   ;;

   No)
      reboot
   ;;
esac
