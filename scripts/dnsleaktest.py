#!/home/sarange/.virtualenvs/i3/bin/python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/.config/i3/scripts/dnsleaktest.py
Project: /home/sarange/.config/i3/scripts
Created Date: Thursday, June 6th 2019, 8:20:59 pm
Author: sarange
-----
Last Modified: Mon Jun 17 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''


import os
import subprocess
import json
from random import randint
from platform import system as system_name
from subprocess import call as system_call
from random import randint

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

def ping(host):
    fn = open(os.devnull, 'w')
    param = '-n' if system_name().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]
    retcode = system_call(command, stdout=fn, stderr=subprocess.STDOUT)
    fn.close()
    return retcode == 0

def main(mode):
    output = ''
    leak_id = randint(1000000,9999999)
    for x in range (0, 10):
        ping('.'.join([str(x),str(leak_id),"bash.ws"]))

    response = urlopen("https://bash.ws/dnsleak/test/"+str(leak_id)+"?json")
    data = response.read().decode("utf-8")
    parsed_data = json.loads(data)

    output += "Your IP:" + '\n'
    for dns_server in parsed_data:
        if dns_server['type'] == "ip":
            if dns_server['country_name']:
                if dns_server['asn']:
                    output += dns_server['ip']+" ["+dns_server['country_name']+", "+dns_server['asn']+"]" + '\n'
                else:
                    output += dns_server['ip']+" ["+dns_server['country_name']+"]" + '\n'
            else:
                output += dns_server['ip'] + '\n'

    servers = 0
    for dns_server in parsed_data:
        if dns_server['type'] == "dns":
            servers = servers + 1

    if servers == 0:
        output += "No DNS servers found" + '\n'
    else:
        output += "You use "+str(servers)+" DNS servers:" + '\n'
        for dns_server in parsed_data:
            if dns_server['type'] == "dns":
                if dns_server['country_name']:
                    if dns_server['asn']:
                        output += dns_server['ip']+" ["+dns_server['country_name']+", "+dns_server['asn']+"]" + '\n'
                    else:
                        output += dns_server['ip']+" ["+dns_server['country_name']+"]" + '\n'
                else:
                    output += dns_server['ip'] + '\n'
        
    output += "Conclusion:" + '\n'
    for dns_server in parsed_data:
        if dns_server['type'] == "conclusion":
            if dns_server['ip']:
                output += dns_server['ip'] + '\n'
                mode2 = dns_server['ip']
    if mode:
        return output
    else:
        return mode2
if __name__ == '__main__':
    print(main(True))