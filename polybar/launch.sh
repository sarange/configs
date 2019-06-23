#!/usr/bin/bash
#####
# File: /home/sarange/.config/i3/polybar/launch.sh
# Project: /home/sarange/.config/i3/polybar
# Created Date: Monday, June 17th 2019, 12:39:47 am
# Author: sarange
# -----
# Last Modified: Sun Jun 23 2019
# Modified By: sarange
# -----
# Copyright (c) 2019 sarange
# 
# Talk is cheap. Show me the code.
#####

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -x polybar >/dev/null; do sleep 1; done

# Launch polybar
polybar -c ~/.config/i3/polybar/config top -r 2>> ~/.config/i3/logs/top.log &
polybar -c ~/.config/i3/polybar/config bottom -r 2>> ~/.config/i3/logs/bottom.log &
