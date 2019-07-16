#!/usr/bin/bash
#####
# File: /home/sarange/i3/scripts/qrcode.sh
# Project: /home/sarange/i3/scripts
# Created Date: Tuesday, July 2nd 2019, 2:02:47 am
# Author: sarange
# -----
# Last Modified: Wed Jul 17 2019
# Modified By: sarange
# -----
# Copyright (c) 2019 sarange
# 
# Talk is cheap. Show me the code.
#####

qrencode "$1" -o /dev/shm/qrcode && feh /dev/shm/qrcode
