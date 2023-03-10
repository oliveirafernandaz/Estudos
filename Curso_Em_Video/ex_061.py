primeiro_termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
cont = 1

print(f'Os 10 primeiros termos dessa PA são: ', end = '')
while cont <= 10:
    termo = termo + razao
    cont = cont + 1
    print(termo, ' ', end = '')