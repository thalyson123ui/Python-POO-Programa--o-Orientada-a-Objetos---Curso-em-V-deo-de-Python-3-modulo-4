# declaração de classes
class Gafanhoto:
    """
    essa classe cria um gafanhoto que é uma pessoa que tem nome e idade.

    para criar uma nova pessoa use
    variavel = Gafanhoto(nome,idade)
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


# declaração de objetos
g1 = Gafanhoto(n="Maria", i=22)
g1.aniversario()
#print(g1.mensagem())

print(g1.__doc__)