import RPi.GPIO as GPIO
import time
import os
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 18
GPIO_ECHO = 17
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
def distance():
        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.1)
        GPIO.output(GPIO_TRIGGER, False)
        StartTime=time.time()
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()

        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()
        TimeElapsed = StopTime-StartTime
        distance = round((TimeElapsed * 34300) / 2,2)
        
        return distance
while True:
    a=distance()
    print(a,"cm")
    time.sleep(5)
    
    if(a<50):
        print("object is nearby")
        os.system('fswebcam -F 4 --fps 20 -r 800*600 /home/pi/supriya/'+str(a)+'.jpg')
        
       




