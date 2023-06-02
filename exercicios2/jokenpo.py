import time
import random
itens = ('Pedra','Papel','Tesoura')
computador = random.randint(0,2)
print('SUAS OPÇÕES:')
print('[0] Pedra \n[1] Papel \n[2]Tesoura ')
jogador = int(input('Qual você escolhe? '))
print('jo')
time.sleep(0.5)
print('ken')
time.sleep(0.5)
print('po')
print('-='*10)
print('o Computador escolheu {}'.format(itens[computador]))
print('o jogaodr jogou {}'.format(itens[jogador]))
print('-='*10)

if computador == 0:
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('Jogador Venceu')
    elif jogador == 2:
        print('Computaador Venceu')
    else:
        print('oplão inmvaçlida')

elif computador == 1:
    if jogador == 0:
        print('Computador venceu')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR Venceu')
    else:
        print('oplão inmvaçlida')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR venceu')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('oplão inmvaçlida')


# escolha = random.randint(1,3)
# if opção == 1 and escolha == 1:
#     print('-='*12)
#     print('Computador jogou Pedra')
#     print('jogador jogou Pedra')
#     print('-='*12)
#     print('EMPATE')
# elif opção == 1 and escolha == 2:
#     print('-='*12)
#     print('Computador jogou Papel')
#     print('Jogador jogou Pedra')
#     print('-='*12)
#     print('Computador Venceu')
# elif opção == 1 and escolha == 3:
#     print('-='*12)
#     print('Computador jogou Tesoura')
#     print('Jogador jogou Pedra')
#     print('-='*12)
#     print('Jogador Venceu')
# elif opção == 2 and escolha == 1:
#     print('-='*12)
#     print('Computador jogou Pedra')
#     print('Jogador jogou Papel')
#     print('-='*12)
#     print('Jogador Venceu')
# elif opção == 2 and escolha == 2:
#     print('-='*12)
#     print('Jogador jogou Papel')
#     print('Computador jogou Papel')
#     print('-='*12)
#     print('EMPATE')
# elif opção == 2 and escolha == 3:
#     print('-='*12)
#     print('Computador jogou Tesoura')
#     print('Jogador jogou Papel')
#     print('-='*12)
#     print('Computador Venceu')
# elif opção == 3 and escolha == 1:
#     print('-='*12)
#     print('Computador jogou Pedra')
#     print('Jogador jogou Tesoura')
#     print('-='*12)
#     print('Computador Venceu')
# elif opção == 3 and escolha == 2:
#     print('-='*12)
#     print('Computador jogou Papel')
#     print('Jogador jogou Tesoura')
#     print('-='*12)
#     print('Jogador Venceu')
# elif opção == 3 and escolha == 3:
#     print('-='*12)
#     print('Computador jogou Tesoura')
#     print('Jogador jogou Tesoura')
#     print('-='*12)
#     print('Empate')
