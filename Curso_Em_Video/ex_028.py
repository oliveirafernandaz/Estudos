import random

num = float(input('Tente adivinhar um número de 0 a 5: '))
l = [0, 1, 2, 3, 4, 5]
sf = random.choice(l)

if num == sf :
    print('Você acertou!')
if num > 5:
    print('Por favor, digite um número de 0 a 5')
else :
    print('Você errou!')
