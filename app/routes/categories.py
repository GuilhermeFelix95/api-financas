# routes/categories.py - Rotas CRUD de categorias

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Categoria
from app.schemas import CategoriaCreate, CategoriaResponse

router = APIRouter(
    prefix="/categories",
    tags=["Categorias"]
)


# --- GET /categories ---
@router.get("/", response_model=list[CategoriaResponse])
def listar_categorias(db: Session = Depends(get_db)):
    """Lista todas as categorias cadastradas"""
    categorias = db.query(Categoria).order_by(Categoria.nome).all()
    return categorias


# --- GET /categories/{id} ---
@router.get("/{categoria_id}", response_model=CategoriaResponse)
def buscar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    """Busca uma categoria pelo ID"""
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()

    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    return categoria


# --- POST /categories ---
@router.post("/", response_model=CategoriaResponse, status_code=201)
def criar_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    """Cria uma nova categoria"""
    # Verifica se já existe categoria com esse nome
    existente = db.query(Categoria).filter(Categoria.nome == categoria.nome).first()
    if existente:
        raise HTTPException(status_code=400, detail="Já existe uma categoria com esse nome")

    db_categoria = Categoria(
        nome=categoria.nome,
        descricao=categoria.descricao
    )

    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)

    return db_categoria


# --- PUT /categories/{id} ---
@router.put("/{categoria_id}", response_model=CategoriaResponse)
def atualizar_categoria(
    categoria_id: int,
    categoria_data: CategoriaCreate,
    db: Session = Depends(get_db)
):
    """Atualiza uma categoria existente"""
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()

    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    categoria.nome = categoria_data.nome
    categoria.descricao = categoria_data.descricao

    db.commit()
    db.refresh(categoria)

    return categoria


# --- DELETE /categories/{id} ---
@router.delete("/{categoria_id}", status_code=204)
def deletar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    """Deleta uma categoria"""
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()

    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    db.delete(categoria)
    db.commit()

    return None
