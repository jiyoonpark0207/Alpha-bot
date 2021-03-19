import RPi.GPIO as GPIO
import time
from AlphaBot2 import AlphaBot2

from random import seed, randint
#from Ultrasonic_Ranging import dist

Ab = AlphaBot2()

TRIG = 22
ECHO = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ECHO,GPIO.IN)

def dist():
	GPIO.output(TRIG,GPIO.HIGH)
	time.sleep(0.000015)
	GPIO.output(TRIG,GPIO.LOW)
	while not GPIO.input(ECHO):
		pass
	t1 = time.time()
	while GPIO.input(ECHO):
		pass
	t2 = time.time()
	return (t2-t1)*34000/2

def alphabot_nav(x, y):
    d = dist()
    print("distance: %s"%d)
    if d >30:
        #Ab.forward()
        #time.sleep(2)
        #Ab.stop()
        if x>60:
            print("move right")
            Ab.right()
            time.sleep(1)
            Ab.stop()
        elif x<40:
            print("move left")
            Ab.left()
            time.sleep(1)
            Ab.stop()
        else:
            print("move forward")
            Ab.forward()
            time.sleep(1)
            Ab.stop()
    else:
        print("stop")
        Ab.stop()

        
try:
    while True:
        #x = input('x: ')
        #y = input('y: ')
        x = randint(0, 100)
        #y = int(y)
        alphabot_nav(x, 0)
        time.sleep(0.02)

except KeyboardInterrupt:
    GPIO.cleanup();










