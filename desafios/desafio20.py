from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


class Gamer:
    def __init__(self, nome: str, nick: str, jogos_favoritos: list[str]):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = jogos_favoritos

    def mostrar_ficha(self):
        tabela = Table(show_header=True, header_style="bold cyan")
        tabela.add_column("Campo", style="bold magenta")
        tabela.add_column("Informação", style="green")

        tabela.add_row("Nome", self.nome)
        tabela.add_row("Nick", self.nick)
        tabela.add_row(
            "Jogos Favoritos",
            ", ".join(self.jogos_favoritos) if self.jogos_favoritos else "Nenhum"
        )

        painel = Panel(
            tabela,
            title="🎮 Ficha do Gamer",
            border_style="bright_blue"
        )

        console.print(painel)


# ===== Exemplo de uso =====
gamer1 = Gamer(
    nome="Thalyson",
    nick="DarkPlayer",
    jogos_favoritos=["Minecraft", "super-mario", "GTA V"]
)

gamer1.mostrar_ficha()
