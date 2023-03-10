num = 0
pergunta = 's'
lista_numeros = []

while pergunta == 's':
    num = int(input('Digite um número: '))
    pergunta = str(input('Deseja continuar? [S/N]: ')).lower()
    lista_numeros.append(num)
    avg = sum(lista_numeros) / len(lista_numeros)
print(f'A média dos números digitados é {avg}.\nO maior número é {max(lista_numeros)}.\nO menor número é {min(lista_numeros)}.')
