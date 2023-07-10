# brasil = []
# estado1 = {'UTF': 'Paraná', 'SIGLA': 'PR'}
# estado2 = {'UTF-8': 'Font-Style', 'SIGLA': 'EUAE'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[0]['UTF'])

estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)