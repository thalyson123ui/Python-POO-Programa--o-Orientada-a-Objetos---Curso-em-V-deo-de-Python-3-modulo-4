from abc import ABC, abstractmethod
from rich.console import Console
from rich.table import Table

console = Console()

class Funcionario(ABC):
    # Valores base conforme instrução
    SALARIO_MINIMO = 1612.00
    INSS_PERCENTUAL = 7.5

    def __init__(self, nome: str, salario_bruto: float):
        self.nome = nome
        self.salario_bruto = salario_bruto

    @abstractmethod
    def calcular_salario(self):
        """Método abstrato que deve ser implementado pelas subclasses."""
        pass

    def analisar_salario(self):
        """Compara o salário calculado com o salário mínimo."""
        salario_final = self.calcular_salario()
        qtd_minimos = salario_final / self.SALARIO_MINIMO
        return f"{qtd_minimos:.2f} salários mínimos"

    def aplicar_inss(self, valor):
        """Aplica o desconto fixo de 7.5% de INSS solicitado."""
        return valor * (1 - self.INSS_PERCENTUAL / 100)

class Horista(Funcionario):
    def __init__(self, nome: str, valor_hora: float, horas_trabalhadas: float):
        # O salário bruto inicial para o horista é o cálculo direto das horas
        super().__init__(nome, valor_hora * horas_trabalhadas)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_salario(self):
        # Cálculo: (Valor/Hora * Horas) - Desconto INSS
        bruto = self.valor_hora * self.horas_trabalhadas
        return self.aplicar_inss(bruto)

class Mensalista(Funcionario):
    def calcular_salario(self):
        # Cálculo: Salário Bruto Fixo - Desconto INSS
        return self.aplicar_inss(self.salario_bruto)

# --- Execução e Exibição com Rich ---

def exibir_resultados(lista_funcionarios):
    table = Table(title="Folha de Pagamento - Desafio Python", style="cyan", header_style="bold magenta")
    
    table.add_column("Nome", style="white")
    table.add_column("Tipo", style="yellow")
    table.add_column("Salário Líquido (c/ INSS)", justify="right", style="green")
    table.add_column("Análise (Qtd Mínimos)", justify="center", style="blue")

    for f in lista_funcionarios:
        tipo = f.__class__.__name__
        salario_liq = f.calcular_salario()
        analise = f.analisar_salario()
        
        table.add_row(f.nome, tipo, f"R$ {salario_liq:,.2f}", analise)

    console.print(table)

# Criando instâncias de teste
if __name__ == "__main__":
    f1 = Mensalista("Ana Silva", 5000.00)
    f2 = Horista("Carlos Souza", 50.00, 160) # 160 horas no mês
    f3 = Mensalista("Bruna Oliveira", 1800.00)

    funcionarios = [f1, f2, f3]
    exibir_resultados(funcionarios)