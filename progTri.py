
AppOn = True

def continuer ():
        
    oui = True

    while oui :

            reponse2 = input("\n\
            Voulez cous comparer d'autres Nombres ?\n\
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

while AppOn :

    nbElements = input("\n\
                    Combien de nombres souhaitez vous classer ? ")

    try:
        nbElements = int(nbElements)

        i=1
        
        tableau = []

        while i<= nbElements :
            nombre = input(f"Nombre {i} = ")

            try:
                nombre = int(nombre)
                element = tableau.insert(i,nombre)
                i+=1
                
            except :
                print("\n\
                        Veuillez entrer une valeur Numerique...")



        ordre = input("\nDans quel ordre voulez vous classer ces nombres ?\n\
                        Croissant(c) ou Décroissant(d) : ")

        if ordre == 'c' or ordre == 'C':

            # Pour classer par Ordre croissant...

            tableau.sort()

            print(f"\n\
                    TabOrdreCroissant = {tableau}\n")

        elif ordre == 'd' or ordre == 'D':
            # Pour classer par ordre décroissant...

            tableau.sort(reverse=True)

            print(f"\n\
                    TabOrdreDécroissant = {tableau}\n")

        
        AppOn = continuer()

    except :

        print("\n\
                ***************************************\n\
                Veuillez entrer une valeur Numerique...\n\
                ***************************************")
       
        AppOn = continuer()

