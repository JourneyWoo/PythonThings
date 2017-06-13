#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 21:31:44 2017

@author: wuzhenglin
"""

import sys

reload(sys)  
sys.setdefaultencoding('utf8')
import io
file_name = '//Users/wuzhenglin/Python_nice/python100/python011/filtered_words.txt'

with io.open(file_name, 'r', encoding='utf-8',) as f:
       
    txt = f.read()
        
    txt = txt.split('\n')
    
    user_enter = input('Please enter your sentence:\n')
    print 'Your enter is :', user_enter
    
    for line in txt:
        
        if line in user_enter:
            flag = True
            user_enter = user_enter.replace(line, len(line)*'*')
        else:
            flag = False
            
    print user_enter
    



