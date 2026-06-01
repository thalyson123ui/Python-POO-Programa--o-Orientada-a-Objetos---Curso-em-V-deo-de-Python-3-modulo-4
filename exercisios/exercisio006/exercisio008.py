class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self._titular = nome
        self.__saldo = saldo

    def __str__(self):
        return f"A conta {self.id} de {self._titular} tem saldo de R${self.__saldo:.2f} reais"

    def depositar(self, valor):
        valor = abs(valor)
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor de depósito inválido")

    def sacar(self, valor):
        valor = abs(valor)
        if valor <= 0:
            print("Valor de saque inválido")
        elif valor > self.__saldo:
            print("Saldo insuficiente")
        else:
            self.__saldo -= valor



