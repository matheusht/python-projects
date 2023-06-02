import random

lista =  [0,1,2,3,4,5]
escolha = random.choice(lista)

pergunta = int(input('pense no mesmo numero que estou pensando(de 0 a 5) \n'))

if (pergunta == escolha):
    print('eu tambem estava pensando no numero \033[1;31;45m{}\033[m GG'.format(escolha))
else:
    print('TDAH Gamer Melhore numero era \033[1;31;45m{}\033[m'.format(escolha))
