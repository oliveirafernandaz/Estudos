termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
decimo = termo + (10 - 1) * razao
for i in range(termo, decimo, razao) : #primeiro termo, número até onde vai, intervalo
    print(i, end = ' ')
