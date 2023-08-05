def moeda(n):
    dolar = 4.80
    novoValor = n / dolar
    return novoValor

def resumo(preço=0,aumento=0,redução=0):
    aumentoInicial = aumento
    reduçãoInicial = redução
    aumento = preço + (preço * aumento/100)
    redução = preço - (preço * redução/100) + preço

    dobro = preço * 2
    metade = preço / 2
    moeda = 'R$'
    print(f'Preço analisado:     {moeda}{preço:>.2f}'.replace('.',','))
    print(f'Dobro do preço:     {moeda}{dobro}')
    print(f'Metade do preço:     {moeda}{metade}')
    print(f'{aumentoInicial:>.2f}% de aumento:     {moeda}{aumento:>.2f}')
    print(f'{reduçãoInicial:>.2f}% de redução:     {moeda}{redução:>.2f}')
