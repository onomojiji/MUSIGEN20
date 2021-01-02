

def factoriel(n):
    for i in range((n-1),1,-1):
        n*=i

    print(n)

def factoriel2(n):
    if n==1 or n==0:
       return 1
    else:
        return n*factoriel2(n-1)

print(factoriel(1142424))
