#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 20:37:17 2017

@author: michael
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0 
    for key in aDict.keys():
       if len(aDict(key)) >= biggestValue:
           result = key
           biggestValue = len(aDict[key])
    return result

           