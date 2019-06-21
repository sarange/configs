#!/home/sarange/.virtualenvs/i3/bin/python
# -*- coding:utf-8 -*-
'''
File: /home/sarange/.config/i3/scripts/potd.py
Project: /home/sarange/.config/i3/scripts
Created Date: Thursday, June 13th 2019, 5:34:19 pm
Author: sarange
-----
Last Modified: Mon Jun 17 2019
Modified By: sarange
-----
Copyright (c) 2019 sarange

Talk is cheap. Show me the code.
'''

import sys
import json
import time
from subprocess import check_output, call
import shlex
import random

def getBing(dirname, locale, resolution):
    photo = json.loads(check_output(shlex.split(f'curl -X GET "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt={locale}"')).decode('utf-8'))['images'][0]['urlbase'] + "_" + resolution + ".jpg"
    url = f'https://www.bing.com{photo}'
    photo_name = photo[photo.find(".") + 1:]
    filename = f'{dirname}/.local/share/wallpapers/Bing/{photo_name}'
    return filename, url

def getNasa(dirname, locale, resolution):
    photo = json.loads(check_output(shlex.split(f'curl -X GET https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&hd=True&date={time.strftime("%Y-%m-%d")}')).decode('utf-8'))
    if 'hdurl' in photo:
        url = photo['hdurl']
        photo_name = url[url.rfind("/") + 1:]
    else:
        return getBing(dirname, locale, resolution)
    filename = f'{dirname}/.local/share/wallpapers/NASA/{photo_name}'
    return filename, url

def setWallpapper(photo):
    call(f'feh --bg-fill {photo}'.split(' '))

def waitForConnection():
    import requests
    while True:
        try:
            response = requests.get("http://www.google.com")
            return True
        except requests.ConnectionError:
            pass

def main():
    #Initialize variables
    locale = 'en-US'
    resolution = '1920x1080'
    dirname = f'/home/{check_output("whoami").decode("utf-8").split()[0]}'
    lastLocation = f'{dirname}/.local/share/wallpapers/last.txt'
    lastPhoto = open(lastLocation, 'r').read().strip()

    #Set old photo as wall 
    setWallpapper(lastPhoto)
    
    #Wait for internet connection
    waitForConnection()

    #Choose site
    if random.getrandbits(1):
        filename, url = getBing(dirname, locale, resolution)
    else:
        filename, url = getNasa(dirname, locale, resolution)
    
    #Download the photo and set it as wallpaper
    call(f'wget {url} -O {filename}'.split(' '))
    setWallpapper(filename)

    #Write changes for the next time
    open(lastLocation, 'w').write(filename)

if __name__ == '__main__':
    main()