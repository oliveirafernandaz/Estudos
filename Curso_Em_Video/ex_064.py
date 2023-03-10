#num = int(input('Digite um número [999 para parar]: '))
lista_numeros = []
num = 0

while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    lista_numeros.append(num)
    if num == 999:
        sum = sum(lista_numeros)
        sum_999 = sum - 999
        print(f'A soma dos números é igual a {sum_999}.')