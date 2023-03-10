comida = ['Mamão', 'Abacate', 'Limão', 'Cenoura', 'Batata', 'Alface', 'Inhame']
valores = [7, 5, 2, 5, 7.5, 0.99, 8.79, 10]

zipped = list(zip(comida, valores))
print('=' * 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('=' * 30)
for c, v in zipped:
    print(f'{c} {".....":.>15} R$ {(float(v)):.2f}')