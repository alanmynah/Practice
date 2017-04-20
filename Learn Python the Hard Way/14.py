#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 21:30:12 2017

@author: michael
"""

from sys import argv 

script, user_name = argv 
prompt = '> '

print ('Hi %s, I\'m the %s script.' % user_name, script)
print ('I\'d like to ask you a few questions.')
print ('Do you like me %s?' % user_name)
likes = input(prompt)

print ("Where do you live %s?" % user_name)
lives = input(prompt)

print ("So you said %r about liking me and you live in %r" % likes, lives)
