''' import random


def U(x):
    if x == 0:
        return 0
    else:
        return 2*U(x-1)-3

print(U(10))

print(random.randint(2,9)) '''
def U(x):
    if x==0:
        return 0
    else:
        for i in range(0,x):
            x = i
            x = 2*i - 3
            x = i
        return x
            

print(U(3))