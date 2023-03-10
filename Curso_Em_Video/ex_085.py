numeros = [[], []]

for i in range(0,8):
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    if valor % 2 != 0:
        numeros[1].append(valor)

print('=-' * 30)
print(f'Os números pares em ordem crescente foram {sorted(numeros[0])}.')
print(f'Os números ímpares em ordem crescente foram {sorted(numeros[1])}.')