valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = float(input('Em quantos anos você quer pagar? '))
mensal = valor / (anos * 12)

if mensal > 0.3 * salario :
    print(f'Empréstimo negado! A prestação de R${mensal:.2f} excede 30% do seu salário.')
else :
    print(f'Empréstimo aprovado! A prestação mensal será de R${mensal:.2f}')
