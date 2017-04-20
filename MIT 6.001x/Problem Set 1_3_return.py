#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 17:41:25 2017

@author: michael

MIT 6.00.1x 
Problem Set 1 Task 2

Task:
    
   Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your 
program should print: "Longest substring in alphabetical order is: beggh"
In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should prin t: "Longest substring in alphabetical order is: abc"

'Note: This problem may be challenging. We encourage you to work smart. 
If you've spent more than a few hours on this problem, we suggest that you move
on to a different part of the course. If you have time, come back to this 
problem after you've had a break and cleared your head.


personal notes:
try (my_string.index('string_character_im_looking_for'))

"""

given_str = 'azcbobobegghakl'
abc_string = 'abcdefghijklmopqrstuvwxyz'
longest_string = []
nth_char = 0

for char in given_str:
    letter_were_looking_for = abc_string.find(char)
    position_of_letter = (abc_string.index(letter_were_looking_for)