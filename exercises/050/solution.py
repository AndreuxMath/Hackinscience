# -*- coding: utf-8 -*-
"""
Created on Fri Oct 02 09:54:08 2015

@author: Mathieu
"""
s = 0
for i in range(1001):
    if(i % 3 == 0) or (i % 5 == 0):
        s += i
print(s)
