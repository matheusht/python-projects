try:
    a = int(input('Numbero: '))
    b = int(input('Numbero: '))
    c  = a / b

except (ValueError, TypeError):
    print(f'O problema encontrado foinos tipos de dado')
except (ZeroDivisionError):
    print('VOCE DIVIDIU POR 0')
else:
    print(f'O resultado e {c}')
finally:
    print('Eu ae')