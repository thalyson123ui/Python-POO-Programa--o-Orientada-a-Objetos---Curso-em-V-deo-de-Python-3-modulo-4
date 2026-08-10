class Porta:
    def abrir(self):
        print("girar a maçaneta - abrir a porta")

class Empresa:
    def abrir(self):
        print("vai ao portal do empreendedor com toda a documentação - abrir a empresa")

class Ovo:
    def abrir(self):
        print("quebrar o ovo - comer o ovo")

class Pedra:
    def abrir(self):
        print("pegar a pedra - abrir a pedra")

# método pythonico polimórfico (duck typing)
def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except Exception:
        print(f"{objeto} nao tem o metodo abrir()")