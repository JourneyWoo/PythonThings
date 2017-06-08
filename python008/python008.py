#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 19:46:55 2017

@author: wuzhenglin
"""

#from bs4 import BeautifulSoup
#import requests
#
#r = 'https://xiaozhou.net/got_hhkb_pro_2-2013-06-03.html'
#headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
#url = requests.get(r)
#soup = BeautifulSoup(url.content, 'lmxl')
#print soup

from goose import Goose
from goose.text import StopWordsChinese
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

url = 'https://xiaozhou.net/got_hhkb_pro_2-2013-06-03.html'

def extract(url):
    g = Goose({'stopwords_class': StopWordsChinese})
    article = g.extract(url = url)
    article = g.extract(url = url)
    return article.cleaned_text

if __name__ == '__main__':
    
    print extract(url)
    