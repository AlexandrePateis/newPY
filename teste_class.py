from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self.nome

    @property
    def idade(self):
        return self.idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, ):
        super().__init__(nome, idade)
        self.conta = None

    def inserir_conta(self, conta):
        self.conta = conta


class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agencia: {self.agencia}')
        print(f'Conta: {self.numero}')
        print(f'Saldo: R${self.saldo}')

    @abstractmethod
    def sacar(self, valor): pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Não é possivel sacar esse valor.')
            return
        self.saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo, limite=100):
        super().__init__(agencia, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente !!')
            return
        self.saldo -= valor
        self.detalhes()


class Banco:
    def __init__(self):
        self.agencias = [111, 222, 333]
        self.clientes = []
        self.contas = []

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False
        if cliente.numero not in self.contas:
            return False
        if cliente.numero.agencia not in self.agencias:
            return False
        return True


banco = Banco()
cliente1 = Cliente('Alexandre', 22)
cliente2 = Cliente('Julia', 42)

conta1 = ContaPoupanca(111, 25, 0)
conta2 = ContaCorrente(222, 48, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)

cliente1.conta.sacar(20)
cliente1.conta.depositar(500)
cliente1.conta.sacar(20)
