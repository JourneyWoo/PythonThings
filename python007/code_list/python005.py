#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 13:33:44 2017

@author: wuzhenglin
"""

#reference: https://zhuanlan.zhihu.com/p/25232848

from PIL import Image
import glob2

def change_pic():
    
    a = glob2.glob('/Users/wuzhenglin/Python_nice/python100/python005/photo_list/*.jpg')
    
    for i in a:
        
        img = Image.open(i)
        img.thumbnail((640, 320))
        print(img.format, img.size, img.mode)
        img.save(i, 'JPEG')
        

if __name__ == '__main__':
    change_pic()