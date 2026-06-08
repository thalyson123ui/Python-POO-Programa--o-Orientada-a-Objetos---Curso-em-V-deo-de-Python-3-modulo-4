from rich import print, inspect


class Avaliacao:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina

        print(
            f"Criando avaliação para "
            f"[bold magenta]{nome}[/bold magenta] "
            f"na disciplina "
            f"[bold cyan]{disciplina}[/bold cyan] "
            f"com nota "
            f"[bold yellow]{nota}[/bold yellow]"
        )

        self.__nota = None
        self.set_nota(nota)

    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        if 0 <= nota <= 10:
            self.__nota = nota
        else:
            raise ValueError("A nota deve estar entre 0 e 10.")


av1 = Avaliacao("Thalyso", "Cálculo 1", 8.5)

print(f"\nNota cadastrada: [green]{av1.get_nota()}[/green]")

inspect(av1, private=True)