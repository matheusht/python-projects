# o simbolo '*' serve para dizer que voce nao sabe quantos parametros vai receber, uma quantia incerta
def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')

contador(2,1,43,4,5,3,1,123,123,123)
contador(1,65,12,23)
contador(1, 2, 3)