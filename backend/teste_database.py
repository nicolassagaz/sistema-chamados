from database import conectar

conexao = conectar()

print("Conexão com PostgreSQL realizada com sucesso")

conexao.close()