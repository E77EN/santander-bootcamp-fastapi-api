from pydantic import BaseModel
from typing import Optional

class CentroTreinamentoIn(BaseModel):
    nome: str
    endereco: str
    proprietario: str

class CentroTreinamentoOut(BaseModel):
    id: int
    nome: str
    endereco: str
    proprietario: str
    
    class Config:
        from_attributes = True

class CentroTreinamentoUpdate(BaseModel):
    nome: Optional[str] = None
    endereco: Optional[str] = None
    proprietario: Optional[str] = None

