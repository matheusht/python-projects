import random
jogador = {}
print('Valores sorteados: ')
for c in range(0,4):
    jogador['escolha'] = random.randint(1,4)
    print(jogador['escolha'])
    print(f'jogador{c} tirou {jogador["escolha"]} no dado.')
print('-='*20)
print('Ranking: ')
sortedDict = sorted(jogador['escolha'])
print(sortedDict)
