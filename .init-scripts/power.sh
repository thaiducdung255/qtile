#!/bin/bash

res=$(xmessage -buttons Lock,Shutdown,Restart,Cancel -print "Power ?" -timeout 5)

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
