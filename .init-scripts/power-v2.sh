#!/bin/bash
res=$(echo -e "Lock\nShutdown\nRestart\nCancel" | rofi -dmenu -i -p "Power: ")

case $res in
   Lock)
      xscreensaver-command -l
   ;;

   Shutdown)
      shutdown now
   ;;

   Restart)
      shutdown -r now
   ;;

  esac
