'''  fonction tamiser(arbre, nœud, n) :
   (* descend arbre[nœud] à sa place, sans dépasser l'indice n *)
   k := nœud
   j := 2k
   tant que j ≤ n
      si j < n et arbre[j] < arbre[j+1]
         j := j+1
      fin si
      si arbre[k] < arbre[j]
         échanger arbre[k] et arbre[j]
         k := j
         j := 2k
      sinon
         j := n+1
      fin si
   fin tant que
fin fonction

fonction triParTas(arbre, longueur) :
   pour i := longueur/2 à 1
       tamiser(arbre, i, longueur)
   fin pour
   pour i := longueur à 2
       échanger arbre[i] et arbre[1]
       tamiser(arbre, 1, i-1)
   fin pour
fin fonction '''


def permutter(tableau,x,y):
    
    Vo = tableau[x] 
    tableau[x] = tableau[y]
    tableau[y] = Vo 

def tamiser(arbre,noeud,n):
    k = noeud
    j = 2*k

    while j <= n:
      if j < n and arbre[j] < arbre[j+1]:
        j +=1
      elif arbre[k] < arbre[j]:
        permutter(arbre,k,j)
        k = j
        j = 2*k
      else:
        j = n+1

def triParTas(arbre, longueur) :
   for i in range(longueur,1) :
      tamiser(arbre, i, longueur)

   for i in range(longueur,2):
        permutter(arbre,i,1) 
        tamiser(arbre, 1, i-1)

tab = [1,67,1,4,575]

triParTas(tab,5)

print(tab)