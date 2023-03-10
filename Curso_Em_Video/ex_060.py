import math
num = int(input('Insira um número para calcular seu fatorial: '))

print(f'O fatorial de {num}! é {math.factorial(num)}')

fact = 1

for i in range(1, num+1):
    fact = fact * i
print(f'O fatorial de {num}! é igual a {fact}')