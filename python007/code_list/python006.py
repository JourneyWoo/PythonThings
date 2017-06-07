#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 17:27:14 2017

@author: wuzhenglin
"""

import re, os
from collections import Counter

stop_word = ['the', 'in', 'of', 'and', 'to', 'has', 'that', 's', 'is', 'are', 'a', 'with', 'as', 'an']

def getCounter(articlefilesource):
    pattern = r'''[A-Za-z]+|\$?\d+%?$'''
    with open(articlefilesource) as f:
        r = re.findall(pattern, f.read())
#        print r
#        print Counter(r)
        return Counter(r)
    
def run(path):
    os.chdir(path)
    sum_count = Counter()
#    print os.listdir(os.getcwd())
    for i in os.listdir(os.getcwd()):
#        print os.path.splitext(i)
#        ('11', '.txt')
#        ('22', '.txt')
        if os.path.splitext(i)[1] == '.txt':
            sum_count += getCounter(i)
    
    for i in stop_word:
        sum_count[i] = 0
    
#    print sum_count.most_common()
    print sum_count.most_common()[0][0]
       
    
if __name__ == '__main__':
    run('/Users/wuzhenglin/Python_nice/python100/python006/diary_list')