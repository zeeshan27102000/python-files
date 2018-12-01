import subprocess
import time
import os
import RPi.GPIO as GPIO
input_pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(input_pin, GPIO.IN)

while True:
    
        print('Button Pressed')
        print("Get ready with your webcam")
        print('Taking snap in next 3 seconds')
        time.sleep(3)  
        print("Taking snap")
        subprocess.call(['fswebcam', '-F 3','-r', '720x340', 'ZERO.jpg'])
        print("Thresholding image")
        subprocess.call(['convert', './ZERO.jpg', '-threshold', '+5%', '1.jpg'])
        print("Performing OCR")
        subprocess.call(['tesseract', 'ZERO.jpg', 'speech'])
        print("The detected text is")
        subprocess.call(['cat', 'speech.txt'])
        print("Speaking text")
        os.system("espeak -s 140 -g 0.8 -vf3 -a 150 -f speech.txt")
GPIO.cleanup()
