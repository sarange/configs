#!/home/sarange/.virtualenvs/i3/bin/python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/.config/i3/scripts/checkUpdates.py
Project: /home/sarange/.config/i3/scripts
Created Date: Sunday, June 23rd 2019, 1:29:08 pm
Author: sarange
-----
Last Modified: Tue Jul 16 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''
import shlex
from subprocess import check_output

def main(lst=False):
    icon = ''
    with open('/dev/null', 'w') as NULL:
        problem = True
        while problem:
            try:
                pacman = str(check_output(['checkupdates'], stderr=NULL))[2:-1].replace('\\n', '\n')
                aur = str(check_output(['yay','-Qum'], stderr=NULL))[2:-1].replace('\\n', '\n')
                problem = False
            except:
                problem = True
    if not lst:
        if pacman == '' and aur == '':
            return ''
        else:
            if 'linux-' in pacman:
                icon = ''
            else:
                icon = ''
            lpacman = len(pacman.split('\n')) - 1
            laur = len(aur.split('\n')) - 1
            return f'{icon} {lpacman}|{laur}'
    else:
        with open(f'{__import__("os").path.realpath(__file__).split("i3")[0]}/i3/logs/updates.log', 'w') as file:
            update = ''
            if not pacman == '':
                update += f'Pacman:\n{pacman}\n'
            if not aur == '':
                update += f'AUR:\n{aur}'
            file.write(update)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        main(True)
    else:
        print(main())