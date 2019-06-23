#!/home/sarange/.virtualenvs/i3/bin/python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/.config/i3/scripts/checkUpdates.py
Project: /home/sarange/.config/i3/scripts
Created Date: Sunday, June 23rd 2019, 1:29:08 pm
Author: sarange
-----
Last Modified: Sun Jun 23 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''
import shlex
from subprocess import check_output

def main():
    kernel = ''
    with open('/dev/null', 'w') as NULL:
        pacman = str(check_output(['checkupdates'], stderr=NULL))[2:-1]
        aur = str(check_output(['yay','-Qum'], stderr=NULL))[2:-1]
    if pacman == '' and aur == '':
        print('')
    else:
        if 'linux' in pacman:
            kernel = ''
        else:
            kernel = ''
        lpacman = len(pacman.split('\\n')) - 1
        laur = len(aur.split('\n')) - 1
        print(f' {lpacman}:{laur} {kernel}')

if __name__ == '__main__':
    main()