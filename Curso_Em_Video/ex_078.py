lista_valores = []

for i in range(0, 5):
    valor = input(f'Digite um valor para a posição {i}: ')
    lista_valores.append(valor)

print(f'Você digitou os valores {lista_valores}.')
indices_maiores = []
indices_menores = []
for i in range(len(lista_valores)): 
    if lista_valores[i] == max(lista_valores):
        indices_maiores.append(i)
    if lista_valores[i] == min(lista_valores):
        indices_menores.append(i)

print(f'O maior valor digitado foi {max(lista_valores)} nas posições {indices_maiores}.')
print(f'O menor valor digitado foi {min(lista_valores)} nas posições {indices_menores}.')