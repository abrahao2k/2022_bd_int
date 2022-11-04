import mariadb
conexao = mariadb.connect(host="localhost",
                          user="root",
                          password="",
                          database="escola")
cursor = conexao.cursor()

pesquisa = input("Digite o nome a ser pesquisado: ")
comando  = "SELECT * FROM aluno WHERE nome = %s"
cursor.execute(comando, (pesquisa,) )
for linha in cursor:
    print(linha)
