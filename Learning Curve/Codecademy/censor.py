#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 19:37:45 2017

@author: michael
"""

text = 'haha i know where you are, yes you. you i said'
word = 'you'
def censor(text, word):
    return text.replace(word, '*' * len(word))

print (censor(text, word))