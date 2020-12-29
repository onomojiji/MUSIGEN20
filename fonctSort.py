

tableau = [2,9,4,0,6,8]

nbElements = len(tableau)

i = 0

while i <= nbElements:

    i+=1

    if tableau[i] > tableau[i+1]:
    
        element = tableau[i]
        tableau[i] = tableau[i+1]
        tableau[i+1] = element

    elif tableau[i] < tableau[i-1]:

        element2 = tableau[i]
        tableau[i] = tableau[i-1]
        tableau[i-1] = element2

    elif tableau[i-1] > tableau[i+1] :
        
        element3 = tableau[i-1]
        tableau[i-1] = tableau[i+1]
        tableau[i+1] = element3

    else:

        tableau[i] = tableau[i]
        tableau[i+1] = tableau[i+1]

    print(tableau[i])
    print(tableau)
