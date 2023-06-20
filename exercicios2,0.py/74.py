import random
numeros = []
for c in range(0,5):
    numeros.append(random.randint(0,100))
    maior = max(numeros)
    menor = min(numeros)
print(f'{numeros}', end=',')
print(f'O maior numero foi {maior}')
print(f'O menor numero foi {menor}')