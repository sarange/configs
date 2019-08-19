#!/usr/bin/zsh
#####
# File: Untitled-1
# Project: <<projectpath>>
# Created Date: Sunday, June 23rd 2019, 4:06:03 pm
# Author: sarange
# -----
# Last Modified: Mon Aug 19 2019
# Modified By: sarange
# -----
# Copyright (c) 2019 sarange
# 
# Talk is cheap. Show me the code.
#####

konsole -e "$@" &

pid="$!"

# Wait for the window to open and grab its window ID
winid=''
while : ; do
	winid="`wmctrl -lp | awk -vpid=$pid '$3==pid {print $1; exit}'`"
	[[ -z "${winid}" ]] || break
done

# Focus the window we found
wmctrl -ia "${winid}"

# Make it float
i3-msg floating enable > /dev/null;

# Move it to the mouse pointer
i3-msg move position mouse > /dev/null;

# Wait for the application to quit
wait "${pid}";