from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.categoria import CategoriaModel
from app.schemas.categoria import CategoriaIn, CategoriaOut, CategoriaUpdate

router = APIRouter(prefix="/categorias", tags=["categorias"])

@router.post("/", response_model=CategoriaOut, status_code=status.HTTP_201_CREATED)
def create_categoria(categoria: CategoriaIn, db: Session = Depends(get_db)):
    # Verificar se já existe uma categoria com o mesmo nome
    db_categoria = db.query(CategoriaModel).filter(CategoriaModel.nome == categoria.nome).first()
    if db_categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Categoria com este nome já existe"
        )
    
    db_categoria = CategoriaModel(**categoria.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

@router.get("/", response_model=List[CategoriaOut])
def read_categorias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categorias = db.query(CategoriaModel).offset(skip).limit(limit).all()
    return categorias

@router.get("/{categoria_id}", response_model=CategoriaOut)
def read_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = db.query(CategoriaModel).filter(CategoriaModel.id == categoria_id).first()
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria

@router.patch("/{categoria_id}", response_model=CategoriaOut)
def update_categoria(categoria_id: int, categoria_update: CategoriaUpdate, db: Session = Depends(get_db)):
    categoria = db.query(CategoriaModel).filter(CategoriaModel.id == categoria_id).first()
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    
    update_data = categoria_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(categoria, field, value)
    
    db.commit()
    db.refresh(categoria)
    return categoria

@router.delete("/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = db.query(CategoriaModel).filter(CategoriaModel.id == categoria_id).first()
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    
    db.delete(categoria)
    db.commit()
    return None

