#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 20:27:24 2017

@author: wuzhenglin
"""
import io

def if_sensitive_word(filename):
      
    with io.open(filename, 'r', encoding='utf-8',) as f:
        txt = f.read()
        
    txt = txt.split('\n')
    
    user_enter = input('Please enter your sentence:\n')
    print 'Your enter is :', user_enter
    
    for line in txt:
        
        if line in user_enter:
            return True
            break

        

if __name__ == '__main__':
    file_name = 'filtered_words.txt'
    if_sen = if_sensitive_word(file_name)
    if if_sen:
        print 'Freedom'
    else:
        print 'Hunamn Rights'