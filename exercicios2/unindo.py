pessoa = {}
info = []
soma = 0
media = 0
mulher = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    info.append(pessoa.copy())
    pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()
    if pessoa['sexo'] == 'F':
        mulher += 1
    if pessoa['sexo'] not in 'MF':
        print('Erro! Digite novamente PORRA')
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()
    resp = str(input('Deseja continuar? [S/N]')).upper()
    if resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).upper()
    elif resp in 'SN':
        if resp == 'N':
            break
media = soma / len(info)
print(f'{len(info)} pessoas foram cadastradas')
print(f'A media de idade e {media:5.2f}')
print(f'Ao todo, {mulher} mulheres foram cadastradas')
