lista_nome = []
lista_peso = []

while True:
    nome = str(input('Digite o nome: '))
    peso = float(input('Digite o peso: '))
    continuar = str(input('Deseja continuar: [S/N]: ')).strip().lower()[0]
    lista_nome.append(nome)
    lista_peso.append(peso)
    zipped = zip(lista_nome, lista_peso)
    lista_zipped = list(zipped)
    max_peso = max(lista_peso)
    min_peso = min(lista_peso)
    nome_max = []
    nome_min = []
    peso_max = []
    peso_min = []
    for n, p in lista_zipped:
        if p == max_peso:
            peso_max.append(p)
            nome_max.append(n)
        if p == min_peso:
            peso_min.append(p)
            nome_min.append(n)
    if continuar == 's':
        continue
    if continuar == 'n':
        break

print(f'O total de pessoas cadastradas foram {len(lista_nome)}.')
print(f'As pessoas com maior peso de chamam {nome_max} e pesam {peso_max[0]}kg cada uma.')
print(f'As pessoas com menor peso se chamam {nome_min} e pesam {peso_min[0]}kg cada uma.')