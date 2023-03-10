from time import sleep

def contagem(inicio, final, intervalo):
    if intervalo < 0:
        intervalo *= - 1
    if intervalo == 0:
        intervalo = 1
    print(f'Contagem de {inicio} até {final} de {intervalo} em {intervalo}')
    if inicio < final:
        for x in range(inicio, final, intervalo):
            print(f'{x} ', end ='', flush = True)
            sleep(0.5)
        print(f'FIM!')
    if final < inicio:
        lista_contagem = []
        for y in range(final, inicio, intervalo):
            lista_contagem.append(y)
            lista_reversa = reversed(lista_contagem)
            nova_lista_reversa = list(lista_reversa)
        for t in nova_lista_reversa:
            print(f'{t} ', end ='', flush = True)
            sleep(0.5)
        print(f'FIM!')

contagem(1, 11, 1)
print('=-' * 30)
contagem(10, 0, 2)
print('=-' * 30)
print(f'Agora é sua vez!')
i = int(input('Início: '))
f = int(input('Fim: '))
t = int(input('Intervalo: '))
contagem(i, f, t)