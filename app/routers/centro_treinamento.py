from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.centro_treinamento import CentroTreinamentoModel
from app.schemas.centro_treinamento import CentroTreinamentoIn, CentroTreinamentoOut, CentroTreinamentoUpdate

router = APIRouter(prefix="/centros-treinamento", tags=["centros-treinamento"])

@router.post("/", response_model=CentroTreinamentoOut, status_code=status.HTTP_201_CREATED)
def create_centro_treinamento(centro: CentroTreinamentoIn, db: Session = Depends(get_db)):
    # Verificar se já existe um centro com o mesmo nome
    db_centro = db.query(CentroTreinamentoModel).filter(CentroTreinamentoModel.nome == centro.nome).first()
    if db_centro:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Centro de treinamento com este nome já existe"
        )
    
    db_centro = CentroTreinamentoModel(**centro.dict())
    db.add(db_centro)
    db.commit()
    db.refresh(db_centro)
    return db_centro

@router.get("/", response_model=List[CentroTreinamentoOut])
def read_centros_treinamento(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    centros = db.query(CentroTreinamentoModel).offset(skip).limit(limit).all()
    return centros

@router.get("/{centro_id}", response_model=CentroTreinamentoOut)
def read_centro_treinamento(centro_id: int, db: Session = Depends(get_db)):
    centro = db.query(CentroTreinamentoModel).filter(CentroTreinamentoModel.id == centro_id).first()
    if centro is None:
        raise HTTPException(status_code=404, detail="Centro de treinamento não encontrado")
    return centro

@router.patch("/{centro_id}", response_model=CentroTreinamentoOut)
def update_centro_treinamento(centro_id: int, centro_update: CentroTreinamentoUpdate, db: Session = Depends(get_db)):
    centro = db.query(CentroTreinamentoModel).filter(CentroTreinamentoModel.id == centro_id).first()
    if centro is None:
        raise HTTPException(status_code=404, detail="Centro de treinamento não encontrado")
    
    update_data = centro_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(centro, field, value)
    
    db.commit()
    db.refresh(centro)
    return centro

@router.delete("/{centro_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_centro_treinamento(centro_id: int, db: Session = Depends(get_db)):
    centro = db.query(CentroTreinamentoModel).filter(CentroTreinamentoModel.id == centro_id).first()
    if centro is None:
        raise HTTPException(status_code=404, detail="Centro de treinamento não encontrado")
    
    db.delete(centro)
    db.commit()
    return None

