import mariadb
conexao = mariadb.connect(host="localhost",
                          user="root",
                          password="",
                          database="escola")
cursor = conexao.cursor()

pesq_nome = input("Digite o nome do aluno: ")
pesq_curso = input("Digite o curso do aluno: ")

comando  = "SELECT * FROM aluno WHERE nome LIKE %s AND curso LIKE %s"
cursor.execute(comando, ("%"+pesq_nome+"%", "%"+pesq_curso+"%") )
for linha in cursor:
    print(linha)


