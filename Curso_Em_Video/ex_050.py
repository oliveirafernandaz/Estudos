sum = 0
cont = 0
for i in range(1, 7) :
    num = (int(input((f'Digite o {i}° número inteiro: '))))
    if num % 2 == 0 :
        sum += num
        cont += 1
print(f'A soma dos {cont} números pares inseridos é {sum}.')
