jogador = {}
jogador['nome'] = str(input('Nome Porra: '))
jogador['quant'] = int(input('partidas jogadas: '))
jogador['total'] = 0
for c in range(0,jogador['quant']):
    jogador['gols'] = int(input(f'quantos gols na partida {c}? '))
    jogador['total'] += jogador['gols']
print('-='*20)
print(jogador)
print('-='*20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
print(f'o jogador {jogador["nome"]} jogou {jogador["quant"]}.')
for c in range(0,jogador['quant']):
    print(f'   => Na partida {c}, fez {jogador["gols"]}')
print(f'foi um total de {jogador["total"]} gols.')