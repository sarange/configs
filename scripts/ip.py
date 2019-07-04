#!/home/sarange/.virtualenvs/i3/bin/python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/.config/i3/scripts/ipDns.py
Project: /home/sarange/.config/i3/scripts
Created Date: Saturday, June 15th 2019, 3:50:36 pm
Author: sarange
-----
Last Modified: Sat Jun 29 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''
#%%
import subprocess, os, sys
sys.path.append('/home/sarange/.config/i3/scripts/')
from dnsleaktest import main as dns
import vpn
import datetime, time

def main():
	wget = subprocess.check_output(('wget', '-qO', '-', 'icanhazip.com'))
	icanhazip = str(wget)[2:-3]
	try:
		int(icanhazip.replace('.', ''))
	except Exception as error:
		print('icanhazip.com didn\'t return an ip')
		exit()
	output = vpn.detect()
	if output == 'VPN Down':
		output = f' {icanhazip}'
		code = 0
	else:
		dnsOutput = dns(True)
		if 'DNS may be leaking' in dnsOutput:
			output = f' {icanhazip}'
			code = 33
			with open('/home/sarange/.config/i3/logs/dns.log', 'a') as f:
				timestamp = datetime.datetime.now()
				f.write(f'{dnsOutput}\n{timestamp}')
		else:
			output = f' {icanhazip}'
			code = 0
	return output, code

def waitForConnection():
	import requests
	while True:
		try:
			response = requests.get('http://www.google.com')
			return True
		except requests.ConnectionError:
			pass
#%%
if __name__ == '__main__':
	enter = True
	try:
		if sys.argv[1] == 'change':
			vpn.change()
			open('/home/sarange/.config/i3/logs/lastDnsTest.log', 'w').write('0')
			print('')
			enter = False
		elif sys.argv[1] == 'changeCustom':
			vpnNum = open('/home/sarange/.config/i3/logs/vpnNum.log', 'r').read().split('\n')[0]
			vpn.change(vpnNum=vpnNum)
			open('/home/sarange/.config/i3/logs/lastDnsTest.log', 'w').write('0')
			open('/home/sarange/.config/i3/logs/vpnNum.log', 'w').write('')
			print('')
			enter = False
		elif sys.argv[1] == 'auto':
			ntime = open('/home/sarange/.config/i3/logs/lastDnsTest.log', 'r').read().split('\n')[0]
			waittime = 60
			until = time.time() - float(ntime)
			if waittime > until:
				enter = False
		elif sys.argv[1] == 'rmtime':
			open('/home/sarange/.config/i3/logs/lastDnsTest.log', 'w').write('0')
			enter = False
	except:
		pass
	if enter:
		waitForConnection()
		output, code = main()
		print(f'{output} ')
		open('/home/sarange/.config/i3/logs/lastDnsTest.log', 'w').write(f'{time.time()}\n{output}')
		exit(code)
	else:
		try:
			t = open('/home/sarange/.config/i3/logs/lastDnsTest.log', 'r').read().split('\n')
			print(f'{t[1]} {int(until//1)}')
		except:
			pass