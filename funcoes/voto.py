def voto(nasc):
    idade = 2023 - nasc
    if idade >= 16 and idade < 18:
        print(f'vOTO OPCIONAL {idade}anos')
    if idade < 16:
        print(f'VOTO NEGAD {idade}anos')
    if idade >= 18:
        print(f'VOTO Onbrigatorio {idade}anos')


idade = int(input('DIGITE SUA DATA DE NASCIMENTO: '))
voto(idade)