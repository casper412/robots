import time
from robot import controller

factory = controller.RobotFactory()
rb = factory.make_robot()


print("Go")

for x in range(1,100): 
	print(str(rb.get_distance()))
	time.sleep(0.2)