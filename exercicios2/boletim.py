boletim = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome,[nota1,nota2],media])
    resp = str(input('Quer continuar? ')).upper()
    if resp not in 'SN':
        resp = str(input('Quer continuar? ')).upper()
    elif resp in 'SN':
        if resp == 'S':
            continue
        else:
            break

print(boletim)