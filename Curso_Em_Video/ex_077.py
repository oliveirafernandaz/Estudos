palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for i in palavras:
    print(f'\nAs vogais de {i} são: ', end='')
    for l in i:
        if l in 'AEIOU':
            print(f'{l} ', end ='')

