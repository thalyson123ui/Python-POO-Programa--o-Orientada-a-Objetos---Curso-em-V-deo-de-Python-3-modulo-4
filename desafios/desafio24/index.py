from abc import ABC, abstractmethod
from rich.console import Console
from rich.panel import Panel

# Inicializamos o console do Rich
console = Console()

# Classe Abstrata (Template)
class BebidaQuente(ABC):
    
    def preparar(self):
        """Método Template que define a ordem do processo."""
        # Usamos um painel para destacar o início do preparo
        console.print(Panel(f"[bold magenta]Preparando {self.__class__.__name__}[/bold magenta]", expand=False))
        
        self.ferver_agua()
        self.misturar()
        self.servir()
        
        console.print("[bold green]✔ Pronto! Aproveite sua bebida.[/bold green]\n")

    def ferver_agua(self):
        console.print("[blue]~[/blue] Fervendo a água a 100°C...")

    @abstractmethod
    def misturar(self):
        """Cada bebida tem sua forma de mistura."""
        pass

    @abstractmethod
    def servir(self):
        """Cada bebida é servida em um recipiente específico."""
        pass

# --- Subclasses ---

class Cafe(BebidaQuente):
    def misturar(self):
        console.print("[yellow]☕[/yellow] Passando a água pelo pó de café moído e filtrando...")

    def servir(self):
        console.print("   Servindo em uma xícara de cerâmica pequena.")

class Cha(BebidaQuente):
    def misturar(self):
        console.print("[green]🍃[/green] Fazendo a infusão das ervas na água quente...")

    def servir(self):
        console.print("   Servindo em uma xícara de porcelana com pires.")

class Leite(BebidaQuente):
    def misturar(self):
        console.print("[white]🥛[/white] Adicionando o leite em pó e mexendo até dissolver...")

    def servir(self):
        console.print("   Servindo em um copo grande de vidro.")

# --- Simulação ---

if __name__ == "__main__":
    pedidos = [Cafe(), Cha(), Leite()]

    for pedido in pedidos:
        pedido.preparar()