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

### PROGRAMA PRINCIPAL ##########################################
while True:
    print("=== MENU ===")
    print("1 Cadastrar")
    print("2 Pesquisar")
    opcao = input("Opção? ")
    
    if opcao == "1" : cadastrar()
    elif opcao == "2" : pesquisar()
    else: break
    