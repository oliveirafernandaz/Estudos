import random

a = input('Primeiro nome: ')
b = input('segundo nome: ')
c = input('Terceiro nome: ')
d = input('Quarto onome: ')

l = [a, b, c, d]
random.shuffle(l)

print(f'A ordem de apresentação é {l}')
