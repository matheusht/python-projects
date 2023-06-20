vogais = ('a,e,i,o,u')
palavrasBastam = ('guizao','ricardo','podre',
                  'guizin','rafa','kau',
                  'tico brai','caio','ian bruno')
for palavra in palavrasBastam:
    print(f'\nNa palavra {palavra} temos:', end=' ')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')