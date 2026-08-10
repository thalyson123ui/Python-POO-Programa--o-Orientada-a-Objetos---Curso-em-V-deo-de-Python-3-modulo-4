class Carteira:

    def __init__(self, valor: int | float = 0):
        self.__saldo = float(valor)

    def __str__(self):
        return f"Você tem R${self.__saldo:,.2f} na sua carteira"

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, _valor):
        raise PermissionError(
            "Você não tem autorização para alterar o saldo diretamente. "
            "Utilize os operadores para alterar o saldo."
        )

    def __eq__(self, other):
        if isinstance(other, Carteira):
            return self.__saldo == other.__saldo
        return False

    def __iadd__(self, valor):
        if isinstance(valor, (int, float)):
            self.__saldo += valor
        else:
            raise TypeError("O valor deve ser um número inteiro ou decimal")
        return self  # Deve retornar self, não self.saldo

    def __isub__(self, valor):
        if isinstance(valor, (int, float)):
            self.__saldo -= valor
        else:
            raise TypeError("O valor deve ser um número inteiro ou decimal")
        return self  # Deve retornar self, não self.saldo