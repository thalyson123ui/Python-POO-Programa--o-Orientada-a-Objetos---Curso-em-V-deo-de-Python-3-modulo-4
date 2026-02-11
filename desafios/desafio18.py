from rich.console import Console
from rich.panel import Panel
from rich.table import Table

class Churrasco:
    def __init__(self, pessoas: int, preco_kg: float):
        self.pessoas = pessoas
        self.consumo_por_pessoa = 0.4  # kg
        self.preco_kg = preco_kg

    def total_carne(self) -> float:
        return self.pessoas * self.consumo_por_pessoa

    def custo_total(self) -> float:
        return self.total_carne() * self.preco_kg

    def preco_por_pessoa(self) -> float:
        return self.custo_total() / self.pessoas

    def mostrar_relatorio(self):
        console = Console()

        tabela = Table(title="🍖 Relatório do Churrasco", show_lines=True)

        tabela.add_column("Descrição", style="cyan", justify="left")
        tabela.add_column("Valor", style="green", justify="right")

        tabela.add_row("Pessoas", str(self.pessoas))
        tabela.add_row("Carne total (kg)", f"{self.total_carne():.2f} kg")
        tabela.add_row("Custo total", f"R$ {self.custo_total():.2f}")
        tabela.add_row("Preço por pessoa", f"R$ {self.preco_por_pessoa():.2f}")

        painel = Panel(tabela, title="🔥 Churrasco Planejado", border_style="red")

        console.print(painel)


# -------------------------------
# Execução do programa
# -------------------------------
if __name__ == "__main__":
    console = Console()

    console.print("[bold yellow]Planejador de Churrasco[/bold yellow]\n")

    pessoas = int(input("Quantas pessoas vão participar? "))
    preco_kg = float(input("Qual o preço do kg da carne? R$ "))

    churrasco = Churrasco(pessoas, preco_kg)
    churrasco.mostrar_relatorio()
