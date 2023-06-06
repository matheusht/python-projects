vel =  int(input('qual a PORRA da velocidade do seu carro Krai '))


if (vel >= 80):
    multa = (vel - 80)  * 7
    print('VC foi multado por estar a \033[7;31;47m{}\033[m km/h, page \033[4;31;47m{}reais AGR'.format(vel,multa))
else:
    print('Yian Bruno')
