import mariadb

conexao = mariadb.connect(
    host="localhost",
    user="root",
    password="",
    database="loja")

cursor = conexao.cursor()

print("==== CADASTRO DE PRODUTOS ====")

while True :
  nome = input("Digite o nome do produto: ")
  preco = input("Digite o preço do produto: ")
  estoque = input("Digite o estoque do produto: ")
  comando = "INSERT INTO produto VALUES(null, %s, %s, %s)"
  cursor.execute(comando, (nome, preco, estoque) )
  conexao.commit() #confirma a gravação
  print(cursor.rowcount, "registro(s) inserido com sucesso.")
  
  resposta = input("Cadastrar outro? (s/n) ")
  if resposta == 'n':
      break

