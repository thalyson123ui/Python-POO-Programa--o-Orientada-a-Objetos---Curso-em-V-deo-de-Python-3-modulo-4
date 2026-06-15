from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Inicializa o console do Rich para formatações visuais
console = Console()

class Retangulo:
    def __init__(self, base: float, altura: float):
        """
        Construtor da classe Retangulo.
        Os atributos começam com '_' indicando que são protegidos/privados
        conforme o símbolo '#' no diagrama UML.
        """
        self._base = base
        self._altura = altura
        # Calcula a área automaticamente na inicialização
        self._area = base * altura

    # --- GETTERS (Propriedades com o decorator @property) ---
    @property
    def base(self) -> float:
        return self._base

    @property
    def altura(self) -> float:
        return self._altura

    @property
    def area(self) -> float:
        return self._area

    # --- MÉTODOS DE EXIBIÇÃO COM RICH ---
    def exibir_painel(self):
        """Exibe os dados do retângulo dentro de um painel estilizado."""
        conteudo = (
            f"[bold blue]Base:[/bold blue] {self._base:.2f}\n"
            f"[bold green]Altura:[/bold green] {self._altura:.2f}\n"
            f"[bold yellow]Área:[/bold yellow] [magenta]{self._area:.2f}[/magenta]"
        )
        
        painel = Panel(
            conteudo, 
            title="[bold cyan]Detalhes do Retângulo[/bold cyan]", 
            expand=False,
            border_style="cyan"
        )
        console.print(painel)

    def exibir_tabela(self):
        """Exibe os dados formatados em uma tabela do Rich."""
        tabela = Table(title="Medidas do Retângulo", title_style="bold magenta")
        
        tabela.add_column("Propriedade", justify="left", style="cyan", no_wrap=True)
        tabela.add_column("Valor", justify="right", style="green")

        tabela.add_row("Base", f"{self._base:.2f}")
        tabela.add_row("Altura", f"{self._altura:.2f}")
        tabela.add_row("Área total", f"{self._area:.2f}")

        console.print(tabela)


# --- CÓDIGO DE TESTE (EXECUÇÃO) ---
if __name__ == "__main__":
    console.print("\n[bold yellow]--- Executando o Desafio 031 ---[/bold yellow]\n")

    # Criando uma instância (objeto) da classe Retangulo
    # Passando os valores de base e altura
    meu_retangulo = Retangulo(base=12.5, altura=5.0)

    # 1. Demonstração usando a estilização em Painel
    console.print("[bold white]Visualização em Painel:[/bold white]")
    meu_retangulo.exibir_painel()
    
    console.print("\n" + "-"*40 + "\n")

    # 2. Demonstração usando a estilização em Tabela
    console.print("[bold white]Visualização em Tabela:[/bold white]")
    meu_retangulo.exibir_tabela()