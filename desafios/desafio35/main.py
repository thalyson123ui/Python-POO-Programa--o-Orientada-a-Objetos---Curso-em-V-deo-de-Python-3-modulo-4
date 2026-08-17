from abc import ABC, abstractmethod


class Arquivo(ABC):

  def __init__(self, nome: str, extensao: str, tamanho: float):
    self.nome = nome
    self._extensao = (
        extensao  # Atributo protegido (#) conforme indicação no UML
    )
    self.tamanho = tamanho  # Tamanho em MB ou KB

  @property
  def nome_completo(self) -> str:
    """Retorna o nome do arquivo concatenado com sua extensão."""
    return f"{self.nome}.{self._extensao}"

  @abstractmethod
  def abrir(self):
    """Método abstrato que deve ser implementado pelas subclasses."""
    pass


class PDF(Arquivo):

  def __init__(self, nome: str, tamanho: float):
    super().__init__(nome, "pdf", tamanho)

  def abrir(self):
    print(
        f" [PDF] Lendo '{self.nome_completo}' ({self.tamanho} MB) no leitor de"
        " PDF..."
    )


class DOC(Arquivo):

  def __init__(self, nome: str, tamanho: float):
    super().__init__(nome, "doc", tamanho)

  def abrir(self):
    print(
        f" [DOC] Abrindo '{self.nome_completo}' ({self.tamanho} MB) no editor"
        " de texto..."
    )


# --- Demonstração de uso ---
if __name__ == "__main__":
  arquivos = [PDF("relatorio_financeiro", 2.5), DOC("contrato_servico", 1.2)]

  for arq in arquivos:
    print(f"Nome do arquivo: {arq.nome_completo}")
    arq.abrir()
    print("-" * 40)