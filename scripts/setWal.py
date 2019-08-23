#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/.config/i3/scripts/setWal.py
Project: /home/sarange/.config/i3/scripts
Created Date: Monday, June 24th 2019, 3:24:32 pm
Author: sarange
-----
Last Modified: Tue Aug 20 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''

def setWall(photo):
	from subprocess import call

	call(f'wal -i {photo} --saturate 0.9 -q'.split(' '))
	with open(f'{__import__("os").path.realpath(__file__).split("i3")[0]}i3/logs/setWal.log', 'w') as f:
		f.write(photo)

def findMax(path):
	from os import listdir
	setWall(f'{path}/{max(listdir(path), key=lambda x : int(x[:-4]))}')

def findLast(path):
	setWall(open(path, 'r').readline())

if __name__ == '__main__':
	import sys
	if len(sys.argv) == 2:
		from os import path
		photo = f'{__import__("os").path.realpath(__file__).split("i3")[0]}i3/wallpapers/{sys.argv[1]}.'
		if path.isfile(f'{photo}jpg'):
			setWall(f'{photo}jpg')
		elif path.isfile(f'{photo}png'):
			setWall(f'{photo}png')
		else:
			findMax(f'{__import__("os").path.realpath(__file__).split("i3")[0]}i3/wallpapers')
	else:
		findLast(f'{__import__("os").path.realpath(__file__).split("i3")[0]}i3/logs/setWal.log')