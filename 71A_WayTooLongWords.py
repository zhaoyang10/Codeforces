# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 11:11:39 2016

@author: Administrator
"""
n = int(raw_input())
for i in range(n):
    input_str = raw_input()
    length = len(input_str)
    if length > 10:
        print input_str[0]+str(length - 2)+input_str[-1]
    else:
        print input_str
