infos = {}
lista_gols = []
lista_jogadores = []

while True:
    infos.clear()
    lista_gols.clear()
    infos['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {infos["nome"]} jogou? '))

    for i in range(partidas):
        gols = int(input(f'     Quantos gols na partida {i}? '))
        lista_gols.append(gols)
    infos['gols'] = lista_gols[:]
    infos['total'] = sum(lista_gols)
    lista_jogadores.append(infos.copy())
    
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'S':
        continue
    if continuar == 'N':
        break

#print('=-' * 30)
#print(lista_jogadores)
print('=-' * 30)

print(f'Cod. {"Nome":<10} {"Gols":<10} {"Total":<10}')

for k, v in enumerate(lista_jogadores):
    print(f'{k:>3} {v["nome"]:<12} {str(v["gols"]):<10} {v["total"]:<15}')

print('=-' * 30)

while True:
    mostrar = int(input('Mostrar dados de qual jogador? (999 para parar) '))

    for k, v in enumerate(lista_jogadores):
        for i in range(len(v["gols"])):
            if mostrar == k:
                print(f'Na partida {i + 1} o jogador fez {v["gols"]} gols.')
    if mostrar == 999:
        break
    if mostrar != k and mostrar != 999:
        print('ERRO! Digite um código válido')
        continue

print('=== ENCERRADO! ===')
print('=-' * 30)

#while True:
#    for k, v in enumerate(lista_jogadores):
#        mostrar = str(input('Mostrar dados de qual jogador? (999 para parar) '))
#        if mostrar == k:
#            print(f'No jogo ele fez {v["gols"]}.')



#for k, v in infos.items():
#    print(f'O campo {k} tem valor {v}.')
#print('=-' * 30)
#print(f'O jogador {infos["nome"]} jogou um total de {partidas} partidas.')
#for k, v in enumerate(lista_gols):
#    print(f'    => Na partida {k}, fez {v} gols.')
#print(f'Foi um total de {sum(lista_gols)} gols.')