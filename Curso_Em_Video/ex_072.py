numero = int(input('Digite um número entre 0 e 20: '))

while numero > 20 or numero < 0:
    numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))

tuple_numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 
'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 
'dezenove', 'vinte')

numero = tuple_numeros[numero]

print(f'O número por extenso é {numero}.')