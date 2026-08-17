from abc import ABC, abstractmethod


class Pagamento(ABC):

    def __init__(self, valor: float):
        self._valor = valor  # Atributo protegido

    @property
    def fvalor(self) -> str:  # Adicionado o 'self' nos parâmetros
        """Formata o valor numérico em moeda BRL (R$)."""
        return (
            f"R$ {self._valor:,.2f}".replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

    @abstractmethod
    def pagar(self):
        """Método abstrato a ser implementado pelas subclasses."""
        pass


class Boleto(Pagamento):

    def pagar(self):
        print(
            f"Boleto gerado no valor de {self.fvalor}. Aguardando compensação bancária..."
        )


class Credito(Pagamento):

    def pagar(self):
        print(
            f"Pagamento de {self.fvalor} processado com sucesso no Cartão de Crédito!"
        )


class Pix(Pagamento):

    def pagar(self):
        print(
            f"Pagamento de {self.fvalor} efetuado via Pix com transferência instantânea!"
        )


# --- Simulação de Uso ---
if __name__ == "__main__":
    compras = [
        Boleto(150.50),
        Credito(1299.90),
        Pix(89.00),
    ]

    print("--- SIMULADOR DE PAGAMENTOS ---")
    for pagamento in compras:
        pagamento.pagar()