v = float(input('Qual a velocidade do seu carro? '))
m = (v-80) * 7
if v > 80 :
    print(f'Seu carro será multado em R${m:.2f}.')
else:
    print('Não há multas para seu carro.')
