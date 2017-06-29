from rrb3 import *

rr = RRB3(9,6)

print("Go")
while(rr.get_distance() == None or rr.get_distance() > 30):
	print("range: " + str(rr.get_distance()))
	rr.forward(0.5,1)
	
print("Stop") 
print("range: " + str(rr.get_distance()))