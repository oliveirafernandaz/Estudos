sal = float(input('Qual o seu salário? '))
x = 1250
if sal > x :
    print(f'Seu novo salário será de R${(sal * 0.1) + sal:.2f}.')
if sal <= x :
    print(f'Seu novo salário de R${(sal * 0.15) + sal:.2f}.')
