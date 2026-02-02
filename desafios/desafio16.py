from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


class Funcionario:
    def __init__(self, nome: str, setor: str, cargo: str):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        texto = Text()
        texto.append("👤 Funcionário\n\n", style="bold cyan")
        texto.append(f"Nome: ", style="bold yellow")
        texto.append(f"{self.nome}\n", style="white")

        texto.append(f"Setor: ", style="bold green")
        texto.append(f"{self.setor}\n", style="white")

        texto.append(f"Cargo: ", style="bold magenta")
        texto.append(f"{self.cargo}", style="white")

        painel = Panel(
            texto,
            title="Apresentação",
            border_style="blue",
            expand=False
        )

        console.print(painel)


# ===== Exemplo de uso =====
funcionario1 = Funcionario(
    nome="Thalyson",
    setor="Tecnologia",
    cargo="Desenvolvedor Python"
)

funcionario1.apresentar()
