n1 = float(input('qual a sua nota \n'))
n2 = float(input('qual a sua nota \n'))
media = (n1 + n2) / 2

print('sua media foi de {}'.format(media))
if (media < 5):
    print('TDAH GAMER')
elif (media > 5 and media <= 6.9):
    print('Semi TDAH')
elif media >= 7:
    print('TDA')
