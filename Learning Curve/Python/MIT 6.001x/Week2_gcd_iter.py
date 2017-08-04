#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 21:43:55 2017

@author: michael
"""

"""
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    c = min(a, b)
    while a % c != 0 or b % c != 0:
        c-=1 
    print (c)
  """ 
       
# Base case is when b = 0
def gcdRecur(a, b):
    if b == 0:
        return a

    # Recursive case
    return gcdRecur(b, a % b)
            
            
        