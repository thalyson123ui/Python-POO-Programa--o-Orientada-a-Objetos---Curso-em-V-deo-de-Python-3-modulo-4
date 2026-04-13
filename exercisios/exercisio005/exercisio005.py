from rich import inspect
from classes import pessoa, aluno, professor, funcionario

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
