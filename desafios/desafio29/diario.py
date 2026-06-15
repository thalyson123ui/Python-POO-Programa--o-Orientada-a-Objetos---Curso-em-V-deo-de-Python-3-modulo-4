import sys
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Secret

# Inicializa o console do Rich para formatações bonitas
console = Console()

class Diario:
    def __init__(self, senha_inicial: str):
        # Atributos privados (encapsulamento)
        self.__segredos = []
        self.__senha = senha_inicial

    def escrever(self, msg: str) -> None:
        """Adiciona um novo segredo ao diário."""
        self.__segredos.append(msg)
        console.print("[green]✓[/green] Pensamento guardado a sete chaves... 🔒")

    def ler(self, senha: str) -> None:
        """Exibe os segredos apenas se a senha estiver correta."""
        if senha == self.__senha:
            if not self.__segredos:
                console.print(Panel("O diário está em branco. Nenhum segredo ainda...", title="📖 Meu Diário", border_style="blue"))
                return
            
            # Formata a exibição dos segredos usando um painel estilizado
            conteudo = "\n".join([f"• {segredo}" for segredo in self.__segredos])
            console.print(Panel(conteudo, title="📖 Meus Segredos", border_style="magenta", expand=False))
        else:
            console.print("[red]❌ Senha incorreta! O diário permanece trancado.[/red]")


# --- Simulação Interativa do Desafio ---
def main():
    console.print(Panel.fit(
        "✨ [bold gold1]Simulador de Diário Secreto POO[/bold gold1] ✨\n[italic white]Protegendo seus pensamentos com Python & Rich[/italic white]",
        border_style="yellow"
    ))

    # Criação do objeto Diário com uma senha inicial
    senha_definida = Secret.ask("Defina a senha mestre para o seu diário")
    meu_diario = Diario(senha_definida)
    console.print("[green]Diário criado com sucesso e trancado![/green]\n")

    while True:
        console.print("\n[bold cyan]Menu de Opções:[/bold cyan]")
        console.print("1. [bold]Escrever[/bold] no diário")
        console.print("2. [bold]Ler[/bold] o diário")
        console.print("3. Sair")
        
        opcao = Prompt.ask("Escolha uma opção", choices=["1", "2", "3"])

        if opcao == "1":
            mensagem = Prompt.ask("O que você está pensando? 🤔")
            meu_diario.escrever(mensagem)
        
        elif opcao == "2":
            senha_tentativa = Secret.ask("Digite a senha para abrir o diário 🔑")
            meu_diario.ler(senha_tentativa)
            
        elif opcao == "3":
            console.print("\n[italic yellow]Fechando o diário... Até a próxima! 🤫[/italic yellow]")
            sys.exit()

if __name__ == "__main__":
    main()