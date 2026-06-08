from rich import print


class Avaliacao:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina

        print(
            "Criando avaliação para [bold magenta]{}[/bold magenta] "
            "na disciplina [bold cyan]{}[/bold cyan] "
            "com nota [bold yellow]{}[/bold yellow]".format(
                nome, disciplina, nota
            )
        )

        self.__nota = None
        self.nota = nota  # Usa o setter para validar

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, valor):
        if valor < 0 or valor > 10:
            print("[bold red]Erro:[/bold red] Nota deve ser entre 0 e 10.")
        else:
            self.__nota = valor
            print(
                "Nota [bold green]{}[/bold green] atribuída com sucesso.".format(
                    valor
                )
            )