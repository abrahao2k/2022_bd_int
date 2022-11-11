import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="loja")
cur = conexao.cursor()
cur.execute("SELECT * FROM produto")
for linha in cur:
    print(linha)
    
codigo = input("Digite o código do produto a ser excluído: ")

cur.execute("SELECT * FROM produto WHERE codigo = " + codigo)
dados = cur.fetchall()
if len(dados) == 0:
    print("Produto não encontrado.")
else:
    print(dados)
    confirmacao = input("Confirma a exclusão? (s/n) ")
    if confirmacao == "s" :
        cur.execute("DELETE FROM produto WHERE codigo = " + codigo)
        conexao.commit()
        print("Excluído com sucesso!")
