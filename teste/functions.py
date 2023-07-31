def fatorial(n=0):
    f = 1
    for c in range(1,n+1):
        f *= c
    return f

def dobro(n):
    return n * 2


def triplo(n):
    return n * 3

def metade(n):
    return n / 2

def aumentar(n):
    novoValor = n / 10 + n
    return novoValor