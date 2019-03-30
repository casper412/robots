from random import randint
import time
from robot import controller

factory = controller.RobotFactory()
rb = factory.make_robot()

def get_range(rb):
	sum = 0
	for x in range(3):
		sum = sum + rb.get_distance()
	return sum / 3

spintime = randint(10, 20)

rb.set_motors(0.5, 0, 0.5, 1) # continue spinning left

print("Go")
time.sleep(spintime)
print("Searching 4 Person")
rb.set_led1(1)
rb.set_led2(1)
dist = get_range(rb)
while(dist > 60):
	print("range: " + str(dist))
	dist = get_range(rb)
	time.sleep(0.1)

rb.set_motors(0, 0, 0, 0)
rb.set_led1(0)
rb.set_led2(0)
print("Stop") 
print("range: " + str(dist))

