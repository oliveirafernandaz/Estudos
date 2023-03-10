import random

numero_list = random.sample(range(0, 10), 5)
numero_tuple = tuple(numero_list)

print(f'Os números sorteados foram: ', end='')
for i in numero_tuple:
    print(i, ' ', end = '')

print(f'\nO menor número é : {min(numero_tuple)}')
print(f'O maior número é: {max(numero_tuple)}')

#print(numero_list)
#print(numero_tuple)
