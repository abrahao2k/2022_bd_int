import mariadb
conexao = mariadb.connect(host="localhost",
                          user="root",
                          password="",
                          database="escola")
cursor = conexao.cursor()
cursor.execute("SELECT * FROM aluno")

dados = cursor.fetchmany(2)  #transfere X registros por vez

        # lin / col
print(dados[0][1])  # pega o nome do primeiro resultado

dados = cursor.fetchone()
print(dados[1])  # pega o nome
