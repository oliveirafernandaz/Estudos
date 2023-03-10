p = int(input('Digite o primeiro seguimento: '))
s = int(input('Digite o segundo seguimento: '))
t = int(input('Digite o terceiro seguimento: '))

if p + s > t or t + p > s or s + t > p :
    if p == s == t == p :
        print('É possível formar um triângulo equilátero.')
    elif p == s or s == t or t == p :
        print('É possível formar um triângulo isósceles.')
    elif p != s != t != p :
        print('É possível formar um triângulo escaleno.')
    #print('É possível formar um triângulo com os valores informados')
else :
    print('Não é possível formar um triângulo com os valores informados')
