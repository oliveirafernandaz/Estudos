expressao = str(input('Digite a expressão: '))
lista_expressao = list(expressao)

lista_parenteses = []

for i in lista_expressao:
    if i == '(':
        lista_parenteses.append('(')
    elif i == ('('):
        if len(lista_parenteses) > 0:
            lista_parenteses.pop()
        else:
            lista_parenteses.append(')')
            break
    
if len(lista_parenteses) == 0:
    print('Sua expressão é valida!')
else:
    print('Sua expressão não é válida.')
