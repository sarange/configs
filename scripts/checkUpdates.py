#!/home/sarange/.virtualenvs/i3/bin/python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/.config/i3/scripts/checkUpdates.py
Project: /home/sarange/.config/i3/scripts
Created Date: Sunday, June 23rd 2019, 1:29:08 pm
Author: sarange
-----
Last Modified: Mon Jun 24 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''
import shlex
from subprocess import check_output

def main(lst=False):
    kernel = ''
    with open('/dev/null', 'w') as NULL:
        problem = True
        while problem:
            try:
                pacman = str(check_output(['checkupdates'], stderr=NULL))[2:-1]
                aur = str(check_output(['yay','-Qum'], stderr=NULL))[2:-1]
                problem = False
            except:
                problem = True
    if pacman == '' and aur == '':
        return ''
    elif not lst:
        if 'linux-' in pacman:
            kernel = ''
        else:
            kernel = ''
        lpacman = len(pacman.split('\\n')) - 1
        laur = len(aur.split('\n')) - 1
        return f'{kernel} {lpacman}|{laur}'
    else:
        with open('/home/sarange/.config/i3/logs/updates.log', 'w') as updates:
            updates.write(f'Pacman: {pacman}AUR: {aur}')

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        main(True)
    else:
        print(main())