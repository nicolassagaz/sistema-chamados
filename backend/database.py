import psycopg2

def conectar ():
    conexao = psycopg2.connect(
        host="localhost",
        database="sistema_chamados",
        user="postgres",
        password="010504",
        port="5432"
    )

    return conexao