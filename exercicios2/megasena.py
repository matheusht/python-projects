import random

jogos = int(input('Quantos palpites de jogos? '))
for c in range(1,jogos+1):
    randomList = [random.sample(range(0,60), 10)]
    randomList.sort()
    print(f'Jogo {c}{randomList}')