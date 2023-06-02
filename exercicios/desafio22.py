nome = input('escreva seu nome').strip()

print('maisculo \n {}'.format(nome.upper()))
print('minusculo \n {}'.format(nome.lower()))
print('voce ian bruno letras\n {}'.format(len(nome) - nome.count(' ')))
print('ian bruno seu primeiro nome \n {} letras '.format(nome.find(' ')))