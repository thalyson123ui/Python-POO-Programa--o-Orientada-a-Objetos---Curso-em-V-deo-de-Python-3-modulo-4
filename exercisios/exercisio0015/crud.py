import sqlite3

NOME_BANCO = "cadast.db"

def criar_banco() -> bool:
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cursor = db.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS pessoas (
                    cod INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nome TEXT NOT NULL, 
                    altura REAL NOT NULL
                );
            """)
            return True
    except sqlite3.Error as error:
        print(f"Falha na criação do banco: {error}")
        return False

def cadastro_em_massa() -> bool:
    cad_pessoas = [
        ("pedro", 1.75),
        ("sofia", 1.65),
        ("ingrid", 1.70),
        ("victor", 1.80),
    ]
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cursor = db.cursor()
            cursor.executemany("INSERT INTO pessoas (nome, altura) VALUES (?, ?);", cad_pessoas)
            print("Cadastro em massa realizado com sucesso.")
            return True
    except sqlite3.Error as error:
        print(f"Falha no cadastro em massa: {error}")
        return False

def cadastrar_pessoa() -> bool:
    print("\n--- NOVO CADASTRO ---")
    nome = input("Nome: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        return True

    altura_str = input("Altura (ex: 1.75): ").strip().replace(",", ".")
    try:
        altura = float(altura_str)
        if altura <= 0:
            print("A altura deve ser maior que zero.")
            return True
    except ValueError:
        print("Altura inválida. Digite um valor numérico.")
        return True

    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO pessoas (nome, altura) VALUES (?, ?);", (nome, altura))
            print("Pessoa cadastrada com sucesso.")
            return True
    except sqlite3.Error as error:
        print(f"Falha ao cadastrar pessoa: {error}")
        return False

def listar_pessoas() -> bool:
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cursor = db.cursor()
            cursor.execute("SELECT cod, nome, altura FROM pessoas ORDER BY cod")
            pessoas = cursor.fetchall()
            if pessoas:
                print("\nLista de Pessoas:")
                for cod, nome, altura in pessoas:
                    print(f"  {cod} - {nome} (Altura: {altura:.2f}m)")
            else:
                print("Nenhuma pessoa cadastrada.")
        return True
    except sqlite3.Error as error:
        print(f"Falha ao listar pessoas: {error}")
        return False

def atualizar_pessoa() -> bool:
    print("\n--- ATUALIZAR PESSOA ---")
    listar_pessoas()
    try:
        cod = int(input("Digite o código da pessoa que deseja atualizar: ").strip())
    except ValueError:
        print("Código inválido.")
        return True

    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cursor = db.cursor()
            cursor.execute("SELECT nome, altura FROM pessoas WHERE cod = ?", (cod,))
            pessoa = cursor.fetchone()
            
            if not pessoa:
                print("Pessoa não encontrada.")
                return True

            nome_atual, altura_atual = pessoa
            print(f"Atualizando: {nome_atual} (Altura: {altura_atual:.2f}m)")
            
            novo_nome = input(f"Novo nome (Enter para manter '{nome_atual}'): ").strip() or nome_atual
            nova_altura_str = input(f"Nova altura (Enter para manter '{altura_atual}'): ").strip().replace(",", ".")
            
            if nova_altura_str:
                try:
                    nova_altura = float(nova_altura_str)
                except ValueError:
                    print("Altura inválida. Atualização cancelada.")
                    return True
            else:
                nova_altura = altura_atual

            cursor.execute(
                "UPDATE pessoas SET nome = ?, altura = ? WHERE cod = ?",
                (novo_nome, nova_altura, cod)
            )
            print("Pessoa atualizada com sucesso.")
            return True
    except sqlite3.Error as error:
        print(f"Falha ao atualizar pessoa: {error}")
        return False

def excluir_pessoa() -> bool:
    print("\n--- EXCLUSÃO DE PESSOA ---")
    listar_pessoas()
    try:
        cod = int(input("Digite o código da pessoa que deseja excluir: ").strip())
    except ValueError:
        print("Código inválido.")
        return True

    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cursor = db.cursor()
            cursor.execute("SELECT nome, altura FROM pessoas WHERE cod = ?", (cod,))
            pessoa = cursor.fetchone()
            if pessoa:
                nome, altura = pessoa
                print(f"Pessoa encontrada: {nome} (Altura: {altura:.2f}m)")
                confirmacao = input("Tem certeza que deseja excluir esta pessoa? (s/n): ").strip().lower()
                if confirmacao == 's':
                    cursor.execute("DELETE FROM pessoas WHERE cod = ?", (cod,))
                    print("Pessoa excluída com sucesso.")
                else:
                    print("Exclusão cancelada.")
            else:
                print("Pessoa não encontrada.")
        return True
    except sqlite3.Error as error:
        print(f"Falha ao excluir pessoa: {error}")
        return False

def buscar_por_nome() -> bool:
    print("\n--- BUSCAR POR NOME ---")
    termo = input("Digite o nome ou parte do nome: ").strip()
    if not termo:
        print("Termo de busca não pode ser vazio.")
        return True

    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cursor = db.cursor()
            cursor.execute("SELECT cod, nome, altura FROM pessoas WHERE nome LIKE ? ORDER BY cod", (f"%{termo}%",))
            resultados = cursor.fetchall()
            if resultados:
                print("\nResultados da busca:")
                for cod, nome, altura in resultados:
                    print(f"  {cod} - {nome} (Altura: {altura:.2f}m)")
            else:
                print("Nenhuma pessoa encontrada com esse termo.")
        return True
    except sqlite3.Error as error:
        print(f"Falha na busca por nome: {error}")
        return False