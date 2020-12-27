#coding : utf-8

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Dites quelque chose : ')
    audio = r.listen(source)

    try :
        text = r.recognize_google(audio)
        print('Vous avez dit : {}'.format(text))

    except :
        print("Désolé, Nous n'avons pa pu identifier votre voix...")