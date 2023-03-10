lista_valores = []

while True:
    for i in range(0, 5):
        valor = int(input('Digite um valor: '))
        lista_valores.append(valor)
        lista_valores.sort()
        print(f'Valor adicionado na posição {lista_valores.index(valor)}.')
    print(lista_valores)
    break