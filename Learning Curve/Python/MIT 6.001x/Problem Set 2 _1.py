#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 12:51:26 2017

@author: michael

Write a program to calculate the credit card balance after one year if a person
 only pays the minimum monthly payment required by the credit card company each
 month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining 
balance. At the end of 12 months, print out the remaining balance. Be sure 
to print out no more than two decimal digits of accuracy

"""

def debt(bal, annIntR, minMonPaymR):
    
    #Calculate monthly interest rate
    monIntR = annIntR / 12
    #Calculate running totals for each month
    runTotal = []
    for i in range(13):
    #Calculate minimum payment monthly payment 
        minMonPaym = minMonPaymR * bal
    #Calculate unpaid balance on which the interest is calculated (no interest)
        monUnBal = bal - minMonPaym
        runTotal.append(bal)
    #Calculate new balance (includes interest)
        newBal = monUnBal + monIntR * monUnBal
        bal = round(newBal, 3)
        
        remBal = runTotal[len(runTotal)-1]
    return remBal

def debt_to_pay(bal, annIntR, minMonPaymR):
    
    #Calculate monthly interest rate
    monIntR = annIntR / 12
    #Calculate running totals for each month
    runTotal = []
    m = 0
    while bal > 1:
    #Calculate minimum payment monthly payment 
        minMonPaym = minMonPaymR * bal
    #Calculate unpaid balance on which the interest is calculated (no interest)
        monUnBal = bal - minMonPaym
        runTotal.append(bal)
    #Calculate new balance (includes interest)
        newBal = monUnBal + monIntR * monUnBal
        bal = round(newBal, 2)
        m += 1
    return m

print ("Remaining Balance after 1st year: %.2f" % debt(484, 0.2, 0.04))
#print ("It will take %i months to pay" % debt_to_pay(2000, 0.24, 0.10))