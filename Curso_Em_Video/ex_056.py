lst_idade = []
lst_nam = []
lst_sex = []
mulher = 0

for i in range(1, 5):
    nome = str(input('\nNome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo F/M: '))
    #stridade = str(idade)
    lst_nam.append(nome)
    lst_idade.append(idade)
    lst_sex.append(sexo)

    if idade < 20 and sexo in 'Ff':
        mulher += 1
print(f'Existem {mulher} mulheres com menos de 20 anos.')

idlist = []
zipped = list(zip(lst_nam, lst_idade, lst_sex))
for n, id, s in zipped:
    idlist.append(id)
    maxid = max(idlist)
    if id == maxid and s in 'Mm':
        print(f'O homem com a maior idade se chama {n}.')

print(f'A idade média é de {sum(lst_idade)/len(lst_idade):.0f} anos.')
