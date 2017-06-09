#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 01:10:56 2017

@author: wuzhenglin
"""

from bs4 import BeautifulSoup
import urllib
import urllib2
import sys
reload (sys)
sys.setdefaultencoding('utf-8')



def extract_all_link(url):
    #get the proto and the domail
    proto, rest = urllib.splittype(url)
    domain = urllib.splithost(rest)[0]
    
    html = urllib2.urlopen(url).read()
    a = BeautifulSoup(html, "lxml").findAll('a')
    #fliter
    alist = [i.attrs['href'] for i in a if i.attrs['href'][0] != 'j']
    alist = map(lambda i: proto + '://' + domain + i if i[0] == '/' else url + i if i[0] == '#' else i, alist)
    
    return alist

if __name__ == '__main__':
    url = 'https://www.apple.com/cn/'
    for i in extract_all_link(url):
        print i
