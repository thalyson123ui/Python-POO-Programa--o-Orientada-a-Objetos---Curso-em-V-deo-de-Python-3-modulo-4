import hashlib
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

class Credencial:
    def __init__(self, senha: str):
        self.senha = senha
        # Atributo privado para armazenar o hash SHA-256
        self.__hash = self._gerar_hash(senha)

    def _gerar_hash(self, texto: str) -> str:
        """Método auxiliar interno para gerar o hash SHA-256 de uma string."""
        return hashlib.sha256(texto.encode('utf-8')).hexdigest()

    def validar(self, chave: str) -> bool:
        """Valida se a chave fornecida corresponde ao hash armazenado."""
        return self._gerar_hash(chave) == self.__hash

    def obter_hash(self) -> str:
        """Método para expor o hash de forma controlada para exibição."""
        return self.__hash


# --- Execução do Programa ---
if __name__ == "__main__":
    console = Console()

    # Cabeçalho decorativo do terminal
    console.print(
        Panel.fit(
            "[bold cyan]🛡️  Gerenciador de Credenciais - SHA-256 🛡️[/bold cyan]\n"
            "[italic white]Insira seus dados para criar a Credencial criptografada[/italic white]",
            border_style="blue",
        )
    )

    # 1. OPÇÃO PARA DIGITAR A SENHA (Criação do objeto)
    # O parâmetro password=True faz com que os caracteres fiquem ocultos como na imagem do escudo
    senha_usuario = Prompt.ask("[bold yellow]Digite a senha que deseja cadastrar[/bold yellow]", password=True)
    
    # Instanciando a classe usando a senha digitada pelo usuário
    credencial = Credencial(senha=senha_usuario)

    # Exibindo os dados da classe criados
    console.print("\n[bold green]🔒 Credencial instanciada com sucesso![/bold green]")
    console.print(
        Panel(
            f"[bold white]Texto da Senha (Público):[/bold white] [magenta]{credencial.senha}[/magenta]\n"
            f"[bold white]Hash SHA-256 Guardado (Privado):[/bold white] [green]{credencial.obter_hash()}[/green]",
            title="[bold blue]Atributos da Instância[/bold blue]",
            border_style="green"
        )
    )

    # 2. OPÇÃO PARA DIGITAR A SENHA NOVAMENTE (Validação)
    console.print("\n[bold cyan]🔄 Teste de Validação Interativo[/bold cyan]")
    senha_teste = Prompt.ask("[bold yellow]Digite uma senha para tentar validar e abrir o cadeado[/bold yellow]", password=True)

    # Criando a tabela de resultados do Rich
    tabela = Table(title="Painel de Verificação", title_style="bold magenta", expand=True)
    tabela.add_column("Chave Fornecida", justify="center", style="cyan")
    tabela.add_column("Resultado do Método .validar()", justify="center", style="bold")

    # Executando a validação com a entrada do usuário
    if credencial.validar(senha_teste):
        tabela.add_row("[dim]Ocultada por segurança[/dim]", "[green]✔️ TRUE (Acesso Permitido)[/green]")
        console.print(tabela)
        console.print("\n[bold green]🔓 Sucesso! A senha digitada confere com o Hash SHA-256 seguro.[/bold green]\n")
    else:
        tabela.add_row("[dim]Ocultada por segurança[/dim]", "[red]❌ FALSE (Acesso Negado)[/red]")
        console.print(tabela)
        console.print("\n[bold red]❌ Erro! O Hash gerado por essa chave não bate com o arquivo original.[/bold red]\n")