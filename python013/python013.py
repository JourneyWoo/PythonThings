#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 22:59:45 2017

@author: wuzhenglin
"""

import urllib, urllib2
import re

def get_url(page_url):
    request = urllib2.Request(page_url)
    reference = urllib2.urlopen(request)
    page = reference.read()
    
    regex=re.compile(r'<img.*?class="BDE_Image" src="(.*?)".*?>')
    img_url_list=re.findall(regex,page)
    
    return img_url_list

def down_img(url_list, image_path):
    for img_url in url_list:
       urllib.urlretrieve(img_url,'%s/%s.jpg'%(image_path,img_url[-8:-5]))
       
    print 'Finish!!!'
    


if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/2166231880?see_lz=1' 
    path = '/Users/wuzhenglin/Python_nice/python100/python013/for_image_save' 
    urllist = get_url(url)
    down_img(urllist, path)