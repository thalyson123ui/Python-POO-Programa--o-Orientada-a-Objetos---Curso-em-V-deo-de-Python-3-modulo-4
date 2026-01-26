from rich import print
from rich import inspect
inspect(int, all=True)

class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem saldo de R${self.saldo:.2f} reais"

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor de depósito inválido")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido")
        elif valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor


# teste
c1 = ContaBancaria(id=145, nome="Rita", saldo=7550)
c1.depositar(500)
c1.sacar(300)
print(c1)

c = ContaBancaria(id=200, nome="Carlos")
inspect(c)