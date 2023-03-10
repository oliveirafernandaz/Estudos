lista_valores = []

for i in range(0, 5):
    valor = int(input('Digite um valor: '))
    if i == 0 or valor > lista_valores[-1]:
        lista_valores.append(valor)
    else:
        posicao = 0
        while posicao < len(lista_valores):
            if valor <= lista_valores[posicao]:
                lista_valores.insert(posicao, valor)
                break
    print(f'Valor adicionado na posição {lista_valores.index(valor)}.')

print(lista_valores)
