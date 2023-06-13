contagem = ('um','dois','tres','quatro','cinco','seis','sete','oito','nove,','dez')
while True:
    num = int(input('digite um numero de 0 a 10 para saber seu extenso'))
    print(contagem[num-1])
    resp = str(input('DSEJA CONTINUAR? [S/N] ')).strip().upper()
    if resp in 'S':
        continue
    else:
        break