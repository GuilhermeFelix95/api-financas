# models.py - Modelos do banco de dados
# Aqui a gente define as tabelas usando SQLAlchemy

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime
import enum


# Enum pro tipo da transação (receita ou despesa)
class TipoTransacao(enum.Enum):
    RECEITA = "receita"
    DESPESA = "despesa"


# Tabela de usuários
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    senha_hash = Column(String, nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow)

    # Um usuário tem muitas transações
    transacoes = relationship("Transacao", back_populates="usuario")


# Tabela de categorias
class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, unique=True)
    descricao = Column(String, nullable=True)

    # Uma categoria tem muitas transações
    transacoes = relationship("Transacao", back_populates="categoria")


# Tabela de transações
class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    tipo = Column(Enum(TipoTransacao), nullable=False)
    data = Column(DateTime, nullable=False, default=datetime.utcnow)
    criado_em = Column(DateTime, default=datetime.utcnow)

    # Chaves estrangeiras
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=True)

    # Relacionamentos
    usuario = relationship("Usuario", back_populates="transacoes")
    categoria = relationship("Categoria", back_populates="transacoes")
