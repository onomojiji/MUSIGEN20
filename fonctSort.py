
''' tableau = [90,9,45,4,3,6,13,123,1] '''

''' tableau = [3,9,90,2,234,4] '''

tableau = [7,123,78,1,4,0,454,9]

nbElements = len(tableau)


def remplaceArriere():
    for k in range(0, i-1) :
        
        if tableau[k] > tableau[i] :
            Vk = tableau[i]
            tableau[i] = tableau[k]
            tableau[k] = Vk

        elif tableau[k] > tableau[k+1] :
            Vk = tableau[k+1]
            tableau[k+1] = tableau[k]
            tableau[k] = Vk
            
        else :
            continue

        print(f"\n Boucle k : {tableau}")


def remplaceAvant():
    

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
            remplaceArriere()

        print(f"\n Boucle j : {tableau}")
            

for i in range(0, nbElements-1) :

    if tableau[0] > tableau[i] :
        Vo = tableau[0]
        tableau[0] = tableau[i]
        tableau[i] = Vo
        remplaceAvant()
            
    else:
        remplaceAvant()


    print(f"\n Boucle i : {tableau}")
    

print(f"\n Résultat = {tableau}\n")