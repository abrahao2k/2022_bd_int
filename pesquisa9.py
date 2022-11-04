import mariadb
conexao = mariadb.connect(host="localhost",
                          user="root",
                          password="",
                          database="escola")
cursor = conexao.cursor()
tabela = "aluno"
comando = "SELECT * FROM " + tabela

cursor.execute(comando, )

for col in cursor.description:  #pegar nomes das colunas
    print(col[0])


