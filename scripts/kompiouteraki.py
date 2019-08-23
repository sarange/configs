#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/i3/scripts/kompiouteraki.py
Project: /home/sarange/i3/scripts
Created Date: Tuesday, August 20th 2019, 3:39:12 pm
Author: sarange
-----
Last Modified: Tue Aug 20 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''

def kompi():
	praxi = input('poia praxi? ')
	ar1 = float(input('arithmos1: '))
	ar2 = float(input('arithmos2: '))
	if praxi == '+':
		print(ar1+ar2)
	elif praxi == '-':
		print(ar1-ar2)
	elif praxi == '*':
		print(ar1*ar2)
	elif praxi == '/':
		print(ar1/ar2)
	else:
		print('den xereis na grafeis')

for i in range(10):
	kompi()