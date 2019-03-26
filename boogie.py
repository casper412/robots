import time
from random import randint
from robot import controller

factory = controller.RobotFactory()
rb = factory.make_robot()

print("Boogie Time")
rb.set_led1(1)
rb.set_led2(1)

for x in range(10):
	left = randint(0,1)
	right = randint(0,1)
	forward = randint(0,1)
	backward = randint(0,1)

	if(left):
		print("Left")
		rb.set_motors(0.5, 1, 0.5, 0)
		time.sleep(1)
	
	if(right): 
		print("Right")
		rb.set_motors(0.5, 0, 0.5, 1)
		time.sleep(1)
		
	if(forward):
		print("Forward")
		rb.set_motors(0.5, 0, 0.5, 0)
		time.sleep(1)
	
	if(backward):
		print("Backward")
		rb.set_motors(0.5, 1, 0.5, 1)
		time.sleep(1)
		
	
	
rb.set_led1(0)
rb.set_led2(0)
print("End of Boogie Time")

