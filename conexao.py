import mariadb

print("driver carregado")

conexao = mariadb.connect(
	host="localhost",
	user="root",
	password="")

print("conectado ao servidor")