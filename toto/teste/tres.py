from teste.numeros import fatorial


num = int(input('Digite um preco fodase '))
print(f'A metade de {num} e {fatorial.metade(num)}')
print(f'A dobro de {num} e {fatorial.dobro(num)}')
print(f'Aumentado em 10%, temos {fatorial.aumentar(num)}')