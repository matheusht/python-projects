peso = float(input('qual smeu peso'))
alt = float(input('qial sua ualtura'))
LCG = 'Luiz Carlos Goulart'

imc = peso / (alt**2)

if (imc < 18.5):
    print('abaixo do pes')
elif (imc > 18.5 and imc < 25):
    print('peso ideal')
elif (imc > 25 and imc < 30):
    print('sobrepeso')
elif (imc > 30 and imc < 40):
    print('obesidade')
else:
    print('{}'.format(LCG))