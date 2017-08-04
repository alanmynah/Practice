#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 12:51:40 2017

@author: michael

MIT 6.00.1x 
Problem Set 1 Task 2

Task:
    
   Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2

"""

s = input("Enter your 'bob' string: ")

nbob = 0
nletter = -1

for char in s:
    nletter += 1
    if s[nletter:nletter+1] == "b":
            if s[nletter+1:nletter+2] == "o":
                        if s[nletter+2:nletter+3] == "b":
                            nbob += 1
print(nbob)

### ACCEPTED