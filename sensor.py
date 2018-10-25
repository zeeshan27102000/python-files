import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
pirpin=6
GPIO.setup(pirpin, GPIO.IN)
counter=1
time.sleep(4)
while counter<=4:
    a=6
    if GPIO.input(pirpin):
        print("Motion Detected")
        
        
        os.system("fswebcam -F4 --fps 20 -r 800*600 /home/pi/supriya/"+str(a)+".jpg")
        

        print("pic taken")
            
        time.sleep(1)
        counter = counter + 1
        a=a+1
print("Testing")
exit()
