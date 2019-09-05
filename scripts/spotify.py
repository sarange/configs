#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/i3/scripts/spotify_status.py
Project: /home/sarange/i3/scripts
Created Date: Friday, June 21st 2019, 3:39:16 pm
Author: sarange
-----
Last Modified: Thu Sep 05 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''
from subprocess import check_output, call
from sys import argv
from os import path


def checkStatus():
	with open('/dev/null', 'w') as NULL:
		status = check_output(['playerctl', '--player=spotify', 'metadata', '--format', '"{{ title }} - {{artist}}"'], stderr=NULL).decode("utf-8").split('"')[1]
		sign = check_output(['playerctl', 'status', '--format', '"{{status}}"'], stderr=NULL).decode("utf-8").split('"')[1]
		if 'Play' in sign:
			sign = ''
		elif 'Pause' in sign:
			sign = ''
	return [status, sign]

def playPause():
	call(['playerctl', '--player=spotify', 'play-pause'])
	return 0

def next():
	logFile = f'{path.realpath(__file__).split("i3")[0]}/i3/logs/spotify.log'
	call(['playerctl', '--player=spotify', 'next'])
	with open(logFile, 'w') as log:
		log.write(f'part: {0}')
	return 0

def rollThat(out, length, part):
	out = f'{out} | '
	part2 = (part+length)%len(out)
	if part < part2:
		return out[part:part2]
	else:
		return f'{out[part:]}{out[:part2]}'

def checkRolling(length):
	stat = checkStatus()
	if length < len(stat[0]):
		logFile = f'{path.realpath(__file__).split("i3")[0]}/i3/logs/spotify.log'
		with open(logFile, 'r') as log:
			try:
				part = int(log.readline().split('part: ')[1])%length
			except:
				part = 0
		with open(logFile, 'w') as log:
			log.write(f'part: {part + 1}')
		return f'{rollThat(stat[0], length, part)} {stat[1]}'
	else: 
		return ' '.join(checkStatus())

if __name__ == "__main__":
	if len(argv) > 1:
		if argv[1] == 'rolling':
			print(checkRolling(int(argv[2])))
		elif argv[1] == 'playPause':
			playPause()
		elif argv[1] == 'next':
			next()
	else:
		print(' '.join(checkStatus()))