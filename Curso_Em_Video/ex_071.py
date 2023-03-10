valor = float(input('Qual valor você deseja sacar? R$'))
print(f'Total de {int(valor/100)} cédulas de R$100')
valor = valor % 100
#print(valor)

while True:
    while valor != 0:
        print(f'Total de {int(valor/50)} cédulas de R$50')
        valor = valor % 50
        #print(valor)
        while valor != 0:
            print(f'Total de {int(valor/20)} cédulas de R$20')
            valor = valor % 20
            #print(valor)
            while valor != 0:
                print(f'Total de {int(valor/10)} cédulas de R$10')
                valor = valor % 10
                #print(valor)
                while valor != 0:
                    print(f'Total de {int(valor/5)} cédulas de R$5')
                    valor = valor % 5
                    #print(valor)
                    while valor != 0:
                        print(f'Total de {int(valor/2)} cédulas de R$2')
                        valor = valor % 2
                        #print(valor)
                        if valor == 0:
                            print('Saque concluído.')
                            break
print('\nObrigada!')