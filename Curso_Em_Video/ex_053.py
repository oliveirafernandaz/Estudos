frase = str(input('Escreva uma frase: '))
space = frase.replace(' ', '')
reverse = space[::-1]
print(f'O inverso de {space.upper()} é {reverse.upper()}.')

if space == reverse:
    print('Sua frase é um palíndromo.')
else:
    print('Sua frase não é um palíndromo.')
