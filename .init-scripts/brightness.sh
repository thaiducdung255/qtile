#!/bin/bash

monitor_index=$2
cmd=$1
monitors=($(xrandr --listmonitors | awk '{printf "%s ", $4}'))
current_brightness=($(xrandr --verbose | awk '/Brightness/ {printf "%s ", $2}'))
new_brightness=1
sample_brightness=0.3

function set_new_brightness {
  case $cmd in
    inc)
      new_brightness=$(bc <<< "${current_brightness[$2]} + 0.1")
    ;;

    des)
      new_brightness=$(bc <<< "${current_brightness[$2]} - 0.1")
    ;;

    dim)
       if (( $(echo "${current_brightness[$2]} > $sample_brightness" | bc -l) ))
       then
         new_brightness=0
       else
         new_brightness=0.8
       fi 
    ;;

  esac
}
if [ "$monitor_index" != "" ]
then
  # change brightness independently
  set_new_brightness $cmd $monitor_index
  xrandr --output ${monitors[$monitor_index]} --brightness $new_brightness
else
  # change brightness of all monitors
  for i in ${!monitors[@]}
    do
      set_new_brightness $cmd $i
      xrandr --output ${monitors[$i]} --brightness $new_brightness
  done
fi
