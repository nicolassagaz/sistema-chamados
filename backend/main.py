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

def listar_chamados():
    for chamado in chamados:
        print(f"#{chamado['id']} - {chamado['titulo']}")
        print(f"Status: {chamado['status']}")
        print(f"Prioridade: {chamado['prioridade']}")

        if chamado["status"] == 'Aberto':
            print("Chamado aguardando atendimento")

def buscar_chamado(id_chamado):
    for chamado in chamados:
        if chamado["id"] == id_chamado:
            return chamado

listar_chamados()
resultado = buscar_chamado(9999)
print(resultado)

