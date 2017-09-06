## Ian, this was written in python 2.7. Hope this helps... 

#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import os, sys
import serial
import smtplib
import time

logging.basicConfig(filename='switchlog.txt', level=logging.INFO)

def turnPlugON():
    ON = 'sudo ~/raspberry-strogonanoff/src/strogonanoff_sender.py --channel 1 --button 1 --gpio 0 on'
    os.system(ON)
    
def turnPlugOFF():
    OFF = 'sudo ~/raspberry-strogonanoff/src/strogonanoff_sender.py --channel 1 --button 1 --gpio 0 off'
    os.system(OFF)

def startingProcedure():
    """
    This function turns the plug off, waits 3 seconds, turns the plug on. It's a chance for you to see that
    everything works. The pause is required as the plug doesn't respond to signals in quick succession. 
    """
    
    ## Console commands for switching the maplin's wifi plug, please check that the channel is correct,
    ## otherwise change the below line for the channel and button required.
    ## PLEASE REFER TO THIS TUTORIAL IF YOU HAVE ANY QUESTIONS
    ## https://riviera.org.uk/2015/01/15/using-a-raspberry-pi-to-control-maplin-power-sockets/
    
    logging.info("Testing")
    time.sleep(3)
    logging.info("Switching off...")
    turnPlugOFF()
    logging.info("Sleeping for 3 seconds")
    time.sleep(3)
    logging.info("Switching on...") 
    turnPlugON()
    time.sleep(2)  
  
  
def sendLogToEngineering():
    """
    This function sends an email with a log to engineering inbox.
    Name: Raspberry Pi
    Surname: Wright Flow
    Birthday: September 5, 1917 (because google doesn't allow me to choose 2017, which is today)
    Gender: Rather not say
    Mobile: +441323509211
    """
    TO = 'VJPWFTENGINEERING@idexcorp.com'
    GMAIL_USER = 'wrightflow.raspberrypi@gmail.com'
    GMAIL_PASS = 'iamwrightflowraspberrypi'
 
    SUBJECT = 'SENSOR TRIGGERED'
    line1 = 'This is an automated email. This message means either of two things:\n'
    line2 = 'Liquid has been detected and motor has been shut down. Please visit the site immediately to confirm.\n'
    line3 = 'or\n' 
    line4 = 'An error in the script has occured.\n'
    line5 = 'Either way, please get to the premises ASAP. \n CHECK LOGS FOR DETAILS.'+3*"/n"
    log = ''
    
    file = open("switchlog.txt", "r") 
    for line in file: 
        log += line 
    
    TEXT = line1+line2+line3+line4+line5 + 3*"\n" + log 
    
    logging.info("Sending email to Engineering")
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject:' + SUBJECT + '\n'
    print header
    msg = header + '\n' + TEXT + ' \n\n'
    smtpserver.sendmail(GMAIL_USER, TO, msg)
    smtpserver.close()
    
try:
    startingProcedure()
except Exception:
    logging.info("There is problem with startingProcedure function. Check it!")
    sendLogToEngineering()   
try:
    ##  Connecting arduino board. Ammend port name below if required.
    ser = serial.Serial('/dev/ttyACM0', 9600)
except Exception:
##  If this error happens, go to Arduino IDE and in "Tools" tab check, whether the connection name
##  and port name match.
    logging.info("Problem with arduino connection. Check the port connection config!")
    sendLogToEngineering()
    
while True:
    message = ser.readline()
    print message
##  Check whether liquid is present
    if message[0] == "1":
        logging.info("Liquid detected, verifying...")
        time.sleep(5)
        message = ser.readline()
        print message
##      Check again in case someone just holds it in their hand
        if message[0] == "1":
            logging.info("Liquid presence confirmed. Shutting down the plug.")
            turnPlugOFF()
            sendLogToEngineering()
            quit() 
    time.sleep(0.5)