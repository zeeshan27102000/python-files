import subprocess
from watson_developer_cloud import TextToSpeechV1
import time
import os
import RPi.GPIO as GPIO
input_pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(input_pin, GPIO.IN)

text_to_speech = TextToSpeechV1(iam_apikey='sT5EVClqWy1I0XcxojSBsH4JYum6ngNrYszCGmopd42s',url='https://gateway-syd.watsonplatform.net/text-to-speech/api')

while True:
        if (GPIO.input(input_pin)):
                print('Button Pressed')
                with open('hello_world1.wav', 'wb') as audio_file:
                        audio_file.write(text_to_speech.synthesize('button pressed','audio/wav','en-US_AllisonVoice').get_result().content)
                        os.system("aplay hello_world1.wav")
                
                print("Get ready with your webcam")
                with open('hello_world2.wav', 'wb') as audio_file:
                        audio_file.write(text_to_speech.synthesize('Get ready with your webcam','audio/wav','en-US_AllisonVoice').get_result().content)
                        os.system("aplay hello_world2.wav")
                
                print('Taking snap in next 5 seconds')
                with open('hello_world3.wav', 'wb') as audio_file:
                        audio_file.write(text_to_speech.synthesize('Taking snap in next 5 seconds','audio/wav','en-US_AllisonVoice').get_result().content)
                        os.system("aplay hello_world3.wav")
                        
                time.sleep(5)
                
                print("Taking snap")
                with open('hello_world4.wav', 'wb') as audio_file:
                        audio_file.write(text_to_speech.synthesize('Taking snap','audio/wav','en-US_AllisonVoice').get_result().content)
                        os.system("aplay hello_world4.wav")
                        
                subprocess.call(['fswebcam', '-F 3','-r', '720x340', 'ZERO.jpg'])
                
                print("Thresholding image")
                
                        
                subprocess.call(['convert', './ZERO.jpg', '-threshold', '+20%', '1.jpg'])
                
                print("Performing OCR")
                
                subprocess.call(['tesseract', 'ZERO.jpg', 'speech'])
                
                print("The detected text is")
                with open('hello_world6.wav', 'wb') as audio_file:
                        audio_file.write(text_to_speech.synthesize('the detected text is','audio/wav','en-US_AllisonVoice').get_result().content)
                        os.system("aplay hello_world6.wav")
                        
                subprocess.call(['cat', 'speech.txt'])
                a=open('speech.txt','r')
                b=a.read()
                
                print("Speaking text")
                with open('hello_world.wav', 'wb') as audio_file:
                        audio_file.write(text_to_speech.synthesize(b,'audio/wav','en-US_AllisonVoice').get_result().content)
                os.system("aplay hello_world.wav")
GPIO.cleanup()
