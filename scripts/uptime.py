#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/.config/i3/scripts/uptime.py
Project: /home/sarange/.config/i3/scripts
Created Date: Sunday, June 23rd 2019, 10:24:11 pm
Author: sarange
-----
Last Modified: Sun Sep 01 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''
from subprocess import check_output
import re

def main():
	uptime = str(check_output(['uptime', '-p']))[5:-3]
	d = {
	'minutes':'m',
	'minute':'m',
	'hours':'h',
	'hour':'h',
	'months':'M',
	'month':'M',
	'year':'Y',
	'years':'Y',
	' ':'',
	',':' '
	}
	pattern = re.compile(r'\b(' + '|'.join(d.keys()) + r')\b')
	result = pattern.sub(lambda x: d[x.group()], uptime)
	return result 

if __name__ == '__main__':
	print(main())