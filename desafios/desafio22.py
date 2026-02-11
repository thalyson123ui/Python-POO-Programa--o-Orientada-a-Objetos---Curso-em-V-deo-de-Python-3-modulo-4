from rich.console import Console
from rich.table import Table

console = Console()

class ControleRemoto:
    def __init__(self):
        self.ligado = False
        self.canal = 1
        self.volume = 10

    def ligar(self):
        self.ligado = True
        console.print("[green]TV ligada[/green]")

    def desligar(self):
        self.ligado = False
        console.print("[red]TV desligada[/red]")

    def aumentar_volume(self):
        if self.ligado:
            if self.volume < 100:
                self.volume += 1
            self.status()
        else:
            console.print("[yellow]A TV está desligada[/yellow]")

    def diminuir_volume(self):
        if self.ligado:
            if self.volume > 0:
                self.volume -= 1
            self.status()
        else:
            console.print("[yellow]A TV está desligada[/yellow]")

    def mudar_canal(self, novo_canal):
        if self.ligado:
            self.canal = novo_canal
            self.status()
        else:
            console.print("[yellow]A TV está desligada[/yellow]")

    def status(self):
        table = Table(title="Status da TV")
        table.add_column("Atributo", style="cyan", justify="center")
        table.add_column("Valor", style="magenta", justify="center")

        table.add_row("Ligada", str(self.ligado))
        table.add_row("Canal", str(self.canal))
        table.add_row("Volume", str(self.volume))

        console.print(table)


# Exemplo de uso
controle = ControleRemoto()
controle.ligar()
controle.mudar_canal(5)
controle.aumentar_volume()
controle.aumentar_volume()
controle.diminuir_volume()
controle.desligar()
