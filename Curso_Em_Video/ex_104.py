num = input('Digite um número: ')

def leiaint():
    while True:
        global num
        if num.isnumeric():
            print(f'Você digitou o número {num}')
            break
        else:
            print('Erro! Digite um número válido')
            num = input('Digite um número: ')
            continue
            

leiaint()