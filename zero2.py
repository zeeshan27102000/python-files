from watson_developer_cloud import TextToSpeechV1
import os
a=three.txt
text_to_speech = TextToSpeechV1(iam_apikey='sT5EVClqWy1I0XcxojSBsH4JYum6ngNrYszCGmopd42s',url='https://gateway-syd.watsonplatform.net/text-to-speech/api')
with open('hello_world.wav', 'wb') as audio_file:
    audio_file.write(text_to_speech.synthesize('a','audio/wav','en-US_AllisonVoice').get_result().content)
os.system("aplay hello_world.wav")
