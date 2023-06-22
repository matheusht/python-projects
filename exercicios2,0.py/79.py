valores = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        
    resp = str(input('Quer continuar? [S/N]')).upper().strip()
    if resp in 'SN':
        if resp == 'N':
            break
        else:
            continue
    else:
        print('OPCAO ERRADA')
        resp = str(input('Quer continuar? [S/N]')).upper().strip()
print(valores)
    