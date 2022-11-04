import mysql.connector
print("Driver importado com sucesso.")

conexao = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	charset="iso8859-1")

print("Conexão estabelecida com sucesso.")