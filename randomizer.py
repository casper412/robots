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

print("Go")

rr.left(spintime,0.5)
	
print("Searching 4 Person")

try:
	range = getRange(rr)
	rr.set_motors(0.5, 1, 0.5, 0) # continue spinning left
	while(range > 60):
		print("range: " + str(range))
		range = getRange(rr)
		sleep(0.5)

	rr.set_motors(0, 0, 0, 0)
	print("Stop") 
	print("range: " + str(range))
finally:
	rr.cleanup()
	