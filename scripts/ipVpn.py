#!/home/sarange/.virtualenvs/i3/bin/python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/.config/i3/scripts/ipVpn.py
Project: /home/sarange/.config/i3/scripts
Created Date: Wednesday, June 12th 2019, 1:04:31 pm
Author: sarange
-----
Last Modified: Mon Jun 17 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''
import sys
sys.path.append('/home/sarange/.config/i3/scripts/')
from myvpn import main as m
from dnsleaktest import main as dns
import subprocess, os

def main():
	FNULL = open(os.devnull, 'w')
	output = m()
	if output == 'VPN Down':
		nl = subprocess.Popen(('nmcli', 'con', 'up', 'c069134e-37a2-484c-8fde-e51fb00c0725'), stdout=FNULL)
		nl.wait()
	elif  'Netherlands 1' in output:
		nl = subprocess.Popen(('nmcli', 'con', 'down', 'c069134e-37a2-484c-8fde-e51fb00c0725'), stdout=FNULL)
		nl.wait()
	else:
		return 'Error'


if __name__ == '__main__':
	main()