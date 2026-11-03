import sqlite3

def cadastrar_pessoa():
    nome = input("Nome da pessoa: ").strip()
    if not nome:
        print("O nome não pode ficar vazio.")
        return True

    try:
        with sqlite3.connect("cadastro.db") as conexao:
            conexao.execute("INSERT INTO pessoas (nome) VALUES (?)", (nome,))
        print("Pessoa cadastrada com sucesso.")
        return True
    except sqlite3.Error as erro:
        print(f"Erro ao cadastrar pessoa: {erro}")
        return False

def listar_pessoas():
    try:
        with sqlite3.connect("cadastro.db") as conexao:
            pessoas = conexao.execute(
                "SELECT id, nome FROM pessoas ORDER BY id"
            ).fetchall()

        if pessoas:
            for pessoa_id, nome in pessoas:
                print(f"ID: {pessoa_id} | Nome: {nome}")
        else:
            print("Nenhuma pessoa cadastrada.")
        return True
    except sqlite3.Error as erro:
        print(f"Erro ao listar pessoas: {erro}")
        return False

def atualizar_pessoa():
    try:
        pessoa_id = int(input("ID da pessoa a atualizar: "))
    except ValueError:
        print("ID inválido.")
        return True

    nome = input("Novo nome: ").strip()
    if not nome:
        print("O nome não pode ficar vazio.")
        return True

    try:
        with sqlite3.connect("cadastro.db") as conexao:
            cursor = conexao.execute(
                "UPDATE pessoas SET nome = ? WHERE id = ?", (nome, pessoa_id)
            )
        if cursor.rowcount:
            print("Pessoa atualizada com sucesso.")
        else:
            print("Pessoa não encontrada.")
        return True
    except sqlite3.Error as erro:
        print(f"Erro ao atualizar pessoa: {erro}")
        return False

def excluir_pessoa():
    try:
        pessoa_id = int(input("ID da pessoa a excluir: "))
    except ValueError:
        print("ID inválido.")
        return True

    try:
        with sqlite3.connect("cadastro.db") as conexao:
            cursor = conexao.execute("DELETE FROM pessoas WHERE id = ?", (pessoa_id,))
        if cursor.rowcount:
            print("Pessoa excluída com sucesso.")
        else:
            print("Pessoa não encontrada.")
        return True
    except sqlite3.Error as erro:
        print(f"Erro ao excluir pessoa: {erro}")
        return False

def buscar_por_nome():
    nome = input("Nome ou parte do nome para buscar: ").strip()
    if not nome:
        print("Informe um nome para a busca.")
        return True

    try:
        with sqlite3.connect("cadastro.db") as conexao:
            pessoas = conexao.execute(
                "SELECT id, nome FROM pessoas WHERE nome LIKE ? ORDER BY id",
                (f"%{nome}%",),
            ).fetchall()

        if pessoas:
            for pessoa_id, nome_encontrado in pessoas:
                print(f"ID: {pessoa_id} | Nome: {nome_encontrado}")
        else:
            print("Nenhuma pessoa encontrada.")
        return True
    except sqlite3.Error as erro:
        print(f"Erro ao buscar pessoa: {erro}")
        return False

def criar_banco():
    try:
        with sqlite3.connect("cadastro.db") as conexao:
            conexao.execute(
                """
                CREATE TABLE IF NOT EXISTS pessoas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL
                )
                """
            )
        return True
    except sqlite3.Error as erro:
        print(f"Erro ao criar o banco de dados: {erro}")
        return False

def exibir_menu():
    print("\n" + "=" * 30)
    print("   SISTEMA DE CADASTRO")
    print("=" * 30)
    print("1. Cadastrar pessoa")
    print("2. Listar pessoas")
    print("3. Atualizar pessoa")
    print("4. Excluir pessoa")
    print("5. Buscar por nome")
    print("0. Sair")
    print("=" * 30)

def main():
    # Corrigido: Agora verifica se a função retornou False (falhou)
    if not criar_banco():
        print("Falha ao criar o banco de dados. Encerrando o programa.")
        raise SystemExit

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            if not cadastrar_pessoa():
                print("Falha ao cadastrar pessoa.")
        elif opcao == "2":
            if not listar_pessoas():
                print("Falha ao listar pessoas.")
        elif opcao == "3":
            if not atualizar_pessoa():
                print("Falha ao atualizar pessoa.")
        elif opcao == "4":
            if not excluir_pessoa():
                print("Falha ao excluir pessoa.")
        elif opcao == "5":
            if not buscar_por_nome():
                print("Falha ao buscar pessoa.")
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()