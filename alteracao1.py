import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="loja")
cur = conexao.cursor()
cur.execute("SELECT * FROM produto")
for linha in cur:
    print(linha)
    
codigo = input("Digite o código do produto a ser alterado: ")

cur.execute("SELECT * FROM produto WHERE codigo = " + codigo)
dados = cur.fetchall()
if len(dados) == 0:
    print("Produto não encontrado.")
else:
    print(f"nome: {dados[0][1]}")
    print(f"preco: {dados[0][2]}")
    print(f"estoque: {dados[0][3]}")
    
    coluna = input("Qual coluna deseja alterar? ")
    
    if coluna in ["nome","preco","estoque"]:
        valor  = input(f"Digite o valor para {coluna}: ")
        cur.execute(f"UPDATE produto SET {coluna} = %s WHERE codigo = %s",
                    (valor,codigo))
        conexao.commit()
        print("Atualizado com sucesso.")
    else:
        print("Essa coluna não pode ser alterada.")  

