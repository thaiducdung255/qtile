#!/usr/bin/env bash
res=$(echo -e "Shutdown\nRestart" | rofi -dmenu -i -p "Power")

case $res in
   Shutdown)
      shutdown now
   ;;

   Restart)
      reboot
   ;;
esac
