import time
num = float(input('Insira o primeiro número: '))
num2 = float(input('Insira o segundo número: '))

lista_numeros = []
lista_numeros.append(num)
lista_numeros.append(num2)
menu = 0

while menu != 5:  
    menu = int(input('Agora escolha uma das opções: \n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos Números \n[5] Sair do programa\n'))  
    if menu == 1:
        sum = num + num2
        print(f'A soma de {num} e {num2} é {sum}')
    elif menu == 2:
        mult = num * num2
        print(f'O resultado de {num} x {num2} é {mult}.')         
    elif menu == 3:
        print(f'O maior número informado é {max(lista_numeros)}')
    elif menu == 4:
        num = float(input('Insira o primeiro número: '))
        num2 = float(input('Insira o segundo número: '))
    elif menu == 5:
        quit()
    else:
        print('Insira uma opção válida')
    time.sleep(1)
    
