total = 0
produtos = 0
menor = 0
barato = ''
cont = 0
while True:
    nome = str(input('qual o nome do produto? '))
    n = int(input('Qual o preço do produto? '))
    cont += 1
    total += n
    if n > 1000:
        produtos += 1
    if cont == 1 or n < menor:
        menor = n
        barato = nome
    else:
        if n < menor:
            menor = n
            barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input(' CONTINUAR? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print(f'O total gasto na compra foi de {total} \n {produtos} custaram mais que 1000RS \n o nome do produto mais menor é {barato}')
    