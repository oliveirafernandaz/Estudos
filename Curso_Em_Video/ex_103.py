nome = input('Nome do jogador: ').strip()
gols = input('Número de gols: ')

def jogador(nome_jogador="<desconhecido>", gols_jogador=0):
    print(f'O jogador {nome_jogador} fez {gols_jogador} gol(s) no campeonato.')

gols = int(gols) if gols.isnumeric() else 0
    
jogador(gols_jogador=gols) if nome == '' else jogador(nome, gols)