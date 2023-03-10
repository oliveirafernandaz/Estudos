d = float(input('Para calcular o valor preciso da distância até o poonro de chegada (em km): '))
if d <= 200:
    p1 = d * 0.50
    print(f'O valor da sua passagem será R${p1}')
else:
    p2 = (d -200)* 0.50
    print(f'O valor da passagem será R${p2}')
