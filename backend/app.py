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

#endpoint
#quando acessar get /chamados, retorna a lista chamados
@app.get("/chamados")
def listar_chamados():
    return chamados


@app.get("/chamados/{id_chamado}")
def buscar_chamado(id_chamado: int):
    for chamado in chamados:
        if chamado["id"] == id_chamado:
            return chamado

    return {"mensagem": "Chamado não encontrado"}


