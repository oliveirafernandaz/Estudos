import colorama
from colorama import Fore, Back, Style
import pandas as pd
from tabulate import tabulate

nomes = []
idades = []

def cadastro():
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    nomes.append(nome)
    idades.append(idade)
    global df
    df = pd.DataFrame({'Nomes': nomes, 'Idade': idades})
    return df

def menu():
    print('-'*30)
    principal = 'MENU PRINCIPAL'
    print(principal.center(30))
    print('-'*30)
    print(Fore.YELLOW + "1" + Fore.BLUE + " Ver pessoas cadastradas") 
    print(Fore.YELLOW + "2" + Fore.BLUE + " Cadastrar nova pessoa")
    print(Fore.YELLOW + "3" + Fore.BLUE + " Sair do sistema")
    print(Style.RESET_ALL)
    print('-'*30)

def salvar_csv():
    df.to_csv('fichas_df.csv', index=False)
    arquivo = pd.read_csv('fichas_df.csv')


def opcoes():
    while True:
        menu()
        try:
            opcao = int(input('Digite uma opção: '))
            print('-'*30)
            if opcao == 1:
                global df
                print(tabulate(df, headers='keys', tablefmt='psql'))
                continue
            elif opcao == 2:
                df = pd.DataFrame(cadastro())
                continue
            elif opcao != 1 and opcao != 2 and opcao != 3:
                print(f'Por favor, digite uma opção válida.')
                continue
            elif opcao == 3:
                fim = Fore.RED + 'FIM DO PROGRAMA'
                print('-'*30)
                print(fim.center(32))
                print(Style.RESET_ALL)
                salvar_csv()
                quit()
        except (ValueError, TypeError):
            print(f'Por favor, digite uma opção válida.')
            continue

print(opcoes())