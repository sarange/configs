#!/bin/bash

if [[ "$@" = "on" ]]; then
  echo Making screen red
  GAMMA=1:0:0
  BRIGHTNESS=0.8
elif [[ "$@" = "off" ]]; then
  echo Making screen normal
  GAMMA=1:1:1
  BRIGHTNESS=1
else
  echo Requires one of: "on", "off"
  exit 128
fi

for output in $(xrandr --prop | grep \ connected | cut -d\  -f1); do
  xrandr --output $output --gamma $GAMMA --brightness $BRIGHTNESS
done