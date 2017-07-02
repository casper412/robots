from rrb3 import *
from random import randint
from time import sleep

def getRange(rr):
	sum = 0
	for x in xrange(3):
		sum = sum + rr.get_distance()
	return sum / 3

spintime = randint(10, 20)
rr = RRB3(9,6)

try:
	rr.set_motors(0.5, 0, 0.5, 1) # continue spinning left
	
	print("Go")
	sleep(spintime)
	print("Searching 4 Person")
	rr.set_led1(1)
	rr.set_led2(1)
	range = getRange(rr)
	while(range > 60):
		print("range: " + str(range))
		range = getRange(rr)
		sleep(0.1)

	rr.set_motors(0, 0, 0, 0)
	rr.set_led1(0)
	rr.set_led2(0)
	print("Stop") 
	print("range: " + str(range))
finally:
	rr.cleanup()
	