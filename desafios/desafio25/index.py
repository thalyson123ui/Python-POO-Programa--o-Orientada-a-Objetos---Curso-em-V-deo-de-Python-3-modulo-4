from abc import ABC, abstractmethod
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Inicializa o console do Rich para formatação
console = Console()

class Transporte(ABC):
    def __init__(self, distancia: float):
        self.distancia = distancia
        self.frete = 0.0

    @abstractmethod
    def calculo_frete(self):
        pass

class Moto(Transporte):
    def __init__(self, distancia: float):
        super().__init__(distancia)
        self.fator = 0.50

    def calculo_frete(self):
        # Cálculo livre (fator * distância)
        self.frete = self.distancia * self.fator
        return self.frete

class Caminhao(Transporte):
    def __init__(self, distancia: float):
        super().__init__(distancia)
        self.fator = 1.20

    def calculo_frete(self):
        # Mínimo de 50 km para efeito de cobrança
        distancia_cobrada = max(self.distancia, 50)
        self.frete = distancia_cobrada * self.fator
        return self.frete

class Drone(Transporte):
    def __init__(self, distancia: float):
        super().__init__(distancia)
        self.fator = 9.50

    def calculo_frete(self):
        # Mínimo de 10 km para efeito de cobrança
        distancia_cobrada = max(self.distancia, 10)
        self.frete = distancia_cobrada * self.fator
        return self.frete

def exibir_simulacao(distancia_teste):
    # Instanciando os transportes
    veiculos = [
        ("Moto", Moto(distancia_teste)),
        ("Caminhão", Caminhao(distancia_teste)),
        ("Drone", Drone(distancia_teste))
    ]

    # Criando a tabela Rich
    table = Table(title=f"Simulação de Frete - Distância: [bold cyan]{distancia_teste} km[/]", 
                  show_header=True, header_style="bold magenta")
    
    table.add_column("Veículo", style="dim", width=15)
    table.add_column("Fator (R$)", justify="right")
    table.add_column("Regra Aplicada", justify="center")
    table.add_column("Total Frete", justify="right", style="green")

    for nome, obj in veiculos:
        valor_final = obj.calculo_frete()
        
        # Lógica para descrever a regra na tabela
        regra = "Livre"
        if nome == "Caminhão" and distancia_teste < 50:
            regra = "Mín. 50km aplicado"
        elif nome == "Drone" and distancia_teste < 10:
            regra = "Mín. 10km aplicado"

        table.add_row(
            nome, 
            f"R$ {obj.fator:.2f}", 
            regra, 
            f"R$ {valor_final:.2f}"
        )

    console.print(Panel(table, expand=False, border_style="blue"))

if __name__ == "__main__":
    # Teste com uma distância curta para validar as regras de mínimo
    exibir_simulacao(5.0)
    
    # Teste com uma distância longa
    exibir_simulacao(100.0)