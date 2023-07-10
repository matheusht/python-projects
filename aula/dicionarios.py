pessoas = {'NAME': 'Ian bruno',
           'GENDER': 'C.F.I.Q',
           'SEX': 'Sexy'}
pessoas['LAST_NAME'] = 'Goulartim'
print(f'o {pessoas["NAME"]} mitou')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')