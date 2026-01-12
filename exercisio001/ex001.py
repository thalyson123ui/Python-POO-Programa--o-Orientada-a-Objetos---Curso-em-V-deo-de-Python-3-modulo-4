# declaração de classes
class gafanhotos:
    def __init__(self): # metodo construtor
        self.nome = ""
        self.idade = 0

    # metodos de instancia
    def aniversario(self):
        self.idade = self.idade + 1

    def menssagem(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."
    
# declaração de objetos
g1 = gafanhotos()
g1.nome = "João"
g1.idade = 20
g1.aniversario()
print(g1.menssagem())

g2 = gafanhotos()
g2.nome = "Maria"
g2.idade = 25
g2.aniversario()
print(g2.menssagem())

g3 = gafanhotos()
print(g3.menssagem())