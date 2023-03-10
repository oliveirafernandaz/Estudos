largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

def calculo_area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno de {largura} x {comprimento} é {area}m².')

calculo_area(largura, comprimento)