from rrb3 import *

rr = RRB3(9,6)

print("Go")
while(rr.get_distance() == None or rr.get_distance() > 30):
    print("range: " + rr.get_distance())
	rr.forward(2,1)
	
print("Stop")