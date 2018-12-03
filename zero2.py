from watson_developer_cloud import TextToSpeechV1
import json
text_to_speech = TextToSpeechV1(iam_apikey='sT5EVClqWy1I0XcxojSBsH4JYum6ngNrYszCGmopd42s',url='https://gateway-syd.watsonplatform.net/text-to-speech/api')
pronunciation = text_to_speech.get_pronunciation('cmr university is big campus','en-US_AllisonVoice','ibm').get_result()
print(json.dumps(pronunciation, indent=2))
