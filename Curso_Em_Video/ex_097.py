frase1 = 'Gustavo Guanabara'
frase2 = 'Curso de Python no YouTube'
frase3 = 'Curso em Vídeo'

def tamanho(fra):
    tamanho = len(fra) + 4
    print('~' * tamanho)
    print(f'  {fra}')
    print('~' * tamanho)


tamanho(frase1)
tamanho(frase2)
tamanho(frase3)