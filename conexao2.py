import mariadb

print("driver carregado")

conexao = mariadb.connect(
  host="localhost",
  user="root",
  password="")

print("conectado ao servidor")

cursor = conexao.cursor()

cursor.execute("SHOW DATABASES")

print(list(cursor))

print(cursor.rowcount, "bancos encontrados.")