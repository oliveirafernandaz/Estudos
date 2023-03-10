import random

num = float(input('Tente adivinhar um número de 0 a 10: '))
l = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
sf = random.choice(l)
palpite = 0

while sf != num:
    palpite += 1
    if num < sf:
        num = float(input('Mais... Tente adivinhar mais uma vez: '))
    elif num > sf:
        num = float(input('Menos... Tente adivinhar mais uma vez: '))
if num == sf:
    print(f'Você acertou depois de {palpite} palpites.')
