from abc import ABC, abstractmethod
from random import choice


class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
        self._saldo = 0
        self._banco = None
        self._agencia = None
        self._tipo_de_conta = None
        self._numero_da_conta = None

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @property
    def banco(self):
        return self._banco

    @banco.setter
    def banco(self, nome_do_banco: str):
        self._banco = nome_do_banco

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, agencia: str):
        self._agencia = agencia

    @property
    def tipo_de_conta(self):
        return self._tipo_de_conta

    @tipo_de_conta.setter
    def tipo_de_conta(self, tipo_de_conta: str):
        self._tipo_de_conta = tipo_de_conta

    @property
    def numero_da_conta(self):
        return self._numero_da_conta

    @numero_da_conta.setter
    def numero_da_conta(self, numero_da_conta: str):
        self._numero_da_conta = numero_da_conta


class TipoDeContaInvalido(Exception):
    def __init__(self, menssagem):
        super().__init__(menssagem)


class Banco:
    def __init__(self, nome_do_banco: str, agencias: list):
        self.nome_do_banco = nome_do_banco
        self.agencias = agencias
        self.clientes = []
        self._numeros_conta_poupanca = []
        self._numeros_conta_corrente = []

    def cadastrar_cliente(self, cliente: Cliente, agencia: str, tipo_de_conta: str):
        self.clientes.append(cliente)
        cliente.banco = self.nome_do_banco
        cliente.agencia = agencia

        # Cadastrar o tipo da conta
        tipos_de_conta = ['Conta Poupança', 'Conta Corrente']
        if tipo_de_conta in tipos_de_conta:
            cliente.tipo_de_conta = tipo_de_conta
        else:
            raise TipoDeContaInvalido(
                'Verifique se o tipo de conta inserido é Conta Poupança ou Conta Corrente.')

        # Criar o número da conta
        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        numero_da_conta = ''
        for _ in range(7):
            numero = choice(numeros)
            numero_da_conta += numero

        # Inserindo o numero da conta na lista equivalente
        if tipo_de_conta == 'Conta Poupança':
            self._numeros_conta_poupanca.append(numero_da_conta)
        else:
            self._numeros_conta_corrente.append(numero_da_conta)

        cliente.numero_da_conta = numero_da_conta

    def autenticar_cliente(self, cliente: Cliente):
        if cliente in self.clientes:
            return True
        return False

    def autenticar_tipo_conta_poupanca(self, cliente: Cliente):
        if cliente.tipo_de_conta == 'Conta Poupança':
            return True
        return False

    def autenticar_tipo_conta_corrente(self, cliente: Cliente):
        if cliente.tipo_de_conta == 'Conta Corrente':
            return True
        return False

    def autenticar_numero_da_conta(self, cliente: Cliente):
        if self.autenticar_tipo_conta_poupanca(cliente):
            if cliente.numero_da_conta in self._numeros_conta_poupanca:
                return True
            else:
                return False
        elif self.autenticar_tipo_conta_corrente(cliente):
            if cliente.numero_da_conta in self._numeros_conta_corrente:
                return True
            else:
                return False

    def detalhes(self, cliente: Cliente):
        print(f'Nome: {cliente.nome}\nAgência: {cliente.agencia}\nTipo de Conta: {cliente.tipo_de_conta}\nNúmero da Conta: {cliente.numero_da_conta}\nSaldo: {cliente.saldo}')


class Conta(ABC):

    @abstractmethod
    def sacar(self, cliente: Cliente, banco: Banco, saque: int):
        pass

    def depositar(self, cliente: Cliente, valor: float):
        cliente.saldo += valor


class ContaPoupanca(Conta):
    def __init__(self):
        super().__init__()

    def sacar(self, cliente: Cliente, banco: Banco, saque: int):
        if banco.autenticar_cliente(cliente) and banco.autenticar_tipo_conta_poupanca(cliente) and banco.autenticar_numero_da_conta(cliente):
            if cliente.saldo > 1 and saque <= cliente.saldo:
                cliente.saldo -= saque
                return True
        else:
            return False


class ContaCorrente(Conta):
    def __init__(self):
        super().__init__()
        self.valor_extra = 1000

    def sacar(self, cliente: Cliente, banco: Banco, saque: int):
        if banco.autenticar_cliente(cliente) and banco.autenticar_tipo_conta_corrente(cliente) and banco.autenticar_numero_da_conta(cliente):
            if cliente.saldo > 1 and saque <= cliente.saldo:
                cliente.saldo -= saque
                return True
            else:
                print('Seu saldo é: R$0,00')
                print('Iniciando empréstimo pessoal...')
                cliente.saldo += 1000
                print('Seu saldo é: R$1000,00.')
                print('O saque será realizado agora...')
                if saque <= cliente.saldo:
                    cliente.saldo -= saque
                    return True
                else:
                    return False
        else:
            return False
