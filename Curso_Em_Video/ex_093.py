infos = {}
infos['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {infos["nome"]} jogou? '))
lista_gols = []

for i in range(partidas):
    gols = int(input(f'     Quantos gols na partida {i}? '))
    lista_gols.append(gols)
infos['gols'] = lista_gols
infos['total'] = sum(lista_gols)

print('=-' * 30)
print(infos)
print('=-' * 30)
for k, v in infos.items():
    print(f'O campo {k} tem valor {v}.')
print('=-' * 30)
print(f'O jogador {infos["nome"]} jogou um total de {partidas} partidas.')
for k, v in enumerate(lista_gols):
    print(f'    => Na partida {k}, fez {v} gols.')
print(f'Foi um total de {sum(lista_gols)} gols.')