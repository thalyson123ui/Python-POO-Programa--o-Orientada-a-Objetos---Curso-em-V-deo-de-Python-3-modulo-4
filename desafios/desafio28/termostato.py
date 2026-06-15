from rich import print


class Termostato:
    def __init__(self, temperatura):
        self.__temperatura = temperatura
        print(
            f":thermometer: [bold green]Termostato criado[/bold green] com temperatura de "
            f"[bold yellow]{temperatura}°C[/bold yellow]"
        )

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, nova_temperatura):
        if 0 <= nova_temperatura <= 50:
            print(
                f":fire: [bold blue]Alterando temperatura para "
                f"{nova_temperatura}°C[/bold blue]"
            )
            self.__temperatura = nova_temperatura
        else:
            print(
                ":warning: [bold red]Erro![/bold red] "
                "A temperatura deve estar entre 0°C e 50°C."
            )


def main():
    termostato = Termostato(25)

    print(
        f"\n:snowflake: Temperatura atual: "
        f"[bold cyan]{termostato.temperatura}°C[/bold cyan]"
    )

    termostato.temperatura = 30

    print(
        f":thermometer: Temperatura atual: "
        f"[bold cyan]{termostato.temperatura}°C[/bold cyan]"
    )

    termostato.temperatura = 60


if __name__ == "__main__":
    main()