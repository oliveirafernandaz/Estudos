nota1 = float(input('Qual foi a sua primeira nota? '))
nota2 = float(input('Qual foi a sua segunda nota? '))
media = (nota1 + nota2) / 2

if media < 5.0 :
    print(f'Sua nota foi {media}. Você está reprovado.')
elif media >= 5.0 and media < 7 :
    print(f'Sua nota foi {media}. Você está de recuperação.')
else:
    print(f'Parabéns! Você está aprovado.')
