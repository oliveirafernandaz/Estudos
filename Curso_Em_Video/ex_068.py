import random
cont = 0

while True:
    jogador = int(input('Escolha um número de 1 a 10: '))
    parouimpar = str(input('Par ou ímpar? [P/I]: ')).lower().strip()[0]
    jogadas = random.randint(0, 10)
    soma = jogador + jogadas
    if soma % 2 == 0 and parouimpar == 'p' or soma % 2 != 0 and parouimpar in 'ií':
        print(f'Você escolheu {jogador} e o computador escolheu {jogadas}.\nO total deu {soma}. Você venceu!')
        cont += 1
    if soma % 2 == 0 and parouimpar != 'p' or soma % 2 != 0 and parouimpar not in 'ií':
        print(f'Você escolheu {jogador} e o computador escolheu {jogadas}.\nO total deu {soma}. Você perdeu!')
        break
print(f'Você venceu um total de {cont} vezes.')
