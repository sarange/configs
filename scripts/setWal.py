#!/home/sarange/.virtualenvs/i3/bin/python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/.config/i3/scripts/setWal.py
Project: /home/sarange/.config/i3/scripts
Created Date: Monday, June 24th 2019, 3:24:32 pm
Author: sarange
-----
Last Modified: Sat Jun 29 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''

def setWall(photo):
    from subprocess import call
    call(f'wal -i {photo} --saturate 0.9 -q'.split(' '))

def findMax(path):
    from os import listdir
    setWall(f'{path}/{max(listdir(path), key=lambda x : int(x[:-4]))}')


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        try:
            setWall(f'/home/sarange/.config/i3/wallpapers/{sys.argv[1]}.jpg')
            setWall(f'/home/sarange/.config/i3/wallpapers/{sys.argv[1]}.png')
        except:
            findMax('/home/sarange/.config/i3/wallpapers')
    else:
        findMax('/home/sarange/.config/i3/wallpapers')
