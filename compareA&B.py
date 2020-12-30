
A = 2
B = 9


if A < B:
    print(f'\n\
            A = {A}\n\
            B = {B}\n')

elif A > B:
    
    grand = A

    A = B 

    B = grand

    print(f'\nA = {A}\n B = {B}\n')

else:
    print(f'\nA et B sont Egaux...\n')

