import mariadb
conexao = mariadb.connect(host="localhost",
                          user="root",
                          password="",
                          database="escola")

cursor = conexao.cursor(dictionary=True) #Ativa dicionário

cursor.execute("SELECT * FROM aluno")
dados = cursor.fetchone()
print(dados)

print(dados["nome"])  #usando a chave para acessar