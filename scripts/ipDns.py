#!/home/sarange/.virtualenvs/i3/bin/python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/.config/i3/scripts/ipDns.py
Project: /home/sarange/.config/i3/scripts
Created Date: Saturday, June 15th 2019, 3:50:36 pm
Author: sarange
-----
Last Modified: Fri Jun 21 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''
#%%
import subprocess, os, sys
sys.path.append('/home/sarange/.config/i3/scripts/')
from dnsleaktest import main as dns
from myvpn import main as m
import ipDns
import datetime, time

def main():
	wget = subprocess.check_output(('wget', '-qO', '-', 'icanhazip.com'))
	out1 = str(wget)[2:-3]
	output = m()
	if output == 'VPN Down':
		output = f' {out1}'
		code = 0
	else:
		dnsOutput = dns(True)
		if 'DNS may be leaking' in dnsOutput:
			output = f' {out1}'
			code = 33
			with open('/home/sarange/.config/i3/dns.log', 'a') as f:
				timestamp = datetime.datetime.now()
				f.write(f'{dnsOutput}\n{timestamp}')
		else:
			output = f' {out1}'
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
			ipDns.main()
		elif sys.argv[1] == 'auto':
			ntime = open('/home/sarange/.config/i3/lastDnsTest.log', 'r').read()
			waittime = 29
			if float(ntime) + waittime > time.time():
				enter = False
	except:
		pass
	if enter:
		waitForConnection()
		output, code = main()
		print(output)
		open('/home/sarange/.config/i3/lastDnsTest.log', 'w').write(str(time.time()))
		exit(code)