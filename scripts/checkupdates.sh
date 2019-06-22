#!/usr/bin/zsh
#####
# File: /home/sarange/.config/i3/scripts/checkupdates.sh
# Project: /home/sarange/.config/i3/scripts
# Created Date: Monday, June 17th 2019, 10:42:55 am
# Author: sarange
# -----
# Last Modified: Fri Jun 21 2019
# Modified By: sarange
# -----
# Copyright (c) 2019 sarange
# 
# Talk is cheap. Show me the code.
#####

#!/bin/sh

if ! updates_arch=$(checkupdates 2> /dev/null | wc -l ); then
    updates_arch=0
fi

if ! updates_aur=$(yay -Qum 2> /dev/null | wc -l); then
    updates_aur=0
fi

updates=$(("$updates_arch" + "$updates_aur"))

if [ "$updates" -gt 0 ]; then
    echo " $updates_arch:$updates_aur"
else
    echo ""
fi
