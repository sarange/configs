#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/.config/i3/scripts/volume.py
Project: /home/sarange/.config/i3/scripts
Created Date: Saturday, June 15th 2019, 12:29:17 pm
Author: sarange
-----
Last Modified: Wed Jul 24 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''

from subprocess import check_output
import shlex
import re

out = str(check_output(shlex.split('amixer get Master')))
if '[off]' in out:
    print('Muted')
else:
    out2 = re.search('\[(.*?)\]', out).group(1)
    print(out2)