import RPi.GPIO as GPIO ## Import GPIO library
import time

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(11, GPIO.OUT) ## Setup GPIO Pin 11 to OUT


for i in xrange(1, 20):
    time.sleep(1)
    print "Turning on %d" % i
    GPIO.output(11,True) ## Turn on GPIO pin 11
    time.sleep(1)
    print "Turning off %d" % i
    GPIO.output(11,False) ## Turn off GPIO pin 11


