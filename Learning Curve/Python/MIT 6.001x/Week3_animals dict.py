#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 21:43:42 2017

@author: michael
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'e': {'a': 'coati',
'f': ['coati'], 'h': ['coati'], 'm': ['coati']}}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    result = 0
    for value in aDict:
        result += len(value)
    return result
