values = []
c = 0
while True:
    newValue = int(input('Digite um valor: '))
    values.append(newValue)
    c += 1
    answer = str(input('Deseja continuar? [S/N]')).strip().upper()
    if answer not in 'SN':
        answer = str(input('Deseja continuar? [S/N]')).strip().upper()
    if answer == 'N':
            break
    else:
            continue
values.sort(reverse=True)
print(f'Voce digitou {c} elementos.')
print(f'os valores em ordem descresent4e sao {values}')
if c in values:
    print(f'o valor {c} faz parte da lista')
