valor = int(input('dIGITE UM VALOR RS: '))
totCedulas = {
    '100':0,
    '50':0,
    '20':0,
    '10':0,
    '5':0,
    '2':0,
    '1':0,
}
while valor > 0:
    if valor / 100 > 0:
        totCedulas['100'] = int(valor/100)
        valor = valor % 100
    if valor / 50 > 0:
        totCedulas['50'] = int(valor/50)
        valor = valor % 50
    if valor / 20 > 0:
        totCedulas['20'] = int(valor/20)
        valor = valor % 20
    if valor / 10 > 0:
        totCedulas['10'] = int(valor/10)
        valor = valor % 10
    if valor / 5 > 0:
        totCedulas['5'] = int(valor/5)
        valor = valor % 5
    if valor / 1 > 0:
        totCedulas['1'] = int(valor/1)
        valor = valor % 1
    break

print(f'Notas de 100: {totCedulas["100"]}\nNotas de 50: {totCedulas["50"]} \nNotas de 20: {totCedulas["20"]} \nNotas de 10: {totCedulas["10"]} \nNotas de 5: {totCedulas["5"]} \nNotas de 1:{totCedulas["1"]}', )
