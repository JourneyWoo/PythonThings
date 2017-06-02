#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 11:23:48 2017

@author: wuzhenglin
"""
import random

def create_code(count):
    
    random_form = 4
    random_list = []
    for i in range(1000, 10000):
        random_list.append(i)
        i = i + 1

    code_200_list = []
    
    for j in range(count):
    
        random_num = random.sample(random_list, random_form)
        code = ''
        for i in range(random_form):
            if i == 3:
                break
            code = code + str(random_num[i]) + '-'
    
    
        code = code + str(random_num[i])
        code_200_list.append(code)
    
    return code_200_list

if __name__ == '__main__':
    code_list = create_code(10)
    print code_list