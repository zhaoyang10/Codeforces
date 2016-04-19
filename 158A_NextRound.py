# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 20:07:56 2016

@author: Administrator
"""

n,k=map(int,raw_input().split())
a=map(int,raw_input().split())
k = k - 1
while k<n-1 and a[k+1]==a[k]:
    k = k + 1
while k>=0 and a[k] == 0:
    k = k - 1
print k + 1