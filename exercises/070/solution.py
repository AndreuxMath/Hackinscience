# -*- coding: utf-8 -*-
"""
Created on Fri Oct 02 10:01:49 2015

@author: Mathieu
"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(alphabet)):
    for j in range(len(alphabet)):
        if(i!=j):
            print(alphabet[i] + alphabet[j])
