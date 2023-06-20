tabela = ()
tabelaPreços = ()
print('-'*20)
print('listagem de precos')
print('-'*20)
while True:
    prod = str(input('Qual o nome do produto? ')).strip()
    preço = float(input('Qual o preço do produto? '))
    tabela += str.format((prod,))
    tabelaPreços += (preço,)
    for c in range(0,10):
        print(f'{tabela} \n')
    if c >= 10:
        break