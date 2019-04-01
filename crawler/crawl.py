# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 21:48:35 2019

@author: dilan
"""

import random
from bs4 import BeautifulSoup
import urllib2
from urlparse import urlparse
from urlparse import urljoin

urls = [line.rstrip('\n') for line in open('alexa.txt')]

def is_relative(url):
    return not bool(urlparse.urlparse(url).netloc)

for i in range(0, 1):
    while True:
        try:
            url0 = random.choice(urls)
            if not urlparse(url0).scheme:
                url0 = 'http://' + url0
            #print("URL0")
            #print(url0)
            page0 = urllib2.urlopen(url0)
            soup0 = BeautifulSoup(page0, 'html.parser')
            url1 = urljoin(url0, random.choice(soup0.find_all('a', href=True))['href'])
            #print("URL1")
            #print(url1)
            page1 = urllib2.urlopen(url1)
            soup1 = BeautifulSoup(page1, 'html.parser')
            url2 = urljoin(url1, random.choice(soup1.find_all('a', href=True))['href'])
            #print("URL2")
            #print(url2)
            page2 = urllib2.urlopen(url2)
            soup2 = BeautifulSoup(page2, 'html.parser')
            url3 = urljoin(url2, random.choice(soup2.find_all('a', href=True))['href'])
            #print("URL3")
            print(url3)
        except Exception as e:
            #print(e)
            continue
        else:
            break