from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

class AtletaIn(BaseModel):
    nome: str = Field(..., description="Nome do atleta", max_length=50)
    cpf: str = Field(..., description="CPF do atleta", max_length=11)
    idade: int = Field(..., description="Idade do atleta", gt=0)
    peso: float = Field(..., description="Peso do atleta", gt=0)
    altura: float = Field(..., description="Altura do atleta", gt=0)
    sexo: str = Field(..., description="Sexo do atleta", max_length=1)
    categoria_id: int = Field(..., description="ID da categoria")
    centro_treinamento_id: int = Field(..., description="ID do centro de treinamento")
    
    @validator('sexo')
    def validate_sexo(cls, v):
        if v.upper() not in ['M', 'F']:
            raise ValueError('Sexo deve ser M ou F')
        return v.upper()
    
    @validator('cpf')
    def validate_cpf(cls, v):
        if len(v) != 11 or not v.isdigit():
            raise ValueError('CPF deve conter exatamente 11 dígitos')
        return v

class AtletaOut(BaseModel):
    id: int
    nome: str
    cpf: str
    idade: int
    peso: float
    altura: float
    sexo: str
    created_at: datetime
    categoria: Optional[dict] = None
    centro_treinamento: Optional[dict] = None
    
    class Config:
        from_attributes = True

class AtletaUpdate(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None
    peso: Optional[float] = None
    altura: Optional[float] = None
    categoria_id: Optional[int] = None
    centro_treinamento_id: Optional[int] = None

