# routes/transactions.py - Rotas CRUD de transações

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from app.database import get_db
from app.models import Transacao, TipoTransacao, Usuario
from app.schemas import TransacaoCreate, TransacaoUpdate, TransacaoResponse
from app.auth import pegar_usuario_atual

router = APIRouter(
    prefix="/transactions",
    tags=["Transações"]
)


# --- GET /transactions ---
@router.get("/", response_model=list[TransacaoResponse])
def listar_transacoes(
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(pegar_usuario_atual),
    tipo: Optional[str] = None,
    limite: int = 100
):
    """Lista as transações do usuário logado"""
    # Filtra só as transações do usuário logado
    query = db.query(Transacao).filter(Transacao.usuario_id == usuario.id)

    # Se informou tipo, filtra por ele
    if tipo:
        query = query.filter(Transacao.tipo == tipo)

    # Ordena por data (mais recente primeiro)
    transacoes = query.order_by(Transacao.data.desc()).limit(limite).all()

    return transacoes


# --- GET /transactions/{id} ---
@router.get("/{transacao_id}", response_model=TransacaoResponse)
def buscar_transacao(
    transacao_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(pegar_usuario_atual)
):
    """Busca uma transação do usuário logado pelo ID"""
    transacao = db.query(Transacao).filter(
        Transacao.id == transacao_id,
        Transacao.usuario_id == usuario.id
    ).first()

    if not transacao:
        raise HTTPException(status_code=404, detail="Transação não encontrada")

    return transacao


# --- POST /transactions ---
@router.post("/", response_model=TransacaoResponse, status_code=201)
def criar_transacao(
    transacao: TransacaoCreate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(pegar_usuario_atual)
):
    """Cria uma nova transação para o usuário logado"""
    db_transacao = Transacao(
        descricao=transacao.descricao,
        valor=transacao.valor,
        tipo=transacao.tipo,
        categoria_id=transacao.categoria_id,
        usuario_id=usuario.id
    )

    db.add(db_transacao)
    db.commit()
    db.refresh(db_transacao)

    return db_transacao


# --- PUT /transactions/{id} ---
@router.put("/{transacao_id}", response_model=TransacaoResponse)
def atualizar_transacao(
    transacao_id: int,
    transacao_data: TransacaoUpdate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(pegar_usuario_atual)
):
    """Atualiza uma transação do usuário logado"""
    transacao = db.query(Transacao).filter(
        Transacao.id == transacao_id,
        Transacao.usuario_id == usuario.id
    ).first()

    if not transacao:
        raise HTTPException(status_code=404, detail="Transação não encontrada")

    # Atualiza só os campos que vieram no request
    if transacao_data.descricao is not None:
        transacao.descricao = transacao_data.descricao

    if transacao_data.valor is not None:
        transacao.valor = transacao_data.valor

    if transacao_data.tipo is not None:
        transacao.tipo = transacao_data.tipo

    if transacao_data.categoria_id is not None:
        transacao.categoria_id = transacao_data.categoria_id

    db.commit()
    db.refresh(transacao)

    return transacao


# --- DELETE /transactions/{id} ---
@router.delete("/{transacao_id}", status_code=204)
def deletar_transacao(
    transacao_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(pegar_usuario_atual)
):
    """Deleta uma transação do usuário logado"""
    transacao = db.query(Transacao).filter(
        Transacao.id == transacao_id,
        Transacao.usuario_id == usuario.id
    ).first()

    if not transacao:
        raise HTTPException(status_code=404, detail="Transação não encontrada")

    db.delete(transacao)
    db.commit()

    return None
