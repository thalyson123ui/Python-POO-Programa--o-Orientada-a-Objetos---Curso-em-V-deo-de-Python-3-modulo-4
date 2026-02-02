from rich import print
from rich.panel import Panel
from rich.text import Text


class Livro:
    def __init__(self, titulo: str, total_paginas: int):
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.pagina_atual = 1

    def avancar_pagina(self):
        if self.pagina_atual < self.total_paginas:
            self.pagina_atual += 1
            self._mostrar_status("Página avançada")
        else:
            print(Panel(
                "[bold red]Você já chegou ao fim do livro! 📚[/bold red]",
                title="Fim da leitura"
            ))

    def voltar_pagina(self):
        if self.pagina_atual > 1:
            self.pagina_atual -= 1
            self._mostrar_status("Página retornada")
        else:
            print(Panel(
                "[bold yellow]Você já está na primeira página.[/bold yellow]",
                title="Atenção"
            ))

    def ir_para_pagina(self, pagina: int):
        if 1 <= pagina <= self.total_paginas:
            self.pagina_atual = pagina
            self._mostrar_status(f"Ir para página {pagina}")
        else:
            print(Panel(
                "[bold red]Página inválida![/bold red]",
                title="Erro"
            ))

    def chegou_ao_fim(self) -> bool:
        return self.pagina_atual == self.total_paginas

    def _mostrar_status(self, acao: str):
        texto = Text()
        texto.append(f"{acao}\n", style="bold cyan")
        texto.append(f"Título: {self.titulo}\n", style="bold")
        texto.append(f"Página atual: {self.pagina_atual}/{self.total_paginas}", style="green")

        print(Panel(texto, title="Status do Livro"))

        if self.chegou_ao_fim():
            print(Panel(
                "[bold green]🎉 Parabéns! Você concluiu a leitura![/bold green]",
                title="Leitura Finalizada"
            ))

# ===== Exemplo de uso =====
livro = Livro("harry potter e as reliquias da morte", 5)

livro.avancar_pagina()
livro.avancar_pagina()
livro.avancar_pagina()
livro.avancar_pagina()
livro.avancar_pagina()  # Aqui atinge o fim
livro.voltar_pagina()
livro.ir_para_pagina(2)
livro.ir_para_pagina(10)  # inválida
