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


c1 = ContaBancaria(id=145, nome="Rita", saldo=7550)
print(c1)
