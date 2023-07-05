valores = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}. valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print('-='*20)
valores.sort()
print(f'Valores digitados: {valores[:]}')
print(f'os valores impares foram: {valores[0]}')
print(f'os valores pares foram: {valores[1]}')