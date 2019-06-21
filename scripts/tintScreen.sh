#!/bin/bash

if [[ "$@" = "1" ]]; then
  echo Making screen red
  GAMMA=1:1:1
  BRIGHTNESS=0.6
elif [[ "$@" = "2" ]]; then
  echo Making screen normal
  GAMMA=1:1:1
  BRIGHTNESS=0.8
elif [[ "$@" = "3" ]]; then
  echo Making screen normal
  GAMMA=1:1:1
  BRIGHTNESS=1.0
else
  echo Requires one of: "1", "2", "3"
  exit 128
fi

for output in $(xrandr --prop | grep \ connected | cut -d\  -f1); do
  xrandr --output $output --gamma $GAMMA --brightness $BRIGHTNESS
done