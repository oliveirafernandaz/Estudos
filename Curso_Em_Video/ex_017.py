from math import hypot
co = float(input('Insira o valor do cateto oposto: '))
ca = float(input('Insira o valor do cateto adjacente: '))
hp = (hypot(co,ca))

print(f'O valor da hipotenusa é {hp:.2f}')
