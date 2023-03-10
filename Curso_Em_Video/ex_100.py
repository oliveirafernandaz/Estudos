import random

valores = list(range(1, 11))

def sortear():
    par = []
    for i in valores:
        if i % 2 == 0:
            par.append(i)
    sorteados = list(random.sample(par, k = 5))
    print(f'Os valores sorteados foram {sorteados}.')
    return sorteados

def soma():
    sum_sorteados = sum(sortear())
    print(f'A soma dos números sorteados foi {sum_sorteados}.')

soma()
