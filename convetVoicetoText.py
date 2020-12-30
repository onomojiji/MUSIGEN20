#coding : utf-8

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('\n\nDites quelque chose : ')
    audio = r.listen(source)

    try :
        text = r.recognize_google(audio)
        print('Vous avez dit : {}'.format(text))

    except :
        print("Desole, Nous n'avons pas pu identifier votre voix...")