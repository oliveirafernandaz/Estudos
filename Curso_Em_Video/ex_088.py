import random
quantidade = int(input('Quantos palpites vc quer? '))
jogos = []
jogadas = []
total = 1

while total <= quantidade:
    cont = 0
    while True:
        sorteio = random.randint(1,60)
        if sorteio not in jogos:
            jogos.append(sorteio)
            cont += 1
        if cont >= 6:
            break
    jogos.sort()
    jogadas.append(jogos[:])
    jogos.clear()
    total += 1
print('=-' * 30)
print(f'Suas jogadas são:')

for i, l in enumerate(jogadas):
    print(f'Jogo {i+1}: {l}')


