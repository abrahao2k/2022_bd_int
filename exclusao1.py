import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="loja")
cur = conexao.cursor()
cur.execute("SELECT * FROM produto")
for linha in cur:
    print(linha)
    
codigo = input("Digite o código do produto a ser excluído: ")
cur.execute("DELETE FROM produto WHERE codigo = " + codigo)
conexao.commit()
print("Excluído com sucesso!")