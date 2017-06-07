#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 23:30:29 2017

@author: wuzhenglin
"""

import glob2

def cal_count(file_every):
    line = 0
    blank = 0
    note = 0
    for filename in file_every:
        f = open(filename, 'rb')
        for l in f:
            l = l.strip()
            line += 1
            if l == '':
                blank += 1
            elif l[0] == '#' or l[0] == '/':
                note += 1
        
        f.close()
    return (line, blank, note)
            
        

if __name__ == '__main__':
    file_every = glob2.glob('/Users/wuzhenglin/Python_nice/python100/python007/code_list/*.py')
    count_list = cal_count(file_every)
    print 'line_count: %d, blank_count: %d, note_count: %d' % (count_list[0], count_list[1], count_list[2])
