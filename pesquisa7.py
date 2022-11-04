import mariadb
conexao = mariadb.connect(host="localhost",
                          user="root",
                          password="",
                          database="escola")
cursor = conexao.cursor()
cursor.execute("SELECT * FROM aluno")

dados = cursor.fetchmany(2)  #transfere X registros por vez
print(dados)

dados = cursor.fetchmany(1)  #transfere X registros por vez
print(dados)

dados = cursor.fetchmany(2)  #transfere X registros por vez
print(dados)