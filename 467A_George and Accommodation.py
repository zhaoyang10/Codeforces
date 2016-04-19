# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 16:59:33 2016

@author: Administrator
"""

#n = input()
#s = 0
#for i in range(n): 
#    if eval(raw_input().replace(' ', '-')) < -1: 
#        s+=1 
#print s

print sum(1 for _ in range(input()) if -eval(raw_input().replace(' ', '-')) >= 2)