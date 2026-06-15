from datetime import date
from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, nascimento: date):
        # Símbolo '#' indica atributos protegidos
        self._nome = nome
        self._nascimento = nascimento

    # Getter para o nascimento (@nascimento)
    @property
    def nascimento(self) -> date:
        return self._nascimento
    
    # Setter para o nascimento caso precise alterar
    @nascimento.setter
    def nascimento(self, novo_nascimento: date):
        self._nascimento = novo_nascimento

    # Propriedade calculada para a idade (@idade)
    @property
    def idade(self) -> int:
        hoje = date.today()
        # Calcula a idade baseada no ano e ajusta se ainda não fez aniversário este ano
        idade = hoje.year - self._nascimento.year - ((hoje.month, hoje.day) < (self._nascimento.month, self._nascimento.day))
        return idade


class Aluno(Pessoa):
    def __init__(self, nome: str, nascimento: date, curso_inicial: str):
        # Inicializa a classe base (Pessoa)
        super().__init__(nome, nascimento)
        
        # Atributos específicos de Aluno
        self.cursos_oficiais = [curso_inicial]  # '+' indica público. Começa com o curso inicial.
        self._curso = curso_inicial              # '#' indica protegido

    # Getter para o curso atual (@curso)
    @property
    def curso(self) -> str:
        return self._curso

    # Setter para alterar o curso atual
    @curso.setter
    def curso(self, novo_curso: str):
        self._curso = novo_curso

    # Método para adicionar um curso à lista (+ add_curso)
    def add_curso(self, curso: str):
        if curso not in self.cursos_oficiais:
            self.cursos_oficiais.append(curso)
            self._curso = curso  # Atualiza o curso atual para o mais recente


# --- Exemplo Prático de Uso ---
if __name__ == "__main__":
    # Criando a data de nascimento (Ano, Mês, Dia)
    data_nasc = date(2004, 5, 15)
    
    # Instanciando o aluno
    aluno1 = Aluno(nome="Lucas Silva", nascimento=data_nasc, curso_inicial="Engenharia de Software")
    
    # Testando os atributos e propriedades herdadas de Pessoa
    print(f"Aluno: {aluno1._nome}")
    print(f"Data de Nascimento: {aluno1.nascimento.strftime('%d/%m/%Y')}")
    print(f"Idade: {aluno1.idade} anos")
    
    print("---")
    
    # Testando os métodos e propriedades de Aluno
    print(f"Curso Atual: {aluno1.curso}")
    print(f"Lista de Cursos Oficiais: {aluno1.cursos_oficiais}")
    
    print("\nAdicionando um novo curso...")
    aluno1.add_curso("Ciência de Dados")
    
    print(f"Novo Curso Atual: {aluno1.curso}")
    print(f"Lista Atualizada de Cursos: {aluno1.cursos_oficiais}")