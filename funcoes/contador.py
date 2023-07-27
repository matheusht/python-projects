import time
def separador():
    print('-='*30)

def contadorInicial():
    print('-='*30)
    print('Contagem Inicial (1-10)')
    print('-='*30)
    return  " ".join(str(num) for num in range(1,11))

def contadorFinal():
    print('-='*30)
    print('Contagem Inicial (1-10)')
    print('-='*30) 
    return " ".join(str(num) for num in range(10, -1, -2))

def contador(i,f,p):
    """
    Função usada para Fodase Eu ae Togs Plan Fodase Eu ae N ligo Fodase
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print("fim")


print(contadorInicial())
separador()
print(contadorFinal())

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
skip = int(input('Passo: '))
separador()
print(f'Contagem de {inicio} ate {fim} de {skip} em {skip}')
contador(inicio,fim,skip)

help(contador)
