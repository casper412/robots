from rrb3 import *
from random import randint

spintime = randint(10, 20)
 
rr = RRB3(9,6)

print("Go")

rr.left(spintime,0.5)
	
print("Stop") 
print("range: " + str(rr.get_distance()))