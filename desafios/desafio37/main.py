from rich.console import Console
from rich.panel import Panel

console = Console()

class Mensagem:
    def __init__(self, mensagem: str, tipo: str, icone: str):
        # Atributos protegidos (# no UML)
        self._mensagem = mensagem
        self._tipo = tipo
        self._icone = icone

    def mostrar(self):
        # Renderiza a mensagem dentro de um painel estilizado do Rich
        console.print(
            Panel(
                f"{self._icone} {self._mensagem}",
                title=f"[bold]{self._tipo}[/bold]",
                border_style="white",
                expand=False
            )
        )

class Erro(Mensagem):
    def __init__(self, mensagem: str):
        super().__init__(mensagem=mensagem, tipo="ERRO", icone="❌")

    def mostrar(self):
        console.print(
            Panel(
                f"{self._icone} {self._mensagem}",
                title="[bold red]ERRO[/bold red]",
                border_style="red",
                expand=False
            )
        )

class Aviso(Mensagem):
    def __init__(self, mensagem: str):
        super().__init__(mensagem=mensagem, tipo="AVISO", icone="⚠️")

    def mostrar(self):
        console.print(
            Panel(
                f"{self._icone} {self._mensagem}",
                title="[bold yellow]AVISO[/bold yellow]",
                border_style="yellow",
                expand=False
            )
        )

# --- Exemplo de Uso ---
if __name__ == "__main__":
    msg_generica = Mensagem("Sistema inicializado com sucesso.", "INFO", "ℹ️")
    msg_erro = Erro("Falha ao conectar ao banco de dados.")
    msg_aviso = Aviso("Seu espaço em disco está prestes a acabar.")

    msg_generica.mostrar()
    msg_erro.mostrar()
    msg_aviso.mostrar()