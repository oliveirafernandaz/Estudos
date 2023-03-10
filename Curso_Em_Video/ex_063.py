num = int(input('Insira quantos termos você deseja: '))
cont = 3
t1 = 0
t2 = 1
print(t1, t2, ' ', end='')
while cont < num:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
    print(t3, ' ', end = '')
print('\nFIM')