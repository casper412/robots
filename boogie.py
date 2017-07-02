from rrb3 import *
from random import randint
from time import sleep

rr = RRB3(9,6)

print("Boogie Time")
rr.set_led1(1)
rr.set_led2(1)

for x in xrange(10):
	left = randint(0,1)
	right = randint(0,1)
	forward = randint(0,1)
	backward = randint(0,1)

	if(left):
		print("Left")
		rr.set_motors(0.5, 1, 0.5, 0)
		sleep(1)
	
	if(right): 
		print("Right")
		rr.set_motors(0.5, 0, 0.5, 1)
		sleep(1)
		
	if(forward):
		print("Forward")
		rr.set_motors(0.5, 0, 0.5, 0)
		sleep(1)
	
	if(forward):
		print("Forward")
		rr.set_motors(0.5, 0, 0.5, 0)
		sleep(1)
	
	if(backward):
		print("Backward")
		rr.set_motors(0.5, 1, 0.5, 1)
		sleep(1)
		
	
	
rr.set_led1(0)
rr.set_led2(0)
print("End of Boogie Time")

