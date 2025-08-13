from pydantic import BaseModel
from typing import Optional

class CategoriaIn(BaseModel):
    nome: str

class CategoriaOut(BaseModel):
    id: int
    nome: str
    
    class Config:
        from_attributes = True

class CategoriaUpdate(BaseModel):
    nome: Optional[str] = None

