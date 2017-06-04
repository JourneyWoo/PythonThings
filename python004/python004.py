#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 21:57:39 2017

@author: wuzhenglin
"""

file_name = 'Jay.txt'
line_count = 0
word_count = 0
word_query_count = 0
wordlist_sum = []

with open(file_name, 'r') as f:
    for line in f:
        words = line.split(' ')
        line_count += 1
        word_count += len(words)
        wordlist_sum = wordlist_sum + words
        
        
print "The number of line(s): ", line_count
print "The number of word(s): ", word_count
print "*************************************"

query_word = raw_input("Please enter the word you want to query:\n")
for i in range(len(wordlist_sum)):
    
    if wordlist_sum[i] == query_word:
        word_query_count += 1

print "The number of word you want to query is: ", word_query_count   
        