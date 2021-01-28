''' 
/* Procédure de tri rapide */

fonction partition(entier[] tab, entier debut, entier fin)
retourne un entier
  entier indicePivot;
  entier k <- debut;
  entier tmp;
  entier i;

  /* la valeur pivot est le premier élément du tableau */
  /* afin d'éviter les mauvaises répartitions pour ce tri */
  /* on tire aléatoirement la valeur du pivot avant de commencer */

  indicePivot <- entier aléatoire entre debut et fin;
  tmp <- tab[indicePivot];
  tab[indicePivot] <-  tab[debut];
  tab[debut] <- tmp;

  pour (i de debut+1 à fin en incrémentant de 1) faire
    si (tab[i] < tab[debut]) alors
      tmp <- tab[i];
      tab[i] <- tab[k+1];
      tab[k+1] <- tmp;
      k <- k + 1;
    fin si
  fin pour
  tmp <- tab[debut]
  tab[debut] <- tab[k];
  tab[k] <- tmp; retourner k; 
fin fonction 

procedure triRapideR(entier[] tab, entier debut, entier fin)
  si (fin > debut) alors
    entier indicePivot <-   partition(tab, debut, fin);
    triRapideR(tab, debut, indicePivot - 1);
    triRapideR(tab, indicePivot + 1, fin);
  fin si
fin procedure

procedure triRapide(entier[] tab)
  triRapideR(tab, 1, N);
fin procedure '''

import random

N = 0

def partition(tableau:list, debut:int, fin:int):
    global N
    indicepivot : int; N+=1
    k = debut ; N+=1
    tmp : int ; N+=1
    i : int ; N+=1

    indicepivot = random.randint(debut, fin) ; N+=1

    tmp = tableau[indicepivot] ; N+=1
    tableau[indicepivot] = tableau[debut] ; N+=1
    tableau[debut] = tmp ; N+=1

    for i in range(debut+1, fin, 1):
        if tableau[i] < tableau[debut]:
            tmp = tableau[i] ; N+=1
            tableau[i] = tableau[k+1] ; N+=1
            tableau[k+1] = tmp ; N+=1
            k+=1 ; N+=1

    tmp = tableau[debut] ; N+=1
    tableau[debut] = tableau[k] ; N+=1
    tableau[k] = tmp ; N+=1

    return k ; N+=1

def triRapideR(tableau:list, debut:int,fin:int):
    global N
    if (fin > debut) :
        indicePivot : int = partition(tableau, debut, fin) ; N+=1
        triRapideR(tableau, debut, indicePivot - 1) ; N+=1
        triRapideR(tableau, indicePivot + 1, fin) ; N+=1

def triRapide(tableau:list):
    global N
    triRapideR(tableau, 0, (len(tableau)-1))
    print(tableau)



with open("fiTab.txt", encoding="utf-8") as fichier:
    tableau = [l.strip() for l in fichier]


triRapide(tableau)

nbInstructions = open('nbInstructions.txt','a')
nbInstructions.write(f"\n\
                        niUpTriRapide = {N}\n")