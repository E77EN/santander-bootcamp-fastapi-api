from sqlalchemy import Column, Integer, String
from app.database import Base

class CentroTreinamentoModel(Base):
    __tablename__ = "centros_treinamento"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), unique=True, nullable=False)
    endereco = Column(String(60), nullable=False)
    proprietario = Column(String(30), nullable=False)

