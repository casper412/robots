from rrb3 import *
from time import sleep

rr = RRB3(9,6)

print("Go")

try:
	rr.set_motors(1, 0, 1, 0) # both motors to full speed

	while(rr.get_distance() > 30):
		print("range: " + str(rr.get_distance()))
		sleep(0.5) # sleep for 50 milliseconds
	
	rr.set_motors(0, 0, 0, 0)
	print("Stop") 
	print("range: " + str(rr.get_distance()))
finally:
	rr.cleanup()