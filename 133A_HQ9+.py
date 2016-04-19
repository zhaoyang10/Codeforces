# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 16:08:08 2016

@author: Administrator
"""

#a = raw_input()
#if a.find('H' or 'Q' or '9') != -1:
#    print 'YES'
#else:
#    print 'NO'
print "YNEOS"[not set('HQ9') & set(raw_input())::2]