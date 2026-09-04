from fastapi import FastAPI

#cria aplicação
app = FastAPI()

#executa função
@app.get("/")
#retorna dicionário python que o fastapi transforma em json
def inicio():
    return {"mensagem": "Sistema de chamados funcionando"}