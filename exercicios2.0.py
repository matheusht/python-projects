maioridade = 0
homens = 0
mulher = 0
while True:
    print('-'*15)
    print('CADASTRE UMA PESSOA')
    print('-'*15)
    idade = int(input('Idade: '))
    sexo = str(input('[M/F] ')).strip().upper()
    escolha = str(input('Quer continuar? [S/N] '))
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade >= 20:
        mulher += 1
    if escolha == 'N' or escolha != 'S':
        break
    elif escolha == 'S':
        continue
    else:
        escolha = str(input('Quer continuar? [S/N] '))

print('='*10+'FIM DO PROGRAMA'+'='*10)
print(f'total de pessoas com mais de 18 anos: {maioridade}')
print(f'total de homens cadastrados: {homens}')
print(f'total de mulheres com mais de 20 anos: {mulher}')