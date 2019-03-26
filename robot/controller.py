import sched, time, _thread
from datetime import datetime
import platform


FORWARD = 0
BACKWARD = 1

class RobotFactory:
    def __init__(self):
        pass

    def make_robot(self):
        if platform.system() == 'Darwin':
            return GUIRobot()
        else:
            return PhysicalRobot()

class Robot:
    def __init__(self):
        self.s = sched.scheduler(time.time, time.sleep)
        self.event = None
        self.DELAY = 0.5
        self.format = "%a, %d %b %Y %H:%M:%S:%f +0000"
    
    def forward(self, duration, rate):
        self.set_motors(rate, FORWARD, rate, FORWARD)
        self.stop_in(duration)
    
    def reverse(self, duration, rate):
        self.set_motors(rate, BACKWARD, rate, BACKWARD)
        self.stop_in(duration)

    def left(self, duration, rate):
        self.set_motors(rate, BACKWARD, rate, FORWARD)
        self.stop_in(duration)
    
    def right(self, duration, rate):
        self.set_motors(rate, FORWARD, rate, BACKWARD)
        self.stop_in(duration)

    def stop_in(self, duration):
        if (self.event != None):
            self.s.cancel(self.event)
            self.event = self.s.enter(duration, 1, self.stop, ())
        else:
            self.event = self.s.enter(duration, 1, self.stop, ())
            _thread.start_new_thread(self._monitor, (("StopThread",)))

    def stop(self):
        print("Delayed STOP!!!")
        self.event = None
        self.set_motors(0., FORWARD, 0., FORWARD)

    def _monitor(self, threadName):
        print("%s: %s" % (threadName, datetime.now().strftime(self.format)))
        self.s.run()
        print("%s: %s" % (threadName, datetime.now().strftime(self.format)))

    def set_motors(self, left, left_dir, right, right_dir):
        pass

    def set_led1(self, on):
        pass
    
    def set_led2(self, on):
        pass
    
    def get_distance(self):
        return 0

    def set_pan(self, angle):
        pass

    def set_tilt(self, angle):
        pass
    
class GUIRobot(Robot):
    def __init__(self):
        Robot.__init__(self)
    
    def set_motors(self, left, left_dir, right, right_dir):
        print("motors: " + str(left) + " " + str(left_dir) + " " + str(right) + " " + str(right_dir))

    def set_led1(self, on):
        print("led1: " + str(on))
    
    def set_led2(self, on):
        print("led2: " + str(on))
    
    def get_distance(self):
        return 330

    def set_pan(self, angle):
        pass

    def set_tilt(self, angle):
        pass
    
class PhysicalRobot(Robot):
    def __init__(self):
        import RPi.GPIO as GPIO ## Import GPIO library
        GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
        GPIO.setup(11, GPIO.OUT) ## Setup GPIO Pin 11 to OUT

    def set_led1(self, on):
        GPIO.output(11, on) ## Turn on GPIO pin 11
    
    def set_led2(self, on):
        GPIO.output(13, on) ## Turn on GPIO pin 11
    