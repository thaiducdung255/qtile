#!/usr/bin/env bash
res=$(echo -e "Yes\nNo" | rofi -dmenu -i -p "Power off ?")

case $res in
   Yes)
      shutdown now
   ;;

   No)
   ;;
esac
