nam = str(input('Escreva seu nome: ')).strip()
mai = nam.upper()
min = nam.lower()
rep = nam.replace(' ', '')
len = len(rep)
fnam = nam.find(' ')


print(f'Seu nome em letras maiúsculas é {mai}')
print(f'Seu nome em letras minúsculas é {min}')
print(f'Seu nome tem um total de {len} letras')
print(f'O total de letras do seu primeiro nome é {fnam}')
