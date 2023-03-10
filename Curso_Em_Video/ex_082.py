lista_valores = []
lista_pares = []
lista_impares = []

while True:
    valor = int(input('Digite um número: '))
    lista_valores.append(valor)
    if valor % 2 == 0:
        lista_pares.append(valor)
    if valor % 2 != 0:
        lista_impares.append(valor)
    continuar = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    if continuar == 's':
        continue
    if continuar == 'n':
        break
print('=-' * 30)
print(f'A lista completa é {lista_valores}.')
print(f'A lista de pares é {lista_pares}.')
print(f'A lista de ímpares é {lista_impares}.')