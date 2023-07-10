aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'media de {aluno["nome"]}: '))
if aluno["media"] < 6:
    aluno['state'] = 'Reprovado'
elif aluno["media"] > 6:
    aluno['state'] = 'Aprovado'
elif aluno["media"] >= 5 and aluno['media'] < 7:
    aluno['state'] = 'Recuperations'
for k,v in aluno.items():
    print(f'  -{k} e igual a {v}')