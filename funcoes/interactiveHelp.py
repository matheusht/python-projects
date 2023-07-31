def home():
    print('-'*28)
    print('   Sistema de AJUDA PyHelp   ')
    print('-'*28)


def pyHelp():
    while True:
        home()
        duvida = str(input('Função ou Biblioteca > ')).strip()
        if duvida.lower() == 'fim':
            break
        else:
            help(f'{duvida}')
        

pyHelp()