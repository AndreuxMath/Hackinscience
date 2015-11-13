# -*- coding: utf-8 -*-
"""
Created on Fri Oct 02 09:58:53 2015

@author: Mathieu
"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(alphabet)):
    for j in range(len(alphabet)):
        print(alphabet[i] + alphabet[j])
