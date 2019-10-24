#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/i3/scripts/spotify_status.py
Project: /home/sarange/i3/scripts
Created Date: Friday, June 21st 2019, 3:39:16 pm
Author: sarange
-----
Last Modified: Sat Oct 19 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''
from subprocess import check_output, call
from os import path
from sys import argv

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
	logFile = f'{path.realpath(__file__).split("i3")[0]}/i3/logs/spotify.log'
	stat = checkStatus()
	if 'Advertisement' in stat[0] or 'Spotify' in stat[0]:
		sink = check_output(['pacmd', 'list-sink-inputs']).decode('utf-8').split('index: ')
		for index in sink:
			if 'Spotify' in index:
				sink = index.split('\n')[0]
		call(['pacmd', 'set-sink-input-mute', sink, 'true'])
		with open(logFile, 'w') as log:
			log.write('\nMuted')
		return 'Advertisement Muted '
	else:
		sink = check_output(['pacmd', 'list-sink-inputs']).decode('utf-8').split('index: ')
		for index in sink:
			if 'spotify' in index.lower():
				call(['pacmd', 'set-sink-input-mute', index.split('\n')[0], 'false'])
	if length < len(stat[0]):
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
	try:
		if len(argv) > 1:
			if argv[1] == 'rolling':
				print(checkRolling(int(argv[2])))
			elif argv[1] == 'playPause':
				playPause()
			elif argv[1] == 'next':
				next()
		else:
			print(' '.join(checkStatus()))
	except:
		pass