pn = int(input('Digite o primeiro número: '))
sn = int(input('Digite o segundo número: '))

if pn > sn :
    print(f'O primeiro número {pn} é maior que o segundo {sn}.')
elif sn > pn :
    print(f'O segundo número {sn} é maior que o primeiro {pn}.')
else :
    print(f'Não existe valor maior, os dois números são iguais.')
