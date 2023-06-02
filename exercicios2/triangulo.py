r1 = int(input('primeiro valor: '))
r2 = int(input('segundo valor: '))
r3 = int(input('terceiro valor: '))
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
#       print('os n sei oq sei q la formar um triangulo fodase')
if r1 == r2 and r2 == r3:
    print('triangulo equilatero')
elif r1 == r2 and r3 != r2:
    print('isosleces')
elif r1 != r2 and r2 != r3:
    print('escaleno')
else:
    print('nao mpodefirnar nao fode kralho')