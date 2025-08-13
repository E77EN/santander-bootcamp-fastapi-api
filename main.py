from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import categoria, centro_treinamento, atleta

app = FastAPI(
    title="CrossFit Academy API",
    description="API para gerenciamento de academia de CrossFit",
    version="1.0.0"
)

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(categoria.router)
app.include_router(centro_treinamento.router)
app.include_router(atleta.router)

@app.get("/")
async def read_root():
    return {
        "message": "Bem-vindo à CrossFit Academy API!",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

