from rrb3 import *
from time import sleep
rr = RRB3(9,6)

print("Go")

try:
	
	range = getRange(rr)
	rr.set_motors(1, 0, 1, 0) # both motors to full speed
	while(range > 30):
		print("range: " + str(range))
		range = getRange(rr)
		sleep(0.5)
	
	rr.set_motors(0, 0, 0, 0)
	print("Stop") 
	print("range: " + str(range))
finally:
	rr.cleanup()
	
def getRange(rr):
    sum = 0
	for x in xrange(3):
		sum = sum + rr.get_distance()
	return sum / 3