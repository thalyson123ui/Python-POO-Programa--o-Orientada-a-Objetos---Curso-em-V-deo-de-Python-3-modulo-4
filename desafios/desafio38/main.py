class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def __repr__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"


class Carrinho:
    def __init__(self, produtos=None):
        # Agregação: o carrinho contém uma lista de objetos do tipo Produto.
        # Os objetos Produto existem independentemente do Carrinho.
        self.produtos = list(produtos) if produtos else []

    def total(self) -> float:
        """Calcula o valor total dos produtos no carrinho."""
        return sum(produto.preco for produto in self.produtos)

    def __add__(self, other):
        """
        Sobrecarga do operador '+'
        Permite: carrinho + produto OU carrinho + outro_carrinho
        Retorna uma nova instância de Carrinho.
        """
        if isinstance(other, Produto):
            return Carrinho(self.produtos + [other])
        elif isinstance(other, Carrinho):
            return Carrinho(self.produtos + other.produtos)
        return NotImplemented

    def __iadd__(self, other):
        """
        Sobrecarga do operador '+='
        Adiciona o produto ou carrinho diretamente à instância atual.
        """
        if isinstance(other, Produto):
            self.produtos.append(other)
            return self
        elif isinstance(other, Carrinho):
            self.produtos.extend(other.produtos)
            return self
        return NotImplemented

    def __str__(self):
        if not self.produtos:
            return "Carrinho vazio."
        itens = "\n  - ".join(str(p) for p in self.produtos)
        return f"Itens no Carrinho:\n  - {itens}\nTotal: R$ {self.total():.2f}"


# ==========================================
# Exemplo de Uso / Demonstração
# ==========================================
if __name__ == "__main__":
    # 1. Criação dos produtos (objetos independentes)
    p1 = Produto("Notebook", 3500.00)
    p2 = Produto("Mouse Gamer", 150.00)
    p3 = Produto("Teclado Mecânico", 300.00)

    # 2. Instanciação do carrinho vazio
    meu_carrinho = Carrinho()

    # 3. Adicionando produtos usando o operador '+'
    meu_carrinho = meu_carrinho + p1
    meu_carrinho = meu_carrinho + p2

    print("--- Após usar '+' ---")
    print(meu_carrinho)

    # 4. Adicionando produto usando o operador '+='
    meu_carrinho += p3

    print("\n--- Após usar '+=' ---")
    print(meu_carrinho)

    # 5. Combinando dois carrinhos usando '+'
    outro_carrinho = Carrinho([Produto("Monitor 27'", 1200.00)])
    carrinho_combinado = meu_carrinho + outro_carrinho

    print("\n--- Soma de dois carrinhos ---")
    print(carrinho_combinado)