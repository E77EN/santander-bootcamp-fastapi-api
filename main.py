from fastapi import FastAPI
from datetime import datetime
from typing import List

app = FastAPI(
    title="API Academia de Crossfit",
    description="Uma API para gerenciar uma academia de crossfit",
    version="1.0.0"
)

# Dados simulados (em uma aplicação real, isso viria do banco de dados)
treinos_simulados = [
    {
        "id": 1,
        "nome": "WOD Iniciante",
        "descricao": "Treino para iniciantes no crossfit",
        "exercicios": ["10 Air Squats", "10 Push-ups", "10 Sit-ups"],
        "duracao_minutos": 15,
        "nivel": "iniciante"
    },
    {
        "id": 2,
        "nome": "WOD Intermediário",
        "descricao": "Treino para praticantes intermediários",
        "exercicios": ["20 Burpees", "30 Box Jumps", "40 Wall Balls"],
        "duracao_minutos": 25,
        "nivel": "intermediario"
    },
    {
        "id": 3,
        "nome": "WOD Avançado",
        "descricao": "Treino intenso para atletas avançados",
        "exercicios": ["50 Double Unders", "40 Pull-ups", "30 Thrusters"],
        "duracao_minutos": 35,
        "nivel": "avancado"
    }
]

membros_simulados = [
    {
        "id": 1,
        "nome": "João Silva",
        "email": "joao@email.com",
        "nivel": "iniciante",
        "data_cadastro": "2024-01-15"
    },
    {
        "id": 2,
        "nome": "Maria Santos",
        "email": "maria@email.com",
        "nivel": "intermediario",
        "data_cadastro": "2024-02-20"
    }
]

# Rota principal
@app.get("/")
async def read_root():
    return {
        "message": "Bem-vindo à API da Academia de Crossfit!",
        "versao": "1.0.0",
        "endpoints_disponiveis": [
            "/treinos",
            "/treinos/{id}",
            "/membros",
            "/membros/{id}",
            "/status"
        ]
    }

# Rota para listar todos os treinos
@app.get("/treinos")
async def listar_treinos():
    return {
        "total": len(treinos_simulados),
        "treinos": treinos_simulados
    }

# Rota para buscar um treino específico por ID
@app.get("/treinos/{treino_id}")
async def buscar_treino(treino_id: int):
    for treino in treinos_simulados:
        if treino["id"] == treino_id:
            return treino
    return {"erro": "Treino não encontrado"}

# Rota para listar todos os membros
@app.get("/membros")
async def listar_membros():
    return {
        "total": len(membros_simulados),
        "membros": membros_simulados
    }

# Rota para buscar um membro específico por ID
@app.get("/membros/{membro_id}")
async def buscar_membro(membro_id: int):
    for membro in membros_simulados:
        if membro["id"] == membro_id:
            return membro
    return {"erro": "Membro não encontrado"}

# Rota para verificar o status da API
@app.get("/status")
async def verificar_status():
    return {
        "status": "online",
        "timestamp": datetime.now().isoformat(),
        "total_treinos": len(treinos_simulados),
        "total_membros": len(membros_simulados)
    }

# Rota para filtrar treinos por nível
@app.get("/treinos/nivel/{nivel}")
async def treinos_por_nivel(nivel: str):
    treinos_filtrados = [treino for treino in treinos_simulados if treino["nivel"] == nivel.lower()]
    return {
        "nivel": nivel,
        "total": len(treinos_filtrados),
        "treinos": treinos_filtrados
    }