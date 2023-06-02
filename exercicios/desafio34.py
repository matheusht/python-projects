sal = float(input('qual seu salario PORRA'))
if (sal > 1250):
    aumento = sal + (sal*10/100)
else:
    aumento = sal + (sal*15/100)

print('seu salario de RS{} com o aumento foi para RS{}'.format(sal,aumento))