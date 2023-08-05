def leiaInt(B: str):
        try:
            valorInt = input(B)
            if valorInt.isnumeric():
                return (f'{valorInt}.')
        except:
            print(f'ERRO! FODASE ')

def leiaFloat(A: str):
        try:
           valorFloat = input(A)
           if float(valorFloat):
                return  (f' {valorFloat}')
        except:
            print(f'ERRO! FODASE ')


num = leiaInt('Digite um numero: ')
numFloat = leiaFloat('dIGITE UM Numero: ')
print(f'O valor inteiro digitado foi {num} e o real foi {numFloat}')

