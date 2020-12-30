
''' 
    Titre : programme complet de tri Basique des elemments d'un tableau ;
            programme de la fonction python sort()

    Evolution du code :

        |-------------------|------------------------------------|
        |   Version         |     Date et Heure de modification  |
        |-------------------|------------------------------------|
        | v1.0.0            |      30-12-2020, 00 h 32 min       |
        | v1.0.1            |      30-12-2020, 00 h 46 min       |
        | v1.0.2            |      30-12-2020, 02 h 47 min       |

 '''




''' tableau = [90,9,45,4,3,6,13,123,1] '''

''' tableau = [3,9,90,2,234,4] '''

''' tableau = [7,123,78,1,4,0,454,9] '''

tableau = [7, 17, 9,0,454,4,78,1,123,-3,-13,79,28,34,654,23,0.34,25]

nbElements = len(tableau)

N = 0
N2 = 0

def OrdreCroissant(tab:list):
    
    global N

    # l'objectif ici étant de classer par ordre croissant les éléments du tableau :
 
    def remplaceCroissant():

        global N

        for k in range(0, i) : #pour chaque nombre allant de la position 0 à la position i :
            
            if tableau[k] > tableau[i] :  #Si le nombre correspondant à la position k > au nombre à la position i
                Vk = tableau[i] ; N += 1
                tableau[i] = tableau[k] ; N += 1   # On permutte leurs positions
                tableau[k] = Vk ; N += 1        #

            elif tableau[k] > tableau[k+1]: #En même temps si le nombre correspondant à la position k  au nombre à la position k+1
                Vk = tableau[k+1] ; N += 1           #
                tableau[k+1] = tableau[k] ; N += 1   # On pemutte leurs positions
                tableau[k] = Vk  ; N += 1            #
                
            else :
                continue

    for i in range(0, nbElements) : 

        if tableau[0] > tableau[i] : # Je compare le nombre à la position i au nombre à la position 0 d'abord pour me rassurer que mon derrière est déjè bon.
            Vo = tableau[0] ; N += 1
            tableau[0] = tableau[i] ; N += 1  # La même chanson
            tableau[i] = Vo ; N += 1
            remplaceCroissant()
                
        else:
            remplaceCroissant()

    print(f"\n TabOrdCroissant = {tab}\n\
                Nombre d'instructions = {N}")


def OrdreDecroissant(tab:list):

    global N2

    # l'objectif ici étant de classer par ordre décroissant les éléments du tableau :

    def remplaceDecroissant():

        global N2

        for k in range(0, i) :
            
            if tableau[i] > tableau[k] :#Si le nombre correspondant à la position k > au nombre à la position i
                Vk = tableau[i]   ; N2 += 1        #
                tableau[i] = tableau[k]  ; N2 += 1 #On permutte leurs valeurs
                tableau[k] = Vk     ; N2 += 1      #

            elif tableau[k+1] > tableau[k] :   # En même temps si le nombre correspondant à la position k  au nombre à la position k+1
                Vk = tableau[k+1]  ; N2 += 1
                tableau[k+1] = tableau[k]  ; N2 += 1   # On pemutte leurs positions
                tableau[k] = Vk  ; N2 += 1
                
            else :
                continue

    for i in range(nbElements-1, 0,-1) :
    
        if tableau[i] > tableau[0] : # La même chanson...
            Vo = tableau[0]  ; N2 += 1
            tableau[0] = tableau[i]  ; N2 += 1
            tableau[i] = Vo  ; N2 += 1
            remplaceDecroissant()  ; N2 += 1
                
        else:
            remplaceDecroissant()

    print(f"\n TabOrdDecroissant = {tab}\n\
                Nombre d'instructions = {N2}\n")


OrdreCroissant(tableau)
OrdreDecroissant(tableau)


# petit bout de code pour me rappeller de là où je viens...

''' def remplaceAvant():


    for j in range(i, nbElements-1):

        if tableau[j] > tableau[j+1] :
            Vj = tableau[j]
            tableau[j] = tableau[j+1]
            tableau[j+1] = Vj
            remplaceArriere()

        elif tableau[j-1] > tableau[j]:
            Vj = tableau[j-1]
            tableau[j-1] = tableau[j]
            tableau[j] = Vj
            remplaceArriere()

        elif tableau[j-1] > tableau[j+1]:
            Vj = tableau[j-1]
            tableau[j-1] = tableau[j+1]
            tableau[j+1] = Vj
            remplaceArriere()

        else:
            remplaceArriere() '''


