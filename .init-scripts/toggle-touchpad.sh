# !/bin/bash

isEnableTouchPadCmd=$1

touchpadDeviceId=$(xinput | grep ^.*Touchpad | sed 's/.+id=//' | awk '{print $4, $5}' | sed 's/[a-zA-Z=\ \[]//g')

if [ $isEnableTouchPadCmd -eq 1 ]
then
   xinput enable $touchpadDeviceId
else
   xinput disable $touchpadDeviceId
fi
