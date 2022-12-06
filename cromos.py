import mariadb
conexao = mariadb.connect(host="localhost",
user="root", password="", database="albumcopa2022")
cur = conexao.cursor()

while True:
    print("=== ALBUM COPA 2022 ===")
    print("1 Cadastrar")
    print("5 Sair")
    opcao = int(input("Opção? "))
    
    if opcao == 1:
        print("\n=== CADASTRAR CROMO ===")
        pais = input("País: ")
        jogador = input("Jogador: ")
        posicao = input("Posição: ")
        peso = input("Peso: ")
        altura = input ("Altura: ")
        ano = input("Ano da convocação: ")
        data_nasc = input("Data Nasc (AAAA-MM-DD): ")
        quant = input("Quantidade: ")
        obs = input("Observação: ")
        valor = input("Valor: ")
        
        cmd = "INSERT INTO cromos VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(cmd, (pais, jogador, posicao, peso, altura, ano, data_nasc, quant, obs, valor) )
        conexao.commit()
        print("Cadastrado com sucesso.\n\n")
