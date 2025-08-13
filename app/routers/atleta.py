from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models.atleta import AtletaModel
from app.models.categoria import CategoriaModel
from app.models.centro_treinamento import CentroTreinamentoModel
from app.schemas.atleta import AtletaIn, AtletaOut, AtletaUpdate

router = APIRouter(prefix="/atletas", tags=["atletas"])

@router.post("/", response_model=AtletaOut, status_code=status.HTTP_201_CREATED)
def create_atleta(atleta: AtletaIn, db: Session = Depends(get_db)):
    # Verificar se já existe um atleta com o mesmo CPF
    db_atleta = db.query(AtletaModel).filter(AtletaModel.cpf == atleta.cpf).first()
    if db_atleta:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Atleta com este CPF já existe"
        )
    
    # Verificar se categoria existe
    categoria = db.query(CategoriaModel).filter(CategoriaModel.id == atleta.categoria_id).first()
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Categoria não encontrada"
        )
    
    # Verificar se centro de treinamento existe
    centro = db.query(CentroTreinamentoModel).filter(CentroTreinamentoModel.id == atleta.centro_treinamento_id).first()
    if not centro:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Centro de treinamento não encontrado"
        )
    
    db_atleta = AtletaModel(**atleta.dict())
    db.add(db_atleta)
    db.commit()
    db.refresh(db_atleta)
    return db_atleta

@router.get("/", response_model=List[AtletaOut])
def read_atletas(
    skip: int = 0, 
    limit: int = 100, 
    nome: Optional[str] = Query(None, description="Filtrar por nome"),
    cpf: Optional[str] = Query(None, description="Filtrar por CPF"),
    db: Session = Depends(get_db)
):
    query = db.query(AtletaModel)
    
    if nome:
        query = query.filter(AtletaModel.nome.ilike(f"%{nome}%"))
    if cpf:
        query = query.filter(AtletaModel.cpf == cpf)
    
    atletas = query.offset(skip).limit(limit).all()
    return atletas

@router.get("/{atleta_id}", response_model=AtletaOut)
def read_atleta(atleta_id: int, db: Session = Depends(get_db)):
    atleta = db.query(AtletaModel).filter(AtletaModel.id == atleta_id).first()
    if atleta is None:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    return atleta

@router.patch("/{atleta_id}", response_model=AtletaOut)
def update_atleta(atleta_id: int, atleta_update: AtletaUpdate, db: Session = Depends(get_db)):
    atleta = db.query(AtletaModel).filter(AtletaModel.id == atleta_id).first()
    if atleta is None:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    
    update_data = atleta_update.dict(exclude_unset=True)
    
    # Verificar se categoria existe (se foi fornecida)
    if 'categoria_id' in update_data:
        categoria = db.query(CategoriaModel).filter(CategoriaModel.id == update_data['categoria_id']).first()
        if not categoria:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Categoria não encontrada"
            )
    
    # Verificar se centro de treinamento existe (se foi fornecido)
    if 'centro_treinamento_id' in update_data:
        centro = db.query(CentroTreinamentoModel).filter(CentroTreinamentoModel.id == update_data['centro_treinamento_id']).first()
        if not centro:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Centro de treinamento não encontrado"
            )
    
    for field, value in update_data.items():
        setattr(atleta, field, value)
    
    db.commit()
    db.refresh(atleta)
    return atleta

@router.delete("/{atleta_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_atleta(atleta_id: int, db: Session = Depends(get_db)):
    atleta = db.query(AtletaModel).filter(AtletaModel.id == atleta_id).first()
    if atleta is None:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    
    db.delete(atleta)
    db.commit()
    return None

