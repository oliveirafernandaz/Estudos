from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print(f'O atleta tem {idade} anos.')

if idade <= 9 :
    print('O atleta faz parte da categoria mirim.')
elif idade > 9 and idade <= 14 :
    print('O atleta faz parte da categoria infantil.')
elif idade > 14 and idade <= 19 :
    print('O atleta faz parte da categoria júnior.')
elif idade > 19 and idade <= 25 :
    print('O atleta faz parte da categoria sênior.')
else :
    print('O atleta faz parte da categoria master.')
