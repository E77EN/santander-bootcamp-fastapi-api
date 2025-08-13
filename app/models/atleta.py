from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class AtletaModel(Base):
    __tablename__ = "atletas"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    idade = Column(Integer, nullable=False)
    peso = Column(Float, nullable=False)
    altura = Column(Float, nullable=False)
    sexo = Column(String(1), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    centro_treinamento_id = Column(Integer, ForeignKey("centros_treinamento.id"))
    
    categoria = relationship("CategoriaModel")
    centro_treinamento = relationship("CentroTreinamentoModel")

