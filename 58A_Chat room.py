# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 16:43:37 2016

@author: Administrator
"""

a = raw_input()
s = 0
for x in a:
    if s == 0 and x == 'h':
        s += 1
    elif s == 1 and x == 'e':
        s += 1
    elif s == 2 and x == 'l':
        s += 1
    elif s == 3 and x == 'l':
        s += 1
    elif s == 4 and x == 'o':
        s += 1
print 'YNEOS'[not s == 5::2]