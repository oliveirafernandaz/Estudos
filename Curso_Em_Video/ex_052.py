import math
num = int(input('Insira um número: '))
flag = False

if num > 1:
    for i in range(1, num + 1,):
        #print(i, end = ' ')
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "não é um número primo.")
else:
    print(num, "não é um número primo.")
