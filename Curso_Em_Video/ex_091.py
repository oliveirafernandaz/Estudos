import random
ranking = {}
lista_ranking = []
for i in range(4):
    sorteio = random.randint(1, 5)
    ranking['Jogador'] = i + 1
    ranking['Número'] = sorteio
    lista_ranking.append(ranking.copy())
    print(f'Jogador {i+1} jogou o número {sorteio}.')

ranking_ordenado = sorted(lista_ranking, key= lambda x:x['Número'], reverse = True)
#print(ranking_ordenado)

print()
print('=-' * 30)
print(f'{"== RANKING FINAL ==":^30s}') 

for x in ranking_ordenado:
    print(f'Jogador {x["Jogador"]} com o número: {x["Número"]}.')