total_notas = []
boletim = []

while True:
    nome = str(input('Nome do aluno: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    cont = 0
    while cont <= 0:
        cont += 1
        media = nota1 + nota2 / 2
        total_notas.append(nome)
        total_notas.append(nota1)
        total_notas.append(nota2)
        total_notas.append(media)
    boletim.append(total_notas[:])
    total_notas.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).lower().strip()[0]
    while continuar not in 'sn':
        print('Por favor, digite uma opção válida: S/N ')
        continuar = str(input('Deseja continuar? [S/N]: ')).lower().strip()[0]
        if continuar == 's':
            continue
    if continuar == 'n':
        break

print('=-' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 26)

for i, l in enumerate(boletim):
    print(f'{i:<3} {l[0]:<10} {l[3]:>6.1f}')

print('=-' * 30)

while True:
    notas = int(input('Deseja saber a nota de qual aluno? (999 interrompe): '))
    if notas == 999:
        print('Finalizando...')
        break
    if notas <= len(boletim) - 1:
        print(f'As notas de {boletim[notas][0]} foram {boletim[notas][1]} e {boletim[notas][2]}.')

print('=-' * 30)
print(f'{"VOLTE SEMPRE!"}')
