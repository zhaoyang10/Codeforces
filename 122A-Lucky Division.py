# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 16:34:57 2016

@author: Administrator
"""
#
#a = [4, 7, 44, 47, 77, 444, 447, 474, 477, 744, 747, 774, 777]
#n = input()
#flag=False
#for x in a:
#    if n % x == 0:
#        flag=True
#print 'YNEOS'[not flag::2]

n=input()
print"YES"if any(set("47")>=set(str(i))and n%i==0 for i in range(1,n+1))else"NO"