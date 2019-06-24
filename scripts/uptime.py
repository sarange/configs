#!/home/sarange/.virtualenvs/i3/bin/python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/.config/i3/scripts/uptime.py
Project: /home/sarange/.config/i3/scripts
Created Date: Sunday, June 23rd 2019, 10:24:11 pm
Author: sarange
-----
Last Modified: Mon Jun 24 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''
from subprocess import check_output

def main():
    uptime = str(check_output('uptime')).split('up')[1].strip().split(',')[0]
    if ':' in uptime:
        hours = int(uptime.split(':')[0])
        minutes = int(uptime.split(':')[1])
        return f'{hours}h {minutes}m'
    else:
        hours = 0
        minutes = int(uptime.split('min')[0].strip())
        return f'{minutes}m'
if __name__ == '__main__':
    print(main())