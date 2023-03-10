lista_valores = []

while True:
    valor = int(input('Digite um valor: '))
    lista_valores.append(valor)
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    if continuar == 's':
        continue
    if continuar == 'n':
        break
print('-=' * 30)
print(f'Você digitou {len(lista_valores)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(lista_valores, reverse = True)}.')

if 5 in lista_valores:
    print(f'O número 5 está na lista.')
elif 5 is not lista_valores:
    print(f'O número 5 não está na lista')