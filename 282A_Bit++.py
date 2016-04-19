# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 22:11:08 2016

@author: Administrator
"""
#
#n = input()
#s = 0
#for i in range(n):
#    s += raw_input()[1] == '-'
#n = n - s * 2
#print n
print sum([-1,1][raw_input()[1] == '+'] for _ in range(input()))