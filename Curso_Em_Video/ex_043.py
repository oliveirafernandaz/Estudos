peso = float(input('Qual seu peso? '))
alt = float(input('Qual sua altura? '))
imc = peso / (alt * alt)

if imc < 18.5 :
    print(f'Seu IMC é {imc:.1f} e você está abaixo do peso.')
elif imc < 25 :
    print(f'Seu IMC é {imc:.1f} e você está no peso ideal.')
elif imc < 30 :
    print(f'Seu IMC é {imc:.1f} e você está com sobrepeso.')
elif imc < 40 :
    print(f'Seu IMC é {imc:.1f} e você está com obesidade.')
elif imc >= 40 :
    print(f'Seu IMC é {imc:.1f} e você está com obesidade mórbida.')
