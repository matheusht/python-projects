matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
valorPar = 0
maior = 0
soma = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'digite um valor para [{l}, {c}]: '))
print('-='*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz[l][c] % 2 == 0:
            valorPar += matriz[l][c]
        if matriz[1][c] > maior:
            maior = matriz[1][c]
        if matriz[2][c] == int:
            soma += matriz[2][c]
    print()
print('-='*20)
print(f'A soma dos valores pares e  {valorPar}')
print(f'a soma dos valores da terceira coluna e {soma}')
print(f'o maior valor foi {maior}')