valores = []
for c in range(0,1):
    novoValor = (int(input('Digite um valor: ')))
    valores.append(novoValor)
    print('VALOR ADICIONADO AO FINAL DA LISTA')
    novoValor = (int(input('Digite um valor: ')))
    valores.insert(0, novoValor)
    print('VALOR ADICIONADO A POSIÇÃO 0')
    novoValor = (int(input('Digite um valor: ')))
    valores.insert(0, novoValor)
    print('VALOR ADICIONADO A POSIÇÃO 1')
    novoValor = (int(input('Digite um valor: ')))
    valores.append(novoValor)
    print('VALOR ADICIONADO AO FINAL DA LISTA')
ricardo = valores.sort()
print(f'a lista é {valores}')
print(f'os valores em ordem sao {ricardo}')
    