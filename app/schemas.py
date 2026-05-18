# schemas.py - Schemas de validação com Pydantic
# Esses schemas validam os dados que chegam e saem da API

from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models import TipoTransacao


# --- Schemas de Usuário ---

class UsuarioCreate(BaseModel):
    """Dados necessários pra criar um usuário"""
    nome: str
    email: str
    senha: str


class UsuarioResponse(BaseModel):
    """Dados que a API retorna sobre um usuário"""
    id: int
    nome: str
    email: str
    criado_em: datetime

    class Config:
        from_attributes = True


# --- Schemas de Categoria ---

class CategoriaCreate(BaseModel):
    """Dados pra criar uma categoria"""
    nome: str
    descricao: Optional[str] = None


class CategoriaResponse(BaseModel):
    """Dados que a API retorna sobre uma categoria"""
    id: int
    nome: str
    descricao: Optional[str] = None

    class Config:
        from_attributes = True


# --- Schemas de Transação ---

class TransacaoCreate(BaseModel):
    """Dados necessários pra criar uma transação"""
    descricao: str
    valor: float
    tipo: TipoTransacao
    data: Optional[str] = None  # Data em texto, ex: "2024-01-15"
    categoria_id: Optional[int] = None


class TransacaoUpdate(BaseModel):
    """Dados pra atualizar uma transação (todos opcionais)"""
    descricao: Optional[str] = None
    valor: Optional[float] = None
    tipo: Optional[TipoTransacao] = None
    data: Optional[str] = None
    categoria_id: Optional[int] = None


class TransacaoResponse(BaseModel):
    """Dados que a API retorna sobre uma transação"""
    id: int
    descricao: str
    valor: float
    tipo: TipoTransacao
    data: datetime
    criado_em: datetime
    usuario_id: int
    categoria_id: Optional[int] = None

    class Config:
        from_attributes = True


# --- Schemas de Login ---

class LoginRequest(BaseModel):
    """Dados pra fazer login"""
    email: str
    senha: str


class TokenResponse(BaseModel):
    """Token JWT retornado após login"""
    access_token: str
    token_type: str = "bearer"
