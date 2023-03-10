lista_valores = []

while True:
    valor = int(input('Digite um valor: '))
    lista_valores.append(valor)
    myset = set(lista_valores)
    if len(lista_valores) != len(myset):
        print('Valor duplicado! Não vou adicionar.')
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
        lista_valores.pop(-1)
        continue
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    if continuar == 's':
        continue
    if continuar == 'n':
        break

print(f'Você digitou os valores {lista_valores}.')

