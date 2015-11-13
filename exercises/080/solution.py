# -*- coding: utf-8 -*-
"""
Created on Fri Oct 02 10:02:57 2015

@author: Mathieu
"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(alphabet)):
    for j in range(i+1, len(alphabet)):
            print(alphabet[i] + alphabet[j])
