def ficha(nome='<unknown>',gol=0):
    print(f'O jogador {nome} fez {gol} gols no total')

nome = str(input('Nome do jogador: '))
gol = int(input('Gols do jogador: '))
ficha(nome,gol)