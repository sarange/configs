#!/home/sarange/.virtualenvs/i3/bin/python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/.config/i3/scripts/ipVpn.py
Project: /home/sarange/.config/i3/scripts
Created Date: Wednesday, June 12th 2019, 1:04:31 pm
Author: sarange
-----
Last Modified: Sat Jun 29 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''
import sys
sys.path.append('/home/sarange/.config/i3/scripts/')
from dnsleaktest import main as dns
import subprocess, os

def change(vpnNum='default'):
	vpn = {'nl1' : 'c069134e-37a2-484c-8fde-e51fb00c0725',
	'nl2' : 'f1808f49-1614-417e-abac-106ac3ec6dcb',
	'us1' : '65f74ec7-4e27-4bee-9d1a-3317692f11d5',
	'us2' : '376213e9-0ef5-491d-bf63-621c7ca6ad4f',
	'jp1' : '89e0310b-9314-4e18-aa49-fe5d3b3a16eb',
	'jp2' : '5617a26e-cd0b-41b5-9e87-ede0a6702820'
	}
	FNULL = open(os.devnull, 'w')
	if vpnNum == 'default':
		output = detect(False)
		vpnNum = 'nl1'
		chose = output == 'VPN Down'
	if chose:
		vpn = subprocess.Popen(('nmcli', 'con', 'up', vpn[vpnNum]), stdout=FNULL)
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