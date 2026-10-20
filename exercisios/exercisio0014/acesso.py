import os
import sqlite3

# Define o caminho do banco na mesma pasta onde o script Python está rodando
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_banco = os.path.join(diretorio_atual, 'meu_banco.db')

# 1. Conecta ao banco de dados (se o arquivo não existir, ele será criado)
conexao = sqlite3.connect(caminho_banco)
cursor = conexao.cursor()

# 2. Comando SQL para criar a tabela de amigos
script_criar_tabela = '''
CREATE TABLE IF NOT EXISTS amigos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    data_nascimento DATE NOT NULL
);
'''

# Executa a criação da tabela
cursor.execute(script_criar_tabela)
print('Tabela "amigos" verificada/criada com sucesso!')

# 3. Inserção de dados de exemplo (opcional)
amigos_exemplo = [
    ('Lucas Silva', '1998-03-15'),
    ('Mariana Costa', '2001-11-02'),
    ('Thiago Rocha', '1995-07-20'),
]

# Insere apenas se a tabela estiver vazia
cursor.execute('SELECT COUNT(*) FROM amigos')
total_registros = cursor.fetchone()[0]

if total_registros == 0:
  cursor.executemany(
      'INSERT INTO amigos (nome, data_nascimento) VALUES (?, ?)', amigos_exemplo
  )
  # Salva as alterações no arquivo do banco
  conexao.commit()
  print('Amigos de exemplo inseridos com sucesso!')

# 4. Consulta os dados para confirmar a gravação
cursor.execute('SELECT id, nome, data_nascimento FROM amigos')
registros = cursor.fetchall()

print('\n--- Lista de Amigos ---')
for amigo in registros:
  print(f'ID: {amigo[0]} | Nome: {amigo[1]} | Nascimento: {amigo[2]}')

# 5. Fecha a conexão com o banco de dados
conexao.close()