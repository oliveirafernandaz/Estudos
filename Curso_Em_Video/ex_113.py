while True:
    try:
        num_int = int(input('Digite um número inteiro: '))
    except Exception:
        print('ERRO! Por favor digite um número inteiro válido')
        continue
    try:
        num_float = float(input('Digite um número real: '))
    except (ValueError, TypeError):
        print('ERRO! Por favor digite um número real válido')
        continue
    finally: 
        print(f'O valor inteiro digitado foi {num_int} e o valor real foi {num_float}')
        break
        