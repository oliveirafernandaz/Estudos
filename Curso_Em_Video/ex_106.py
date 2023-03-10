color = ('\033m', # 0 - semcor
        '\033[0;30;41m', # 1 - vermelho
        '\033[0;30;42m', # 2 - verde
        '\033[0;30;43m', # 3 - amarelo
        '\033[0;30;44m', # 4 - azul
        '\033[0;30;45m', # 5 - roxo
        '\033[0;30m' # 6 - branco
        );

def ajuda(funcao):
    titulo(f'Acessando o manual do comando \'{funcao}\'', 4)
    print(color[1], end='')
    help(funcao)
    print(color[0], end='')

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(color[cor], end='')
    print( '~' * tam)
    print(f'  {msg}')
    print( '~' * tam)
    print(color[0], end='')

comando = ''

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)