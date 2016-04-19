# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 16:27:41 2016

@author: Administrator
"""

n = input()
a = sorted(map(int,raw_input().split()))
s = sum(a)
s0 = 0
for i in range(len(a)-1, -1, -1):
    s0 += a[i]
    if s0*2 > s:
        break
print len(a) - i