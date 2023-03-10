from datetime import date
lista_menor = []
lista_maior = []
c_date = date.today()
c_year = c_date.year

for ano in range(1, 8):
    ano = int(input(f'Em que ano a {ano}° pessoa nasceu? '))
    age = c_year - ano
    if age < 18:
        lista_menor.append(age)
    if age >= 18:
        lista_maior.append(age)

print(f'\nExistem {len(lista_menor)} pessoas menores de idade e {len(lista_maior)} pessoas maiores de idade.')
