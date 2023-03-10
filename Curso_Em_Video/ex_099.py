def analisar(*num):
    lista_valores = list(num)
    print('=-' * 30)
    if len(lista_valores) == 0:
        print(f'Foram informados ao todo 0 valores.')
        print(f'O maior valor informado foi 0')
    else:
        print(f'Foram informados ao todo {len(lista_valores)} valores: {num}.')
        print(f'O maior valor informado foi {max(lista_valores)}')
    print('=-' * 30)

analisar(1, 2, 4, 5, 6)
analisar (8, 90, 40, 76, 22)
analisar(76, 45, 83, 15, 3, 0)
analisar()