# declaração de classes
class Gafanhoto: 
    def__init__(self, n = "vazio", i = 0):
    # atributos de instancia
    self.nome = n
    self.idade = i

    # métodos de instancia
    def aniversario(self):
        self.idade = self.idade +1

    def messagem(self):
        return f"{self.name} é Gafanhoto(a) e tem {self.idade} anos de idade."
    
# declaração de objetos
g1 = Gafanhoto(n"maria", i= 22)
g1.aniversario()
print(g1.messagem())

g2 = Gafanhoto(n="joão", i= 20)
g2.aniversario()
print(g2.messagem())