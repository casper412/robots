import sched, time, _thread
from datetime import datetime
import platform
if platform.system() != 'Darwin':
    import RPi.GPIO as GPIO ## Import GPIO library
    from robot import PiMotor

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
    
    def __enter__(self):
        return self
    
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
        if (self.event):
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
    
    def cleanup(self):
        pass
        
    def __exit__(self, type, value, traceback):
        self.cleanup()

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
    
    def cleanup(self):
        print("Cleaning up")

class PhysicalRobot(Robot):
    def __init__(self):
        Robot.__init__(self)
        GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
        
        self.PAN_SERVO_PIN = 35
        self.TILT_SERVO_PIN = 36
        self.LED1_PIN = 38 
        self.LED2_PIN = 37
        self.GPIO_TRIGGER = 29
        self.GPIO_ECHO = 31
        GPIO.setup(self.LED1_PIN, GPIO.OUT) ## Setup GPIO Pin to OUT
        GPIO.setup(self.LED2_PIN, GPIO.OUT) ## Setup GPIO Pin to OUT
        GPIO.setup(self.PAN_SERVO_PIN, GPIO.OUT)
        GPIO.setup(self.TILT_SERVO_PIN, GPIO.OUT)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

        self.panServo = GPIO.PWM(self.PAN_SERVO_PIN, 100) # GPIO 17 for PWM with 50Hz
        self.tiltServo = GPIO.PWM(self.TILT_SERVO_PIN, 100) # GPIO 17 for PWM with 50Hz
        self.panServo.start(2.5) # Initialization
        self.tiltServo.start(2.5) # Initialization

        self.set_tilt(90)
        self.set_pan(90)

        self.left_motor = PiMotor.Motor("MOTOR2",1)
        self.right_motor = PiMotor.Motor("MOTOR3",1)

    def set_led1(self, on):
        GPIO.output(self.LED1_PIN, 1 if on else 0) ## Turn on GPIO pin
    
    def set_led2(self, on):
        print("Turning LED2 to " + str(on))
        GPIO.output(self.LED2_PIN, 1 if on else 0) ## Turn on GPIO pin
    
    def get_distance(self):
       # set Trigger to HIGH
       GPIO.output(self.GPIO_TRIGGER, True)
 
       # set Trigger after 0.01ms to LOW
       time.sleep(0.00001)
       GPIO.output(self.GPIO_TRIGGER, False)
 
       StartTime = time.time()
       StopTime = time.time()
 
       # save StartTime
       while GPIO.input(self.GPIO_ECHO) == 0:
           StartTime = time.time()
 
       # save time of arrival
       while GPIO.input(self.GPIO_ECHO) == 1:
          StopTime = time.time()
 
       # time difference between start and arrival
       TimeElapsed = StopTime - StartTime
       # multiply with the sonic speed (34300 cm/s)
       # and divide by 2, because there and back
       distance = (TimeElapsed * 34300) / 2
 
       return distance

    def set_motors(self, left, left_dir, right, right_dir):
        left = left * 100
        right = right * 100
        if (left_dir == FORWARD):
            self.left_motor.forward(left)
        else:
            self.left_motor.reverse(left)
        if (right_dir == FORWARD):
            self.right_motor.forward(right)
        else:
            self.right_motor.reverse(right)

    def set_pan(self, angle):
        duty = self._compute_duty(angle)
        self.panServo.ChangeDutyCycle(duty)

    def set_tilt(self, angle):
        #Limit Tilt
        angle = min(114, max(45, angle))
        duty = self._compute_duty(angle)
        self.tiltServo.ChangeDutyCycle(duty)

    def _compute_duty(self, angle):
        return float(angle) * 25 / 180.0 + 3.0

    def cleanup(self):
        GPIO.cleanup()

