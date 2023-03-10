year = int(input('Escreva um ano qualquer: '))
from calendar import isleap
leap = isleap(year)

print(f'O ano {year} é bissexto.' if leap is True else print(f'O ano {year} não é bissexto.'))
#if leap is True:
#    print(f'O ano {year} é bissexto.')
#else:
#    print(f'O ano {year} não é bissexto.')
