import random

a = input('Escreva o primeiro nome: ')
b = input('Escreva o segundo nome: ')
c = input('Escreva o terceiro nome: ')
d = input('Escreva o quarto nome: ')

l = [a, b, c, d]

nam = random.choices(l)
print(f'O aluno {nam} foi o escolhido.')
