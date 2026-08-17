from abc import ABC, abstractmethod

# classe abstrata funcionario
class funcionario(ABC):
    def __init__(self, nome: str, salario: float):
        self.nome = nome  # atributo publico
        self.__salario = salario

    #getter para o atributo privado salario
    @property
    def salario(self) -> float:
        return self.__salario

    # setter para atualizar o salario com validação
    @salario.setter
    def salario(self, novo_salario: float):
        if novo_salario > 0:
            self.__salario = novo_salario
        else:
            raise ValueError("o salario deve ser maior que ZERO!")

    # metodo abstrato (+calcular_bonus())
    @abstractmethod
    def calcular_bonus(self) -> float:
        pass

# subclasse gerente
class gerente(funcionario):
    def calcular_bonus(self) -> float:
        return self.salario * 0.20  # 20% do salario

# subclasse designer
class designer(funcionario):
    def calcular_bonus(self) -> float:
        return self.salario * 0.10  # 10% do salario

# subclasse desenvolvedor
class desenvolvedor(funcionario):
    def calcular_bonus(self) -> float:
        return self.salario * 0.15  # 15% do salario

# exemplo de uso
if __name__ == "__main__":
    funcionarios = [
        gerente("Ana", 10000.0),
        designer("Carlos", 5000.0),
        desenvolvedor("Beatriz", 7000.0)
    ]

    for f in funcionarios:
        bonus = f.calcular_bonus()
        total = f.salario + bonus
        print(f"{f.nome} ({type(f).__name__}):")
        print(f"  Salário: R$ {f.salario:.2f}")
        print(f"  Bônus: R$ {bonus:.2f}")
        print(f"  Total: R$ {total:.2f}\n")