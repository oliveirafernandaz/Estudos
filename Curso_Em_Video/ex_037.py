n = int(input('Digite um número inteiro: '))
q = int(input('Agora, escolha uma base de conversão: \n[1] Binário \n[2] Octal \n[3] Hexadecimal \nDigite aqui: '))

if q == 1 :
    print(f'O número {n} em base binária é {bin(n)}.')
elif q == 2 :
    print(f'O número {n} em base octal é {oct(n)}.')
elif q == 3 :
    print(f'O número {n} em base hexadecimal é {hex(n)}.')
else :
    print('Por favor, digite um número entre 1 e 3.')
