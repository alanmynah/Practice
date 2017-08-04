#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 21:04:16 2017

@author: michael
"""

def remove_dups(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
            
def remove_dups2(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
            
L1 = [1, 2, 4, 5, 6]
L2 = [1, 3, 4, 5, 7]

