from robot import controller
from robot import PiMotor
import time
import subprocess

ab = PiMotor.Arrow(3)

def pic(name):
  subprocess.check_output(['fswebcam', '-r', '1280x960', name])

factory = controller.RobotFactory()
with factory.make_robot() as rb:
    ab.on()
    rb.set_tilt(180)
    time.sleep(1000)   
    

def other():
    for x in range(180):
        for y in range(180):
            print("Pan:" + str(x) + " Tilt: " + str(y))
            rb.set_pan(y)
            rb.set_tilt(y)
            time.sleep(0.1)
        #pic('image'+str(x)+'.jpg')


