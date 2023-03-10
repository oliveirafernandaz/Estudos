matrix = []
valores = []

for i in range(9):
    valor = int(input('Digite um valor: '))
    valores.append(valor)

for x in range(1):
    matrix.append(valores[:3])
    matrix.append(valores[3:6])
    matrix.append(valores[6:10])

print('=-' * 30)
print(f'{matrix[0]}\n{matrix[1]}\n{matrix[2]}')
print('=-' * 30)

soma = 0
for y in valores:
    if y % 2 == 0:
        soma += y
print(f'A soma dos valores pares é de {soma}.')

for s in matrix:
    soma2 = matrix[0][2] + matrix[1][2] + matrix[2][2]
print(f'A soma dos valores da terceira coluna é {soma2}.')
print(f'O maior valor da segunda linha {max(matrix[1])}.')