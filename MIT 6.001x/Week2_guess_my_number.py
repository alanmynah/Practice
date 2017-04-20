#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 15:58:57 2017

@author: michael

MIT 6.00.1x 
Problem Set 1 Task 2

Task:
    
   In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 
(inclusive) and 100 (not inclusive). The computer makes guesses, and you give 
it input - is its guess too high or too low? Using bisection search, the 
computer will guess the user's secret number!

"""

app_val = 1
step = 1
guess_counter = 0
high = 99
low = 0
guess = int((high+low)/2)

number = int(input('Please think of a number between 0 and 100! '))
if guess == number: 
    print ('I thought so.\n'
           'So to sum it up.\n'
           'It took me %d attempts to guess and %d is your number' % 
           (guess_counter, guess)
           )
else:
    while abs(guess - number) >= app_val:
        print ('Is your number %d?' % guess)
        guess_counter += 1 
        reply = str(input("""
                          Enter 'h' to indicate the guess is too high. 
                          Enter 'l' to indicate the guess is too low. 
                          Enter 'c' to indicate I guessed correctly """
                          ))
        if reply in ['h']:
            high = guess
        elif reply in ['l']:
            low = guess
        elif reply in ['c']:
            print ('I thought so.\n'
                   'So to sum it up.\n'
                   'It took me %d attempts to guess and %d is your number' % 
                   (guess_counter, guess)
                   )
        else:
            print ('Sorry, I did not catch that. Please try again.')
        guess = int((high+low)/2)
        
        if guess == number: 
             print ('I thought so.\n'
                   'So to sum it up.\n'
                   'It took me %d attempts to guess and %d is your number' % 
                   (guess_counter, guess)
                   )