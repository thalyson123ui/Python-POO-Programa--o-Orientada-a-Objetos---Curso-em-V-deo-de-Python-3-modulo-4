# declaração de classes
class Gafanhoto:
    def __init__(self, n="vazio", i=0):
        # atributos de instância
        self.nome = n
        self.idade = i

    # métodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."


# declaração de objetos
g1 = Gafanhoto(n="Maria", i=22)
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto(n="João", i=20)
g2.aniversario()
print(g2.mensagem())
