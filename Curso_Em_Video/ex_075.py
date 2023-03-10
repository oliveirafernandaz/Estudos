list_number = []

for i in range(4):
    num = int(input('Digite um número: '))
    list_number.append(num)

tuple_number = tuple(list_number)

print(f'Você digitou os valores: {tuple_number}.')
print(f'O número 9 apareceu {tuple_number.count(9)} vezes.')
if 3 in tuple_number:
    print(f'O valor 3 apareceu na {tuple_number.index(3) + 1}° posição.')
else:
    print(f'O valor 3 não foi encontrado')
print(f'Os valores pares são: ', end='')

for i in tuple_number:
    if i % 2 == 0:
        print(i, ' ', end='')