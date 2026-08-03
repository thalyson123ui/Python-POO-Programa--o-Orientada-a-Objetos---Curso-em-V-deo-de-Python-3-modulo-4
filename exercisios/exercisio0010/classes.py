from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str = ""):
        self.nome = nome  # Atributo público/protegido para ser acessado pelas subclasses

    @abstractmethod
    def emitir_som(self):
        pass

class Pato(Animal):
    def emitir_som(self):
        print(f"{self.nome} é {self.__class__.__name__} e está grasnando")

class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} é {self.__class__.__name__} e está latindo")

class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} é {self.__class__.__name__} e está miando")

class Galinha(Animal):
    def emitir_som(self):
        print(f"{self.nome} é {self.__class__.__name__} e está cacarejando")