from os import system


def clean_console():
    system('cls') or None


def definindo_opcao(lista_de_opcoes: list):
    opcao = None
    while opcao not in lista_de_opcoes:
        opcao = input('Insira sua escolha aqui: ')
    return opcao


def continuar():
    prosseguir = None
    while prosseguir not in ['S', 'N']:
        prosseguir = input('Deseja continuar [S/N]: ').strip().upper()

    if prosseguir == 'S':
        return True
    return False
