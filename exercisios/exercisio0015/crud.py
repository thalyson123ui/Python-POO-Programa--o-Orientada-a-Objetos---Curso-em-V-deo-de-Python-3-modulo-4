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

def cadastro_em_massa():
    # Removido o 'cod' das tuplas. O banco vai gerar o ID automaticamente.
    cad_pessoas = [
        ("pedro", 1.75),
        ("sofia", 1.65),
        ("ingrid", 1.70),
        ("victor", 1.80),
    ]

    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cursor = db.cursor()
            # Ocultamos a coluna 'cod' no INSERT para o AUTOINCREMENT agir
            cursor.executemany("INSERT INTO pessoas (nome, altura) VALUES (?, ?);", cad_pessoas)
            print("Cadastro em massa realizado com sucesso.")
    except sqlite3.Error as error:
        print(f"Falha no cadastro em massa: {error}")

def cadastrar_pessoa() -> bool:
    print("\n novo cadastro de pessoa")
    nome = input("Nome: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        return True

    altura = input("Altura: ").strip()
    if not altura:
        print("Altura não pode ser vazia.")
        return True

    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO pessoas (nome, altura) VALUES (?, ?);", (nome, float(altura)))
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
                    print(f"  {cod} - {nome} (Altura: {altura})")
            else:
                print("Nenhuma pessoa cadastrada.")
        return True
    except sqlite3.Error as error:
        print(f"Falha ao listar pessoas: {error}")
        return False

def atualizar_pessoa() -> bool:
    pass

def excluir_pessoa() -> bool:
    pass

def buscar_por_nome() -> bool:
    pass

# Exemplo de uso para testar se está tudo funcionando
if __name__ == "__main__":
    if criar_banco():
        cadastro_em_massa()