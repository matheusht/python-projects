val = float(input('qual o valor da PORRA da casa'))
sal = float(input('qual a MERDA do seu salario'))
parc = int(input('em quantos anos ouahsduig PORRA'))
prestação = val / (parc * 12)
min = sal * 30 / 100
print('pra pagr uma casa de R${:.2f} em {}anos com {}reais de salario,'.format(val,parc,sal), end='')
print('tera que pagar{:.2f}reais como prestaãao'.format(prestação))

print('Comparação entre salario {} e valor a se pagar minimo {}'.format(sal,min))

if prestação >= min:
    print('prestação negada')
else:
    print('FOndase')