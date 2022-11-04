import mariadb

conexao = mariadb.connect(host="localhost",
                          user="root",
                          password="",
                          database="escola")

cursor = conexao.cursor()

cursor.execute("SELECT * FROM aluno")

for linha in cursor:               #  0     1           2
    #print(linha)                  # (1, "João", "Informática")
    print("Código:", linha[0])
    print("Nome:", linha[1])
    print("Curso:", linha[2])
    print("=================")

