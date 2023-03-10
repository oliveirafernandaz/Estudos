din = float(input('Quanto você vai pagar? R$'))
pag = float(input('Selecione uma opção: \n[1] À vista no dinheiro ou cheque \n[2] À vista no cartão \n[3] Parcelado em 2x no cartão \n[4] Parcelado em 3x ou mais \n'))

if pag == 1 :
    print(f'Você obteve R${din * 0.1:.2f} de desconto. Seu pagamento será de R${din - (din * 0.1):.2f}.')
elif pag == 2 :
    print(f'Você obteve R${din * 0.05:.2f} de desconto. Seu pagamento será de R${din - (din * 0.05):.2f}.')
elif pag == 3 :
    print(f'Você pagará 2 parcelas de R${din / 2:.2f}, com um total de R${din:.2f}.')
elif pag == 4 :
    par = int(input('Em quantas parcelas você quer pagar? (3x a 12x): '))
    jur = din * 0.2
    print(f'Você pagará {par} parcelas de R${(din + jur) / par:.2f}, com acréscimo de R${jur:.2f} de juros, totalizando R${din + jur}.')
else:
    print('Escolha uma opção válida, por favor')
