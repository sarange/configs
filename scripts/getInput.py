#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/.config/i3/scripts/getInput.py
Project: /home/sarange/.config/i3/scripts
Created Date: Saturday, June 29th 2019, 6:41:33 pm
Author: sarange
-----
Last Modified: Wed Jul 24 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''
with open(f'{__import__("os").path.realpath(__file__).split("i3")[0]}/i3/logs/vpnNum.log', 'w') as f:
    sec = ['nl1', 'nl2', 'us1', 'us2', 'jp1', 'jp2']
    user = input('Options: nl1, nl2, us1, us2, jp1, jp2\nChose VPN:\n')
    if user in sec:
        f.write(user)
    else:
        print('Invalid option')