#!/home/sarange/.virtualenvs/i3/bin/python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/.config/i3/scripts/myvpn.py
Project: /home/sarange/.config/i3/scripts
Created Date: Wednesday, June 12th 2019, 1:03:22 pm
Author: sarange
-----
Last Modified: Mon Jun 17 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''

import subprocess

def main():
	nmcli = subprocess.Popen(('nmcli', 'con'), stdout=subprocess.PIPE)
	grep = str(subprocess.check_output(('grep', 'vpn'), stdin=nmcli.stdout))[2:]
	nmcli.wait()
	res = ''
	for greps in grep.split('\\n'):
		if 'enp2s0' in greps or 'bridge0' in greps:
			res = greps
	if res != '':
		return f"{res.split(' ')[1]} {res.split(' ')[2]}"
	else:
		return 'VPN Down'

if __name__ == '__main__':
	print(main())