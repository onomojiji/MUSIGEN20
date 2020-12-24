#coding : utf-8

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speack Anything : ')
    audio = r.listen(source)

    try :
        text = r.recognize_google(audio)
        print('You said : {}'.format(text))

    except :
        print("Sorry could not recognize your voice")