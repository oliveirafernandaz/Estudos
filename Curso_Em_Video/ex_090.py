nome = str(input('Digite o nome do aluno: '))
media = float(input('Digite a média: '))

aluno = {}
aluno['nome'] = nome
aluno['média'] = media

print(f'O nome do aluno é {aluno["nome"]}.')
print(f'A média de {aluno["nome"]} é {aluno["média"]}.')

if aluno['média'] < 5:
    print(f'O aluno {aluno["nome"]} está reprovado.')
if aluno['média'] > 5 and aluno['média'] < 7:
    print(f'O aluno {aluno["nome"]} está em recuperação.')
if aluno['média'] >= 7:
    print(f'O aluno {aluno["nome"]} está aprovado. Parabéns!')