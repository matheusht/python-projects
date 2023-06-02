from datetime import date

nasc = int(input('que ano VC nasceu PORRA?'))
tempo = date.today().year
idade = tempo - nasc

print('quem nasceu em {} tem {}anos em {}'.format(nasc,idade,tempo))

if (idade < 18):
    resto = 18 - idade
    print('VC vai se alistar em {}anos para o exercito'.format(resto))
    print('seu alistamento sera em {}'.format(tempo + resto))
elif (idade == 18):
    print('n sei la oq listar')
elif (idade > 18):
    resto = idade - 18
    print('ja passou {}anos de se alistar'.format(resto))
    print('seu alistamento foi em {}'.format(tempo - resto))
