BOARD = 1
OUT = 1
IN = 1

def setmode(a):
   print(a)
def setup(a, b):
   print("setup: " + str(a) + " " + str(b))
def output(a, b):
   print("output: " + str(a) + " " + str(b))
def cleanup():
   print("cleanup")
def setmode(a):
   print("setmode: " + str(a))
def setwarnings(flag):
   print('setwarnings: False')
