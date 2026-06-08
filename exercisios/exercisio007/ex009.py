from rich import print, inspect


class Avaliacao:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        print("Criando avaliação para [bold magenta]{}[/bold magenta] na disciplina [bold cyan]{}[/bold cyan] com nota [bold yellow]{}[/bold yellow]".format(nome, disciplina, nota))
        self.__nota = None
        self.set_nota(nota)

    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        if 0 <= nota <= 10:
            self.__nota = nota
        else:
            print("Nota inválida. A nota deve estar entre 0 e 10.")


# inspeciona a classe incluindo atributos privados
inspect(Avaliacao, private=True)