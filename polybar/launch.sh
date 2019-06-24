#!/usr/bin/zsh
#####
# File: /home/sarange/.config/i3/polybar/launch.sh
# Project: /home/sarange/.config/i3/polybar
# Created Date: Monday, June 24th 2019, 3:08:45 pm
# Author: sarange
# -----
# Last Modified: Mon Jun 24 2019
# Modified By: sarange
# -----
# Copyright (c) 2019 sarange
# 
# Talk is cheap. Show me the code.
#####

# Terminate already running bar instances
killall -q polybar -9

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

for m in $(polybar --list-monitors | cut -d":" -f1); do
	WIRELESS=$(ls /sys/class/net/ | grep ^wl | awk 'NR==1{print $1}') MONITOR=$m polybar -c ~/.config/i3/polybar/config top -r 2>> ~/.config/i3/logs/top.log &
	WIRELESS=$(ls /sys/class/net/ | grep ^wl | awk 'NR==1{print $1}') MONITOR=$m polybar -c ~/.config/i3/polybar/config bottom -r 2>> ~/.config/i3/logs/bottom.log &
done


# # Launch polybar
# polybar -c ~/.config/i3/polybar/config top -r 2>> ~/.config/i3/logs/top.log &
# polybar -c ~/.config/i3/polybar/config bottom -r 2>> ~/.config/i3/logs/bottom.log &
