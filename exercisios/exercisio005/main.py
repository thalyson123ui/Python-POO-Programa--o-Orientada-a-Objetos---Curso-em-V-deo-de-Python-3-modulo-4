from abc import ABC, abstractmethod

# ==========================================
# 1. CLASSE ABSTRATA (O MOLDE)
# ==========================================
class Pessoa(ABC):
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    @abstractmethod
    def registrar_presenca(self):
        """Obrigatório implementar: define como a pessoa marca presença."""
        pass

    @abstractmethod
    def obter_papel(self):
        """Obrigatório implementar: define a função da pessoa."""
        pass

# ==========================================
# 2. CLASSES FILHAS (IMPLEMENTAÇÕES)
# ==========================================

class Aluno(Pessoa):
    def __init__(self, nome, matricula, curso):
        super().__init__(nome, matricula)
        self.curso = curso

    def registrar_presenca(self):
        print(f"[ALUNO] {self.nome} (Matrícula: {self.matricula}) marcou presença via App de Estudante.")

    def obter_papel(self):
        return f"Estudante de {self.curso}"

class Professor(Pessoa):
    def __init__(self, nome, matricula, disciplina):
        super().__init__(nome, matricula)
        self.disciplina = disciplina

    def registrar_presenca(self):
        print(f"[PROFESSOR] {self.nome} assinou a folha de ponto na sala dos professores.")

    def obter_papel(self):
        return f"Docente da disciplina: {self.disciplina}"

class Funcionario(Pessoa):
    def __init__(self, nome, matricula, setor):
        super().__init__(nome, matricula)
        self.setor = setor

    def registrar_presenca(self):
        print(f"[FUNCIONÁRIO] {self.nome} registrou o ponto biométrico no setor {self.setor}.")

    def obter_papel(self):
        return f"Colaborador Administrativo ({self.setor})"

# ==========================================
# 3. EXECUÇÃO (MAIN)
# ==========================================

if __name__ == "__main__":
    # Criamos uma lista de pessoas para demonstrar o polimorfismo
    comunidade_escolar = [
        Aluno("Gabriel Ribeiro", "2023001", "Ciência da Computação"),
        Professor("Dr. Wilson Silva", "9905", "Algoritmos Avançados"),
        Funcionario("Marta Souza", "F-45", "Recursos Humanos")
    ]

    print("--- SISTEMA DE GESTÃO ESCOLAR ---")
    print("-" * 40)

    for pessoa in comunidade_escolar:
        # Perceba que chamamos os mesmos métodos, mas cada objeto reage de um jeito
        print(f"Nome: {pessoa.nome}")
        print(f"Papel: {pessoa.obter_papel()}")
        pessoa.registrar_presenca()
        print("-" * 40)