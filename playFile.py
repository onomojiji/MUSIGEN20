#coding : utf-8

import os, sys, time

''' import vlc

file = vlc.MediaPlayer("Files/ciermx.wav")

file.play() '''

compo1 = 'totem\
        Files/Kicks/Attack\ Kick\ 07.wv\
        Files/Claps/Attack\ Clap\ 01.wv\
        Files/Kicks/Attack\ Kick\ 07.wv\
        Files/Claps/Attack\ Clap\ 01.wv\
        Files/Claps/Attack\ Clap\ 01.wv\
        Files/Claps/Attack\ Clap\ 01.wv'

compo2 = 'totem\
        Files/Shakers/Attack\ Shaker\ 01.wv'

AppActif = True

def continuer ():
        
        oui = True

        while oui :

                reponse2 = input("\n\
                Continuer à explorer d'autres styles ?\n\
                Oui(o) / Non(n) : ")


                try :
                        reponse2 = str(reponse2)

                        if reponse2 == 'o' or reponse2 == 'O':
                                break

                        elif reponse2 == 'n' or reponse2 == 'N':

                                print("\n\
                                        ------------------------------\n\
                                        À Bientôt, Portez vous Bien...\n\
                                        ------------------------------\n")

                                oui = False

                        else:
                                print("\n\
                                Veuillez Enter 'o' pour Oui et 'n' pour Non...\n")


                except :
                        print("\n\
                                Veuillez Enter 'o' pour Oui et 'n' pour Non...\n")
                                
                        
        return oui


while AppActif :

        reponse = input("\n\
                -------------------------------\n\
                CHOISISSEZ VOTRE RYTHME MUSICAL\n\
                -------------------------------\n\
                1 ) RAP\n\
                2 ) BIKUTSI\n\n\
                Votre choix : ")

        try :
                reponse = int(reponse)

                if reponse == 1 :

                        print("\n\
                                Très Jolie Choix..!!\n\
                                Bonne dégustation\n\
                                Veuillez patienter 5 secondes svp...\n")

                        time.sleep(5)

                        os.system(compo1)

                        AppActif = continuer()

                elif reponse == 2:

                        print("\n\
                                Cette partie est encore en devellopement...\n\
                                Merci pour votre comprehension....\n")

                        AppActif = continuer()

                else :
                        print("\n\
                        Choix Indisponible...\n\
                        Entrez '1' Pour RAP et '2' pour BIKUTSI...\n")
                        
                        AppActif = continuer()

        except :
                print("\n\
                        Choix Indisponible...\n\
                        Entrez '1' Pour RAP et '2' pour BIKUTSI...\n")

                AppActif = continuer()
                        


