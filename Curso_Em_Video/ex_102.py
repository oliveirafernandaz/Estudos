def fatorial(num, bol_num=0):
    """_summary_
    Calcula o fatorial de um número
    Args:
        num (int): número a ser calculado
        bol_num (int, optional): Mostra ou não a equação por extenso. Defaults to 0.
    """
    fact = 1
    for i in range(num, 0, -1):
        print(i, end='')
        if i > 1:
            print(' x ', end ='')
        else:
            print(' = ', end='')
        fact *= i
    print(fact)

fatorial(5, bol_num=True)