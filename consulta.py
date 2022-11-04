from conexaobd import *
#import conexaobd

cursor = conexao.cursor()

cursor.execute("SELECT * FROM aluno")

for linha in cursor:
    print(linha)


