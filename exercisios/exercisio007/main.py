import inspect


class Avaliacao:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self.nota = nota


def avaliacao(nome, disciplina, nota):
    return Avaliacao(nome, disciplina, nota)


def main():
    av1 = avaliacao("thalyso", "calculo 1", 8.5)
    # mostrar atributos da instância
    print(dict(inspect.getmembers(av1)))


if __name__ == '__main__':
    main()