num1 = int(input('digite 1 numero: \n'))
num2 = int(input('digite 2 numero: \n'))

if (num1 > num2):
    print('{} é maior que {}'.format(num1, num2))
elif (num2 > num1):
    print('{} é maior que {}'.format(num2,num1))
elif (num1 == num2):
    print('os dois sao iguais')
else: 
    print('TDAH detecadp')