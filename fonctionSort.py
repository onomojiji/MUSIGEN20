import random
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
        | v1.0.3            |      31-12-2020, 09 h 52 min       |

 '''

##################################### F.O.N.C.T.I.O.N.S #######################################

def permutter(x,y):

    Vo = tableau[x] 
    tableau[x] = tableau[y]
    tableau[y] = Vo 

def remplaceCroissant(i):
    
    global N

    for k in range(0, i) : #pour chaque nombre allant de la position 0 à la position i :
        
        if tableau[k] > tableau[i] :  #Si le nombre correspondant à la position k > au nombre à la position i
            permutter(k,i); N+=3        
        elif tableau[k] > tableau[k+1]: #En même temps si le nombre correspondant à la position k  au nombre à la position k+1
            permutter(k,k+1); N+=3    
            
        else :
            continue

def remplaceDecroissant(i):

    global N2

    for k in range(0, i) :
        
        if tableau[i] > tableau[k] :#Si le nombre correspondant à la position k > au nombre à la position i
            permutter(i,k); N2 += 3      #

        elif tableau[k+1] > tableau[k] :   # En même temps si le nombre correspondant à la position k  au nombre à la position k+1
            permutter(k,k+1) ; N2 += 3
            
        else :
            continue

def OrdreCroissant(tab:list):
    
    global N

    # l'objectif ici étant de classer par ordre croissant les éléments du tableau :

    for i in range(0, len(tableau)) : 

        if tableau[0] > tableau[i] : # Je compare le nombre à la position i au nombre à la position 0 d'abord pour me rassurer que mon derrière est déjè bon.
            permutter(0,i); N+=3
            remplaceCroissant(i)
                
        else:
            remplaceCroissant(i)

    print(f"\n\
        TabOrdCroissant = {tab}\n\
        Nombre d'instructions = {N}")

def OrdreDecroissant(tab:list):

    global N2

    # l'objectif ici étant de classer par ordre décroissant les éléments du tableau :

    for i in range(len(tableau)-1, 0,-1) :
    
        if tableau[i] > tableau[0] : # La même chanson...
            permutter(i,0); N2+=3
            remplaceDecroissant(i)
                
        else:
            remplaceDecroissant(i)

    print(f"\n\
        TabOrdDecroissant = {tab}\n\
        Nombre d'instructions = {N2}\n")
    

#################################### P.R.O.G.R.A.M.M.E ############################################

''' tableau = [7, 17, 9,0,454,4,78,1,123,-3,-13,79,908,28,34,654,23,0.34,25] '''

with open("fiTab.txt", encoding="utf-8") as fichier:
    tableau = [l.strip() for l in fichier]


N = 0 ; N2 = 0

OrdreCroissant(tableau)
OrdreDecroissant(tableau)

nbInstructions = open('nbInstructions.txt','a')
nbInstructions.write(f"\n\
                        niUpMethoduBoeuf = {N}\n\
                        niDownMethoduBoeuf = {N2}\n")
