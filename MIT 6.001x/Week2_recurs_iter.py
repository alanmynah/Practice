#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:47:25 2017

@author: michael
"""

"""
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp <= 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)
   """     
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1 
    while exp > 1:
        result *= base
        exp -= 1
    return result

