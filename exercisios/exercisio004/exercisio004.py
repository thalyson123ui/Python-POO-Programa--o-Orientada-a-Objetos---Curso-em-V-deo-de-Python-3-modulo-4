from rich import inspect
class pessoa:
    def __init__(self, nome, idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1


class aluno(pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} fez matrícula no curso de {self.curso} na turma {self.turma}.")


class professor(pessoa):
    def __init__(self, nome, idade, nivel):
        super().__init__(nome, idade)
        self.especialidade = "especialidade"
        self.nivel = nivel

    def dar_aula(self):
        print(f"{self.nome} está dando aula com nível {self.nivel}.")


class funcionario(pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        pass

a1 = aluno(nome="joao", idade=20, curso="Engenharia", turma="A")
a1.fazer_aniversario()
a1.fazer_matricula()
inspect(a1, methods=True)

p1 = professor(nome="maria", idade=35, nivel="Doutorado")
p1.fazer_aniversario()
p1.dar_aula()
inspect(p1, methods=True)

f1 = funcionario(nome="carlos", idade=40, cargo="Gerente", setor="Financeiro")
f1.fazer_aniversario()
f1.bater_ponto()
inspect(f1, methods=True)