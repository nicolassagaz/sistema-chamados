from fastapi import FastAPI

#cria aplicação
app = FastAPI()

chamados = [
    {
        "id": 1010,
        "titulo": "Computador não liga",
        "descricao": "Equipamento não inicia",
        "prioridade": "Alta",
        "status": "Aberto",
        "solicitante": "João",
        "tecnico": None,
        "data": "01/09/2026"
    },
    {
        "id": 1011,
        "titulo": "Notebook sem imagem",
        "descricao": "Tela permanece preta ao ligar",
        "prioridade": "Alta",
        "status": "Fechado",
        "solicitante": "Maria",
        "tecnico": None,
        "data": "02/09/2026"
    }
]

#executa função
@app.get("/")
#retorna dicionário python que o fastapi transforma em json
def inicio():
    return {"mensagem": "Sistema de chamados funcionando"}


@app.get("/chamados")
def listar_chamados():
    return chamados

