import mariadb
conexao = mariadb.connect(host="localhost",
                          user="root",
                          password="",
                          database="escola")
cursor = conexao.cursor()
cursor.execute("SELECT * FROM aluno")

dados = cursor.fetchone()  #transfere UM registro por vez
print(dados)

dados = cursor.fetchone()  #transfere UM registro por vez
print(dados)

dados = cursor.fetchone()  #transfere UM registro por vez
print(dados)

print("AINDA NO CURSOR ============")
for linha in cursor:
    print(linha)




