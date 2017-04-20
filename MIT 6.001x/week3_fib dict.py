#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 20:46:53 2017

@author: michael
"""

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
    
def fib_eff(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_eff(n-1, d) + fib_eff(n-2, d)
        d[n] = ans
        return ans

d = {1:1, 2:2}