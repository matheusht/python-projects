contagem = 0
dado = []
dados = []
while True:
    dado.append((input('Nome: ')))
    dado.append((input('Peso: ')))
    dados.append(dado[:])
    dado.clear()
    contagem += 1
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    elif resp == 'N':
        break
    else:
        continue        
for cont in dados:
    c
print(f'Ao todo voce cadastrou {contagem} pessoas.')
print('o maior peso foi de {}kg. peso de ')
print(f'{dados}')