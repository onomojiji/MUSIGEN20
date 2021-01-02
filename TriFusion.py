''' entrée ː un tableau T
sortie ː une permutation triée de T
fonction triFusion(T[1, …, n])
      si n ≤ 1
              renvoyer T
      sinon
              renvoyer fusion(triFusion(T[1, …, n/2]), triFusion(T[n/2 + 1, …, n]))

entrée ː deux tableaux triés A et B
sortie : un tableau trié qui contient exactement les éléments des tableaux A et B
fonction fusion(A[1, …, a], B[1, …, b])
      si A est le tableau vide
              renvoyer B
      si B est le tableau vide
              renvoyer A
      si A[1] ≤ B[1]
              renvoyer A[1] ⊕ fusion(A[2, …, a], B)
      sinon
              renvoyer B[1] ⊕ fusion(A, B[2, …, b])
 '''

def fusion(liste1,liste2):
    liste=[]
    i,j=0,0
    while i<len(liste1) and j<len(liste2):
        if liste1[i]<=liste2[j]:
            liste.append(liste1[i])
            i+=1
        else:
            liste.append(liste2[j])
            j+=1
    while i<len(liste1):
        liste.append(liste1[i])
        i+=1
    while j<len(liste2):
        liste.append(liste2[j])
        j+=1
    return liste

def tri_fusion(liste):
    if len(liste)<2:
        return liste[:]
    else:
        milieu=len(liste)//2
        liste1=tri_fusion(liste[:milieu])
        liste2=tri_fusion(liste[milieu:])
        return fusion(liste1,liste2)


with open("fiTab.txt", encoding="utf-8") as fichier:
    tableau = [l.strip() for l in fichier]

tri_fusion(tableau)

print(tableau)