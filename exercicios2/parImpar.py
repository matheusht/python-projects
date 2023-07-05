values = []
valorPar = []
valorImpar  = []
c = 0
while True:
    newValue = int(input('Digite um valor: '))
    if newValue % 2 == 0:
        valorPar.append(newValue)
    values.append(newValue)
    if newValue % 2 != 0:
          valorImpar.append(newValue)
    c += 1
    answer = str(input('Deseja continuar? [S/N]')).strip().upper()
    if answer not in 'SN':
        answer = str(input('Deseja continuar? [S/N]')).strip().upper()
    if answer == 'N':
            break
    else:
            continue
print(f'a lista completa e {values}')
print(f'a lista de pares e {valorPar}')
print(f'a lista de impares e {valorImpar}')