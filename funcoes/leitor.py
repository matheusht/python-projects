def leiaInt(B: str):
    while True:
        valor = input(B)
        if valor.isnumeric():
            print(f'voce digitou o valor {valor}')
        else:
            print(f'ERRO! FODASE ')

n = leiaInt('TDAH? ')
