# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 22:21:54 2016

@author: Administrator
"""

n = input()
a = [0]*5
for i in map(int, raw_input().split()):
    a[i] += 1
print a[4] + a[3] + (a[2]+1)/2 + (max(0, a[1] - a[3] - (a[2]&1)*2) + 3) / 4