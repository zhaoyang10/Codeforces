# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 15:15:01 2016

@author: Administrator
"""

a = raw_input()
flag = 0
for x in a:
    if x < 'A' or x > 'Z':
        flag = 1
if flag == 0:
    print a.lower()
else:
    for x in a[1:len(a)]:
        if x < 'A' or x > 'Z':
            flag = 2
    if flag == 1:
        print a[0].upper() + a[1:len(a)].lower()
    else:
        print a            
