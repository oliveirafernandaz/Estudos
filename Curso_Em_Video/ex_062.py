import time
primeiro_termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
cont = 1
total = 0
pergunta = 10

print(f'Os 10 primeiros termos dessa PA são: ', end = '')
while pergunta != 0:
    total = total + pergunta
    while cont <= total:
        termo = termo + razao
        cont = cont + 1
        print(termo, ' ', end = '')
    pergunta = int(input('\nQuantos termos deseja acrescentar? '))
print('FIM')
