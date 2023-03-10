cont = homem = mulher = 0

while True:
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    continuar = ' '
    while sexo not in 'fm':
        sexo = str(input('Sexo [F/M]: ')).strip().lower()[0]
    if idade > 18:
        cont += 1
    if sexo == 'm':
        homem += 1
    if sexo == 'f' and idade < 20:
        mulher += 1
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    if continuar == 'n':
        break
print('-' * 30)
print(f'O total de pessoas com mais de 18 anos é: {cont}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher} mulher com menos de 20 anos.')