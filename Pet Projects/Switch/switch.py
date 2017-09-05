import time
import serial
import smtplib
import os

ON = 'sudo ~/raspberry-strogonanoff/src/strogonanoff_sender.py --channel 1 --button 1 --gpio 0 on'
OFF = 'sudo ~/raspberry-strogonanoff/src/strogonanoff_sender.py --channel 1 --button 1 --gpio 0 off'

print "Testing"
time.sleep(3)
os.system(OFF)
print "Sleeping for 3 seconds"
time.sleep(3)
print "Further testing"
time.sleep(3)
print "Tests went well. Turning on the plug!"
os.system(ON)
time.sleep (2)
ser = serial.Serial('/dev/ttyACM1', 9600)

while True:
    message = ser.readline()
    print message
    if message[0] == "T":
        os.system(OFF)
        print "THERE IS TEA!!! TURNING OFF!!!"
        quit()
    time.sleep(0.5)