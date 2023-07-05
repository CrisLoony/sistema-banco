from math import floor
from time import sleep

from classes import Banco, Cliente, ContaCorrente, ContaPoupanca
from funcoes import clean_console, continuar, definindo_opcao

# Informções pessoais
nome_cliente = input('Insira o seu nome: ').strip().title()
idade_cliente = None
while not isinstance(idade_cliente, int):
    idade_cliente = input('Insira a sua idade: ').strip().title()
    idade_cliente = int(idade_cliente)

cliente = Cliente(nome_cliente, idade_cliente)
sleep(0.5)

print()
# Banco variáveis
banco_python_agencias = ['0256', '0136', '1654', '0475']
dev_banco_agencias = ['1426', '0075', '0987', '1541']
poo_banco_agencias = ['0045', '0068', '1412', '0698']

# Escolhendo Banco
print('Escolha um banco para se cadastrar:')
print('[1] Banco do Python')
print('[2] Dev Banco')
print('[3] POO Banco')

banco_opcoes = ['1', '2', '3']
opcao_banco = definindo_opcao(banco_opcoes)

print()
if opcao_banco == '1':
    # Banco Python
    banco = Banco('Banco do Python', banco_python_agencias)
    print('Agora, escolha a agência onde deseja se cadastrar: ')
    print(*banco_python_agencias)
    print()
    agencia = definindo_opcao(banco_python_agencias)

elif opcao_banco == '2':
    # Dev Banco
    banco = Banco('Dev Banco', dev_banco_agencias)
    print('Agora, escolha a agência onde deseja se cadastrar: ')
    print(*dev_banco_agencias)
    print()
    agencia = definindo_opcao(dev_banco_agencias)

else:
    # POO Banco
    banco = Banco('POO Banco', poo_banco_agencias)
    print('Agora, escolha a agência onde deseja se cadastrar: ')
    print(*poo_banco_agencias)
    print()
    agencia = definindo_opcao(poo_banco_agencias)

print()
# Escolher o tipo de conta
print('Escolha o tipo de conta que deseja criar:')
print('[1] Conta Poupança')
print('[2] Conta Corrente')
opcao_conta = definindo_opcao(['1', '2'])

if opcao_conta == '1':
    tipo_de_conta = 'Conta Poupança'
    conta_cliente = ContaPoupanca()
else:
    tipo_de_conta = 'Conta Corrente'
    conta_cliente = ContaCorrente()

banco.cadastrar_cliente(cliente, agencia, tipo_de_conta)

print(f'O cliente {cliente.nome} foi cadastrado com sucesso')
sleep(1)
clean_console()

while True:

    print('O que deseja fazer com sua conta: ')
    print('[1] Ver detalhes')
    print('[2] Depositar')
    print('[3] Sacar')

    acao = definindo_opcao(['1', '2', '3'])
    print()

    if acao == '1':
        print('Você escolheu "Ver detalhes"')
        sleep(0.2)
        print('Estamos acessando as informações no sistema...')
        sleep(0.5)
        banco.detalhes(cliente)
        print()
        if continuar():
            clean_console()
            continue
        else:
            break

    elif acao == '2':
        print('Você escolheu "Depositar"')
        sleep(0.2)
        valor = None
        print('Insira o valor que deseja depositar: ')

        while not isinstance(valor, float):
            valor = input('>>> R$ ').strip()
            valor = valor.replace(',', '.')
            valor = float(valor)

        try:
            conta_cliente.depositar(cliente, valor)
            print('O valor foi depositado com sucesso!')
        except:
            print(
                'Não foi possível depositar o valor solicitado, verifique se foi inserido corretamente.')
        print()

        if continuar():
            clean_console()
            continue
        else:
            break

    else:
        print('Você escolheu "Sacar"')
        sleep(0.2)
        valor = None
        print('Obs.: Não é possível sacar moedas, por favor insira um valor inteiro.')
        print('Insira o valor que deseja sacar: ')

        while not isinstance(valor, int):
            valor = input('>>> R$ ').strip()
            valor = valor.replace(',', '.')
            try:
                valor = float(valor)
                valor = floor(valor)
            except:
                print('O valor inserido é inválido, tente novamente!')

        if conta_cliente.sacar(cliente, banco, valor):
            print('Saque realizado com sucesso')
        else:
            print(
                'Não foi possível sacar, verifique seu saldo ou as informações inseridas.')
        print()

        if continuar():
            clean_console()
            continue
        else:
            break

sleep(0.5)
clean_console()
print('Seu atendimento foi encerrado, volte sempre!')
clean_console()
