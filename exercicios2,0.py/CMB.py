membros = ('caiovksy','ian bruno','tico brai','guizin mito','m.t.h','b. pintos',
           'rian','queijo','iq moller','backes','rain',
           'pistolinha','l.c.g','jota','licas','lelis')

membrosSimps = ('bitolinha','l.c.g','quejo','lelis','iq molinho','tico brown','B. Prates \n')
membrosBetasGoulartOpiniaoMerdaFodaseEuaeLCG = ('bitolinha','quejo','iq molinho','lelis','tico brown','B. Prates \n') # L.C.G ULTIMO LUGAR DA LISTA 

print('Lista de membros Z\/eros C.M.B \033[0;40;41mTOTTA TOLLA ERA\033[m')
print('\n')
membrosA = sorted(membros)
print('=-'*30)
print(f'{(membros)} ')
print('=-'*30)

print('Lista de membros Betas C.M.B \033[7;42;4mTOTTA TOLLA ERA\033[m \n ')

print('=-'*30)
print(f'{membrosSimps}')
print('=-'*30)

print(f'Luiz carlos GuGu')

print('\n')
print(f'Os cinco mais zueros sao: {membros[:5]} \n')
print(f'os qautro menos zueros sao: {membros[-4:]} \n')

resp = str(input('Digite o membro no qual quer saber sua posicao \n ')).strip().lower()
if resp in membros:
    print(f'{resp} esta na posicao {membros.index(resp)}')