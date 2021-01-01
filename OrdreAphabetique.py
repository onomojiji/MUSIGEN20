
''' nbMots = input("nombre de mots : ")

nbMots = int(nbMots)

for i in range(0,nbMots):
    mot = input(f"Mot {i+1} : ") '''

''' # Caractères 0 à 1023
for bloc in range(8):
   for lig in range(16):
      for col in range(8):
         code = 128 * bloc + 16 * col + lig
         caractere = chr(code)
         if code < 32:
            caractere = " "
         print("{:04d} {}  ".format(code, caractere), end = "")
      print()
   print() '''


''' mot1 = 'babana'
mot2 = 'abada'

mot1 = list(mot1)
mot2 = list(mot2)

tableau = [mot1[0],mot2[0]]

for i in range(0,len(mot1)):
    print(mot1[i],end='')
print()
 '''

On = True

N = 0

def continuer ():
        
    oui = True

    while oui :

        reponse2 = input("\n\
        Voulez vous réessayer ?\n\
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


def permutter(tableau:list,x,y):
    
    Vo = tableau[x] 
    tableau[x] = tableau[y]
    tableau[y] = Vo 


def remplaceCroissant(tableau:list,i):
    
    global N

    for k in range(0, i) : #pour chaque nombre allant de la position 0 à la position i :
        
        if tableau[k] > tableau[i] :  #Si le nombre correspondant à la position k > au nombre à la position i
            permutter(tableau,k,i); N+=3        
        elif tableau[k] > tableau[k+1]: #En même temps si le nombre correspondant à la position k  au nombre à la position k+1
            permutter(tableau,k,k+1); N+=3    
            
        else :
            continue

def OrdreCroissant(tableau:list):
    
    global N

    # l'objectif ici étant de classer par ordre croissant les éléments du tableau :

    for i in range(0, len(tableau)) : 

        if tableau[0] > tableau[i] : # Je compare le nombre à la position i au nombre à la position 0 d'abord pour me rassurer que mon derrière est déjè bon.
            permutter(tableau,0,i); N+=3
            remplaceCroissant(tableau,i)
                
        else:
            remplaceCroissant(tableau,i)

    ''' print(f"\n\
        TabOrdCroissant = {tableau}\n\
        Nombre d'instructions = {N}") '''

while On:
    
    nbmots = input("\nCombien de mots souhaitez vous classer : ")

    nbmots = int(nbmots)

    TabMots = []

    TabIndice1 = []

    for i in range(0,nbmots):
        
        mot = input(f"Mot {i+1} : ")
        
        TabMots.insert(i,f"{mot}")

        motn = list(TabMots[i])

        TabIndice1.insert(i,ord(motn[0]))

        OrdreCroissant(TabIndice1)

        print(TabIndice1)

        for j in range(0,len(TabIndice1)-1):
            for k in range(0, len(TabMots)-1):
                if TabIndice1[j] == ord((motn[k])[0]):
                    permutter(TabMots,i,j)
                else:
                    continue



    print(TabMots)

    On = continuer()

'''  except:
        print("\n\
            Entrez une valeur Numérique Entière")
        On = continuer() '''



