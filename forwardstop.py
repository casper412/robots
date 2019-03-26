import time
from robot import controller

factory = controller.RobotFactory()
rb = factory.make_robot()

print("Go")
while(rb.get_distance() == None or rb.get_distance() > 30):
	print("range: " + str(rb.get_distance()))
	rb.forward(0.5,1)
	
print("Stop") 
print("range: " + str(rb.get_distance()))
