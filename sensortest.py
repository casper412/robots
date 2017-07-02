from rrb3 import *
from time import sleep
rr = RRB3(9,6)

print("Go")

try:
	for x in xrange(1,100): 
		print(str(rr.get_distance()))
		sleep(0.2)
finally:
	rr.cleanup()