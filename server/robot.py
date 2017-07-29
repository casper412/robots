import sched, time, thread
from datetime import datetime
from rrb3 import *

class Robot:
    def __init__(self):
        self.state = None
        self.s = sched.scheduler(time.time, time.sleep)
        self.event = None
        self.DELAY = 0.5
        self.format = "%a, %d %b %Y %H:%M:%S:%f +0000"
        self.rr = RRB3(9,6)

    def move(self, dx, dy):
        dy = -1 * dy # flip y coords
        width = 300
        height = 300
        dxRatio = min(1, max(-1, dx / width))
        dyRatio = min(1, max(-1, dy / height))

        print "dx ratio: %f / dy ratio: %f" % (dxRatio, dyRatio)
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

        self.setMotors(left_motor, left_dir, right_motor, right_dir)
        return rr.get_distance()

    def forward(self, dx, dy):
        print ("\t%s: %s" % (datetime.now().strftime(self.format), "forward"))
        self.setMotors(1.0,0,1.0,0)

    def back(self, dx, dy):
        print ("\t%s: %s" % (datetime.now().strftime(self.format), "back"))
        self.setMotors(1.0,1,1.0,1)

    def left(self, dx, dy):
        print ("\t%s: %s" % (datetime.now().strftime(self.format), "left"))
        self.setMotors(1.0,1,1.0,0)

    def right(self, dx, dy):
        print ("\t%s: %s" % (datetime.now().strftime(self.format), "right"))
        self.setMotors(1.0,0,1.0,1)

    def stop(self):
        print "\tSTOP!!!"
        self.event = None
        self.rr.set_motors(0,0,0,0)

    def setMotors(self, left_motor_speed, left_motor_dir,  right_motor_speed, right_motor_dir):
        print (left_motor_speed, left_motor_dir,  right_motor_speed, right_motor_dir)
        if (self.event != None):
            self.s.cancel(self.event)
            self.event = self.s.enter(self.DELAY, 1, self.stop, ())
        else:
            self.event = self.s.enter(self.DELAY, 1, self.stop, ())
            thread.start_new_thread(self.monitor, (("Thread-1",)))
        self.rr.set_motors(left_motor_speed, left_motor_dir,  right_motor_speed, right_motor_dir)

    def monitor(self, threadName):
        print "%s: %s" % (threadName, datetime.now().strftime(self.format))
        self.s.run()
        print "%s: %s" % (threadName, datetime.now().strftime(self.format))


