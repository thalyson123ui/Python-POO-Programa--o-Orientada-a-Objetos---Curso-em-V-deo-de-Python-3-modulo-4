from functools import singledispatchmethod

class analisador:
    @singledispatchmethod
    def analisar(self, valor):
        print(f"não foi possível analisar o valor {valor}")

    @analisar.register
    def _(self, valor: int):
        print(f"{valor} é um numero inteiro")

    @analisar.register
    def _(self, valor: float):
        print(f"{valor} é um numero com ponto flutuante") 

    @analisar.register
    def _(self, valor: str):
        print(f"{valor} é uma cadeia de caracteres")

    @analisar.register
    def _(self, valoe: tuple| list| dict):
        print(f"{valoe} é uma coleção de dados")