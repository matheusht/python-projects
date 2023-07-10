import datetime
info = {}
for c in range(0,1):
    info['nome'] = str(input('Nome: '))
    info['nasc'] = int(input('Ano de Nascimento: '))
    info['trab'] = int(input('Carteira de Trabalho [0 NAO TEM] '))
    if info['trab'] != 0:
        info['contrato'] = int(input('Ano de Contratacao: '))
        info['sal'] = float(input('Salario R$'))
        info['aposentadoria'] = info['nasc'] + ((info['contrato'] + 35) - 2023)
for k, v in info.items():
    print(f' -{k} e igual a {v}')