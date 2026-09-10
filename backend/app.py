from enum import Enum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

#cria aplicação
app = FastAPI()

class Prioridade(str, Enum):
    baixa = "Baixa"
    media = "Média"
    alta = "Alta"

class ChamadoCreate(BaseModel):
    titulo: str = Field(min_length=3)
    descricao: str
    prioridade: Prioridade
    solicitante: str

class ChamadoUpdate(BaseModel):
    status: str

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

    raise HTTPException(status_code=404, detail="Chamado não encontrado")

@app.post("/chamados", status_code=201)
def criar_chamado(novo_chamado: ChamadoCreate):
    novo_id = max(chamado["id"] for chamado in chamados) + 1

    chamado = {
        "id": novo_id,
        "titulo": novo_chamado.titulo,
        "descricao": novo_chamado.descricao,
        "prioridade": novo_chamado.prioridade,
        "status": "Aberto",
        "solicitante": novo_chamado.solicitante,
        "tecnico": None,
        "data": "09/09/2026"
    }

    chamados.append(chamado)

    return chamado


@app.put("/chamados/{id_chamado}")
def atualizar_chamado(id_chamado: int, dados: ChamadoUpdate):
    for chamado in chamados:
        if chamado["id"] == id_chamado:
            chamado["status"] = dados.status
            return chamado

        raise HTTPException(status_code=404, detail="Chamado não encontrado")
    