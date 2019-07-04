#!/home/sarange/.virtualenvs/i3/bin/python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/.config/i3/polybar/crypto.py
Project: /home/sarange/.config/i3/polybar
Created Date: Monday, June 17th 2019, 12:36:52 am
Author: sarange
-----
Last Modified: Mon Jul 01 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''
#%%
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from decimal import Decimal
import json
import re

def main():
	apiKey = open('/home/sarange/.config/i3/scripts/apiKey', 'r').read()
	url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
	headers = {
		'Accepts': 'application/json',
		'X-CMC_PRO_API_KEY': apiKey,
	}
	currencies = 'BTC,ETH'
	parameters = {
		'symbol' : currencies,
		'convert' : 'EUR'
	}
	session = Session()
	session.headers.update(headers)
	try:
		response = session.get(url, params=parameters)
		data = json.loads(response.text)['data']
	except (ConnectionError, Timeout, TooManyRedirects) as e:
		return e
	first = True
	output = ''
	ending = ''
	for currency in currencies.split(','):
		if not first:
			ending = '  '
		output += f"{ending}{currency}: {round(data[currency]['quote']['EUR']['price'])} {data[currency]['quote']['EUR']['percent_change_24h']}% "
		first = False
	return output

def waitForConnection():
	import requests
	while True:
		try:
			response = requests.get('http://www.google.com')
			return True
		except requests.ConnectionError:
			pass

if __name__ == '__main__':
	waitForConnection()
	print(main())