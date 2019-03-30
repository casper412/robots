import time
from robot import controller

factory = controller.RobotFactory()
rb = factory.make_robot()


for i in range(1, 20):
    time.sleep(1)
    print("Turning on %d" % i)
    rb.set_led1(True)
    rb.set_led2(True)
    time.sleep(1)
    print("Turning off %d" % i)
    rb.set_led1(False)
    rb.set_led2(False)


