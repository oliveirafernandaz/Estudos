times = ('Fluminense', 'Fortaleza', 'Goiás', 'Fortaleza',
         'América-MG', 'Athletico', 'Palmeiras', 'Santos', 
         'São Paulo', 'Atlético-GO', 'Atlético-MG', 'Avaí', 
         'Botafogo', 'Bragantino',
         'Ceará', 'Corinthians', 'Coritiba', 'Cuiabá', 'Flamengo',
         'Internacional')

print(f'Os times do Campeonato Brasileiro 2022 são:\n{times}')
print('=' * 70)
print(f'Os 5 primeiros colocados são:\n{times[:5]}')
print('=' * 70)
print(f'Os 4 últimos colocados são:\n{times[-4:]}')
print('=' * 70)
print(f'Os times em ordem alfabética são:\n{sorted(times)}')
print('=' * 70)
posicao = times.index('Goiás')
print(f'O time na Goiás está na {posicao + 1}º posição.')
