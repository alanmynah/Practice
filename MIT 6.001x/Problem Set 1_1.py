#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 10:45:16 2017

@author: michael

MIT 6.00.1x 
Problem Set 1 Task 1

Task:
    
    Assume s is a string of lower case characters.

    Write a program that counts up the number of vowels 
    contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
    For example, if s = 'azcbobobegghakl', your program should print:
    Number of vowels: 5

"""

s = input('Give me your string: ')
count = 0

for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or \
    letter == 'u':
        count += 1

print ("Number of vowels: ", count)  


### ACCEPTED
