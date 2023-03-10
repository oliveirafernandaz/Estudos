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