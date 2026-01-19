# declaração de classes
class Gafanhoto:
    """
    Essa classe cria um gafanhoto que é uma pessoa que tem nome e idade.

    Para criar uma nova pessoa use:
    variavel = Gafanhoto(nome, idade)
    """

    def __init__(self, nome="vazio", idade=0):
        # atributos de instância
        self.nome = nome
        self.idade = idade

    # métodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."


# declaração de objetos
g1 = Gafanhoto(nome="Maria", idade=22)
g1.aniversario()

print(g1.__doc__)  # exibe a docstring da classe
print(g1)
