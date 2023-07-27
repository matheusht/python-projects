def fatorial(num=1,show=False):
    if show == True:
        f = 1
        for c in range(num, 0, -1):
            print(f'{c} x ',end='')
            f *= c
        print(f'= {f}')
    else:
        f = 1
        for c in range(num, 0, -1):
            f *= c
        print(f'{f}')

        
            

print('-'*20)
fatorial(4, show=False)
