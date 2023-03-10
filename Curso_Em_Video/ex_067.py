num = float(input('Digite o número que deseja saber a tabuada: '))

while True:
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
    num = float(input('Digite o número que deseja saber a tabuada: '))
    if num < 0:
        break
print('Programa encerrado')