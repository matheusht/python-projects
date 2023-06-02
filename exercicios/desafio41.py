from datetime import date

nasc = int(input('que ano voce nasceu PORRA'))
atual = date.today().year
idade = atual - nasc

if idade <= 9:
    print('Cantegoria PePe')
elif idade <= 14:
    print('Contegoria Kids')
elif idade <= 19:
    print('Mitinho Jr.')
elif idade == 20:
    print('Mitinho The Third ')
else:
    print('\033[0;41;42mAi Sim em meu patrao')