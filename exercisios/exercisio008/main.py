import inspect
import importlib.util
import os


def import_avaliacao():
    module_name = "avaliacao"
    module_path = os.path.join(os.path.dirname(__file__), "avaliacao.py")
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Não foi possível carregar o módulo {module_name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Avaliacao

Avaliacao = import_avaliacao()


def avaliacao(nome, disciplina, nota):
    return Avaliacao(nome, disciplina, nota)


def main():
    av1 = avaliacao("Thalyson", "Cálculo 1", 8.5)

    print("\n=== Dados da Avaliação ===")
    print("Nome:", av1.nome)
    print("Disciplina:", av1.disciplina)
    print("Nota:", av1.nota)

    print("\n=== Atributos da Instância (__dict__) ===")
    print(av1.__dict__)

    print("\n=== Membros da Instância (inspect.getmembers) ===")
    for nome, valor in inspect.getmembers(av1):
        if not nome.startswith("__"):
            print(f"{nome}: {valor}")

    print("\n=== Testando validação ===")
    av1.nota = 12  # inválida
    av1.nota = 9.5  # válida

    print("\nNota final:", av1.nota)


if __name__ == "__main__":
    main()