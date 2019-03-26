import time
import sys, os

parent = os.path.abspath(os.path.dirname(__file__) + "/../")
print("Adding Import: " + parent)
sys.path.append(parent)
from robot import controller

class RobotHttp:
    def __init__(self):
        factory = controller.RobotFactory()
        self.rb = factory.make_robot()
        self.DELAY = 0.5

    def move(self, dx, dy):
        dy = -1 * dy # flip y coords
        width = 300
        height = 300
        dxRatio = min(1, max(-1, dx / width))
        dyRatio = min(1, max(-1, dy / height))

        print("dx ratio: %f / dy ratio: %f" % (dxRatio, dyRatio))
        left_motor = 0
        right_motor = 0
        count = 0
        if (dx == 0):
            pass
        else:
            left_motor = dxRatio
            right_motor = -1 * dxRatio
            count = abs(dxRatio)

        if (dy == 0):
            pass
        else:
            left_motor += dyRatio
            right_motor += dyRatio
            count = count + abs(dyRatio)

        if (count > 1):
            left_motor = left_motor / count
            right_motor = right_motor / count

        if (left_motor >= 0):
            left_dir = 0
        else:
            left_dir = 1
        if (right_motor >= 0):
            right_dir = 0
        else:
            right_dir = 1
        left_motor = abs(left_motor)
        right_motor = abs(right_motor)

        self.rb.set_motors(left_motor, left_dir, right_motor, right_dir)
        self.rb.stop_in(self.DELAY)
        return self.rb.get_distance()

    def forward(self, dx, dy):
        print("\t%s: %s" % (datetime.now().strftime(self.format), "forward"))
        self.forward(self.DELAY, 1.0)

    def back(self, dx, dy):
        print("\t%s: %s" % (datetime.now().strftime(self.format), "back"))
        self.reverse(self.DELAY, 1.0)

    def left(self, dx, dy):
        print ("\t%s: %s" % (datetime.now().strftime(self.format), "left"))
        self.left(self.DELAY, 1.0)

    def right(self, dx, dy):
        print("\t%s: %s" % (datetime.now().strftime(self.format), "right"))
        self.right(self.DELAY, 1.0)

