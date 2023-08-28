from funcoes import functions

whitelist = [1,2,3]
numeros = range(3,10)
option = 0

while option != 3:
    functions.content()
    try:
        option = int(input('Sua opção: '))
        if option not in whitelist:
             if option in numeros:
                  raise Exception
             else:
                  raise Exception(ValueError,TypeError)
    except (TypeError, ValueError):
        print('ERRO! DIGITE UM NUMERO INTEIRO VALIDO')
    except (Exception):
        print('ERRO! DIGITE UMA OPÇÃO VALIDA')            
            
    

