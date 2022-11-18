import mariadb
conexao = mariadb.connect(host="localhost",user="root",password="",database="loja")
cur = conexao.cursor()

def cadastrar():
    print("=== CADASTRO DE PRODUTO ===")
    nome = input("Nome: ")
    preco = input("Preco: ")
    estoque = input("Estoque: ")
    cur.execute("INSERT INTO produto VALUES(null,%s,%s,%s)",(nome,preco,estoque))
    conexao.commit()
    print("Inserido com sucesso! \n")

def pesquisar():
    print("=== PESQUISA DE PRODUTOS ===")
    nome = input("Digite o nome do produto: ")
    cur.execute("SELECT * FROM produto WHERE nome LIKE %s", ("%" + nome + "%",))
    dados = cur.fetchall()
    if len(dados) == 0:
        print("Nenhum resultado encontrado. \n")
    else:
        for linha in dados:
            print(f"codigo: {linha[0]}")
            print(f"nome: {linha[1]}")
            print(f"preco: {linha[2]}")
            print(f"estoque: {linha[3]}")
            print("----------------------------------")
        print(f"{len(dados)} Resultados encontrados. \n")

def alterar():
    print("=== ALTERAÇÃO DE DADOS DO PRODUTO ===")
    codigo = input("Código do produto: ")
    cur.execute("SELECT * FROM produto WHERE codigo = %s", (codigo,))
    dados = cur.fetchall()
    if len(dados) == 0:
        print("Código não encontrado!\n")
    else:
        print(f"nome: {dados[0][1]}")
        print(f"preco: {dados[0][2]}")
        print(f"estoque: {dados[0][3]}")
        
        coluna = input("Qual coluna deseja alterar? ")
        
        if coluna in ('nome', 'preco', 'estoque'):
            valor  = input(f"Digite o novo {coluna}: ")
            comando = "UPDATE produto SET " + coluna + " = %s WHERE codigo = %s"
            cur.execute(comando, (valor, codigo) )
            conexao.commit()
            print("Atualizado com sucesso.\n")
            input("")
        else:
            print("Coluna inválida!\n")


def excluir():
    print("=== EXCLUSÃO DE DADOS DO PRODUTO ===")
    codigo = input("Código do produto: ")
    cur.execute("SELECT * FROM produto WHERE codigo =  %s ", (codigo,))
    dados = cur.fetchall()
    if len(dados) == 0:
        print("Código não encontrado!\n")
    else:
        print(f"nome: {dados[0][1]}")
        print(f"preco: {dados[0][2]}")
        print(f"estoque: {dados[0][3]}")
        
        resp = input("Confirma a exclusão? (s/n) ")
        if resp == "s":
            cur.execute("DELETE FROM produto WHERE codigo = %s ", (codigo,))
            conexao.commit()
            print("Excluído com sucesso.\n")
    


### PROGRAMA PRINCIPAL ##########################################
while True:
    print("=== MENU ===")
    print("1 Cadastrar")
    print("2 Pesquisar")
    print("3 Alterar")
    print("4 Excluir")
    opcao = input("Opção? ")
    
    if   opcao == "1" : cadastrar()
    elif opcao == "2" : pesquisar()
    elif opcao == "3" : alterar()
    elif opcao == "4" : excluir()
    else: break
    
