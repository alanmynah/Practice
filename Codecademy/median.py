#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 19:41:59 2017

@author: michael
"""

given_list = [6, 8, 12, 2, 23]

def median(given_list):
    new_list = sorted(given_list)
    length = len(given_list)
    if length % 2 == 0:
        digit1 = int(len(new_list)/2)
        digit2 = int(len(new_list)/2 - 1)
        disp_digit = float(new_list[digit1] + new_list[digit2])/2
        return disp_digit
    else:
        disp_digit = float(len(new_list)/2) # .5 is rounded down here
        disp_digit = int(disp_digit)
        return new_list[disp_digit]
        
print (median(given_list))