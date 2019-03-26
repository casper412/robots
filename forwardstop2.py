
import time
from robot import controller

factory = controller.RobotFactory()
rb = factory.make_robot()

def get_range(rb):
    sum = 0
    for x in range(3):
        sum = sum + rb.get_distance()
    return sum / 3

print("Go")

dist = get_range(rb)
rb.set_motors(1, 0, 1, 0) # both motors to full speed
while(dist > 30):
	print("range: " + str(dist))
	dist = get_range(rb)
	time.sleep(0.5)

rb.set_motors(0, 0, 0, 0)
print("Stop") 
print("range: " + str(range))
