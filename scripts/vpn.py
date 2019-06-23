#!/home/sarange/.virtualenvs/i3/bin/python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/.config/i3/scripts/ipVpn.py
Project: /home/sarange/.config/i3/scripts
Created Date: Wednesday, June 12th 2019, 1:04:31 pm
Author: sarange
-----
Last Modified: Sun Jun 23 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''
import sys
sys.path.append('/home/sarange/.config/i3/scripts/')
from dnsleaktest import main as dns
import subprocess, os

def change():
	FNULL = open(os.devnull, 'w')
	output = detect(False)
	if output == 'VPN Down':
		vpn = subprocess.Popen(('nmcli', 'con', 'up', 'c069134e-37a2-484c-8fde-e51fb00c0725'), stdout=FNULL)
		vpn.wait()
	else:
		vpn = subprocess.Popen(('nmcli', 'con', 'down', output), stdout=FNULL)
		vpn.wait()

def detect(default=True):
	nmcli = subprocess.Popen(('nmcli', 'con'), stdout=subprocess.PIPE)
	grep = str(subprocess.check_output(('grep', 'vpn'), stdin=nmcli.stdout))[2:]
	nmcli.wait()
	res = ''
	for greps in grep.split('\\n'):
		if 'enp2s0' in greps or 'bridge0' in greps:
			res = greps
	if res != '':
		if default:
			return f"{res.split(' ')[1]} {res.split(' ')[2]}"
		else:
			for part in res.split(' '):
				if '-' in part:
					return part
	else:
		return 'VPN Down'

if __name__ == '__main__':
	print(detect())