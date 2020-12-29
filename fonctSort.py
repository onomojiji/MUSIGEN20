

tableau = [2,9,4,0,6,8]

nbElements = len(tableau)

i = 0

for i in nbElements :

    if tableau[i] < tableau[i+1]:
        
        tableau.index(tableau[i]) = tableau.index(tableau[i+1])
        tableau.index(tableau[i+1]) = tableau.index(tableau[i])


    else:
        pass


