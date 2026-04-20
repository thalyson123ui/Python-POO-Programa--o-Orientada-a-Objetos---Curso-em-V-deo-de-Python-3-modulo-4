from rich import print
from rich.panel import Panel
from rich.table import Table
from abc import ABC, abstractmethod
import math

# Classe Abstrata (Interface)
class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

# Subclasse Quadrado
class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(qtd_lados=4)
        self.lado = lado

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado ** 2

# Subclasse Circulo
class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(qtd_lados=0)
        self.raio = raio

    def perimetro(self):
        return 2 * math.pi * self.raio

    def area(self):
        return math.pi * (self.raio ** 2)

# --- Exemplo de Uso com Rich ---

# Criando os objetos
quad = Quadrado(5)
circ = Circulo(3)

# 1. Usando Print formatado (Interpolation com cores)
print(Panel("[bold blue]Cálculo de Geometria[/bold blue]", expand=False))

# 2. Criando uma tabela para exibir os resultados
tabela = Table(title="Resultados dos Polígonos")

tabela.add_column("Forma", style="cyan", no_wrap=True)
tabela.add_column("Lados", style="magenta")
tabela.add_column("Área", justify="right", style="green")
tabela.add_column("Perímetro", justify="right", style="yellow")

tabela.add_row(
    "Quadrado", 
    str(quad.qtd_lados), 
    f"{quad.area():.2f}", 
    f"{quad.perimetro():.2f}"
)

tabela.add_row(
    "Círculo", 
    "N/A", 
    f"{circ.area():.2f}", 
    f"{circ.perimetro():.2f}"
)

print(tabela)