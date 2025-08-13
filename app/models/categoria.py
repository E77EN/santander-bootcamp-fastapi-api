from sqlalchemy import Column, Integer, String
from app.database import Base

class CategoriaModel(Base):
    __tablename__ = "categorias"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), unique=True, nullable=False)

