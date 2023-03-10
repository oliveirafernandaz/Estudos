lista = []
for i in range(1, 6):
    i = float(input(f'Qual o peso da {i}° pessoa? '))
    lista.append(i)
print(f'O menor peso é {min(lista)} e o maior é {max(lista)}.')
