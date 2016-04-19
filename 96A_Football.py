# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 22:38:33 2016

@author: Administrator
"""

#a = raw_input()
#b = '2'
#c = [-1]
#for i in range(len(a)):
#    if a[i] != b:
#        c.append(i)
#        b = a[i]
#c.append(len(a))
#flag= False
#for i in range(len(c) - 1):
#    if c[i + 1] - c[i] >= 7:
#        flag = True
#        break
#if flag:
#    print 'YES'
#else:
#    print 'NO'

a = raw_input()
print 'YES' if '1'*7 in a or '0'*7 in a else 'NO'