import time
from robot import controller

factory = controller.RobotFactory()
rb = factory.make_robot()
rb.set_led1(True)

rb.forward(5, 1)
rb.left(5, 1)
rb.right(5, 1)
rb.reverse(5, 1)

time.sleep(5)