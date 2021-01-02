''' procédure tri_insertion(tableau T)
       n ← taille(T)
       pour i de 1 à n - 1

            # mémoriser T[i] dans x
            x ← T[i]                            

            # décaler vers la droite les éléments de T[0]..T[i-1] qui sont plus grands que x en partant de T[i-1]
            j ← i                               
            tant que j > 0 et T[j - 1] > x
                     T[j] ← T[j - 1]
                     j ← j - 1

            # placer x dans le "trou" laissé par le décalage
            T[j] ← x   '''

import random

N = 0
N2 = 0

def tri_insertion(tableau:list):
    
    global N
    
    n = len(tableau); N+=1

    for i in range(1,n):
        x = tableau[i]; N+=1
        j = i ; N+=1

        while j > 0 and tableau[j-1] > x:
            tableau[j] = tableau[j-1];N+=1
            j-=1; N+=1
        
        tableau[j] = x ; N+=1

    print(f"\n\
        TabOrdonne = {tableau}\n\
        Nombre d'instructions = {N}")

def tri_insertion_inverse(tableau:list):
    global N2
    n = len(tableau); N2+=1

    for i in range(1,n):
        x = tableau[i]; N2+=1
        j = i ; N2+=1

        while j > 0 and tableau[j-1] < x:
            tableau[j] = tableau[j-1];N2+=1
            j-=1; N2+=1
        
        tableau[j] = x ; N2+=1

    print(f"\n\
        TabOrdonneInverse = {tableau}\n\
        Nombre d'instructions = {N2}")


with open("fiTab.txt", encoding="utf-8") as fichier:
    tableau = [l.strip() for l in fichier]

''' fichier = open('fiTab.txt','w')
for i in range(0,len(tableau)):

    fichier.write(f"{tableau[i]}\n")

fichier.close() '''

tri_insertion(tableau)
tri_insertion_inverse(tableau)

nbInstructions = open('nbInstructions.txt','a')
nbInstructions.write(f"\n\
                        niUpTriparInsertion = {N}\n\
                        niDownTriparInsertion = {N2}\n")



