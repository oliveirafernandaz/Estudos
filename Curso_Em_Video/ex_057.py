sexo = str(input('Digite seu sexo [M ou F]: ')).strip()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Digite seu sexo [M ou F]: ')).strip()
print(f'Sexo {sexo} registrado com sucesso.')
