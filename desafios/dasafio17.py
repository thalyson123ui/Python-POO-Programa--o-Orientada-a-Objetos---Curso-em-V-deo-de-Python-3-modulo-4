from rich import print
from rich.panel import Panel
from rich.text import Text


class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def etiqueta_preco(self):
        texto = Text()
        texto.append("Produto: ", style="bold cyan")
        texto.append(f"{self.nome}\n", style="bold white")
        texto.append("Preço: ", style="bold green")
        texto.append(f"R$ {self.preco:.2f}", style="bold yellow")

        painel = Panel(
            texto,
            title="Etiqueta de Preço",
            border_style="magenta",
            padding=(1, 4)
        )

        print(painel)


# --- Exemplo de uso ---
produto1 = Produto("Teclado Mecânico corsair", 299.90)
produto1.etiqueta_preco()
