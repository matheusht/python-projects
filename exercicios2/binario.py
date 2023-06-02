integer = int(input('digite um numero  para saber sua base: '))
option = int(input('[1] para binario \n[2] para octal \n[3] para hexadecimal \n '))

if option == 1:
    binary = bin(integer)
    print(' a base numerica de {} em forma binaria seria de {}'.format(integer,binary))
elif option == 2:
    octal = oct(integer)
    print('a base numerica de {} em forma octal seria de {}'.format(integer,octal))
elif option == 3:
    hexa = hex(integer)
    print(' a base numerica de {} em forma hexadecimal seria de {}'.format(integer,hexa))
else:
    print('TDAH detectadp')
