viagem = int(input('sua viagem sera quantos KM?'))

if (viagem <= 200):
    valor = viagem * .5
    print('o valor de sua viagem de {}km, sera de {:.2f}RS'.format(viagem,valor))
else:
    valor = viagem * .45
    print('o valor de sua viagem de {}km, sera de {:.3f}RS'.format(viagem,valor))
    