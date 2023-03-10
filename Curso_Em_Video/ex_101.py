from datetime import date

nascimento = int(input('Em que ano você nasceu? '))

def votacao(ano):
    ano_atual = date.today().year
    idade = ano_atual - nascimento
    if idade >= 18 and idade <= 65:
        print(f'Com {idade} anos: Voto obrigatório!')
    elif idade >= 16 and idade < 18 or idade > 65:
        print(f'Com {idade} anos: Voto opcional.')
    else:
        print(f'Com {idade} anos: Voto proibido')
        
votacao(nascimento)