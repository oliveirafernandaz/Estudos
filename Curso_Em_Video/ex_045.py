import random
jogo = int(input('Escolha uma opçao \n[1] Pedra \n[2] Papel \n[3] Tesoura \nDigite aqui: '))

#gam = random.choice([pedra, papel, tesoura])

options = {
        'PEDRA!' : 1,
        'PAPEL!' : 2,
        'TESOURA!' : 3
    }

gam = random.choice(list(options.values()))
print(gam)

if jogo == 1 : #PEDRA
    if gam == 1 :
        print('O computador escolheu PEDRA! O jogo empatou!')
    elif gam == 2 :
        print('O computador escolheu PAPEL! Você perdeu!')
    elif gam == 3 :
        print('O computador escolheu TESOURA! Você ganhou!')

if jogo == 2 : #PAPEL
    if gam == 1 :
        print('O computador escolheu PEDRA! Você ganhou!')
    elif gam == 2 :
        print('O computador escolheu PAPEL! O jogo empatou!')
    elif gam == 3 :
        print('O computador escolheu TESOURA! Você perdeu!')

if jogo == 3 : #TESOURA
    if gam == 1 :
        print('O computador escolheu PEDRA! Você perdeu!')
    elif gam == 2 :
        print('O computador escolheu PAPEL! Você ganhou!')
    elif gam == 3 :
        print('O computador escolheu TESOURA! O jogo empatou!')
