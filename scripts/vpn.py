#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/.config/i3/scripts/ipVpn.py
Project: /home/sarange/.config/i3/scripts
Created Date: Wednesday, June 12th 2019, 1:04:31 pm
Author: sarange
-----
Last Modified: Tue Oct 29 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''
import sys
sys.path.append(f'{__import__("os").path.realpath(__file__).split("i3")[0]}/i3/scripts/')
from dnsleaktest import main as dns
import subprocess, os
from re import search

def ufw(enable, ip=None):
	FNULL = open(os.devnull, 'w')
	if enable:
		com = subprocess.Popen(('sudo ufw default deny outgoing'.split(' ')), stdout=FNULL)
		com.wait()
		com = subprocess.Popen(('sudo ufw default deny incoming'.split(' ')), stdout=FNULL)
		com.wait()
		com = subprocess.Popen(('sudo ufw allow out on tun0 from any to any'.split(' ')), stdout=FNULL)
		com.wait()
		com = subprocess.Popen(('sudo ufw allow out to 172.16.0.0/12'.split(' ')), stdout=FNULL)
		com.wait()
		com = subprocess.Popen(('sudo ufw allow out to 192.168.1.0/24'.split(' ')), stdout=FNULL)
		com.wait()
		com = subprocess.Popen(('sudo ufw allow in to 192.168.1.0/24'.split(' ')), stdout=FNULL)
		com.wait()
		com = subprocess.Popen((f'sudo ufw allow out to {ip} port 1194 proto udp'.split(' ')), stdout=FNULL)
		com.wait()
	else:
		
		com = subprocess.Popen(('sudo ufw default allow outgoing'.split(' ')), stdout=FNULL)
		com.wait()
		com = subprocess.Popen(('sudo ufw default allow incoming'.split(' ')), stdout=FNULL)
		com.wait()
		com = subprocess.Popen(('sudo ufw delete allow out on tun0 from any to any'.split(' ')), stdout=FNULL)
		com.wait()
		try:
			numP = subprocess.check_output(('sudo ufw status numbered'.split(' ')))
			num = search('\[ (\d+)\][\d\. ]+1194/udp[ ]+ALLOW OUT[ ]+Anywhere', str(numP))
			com = subprocess.Popen((f'sudo ufw --force delete {num.group(1)}'.split(' ')), stdout=FNULL)
			com.wait()
		except:
			pass
		com = subprocess.Popen(('sudo ufw delete allow out to 172.16.0.0/12'.split(' ')), stdout=FNULL)
		com.wait()
		com = subprocess.Popen(('sudo ufw delete allow out to 192.168.1.0/24'.split(' ')), stdout=FNULL)
		com.wait()
		com = subprocess.Popen(('sudo ufw delete allow in to 192.168.1.0/24'.split(' ')), stdout=FNULL)
		com.wait()

def down():
	ufw(False)
	FNULL = open(os.devnull, 'w')
	if not detect(False) == 'VPN Down':
		vpn = subprocess.Popen(('nmcli', 'con', 'down', detect(False)), stdout=FNULL)
		vpn.wait()

def up(num):
	FNULL = open(os.devnull, 'w')
	vpn = subprocess.Popen(('nmcli', 'con', 'up', num), stdout=FNULL)
	vpn.wait()
	wget = subprocess.check_output(('wget', '-qO', '-', 'icanhazip.com'))
	icanhazip = str(wget)[2:-3]
	try:
		int(icanhazip.replace('.', ''))
	except Exception as error:
		print('icanhazip.com didn\'t return an ip')
		exit()
	ufw(True, icanhazip)

def change(vpnNum='default'):
	vpnlst = {
	'nl1' : 'c069134e-37a2-484c-8fde-e51fb00c0725',
	'nl2' : 'f1808f49-1614-417e-abac-106ac3ec6dcb',
	'nl3' : '73809dd5-d76d-4658-807c-ef4d9865491a',
	'us1' : '65f74ec7-4e27-4bee-9d1a-3317692f11d5',
	'us2' : '376213e9-0ef5-491d-bf63-621c7ca6ad4f',
	'jp1' : '89e0310b-9314-4e18-aa49-fe5d3b3a16eb',
	'jp2' : '5617a26e-cd0b-41b5-9e87-ede0a6702820',
	'jp3' : 'f01e9ca4-298a-459c-aac5-123f0b9740cb',
	}
	if vpnNum == 'default':
		output = detect(False)
		if output == 'VPN Down':
			up(vpnlst['nl1'])
		else:
			down()
	else:
		down()
		up(vpnlst[vpnNum])

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