preço = float(input('valor a ser pago: '))
print('escolha uma opção para pagar: ')
opção = str(input('[1] para á vista ou cheque \n[2] para á vista no cartão \n[3] para até 2x no cartão \n[4] 3x ou mais no cartão:'))

if opção == '1':
    desconto = preço - (preço * 10 / 100)
    print('pagandom á vista com {} de desconto, pagarás: {:.2f}'.format('10%',desconto))
elif opção == '2':
    desconto = preço - (preço * 5 / 100)
    print('pagandom á vista no cartao com {} de desconto, pagarás: {:.2f}'.format('5%',desconto))
elif opção == '3':
    parcela = preço / 2
    print('pagandom em até 2x no cartao, pagarás o valor parcelado de: {:.2f}'.format(parcela))
elif opção == '4':
    juros = preço + (preço * 20 / 100)
    totparc = int(input('quantas parcelas?'))
    parcela = juros / totparc
    print('pagando em {}x no cartão, o valor total da sua compra sera de {:.2f} com valores de {} parcelados amo mes'.format(totparc,juros,parcela))
else:
    print('opção ivalidade tente novamente')
