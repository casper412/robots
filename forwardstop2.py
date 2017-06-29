from rrb3 import *
from time import sleep

rr = RRB3(9,6)

print("Go")
rr.set_motors(1, 0, 1, 0) # both motors to full speed
range = rr.get_distance()
while(range == None or range > 30):
	print("range: " + str(range))
	sleep(0.05) # sleep for 50 milliseconds
	range = rr.get_distance()
	
 rr.set_motors(0, 0, 0, 0) 
print("Stop") 
print("range: " + str(rr.get_distance()))