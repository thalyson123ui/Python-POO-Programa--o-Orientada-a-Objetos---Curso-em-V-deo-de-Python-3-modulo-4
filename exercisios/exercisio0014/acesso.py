from datetime import datetime
import os
import sqlite3

# Define o caminho do banco de dados no mesmo diretório do script
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_banco = os.path.join(diretorio_atual, 'meu_banco.db')

# 1. Conexão com o banco de dados
conexao = sqlite3.connect(caminho_banco)
cursor = conexao.cursor()

# 2. Criação da tabela
script_criar_tabela = '''
CREATE TABLE IF NOT EXISTS amigos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    data_nascimento DATE
);
'''
cursor.execute(script_criar_tabela)

# 3. Dados de exemplo (incluindo datas de teste: normais, vazia e inválida)
amigos_exemplo = [
    ('Lucas Silva', '1998-03-15'),
    ('Mariana Costa', '2001-11-02'),
    ('Thiago Rocha', '1995-07-20'),
    ('Amigo sem data', None),
    ('Amigo data invalida', '31-02-2020'),
]

# Insere registros iniciais caso a tabela esteja vazia
cursor.execute('SELECT COUNT(*) FROM amigos')
if cursor.fetchone()[0] == 0:
  cursor.executemany(
      'INSERT INTO amigos (nome, data_nascimento) VALUES (?, ?)', amigos_exemplo
  )
  conexao.commit()

# 4. Consulta e exibição tratada dos dados
try:
  cursor.execute('SELECT id, nome, data_nascimento FROM amigos')
  registros = cursor.fetchall()

  print('\n--- LISTA DE AMIGOS ---')

  # REQUISITO 1: Mensagem caso não seja encontrado nenhum registro
  if not registros:
    print('Nenhum registro encontrado no banco de dados.')
  else:
    hoje = datetime.now()

    for amigo in registros:
      id_amigo, nome, data_str = amigo

      # REQUISITO 2: Tratamento de datas inválidas e vazias
      if not data_str or str(data_str).strip() == '':
        data_formatada = 'Data não informada'
        idade_str = 'N/A'
      else:
        try:
          # Converte a string YYYY-MM-DD para objeto datetime
          data_dt = datetime.strptime(data_str, '%Y-%m-%d')

          # REQUISITO 3: Data formatada no padrão brasileiro (DD/MM/AAAA)
          data_formatada = data_dt.strftime('%d/%m/%Y')

          # REQUISITO 4: Cálculo da idade real da pessoa
          idade = (
              hoje.year
              - data_dt.year
              - ((hoje.month, hoje.day) < (data_dt.month, data_dt.day))
          )
          idade_str = f'{idade} anos'

        except ValueError:
          # Trata datas em formatos incorretos ou inexistentes (ex: 31/02)
          data_formatada = f'Data inválida ("{data_str}")'
          idade_str = 'N/A'

      print(
          f'ID: {id_amigo} | Nome: {nome:<20} | Nascimento:'
          f' {data_formatada:<25} | Idade: {idade_str}'
      )

except sqlite3.Error as e:
  print(f'Erro ao acessar o banco de dados: {e}')

finally:
  # 5. Fechamento da conexão
  conexao.close()