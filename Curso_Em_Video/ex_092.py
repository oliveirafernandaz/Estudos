from datetime import date

infos = {}
infos['Nome'] = str(input('Nome: '))
infos['Nascimento'] = int(input('Ano de nascimento: '))
infos['Carteira'] = int(input('CTPS (0 = não tem): '))

if infos['Carteira'] != 0:
    infos['Contratacao'] = int(input('Ano de contratação: '))
    infos['Salario'] = float(input('Salário: R$'))
    ano_atual = date.today().year
    idade_trabalho = ano_atual - infos['Nascimento']
    idade_aposentadoria = idade_trabalho + 30
    print('=-' * 30)
    for k, v in infos.items():
        print(f'    {k} tem valor {v}.')
print(f'    Idade: {(infos["Nascimento"] - ano_atual) * -1}')
print(f'    {infos["Nome"]} irá se aposentar aos {idade_aposentadoria} anos.')
if infos['Carteira'] == 0:
    print('=-' * 30)
    for k, v in infos.items():
        print(f'    {k} tem valor {v}.')
    print(f'Idade: {(infos["Nascimento"] - ano_atual) * -1}')