import mariadb
conexao = mariadb.connect(host="localhost",
                          user="root",
                          password="",
                          database="escola")
cursor = conexao.cursor()
cursor.execute("SELECT * FROM aluno WHERE nome = 'Diego' ")
dados = cursor.fetchall()
print(dados)
print(len(dados), "resultados encontrados.")