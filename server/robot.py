import sched, time, thread
from datetime import datetime

class Robot:
    def __init__(self):
        self.state = None
        self.s = sched.scheduler(time.time, time.sleep)
        self.event = None
        self.DELAY = 0.5
        self.format = "%a, %d %b %Y %H:%M:%S:%f +0000"
        thread.start_new_thread(self.monitor, (("Thread-1",)))

    def forward(self):
        print ("\t%s: %s" % (datetime.now().strftime(self.format), "forward"))
        self.setMotors(0,0,0,0)

    def back(self):
        print ("\t%s: %s" % (datetime.now().strftime(self.format), "back"))
        self.setMotors(0,0,0,0)

    def left(self):
        print ("\t%s: %s" % (datetime.now().strftime(self.format), "left"))
        self.setMotors(0,0,0,0)

    def right(self):
        print ("\t%s: %s" % (datetime.now().strftime(self.format), "right"))
        self.setMotors(0,0,0,0)

    def stop(self):
        print "\tSTOP!!!"
        self.event = None

    def setMotors(self, left_motor_speed, left_motor_dir,  right_motor_speed, right_motor_dir):
        if (self.event != None):
            self.s.cancel(self.event)
            self.event = self.s.enter(self.DELAY, 1, self.stop, ())
        else:
            self.event = self.s.enter(self.DELAY, 1, self.stop, ())
            thread.start_new_thread(self.monitor, (("Thread-1",)))
        # Set robot motors here

    def monitor(self, threadName):
        print "%s: %s" % (threadName, datetime.now().strftime(self.format))
        self.s.run()
        print "%s: %s" % (threadName, datetime.now().strftime(self.format))


