from rrb3 import *

rr = RRB3(9,6)

print("Go")

try:
	
	range = rr.get_distance()
	rr.set_motors(1, 0, 1, 0) # both motors to full speed
	while(range > 30):
		print("range: " + str(range))
		range = rr.get_distance()
	
	rr.set_motors(0, 0, 0, 0)
	print("Stop") 
	print("range: " + str(range))
finally:
	rr.cleanup()