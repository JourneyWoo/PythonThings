#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 00:04:57 2017

@author: wuzhenglin
"""

import sys
sys.path.insert(0, '//Users/wuzhenglin/Python_nice/python100/python001')

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

from python001_net import generate

def get_pic():
    code = generate(1)
    code = code[0] 
    code = code[0 : 4]
    #print code
    
    width = 280
    height = 80
    
    image = Image.new('RGB', (width, height), (180, 180, 180))
    font = ImageFont.truetype('/Library/Fonts/Microsoft/Gulim.ttf', 80)
    draw = ImageDraw.Draw(image)
    
    
    RandomColor_1 = (random.randint(0, 80), random.randint(80, 160), random.randint(160, 240))
    RandomColor_2 = (random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))
    #if you want that different letter has different color
    #you could set a loop for 4 times
    draw.text( (40,0), unicode(code,'UTF-8'), font=font, fill = RandomColor_1)
    
    for i in range(1800):
        draw.point((random.randint(0,width), random.randint(0,height)), fill = RandomColor_2)
    
    
    image = image.filter(ImageFilter.BLUR)
    image.save('code_pic.JPEG')
        

    
    
if __name__ == '__main__':
    get_pic()