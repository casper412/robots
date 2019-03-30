#!/usr/bin/python
import sys
import time
from evdev import InputDevice, list_devices, ecodes
import sched, time, thread
from datetime import datetime
from rrb3 import *

print("Press Ctrl-C to quit")

rr = RRB3(12,6)
max=130
devices = [InputDevice(fn) for fn in list_devices()]
dev = devices[0]


last_y = 0
last_x = 0

global_event = None
s = sched.scheduler(time.time, time.sleep)
DELAY = 0.5
format = "%a, %d %b %Y %H:%M:%S:%f +0000"



def handle_y(value):
  global last_y 
  value = -1*value + 127
  print("y: " + str(value))
  last_y = value
  setMotors()
  
def handle_x(value):
  global last_x
  value = -1*value + 127
  print("x: " + str(value))
  last_x = value
  setMotors()

def stop():
    global global_event
    global last_y
    global last_x 
    print("\tSTOP!!!")
    global_event = None
    rr.set_motors(0,0,0,0)
    last_y = 0
    last_x = 0

def setMotors():
    global global_event
    global last_x
    global last_y
    global s 
    abs_last_y = abs(last_y)
    y_dir = 0
    if last_y <= 0:
        y_dir = 1
    abs_last_x = abs(last_x)
    x_dir = 0
    if last_x <= 0:
        x_dir = 1
    print ("%d %d %d %d"% (abs_last_y, y_dir, abs_last_x, x_dir)) 
    if global_event:
        s.cancel(global_event)
        global_event = s.enter(DELAY, 1, stop, ())
    else:
        global_event = s.enter(DELAY, 1, stop, ())
        thread.start_new_thread(monitor, (("Thread-1",)))
    rr.set_motors((max - abs_last_y)/max, y_dir,  (max-last_x)/max, x_dir)

def monitor(threadName):
    global s
    print( "%s: %s" % (threadName, datetime.now().strftime(format)))
    s.run()
    print( "%s: %s" % (threadName, datetime.now().strftime(format)))




print("input:")
try:
    for key_event in dev.read_loop():
        print(key_event) 
        if key_event.type == ecodes.EV_ABS:
            if key_event.code == ecodes.ABS_RZ:  # y 
                handle_y(key_event.value)
            if key_event.code == ecodes.ABS_Z:  # x 
                handle_x(key_event.value)
except KeyboardInterrupt:
    sys.exit()
