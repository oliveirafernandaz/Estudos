import random

def sortear():
    valores = random.sample(range(1, 11), k = 5)
    print(f'A lista sorteada foi {valores}.')
    return valores

def soma():
    sum_sorteados = []
    for i in sortear():
        if i % 2 == 0:
            sum_sorteados.append(i)
    soma = sum(sum_sorteados)
    print(f'A soma dos números sorteados foi {soma}.')

soma()
