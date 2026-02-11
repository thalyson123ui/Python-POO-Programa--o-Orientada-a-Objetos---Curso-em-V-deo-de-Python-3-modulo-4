from rich.console import Console

class Caneta:
    def __init__(self, cor: str = "white"):
        """
        Inicializa a caneta com uma cor padrão.
        """
        self.cor = cor
        self.console = Console()

    def mudar_cor(self, nova_cor: str):
        """
        Altera a cor da caneta.
        """
        self.cor = nova_cor

    def escrever(self, texto: str):
        """
        Escreve o texto na cor atual da caneta.
        """
        self.console.print(texto, style=self.cor)


# Exemplo de uso
if __name__ == "__main__":
    caneta = Caneta("blue")   # cria uma caneta azul
    caneta.escrever("Olá, estou escrevendo em azul!")

    caneta.mudar_cor("red")   # muda para vermelho
    caneta.escrever("Agora estou escrevendo em vermelho!")

    caneta.mudar_cor("green") # muda para verde
    caneta.escrever("E finalmente em verde!")
