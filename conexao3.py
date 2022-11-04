import mariadb

print("driver carregado")

conexao = mariadb.connect(
  host="localhost",
  user="root",
  password="")

print("conectado ao servidor")

cursor = conexao.cursor()

cursor.execute("CREATE DATABASE aula")

cursor.execute("USE aula")

cursor.execute("""
  CREATE TABLE disciplina(
  id int,
  nome varchar(100))
  """)

print("tabela criada com sucesso")

cursor.execute("INSERT INTO disciplina VALUES(1,'Matemática')")

# conexao.commit()

print("Inserido com sucesso.")

