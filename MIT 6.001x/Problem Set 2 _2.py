#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 18:02:29 2017

@author: michael

Now write a program that calculates the minimum fixed monthly payment needed 
in order pay off a credit card balance within 12 months. By a fixed monthly 
payment, we mean a single number which does not change each month, but instead 
is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will 
pay off all debt in under 1 year
"""

def debt_repay(balance, annualInterestRate):
    
    monthlyInterestRate = annualInterestRate/12.0
    fixedPayment = 0
    while True:
        month = 0
        prevBal = balance
        while month < 12:
            prevBal = prevBal - fixedPayment
            prevBal = prevBal + monthlyInterestRate*prevBal
            month += 1
        if prevBal <= 0:
            break
        fixedPayment += 10
    return fixedPayment

print("Lowest payment:", debt_repay(3926, 0.2))