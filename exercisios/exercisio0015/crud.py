import sqlite3

NOME_BANCO = "cadast.db"

def criar_banco() -> bool:
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cursor = db.cursor()
            # Removida a vírgula antes de AUTOINCREMENT
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

def cadastrar_pessoa() -> bool:
    pass

def listar_pessoas() -> bool:
    pass

def atualizar_pessoa() -> bool:
    pass

def excluir_pessoa() -> bool:
    pass

def buscar_por_nome() -> bool:
    pass