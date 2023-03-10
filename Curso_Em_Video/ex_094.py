infos = {}
lista_infos = []

while True:
    infos.clear()
    infos['nome'] = str(input('Nome: '))
    while True:
        infos['sexo'] = str(input('Sexo: [F/M] ')).upper()[0]
        if infos['sexo'] in 'FM':
            break
        print(f'ERRO! Digite apenas F ou M.')
    infos['idade'] = int(input('Idade: '))
    lista_infos.append(infos.copy())
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print(f'ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break

print('-=' * 30)
print(f'Ao todo temos {len(lista_infos)} pessoas cadastradas.')
sum_idade = sum(item['idade'] for item in lista_infos)
media_idade = sum_idade/len(lista_infos)
print(f'A idade média das pessoas é {media_idade:.1f}.')

mulheres = []
for item in lista_infos:
    if item['sexo'] == 'F':
        mulheres.append(item['nome'])
print(f'As mulheres dessa lista são: {mulheres}.')
print('As pessoas com idade acima da média são:')
acima_idade = []
for item in lista_infos:
    if item['idade'] > media_idade:
        print(f'      Nome: {item["nome"]}, Sexo: {item["sexo"]}, Idade: {item["idade"]};')
print('\n=== ENCERRADO ===')

