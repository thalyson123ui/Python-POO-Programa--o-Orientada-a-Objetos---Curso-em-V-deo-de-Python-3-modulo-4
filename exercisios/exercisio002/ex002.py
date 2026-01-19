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

    

    def __str__(self): # dunder method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    
    def __getstate__(self):
        return f"estado: nome={self.nome}, idade-{self.idade}"


# declaração de objetos
g1 = Gafanhoto(nome="Maria", idade=22)
#g1.aniversario()
print(g1.__dict__)  # exibe os atributos do objeto em forma de dicionário
print(g1.__getstate__()) # exibe os atributos do objeto em forma de dicionário

#print(g1.__doc__)  # exibe a docstring da classe

