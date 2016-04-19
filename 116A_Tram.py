# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 14:57:26 2016

@author: Administrator
"""

n = input()
ans = 0
cap = 0
for i in range(n):
    a,b = map(int, raw_input().split())
    c = b - a
    cap += c
    if cap > ans:
        ans = cap
print ans