l = []
x = 3
for num in range(x) :
    num = input('Digite um número: ')
    l.append(num)
print(f'O maior número digitado foi {max(l)}.')
print(f'O menor número digitado foi {min(l)}.')
